"""
Latency Evaluation Script for Heartify AI Service
Measures end-to-end latency breakdown of ECG processing pipeline
"""

import time
import requests
import numpy as np
import json
import os
from typing import Dict, Any, List


# Configuration
API_BASE_URL = "http://k8s-heartify-apigatew-c9e4853fd6-36c22647130c08e3.elb.ap-southeast-1.amazonaws.com"  # Adjust to your API Gateway URL
ECG_SESSION_ENDPOINT = f"{API_BASE_URL}/api/v1/ecg-sessions"
DEVICE_ID = "latency-test-device"

# JWT Token (replace with your actual token)
JWT_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoidXNlciIsInVzZXJfaWQiOiIyY2ZiYzk0My0yMGVkLTQ3MzItYjUyYS01NjYyZTk2M2VkZTUiLCJlbWFpbCI6InNvbmdva3Vwa2pAZ21haWwuY29tIiwidXNlcm5hbWUiOiJzb25nb2t1cGtqIiwic3ViIjoic29uZ29rdXBraiIsImlhdCI6MTc2NjI1NTA2NCwiZXhwIjoxNzY2MzQxNDY0fQ.EkrXoOdHFRcozz3Ny0ViB1JS_OYoPj43wfOtILVWAtGvM5YtfBwNUo08qc57m2iW68ntCry71yqwMyMtMsZo-Q"

# Output configuration
OUTPUT_FILE = "latency_results.json"

# ECG Signal Configuration
SAMPLING_RATE = 130  # Hz
DURATION = 10  # seconds
NUM_SAMPLES = SAMPLING_RATE * DURATION


def generate_dummy_ecg_signal() -> list:
    """
    Generate a synthetic 10-second ECG signal
    Returns a list of float values representing the ECG signal
    """
    t = np.linspace(0, DURATION, NUM_SAMPLES)
    
    # Simple synthetic ECG: sine wave with noise
    # Real ECG would have P-QRS-T complex, but this is sufficient for latency testing
    heart_rate = 75  # beats per minute
    frequency = heart_rate / 60  # Hz
    
    # Base signal: sine wave simulating heartbeat
    signal = np.sin(2 * np.pi * frequency * t)
    
    # Add some harmonics to make it more realistic
    signal += 0.3 * np.sin(2 * np.pi * frequency * 2 * t)
    signal += 0.2 * np.sin(2 * np.pi * frequency * 3 * t)
    
    # Add small random noise
    noise = np.random.normal(0, 0.05, NUM_SAMPLES)
    signal = signal + noise
    
    # Normalize to range [-1, 1]
    signal = signal / np.max(np.abs(signal))
    
    return signal.tolist()


def send_evaluation_request(ecg_signal: list) -> Dict[str, Any]:
    """
    Send POST request to ECG session endpoint with latency tracking
    
    Args:
        ecg_signal: List of float values representing ECG signal
        
    Returns:
        Dictionary containing response data and timing information
    """
    # Capture timestamp before sending request
    requested_at = int(time.time() * 1000)
    
    # Construct request payload (match request.json structure, include requestedAt)
    payload = {
        "deviceId": DEVICE_ID,
        "rawData": {
            "signal": ecg_signal,
            "lead": "I",
            "duration": DURATION
        },
        "samplingRate": SAMPLING_RATE,
        "requestedAt": requested_at
    }
    
    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {JWT_TOKEN}"
    }
    
    print(f"Sending request to: {ECG_SESSION_ENDPOINT}")
    print(f"Signal length: {len(ecg_signal)} samples")
    print(f"Request timestamp: {requested_at}")
    print("-" * 50)
    
    try:
        # Send POST request
        response = requests.post(
            ECG_SESSION_ENDPOINT,
            json=payload,
            headers=headers,
            timeout=120  # 2 minute timeout for processing
        )
        
        # Capture timestamp when response received
        received_at = int(time.time() * 1000)
        
        # Check response status
        response.raise_for_status()
        
        # Parse JSON response
        response_data = response.json()
        
        return {
            "success": True,
            "requested_at": requested_at,
            "received_at": received_at,
            "response": response_data
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "requested_at": requested_at,
            "received_at": int(time.time() * 1000)
        }


