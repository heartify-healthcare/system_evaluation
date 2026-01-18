import json
import matplotlib.pyplot as plt
from pathlib import Path
import os

def kebab_to_normal_case(kebab_string):
    """Convert kebab-case to Normal Case"""
    words = kebab_string.split('-')
    return ' '.join(word.capitalize() for word in words)

def calculate_cpu_average(data):
    """Calculate average CPU usage for each field"""
    averages = {}
    for field_name, values in data.items():
        avg = sum(values) / len(values) if values else 0
        averages[field_name] = round(avg, 6)
    return averages

def calculate_memory_average(data):
    """Calculate average memory usage for each field (convert bytes to MB)"""
    averages = {}
    for field_name, values in data.items():
        # Convert bytes to MB
        values_mb = [v / (1024 * 1024) for v in values]
        avg = sum(values_mb) / len(values_mb) if values_mb else 0
        averages[field_name] = round(avg, 2)
    return averages

def plot_cpu_usage(data, output_folder):
    """Plot CPU usage graphs for each field"""
    output_path = Path(output_folder) / 'graphs'
    output_path.mkdir(exist_ok=True)
    
    print(f"\nVẽ biểu đồ CPU Usage...")
    
    for field_name, values in data.items():
        # Convert field name to normal case
        service_name = kebab_to_normal_case(field_name)
        
        # Create plot
        plt.figure(figsize=(12, 6))
        plt.plot(range(len(values)), values, marker='o', linestyle='-', linewidth=2, markersize=4)
        plt.title(f'CPU Usage của {service_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Thời điểm đo', fontsize=12)
        plt.ylabel('CPU (cores)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save plot
        output_file = output_path / f'{field_name}_cpu_usage.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"  ✓ {service_name}: {output_file}")

def plot_memory_usage(data, output_folder):
    """Plot memory usage graphs for each field (convert bytes to MB)"""
    output_path = Path(output_folder) / 'graphs'
    output_path.mkdir(exist_ok=True)
    
    print(f"\nVẽ biểu đồ Memory Usage...")
    
    for field_name, values in data.items():
        # Convert field name to normal case
        service_name = kebab_to_normal_case(field_name)
        
        # Convert bytes to MB
        values_mb = [v / (1024 * 1024) for v in values]
        
        # Create plot
        plt.figure(figsize=(12, 6))
        plt.plot(range(len(values_mb)), values_mb, marker='o', linestyle='-', linewidth=2, markersize=4, color='#ff7f0e')
        plt.title(f'Memory Usage của {service_name}', fontsize=14, fontweight='bold')
        plt.xlabel('Thời điểm đo', fontsize=12)
        plt.ylabel('Memory (MB)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save plot
        output_file = output_path / f'{field_name}_memory_usage.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"  ✓ {service_name}: {output_file}")

def main():
    print("=" * 70)
    print("BẮT ĐẦU VẼ BIỂU ĐỒ VÀ TÍNH TRUNG BÌNH")
    print("=" * 70)
    
    averages_result = {}
    
    # Process CPU usage
    cpu_json_path = Path('cpu_usage') / 'cpu_usage.json'
    if cpu_json_path.exists():
        with open(cpu_json_path, 'r', encoding='utf-8') as f:
            cpu_data = json.load(f)
        plot_cpu_usage(cpu_data, 'cpu_usage')
        print(f"\n✓ Đã tạo {len(cpu_data)} biểu đồ CPU Usage trong cpu_usage/graphs/")
        
        # Calculate CPU averages
        cpu_averages = calculate_cpu_average(cpu_data)
        averages_result['cpu_usage_average_cores'] = cpu_averages
        print(f"\n✓ Đã tính trung bình CPU Usage (cores)")
    else:
        print(f"⚠ Không tìm thấy {cpu_json_path}")
    
    # Process Memory usage
    memory_json_path = Path('memory_usage') / 'memory_usage.json'
    if memory_json_path.exists():
        with open(memory_json_path, 'r', encoding='utf-8') as f:
            memory_data = json.load(f)
        plot_memory_usage(memory_data, 'memory_usage')
        print(f"\n✓ Đã tạo {len(memory_data)} biểu đồ Memory Usage trong memory_usage/graphs/")
        
        # Calculate Memory averages
        memory_averages = calculate_memory_average(memory_data)
        averages_result['memory_usage_average_mb'] = memory_averages
        print(f"\n✓ Đã tính trung bình Memory Usage (MB)")
    else:
        print(f"⚠ Không tìm thấy {memory_json_path}")
    
    # Save averages to JSON file
    if averages_result:
        output_file = Path('averages.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(averages_result, f, indent=4, ensure_ascii=False)
        print(f"\n✓ Đã lưu kết quả trung bình vào {output_file}")
    
    print("\n" + "=" * 70)
    print("HOÀN THÀNH!")
    print("=" * 70)

if __name__ == "__main__":
    main()
