import json
import csv
from datetime import datetime
from pathlib import Path
import os

def parse_datetime(dt_string):
    """Parse datetime string to datetime object"""
    return datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")

def is_in_gaps(timestamp, gaps):
    """Check if timestamp falls within any gap range"""
    dt = parse_datetime(timestamp)
    for gap in gaps:
        from_dt = parse_datetime(gap['from'])
        to_dt = parse_datetime(gap['to'])
        if from_dt <= dt <= to_dt:
            return True
    return False

def process_csv_files(folder_name, gaps, output_filename):
    """Process all CSV files in a folder based on time gaps"""
    folder_path = Path(folder_name)
    result = {}
    
    # Get all CSV files in the folder (excluding no_access subfolder)
    csv_files = [f for f in folder_path.glob('*.csv') if f.is_file()]
    
    print(f"Processing {len(csv_files)} files from {folder_name}...")
    
    for csv_file in csv_files:
        print(f"  Reading {csv_file.name}...")
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            
            for row in reader:
                # Get the time column (might have quotes or not)
                timestamp = row.get('Time') or row.get('"Time"')
                if not timestamp:
                    # Try to get the first column
                    timestamp = list(row.values())[0] if row else None
                if not timestamp:
                    continue
                
                # Check if timestamp is in any gap
                if is_in_gaps(timestamp, gaps):
                    # Process all columns except 'Time'
                    for column_name, value in row.items():
                        if column_name != 'Time':
                            if column_name not in result:
                                result[column_name] = []
                            
                            # Try to convert to appropriate type
                            try:
                                # Try float first
                                result[column_name].append(float(value))
                            except ValueError:
                                # If not a number, keep as string
                                result[column_name].append(value)
    
    # Save result to JSON file in the same folder
    output_path = folder_path / Path(output_filename).name
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    
    print(f"✓ Saved results to {output_path}")
    return result

def main():
    # Read gaps to process
    print("Loading gaps_to_process.json...")
    with open('gaps_to_process.json', 'r', encoding='utf-8') as f:
        gaps = json.load(f)
    
    print(f"Found {len(gaps)} time gaps to process\n")
    
    # Process CPU usage files
    print("=" * 60)
    cpu_result = process_csv_files('cpu_usage', gaps, 'cpu_usage.json')
    for col_name, values in cpu_result.items():
        print(f"  {col_name}: {len(values)} values")
    
    print("\n" + "=" * 60)
    # Process memory usage files
    memory_result = process_csv_files('memory_usage', gaps, 'memory_usage.json')
    for col_name, values in memory_result.items():
        print(f"  {col_name}: {len(values)} values")
    
    print("\n" + "=" * 60)
    print("Processing complete!")

if __name__ == "__main__":
    main()