def extract_timing_data(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract timing information from API response
    
    Args:
        result: Dictionary containing evaluation results
        
    Returns:
        Dictionary with timing data or None if extraction fails
    """
    if not result["success"]:
        return None
    
    response = result["response"]
    evaluations = response.get("evaluations")
    
    if not evaluations:
        return None
    
    # Extract timing information (as returned by server)
    t_upload = evaluations.get("tupload")
    t_denoise = evaluations.get("tdenoise")
    t_classify = evaluations.get("tclassify")
    t_llm = evaluations.get("tllm")
    responsed_at = evaluations.get("responsedAt")
    
    requested_at = result["requested_at"]
    received_at = result["received_at"]
    
    # Calculate T_return (may be negative due to clock skew between client and server)
    if responsed_at:
        t_return = received_at - responsed_at
    else:
        t_return = None
    
    # Return timing data
    return {
        "T_upload": t_upload,
        "T_denoise": t_denoise,
        "T_classify": t_classify,
        "T_LLM": t_llm,
        "T_return": t_return,
        "timestamp": requested_at,
        "session_id": response.get('id', 'N/A')
    }


def load_results() -> List[Dict[str, Any]]:
    """
    Load existing results from JSON file
    
    Returns:
        List of result dictionaries
    """
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️  Warning: Could not parse {OUTPUT_FILE}, starting fresh")
            return []
    return []


def save_results(results: List[Dict[str, Any]]):
    """
    Save results to JSON file
    
    Args:
        results: List of result dictionaries
    """
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"✅ Results saved to {OUTPUT_FILE}")


def print_latency_report(result: Dict[str, Any]):
    """
    Print detailed latency evaluation report
    
    Args:
        result: Dictionary containing evaluation results
    """
    if not result["success"]:
        print("\n❌ Request Failed!")
        print(f"Error: {result['error']}")
        print(f"Total time: {result['received_at'] - result['requested_at']} ms")
        return
    
    response = result["response"]
    evaluations = response.get("evaluations")
    if not evaluations:
        print("\n⚠️  Warning: No evaluation metrics found in response")
        print("Make sure the backend is configured to return evaluation metrics")
        return

    # Extract timing information (keys are lowercase in new response)
    t_upload = evaluations.get("tupload", "N/A")
    t_denoise = evaluations.get("tdenoise", "N/A")
    t_classify = evaluations.get("tclassify", "N/A")
    t_llm = evaluations.get("tllm", "N/A")
    responsed_at = evaluations.get("responsedAt")

    requested_at = result["requested_at"]
    received_at = result["received_at"]

    # Calculate additional metrics
    if responsed_at:
        t_return = received_at - responsed_at
    else:
        t_return = "N/A"

    t_total = received_at - requested_at

    # Calculate processing time (sum of internal steps)
    if all(isinstance(x, (int, float)) for x in [t_denoise, t_classify, t_llm]):
        t_processing = t_denoise + t_classify + t_llm
    else:
        t_processing = "N/A"

    # Print report
    print("\n" + "=" * 60)
    print("         LATENCY EVALUATION REPORT")
    print("=" * 60)
    print("\n📊 Timing Breakdown:\n")
    print(f"  1. T_upload    : {t_upload:>8} ms  (Client → Server Entry)")
    print(f"  2. T_denoise   : {t_denoise:>8} ms  (Denoising Model)")
    print(f"  3. T_classify  : {t_classify:>8} ms  (Classification Model)")
    print(f"  4. T_LLM       : {t_llm:>8} ms  (LLM Explanation)")
    print(f"  5. T_return    : {t_return:>8} ms  (Server Exit → Client)")
    print("-" * 60)
    print(f"  Total E2E      : {t_total:>8} ms  (End-to-End Latency)")
    print(f"  Processing     : {t_processing:>8} ms  (Sum of Steps 2-4)")
    print("=" * 60)

    # Print diagnosis result
    prediction = response.get("prediction", {})
    if prediction:
        diagnosis = prediction.get("diagnosis", "Unknown")
        probability = prediction.get("probability", 0)
        print(f"\n🩺 Diagnosis: {diagnosis} ({probability:.2%} confidence)")

    print(f"\n✅ Session ID: {response.get('id', 'N/A')}")
    print()


def main():
    """Main execution function"""
    print("=" * 60)
    print("  Heartify AI Service - Sequential Latency Evaluation")
    print("=" * 60)
    print()
    
    # Load existing results
    results = load_results()
    print(f"📂 Loaded {len(results)} existing result(s)")
    print()
    
    # Ask how many requests to make
    try:
        num_requests = int(input("🔢 How many sequential requests do you want to make? "))
        if num_requests <= 0:
            print("❌ Number of requests must be positive")
            return
    except ValueError:
        print("❌ Invalid input")
        return
    
    print()
    print(f"🚀 Starting {num_requests} sequential requests...")
    print("=" * 60)
    
    # Generate dummy ECG signal once (reuse for all requests)
    print("📈 Generating synthetic ECG signal...")
    ecg_signal = generate_dummy_ecg_signal()
    print(f"✓ Generated {len(ecg_signal)} samples ({DURATION}s @ {SAMPLING_RATE}Hz)")
    print()
    
    # Make sequential requests
    for i in range(1, num_requests + 1):
        print(f"\n{'='*60}")
        print(f"  Request {i}/{num_requests}")
        print(f"{'='*60}")
        
        # Send evaluation request
        print("🚀 Sending evaluation request...")
        result = send_evaluation_request(ecg_signal)
        
        # Check if request was successful
        if not result["success"]:
            print("\n❌ Request Failed!")
            print(f"Error: {result['error']}")
            print("\n⚠️  API call failed. Please check your API KEY and try again.")
            print("Update the JWT_TOKEN variable in the script with a valid token.")
            break
        
        # Extract timing data
        timing_data = extract_timing_data(result)
        
        if timing_data is None:
            print("\n⚠️  Warning: Could not extract timing data from response")
            print("Response may be missing 'evaluations' field")
            print("\n⚠️  Please check the API response format or update your API KEY.")
            break
        
        # Append to results
        results.append(timing_data)
        
        # Print latency report
        print_latency_report(result)
        
        print(f"\n✅ Successfully recorded timing data (Total: {len(results)} results)")
        
        # Save after each successful request
        save_results(results)
        
        # Small delay between requests to avoid overwhelming the server
        if i < num_requests:
            print("\n⏳ Waiting 1 second before next request...")
            time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"  Completed: {len(results)} total results saved to {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
