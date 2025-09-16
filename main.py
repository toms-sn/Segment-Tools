"""Main application entry point."""
import sys
import time
from generators.data_generator import UserDataGenerator
from services.segment_client import SegmentClient
from utils.output import OutputFormatter, ExecutionStats

# Import configuration
try:
    from config import SEGMENT_WRITE_KEY, SEGMENT_URL, NUM_ITERATIONS, REQUEST_DELAY
except ImportError:
    print("❌ ERROR: config.py not found. Please create it with your settings.")
    sys.exit(1)

def validate_configuration():
    """Validate configuration settings."""
    if SEGMENT_WRITE_KEY == "YOUR_SEGMENT_WRITE_KEY_HERE":
        print("❌ ERROR: Please update SEGMENT_WRITE_KEY in config.py")
        print("   Find your write key in Segment dashboard > Sources > Marketing Preference Center > Settings > API Keys")
        return False
    return True

def main():
    """Main function to generate and send test data."""
    if not validate_configuration():
        return
    
    # Initialize components
    generator = UserDataGenerator()
    segment_client = SegmentClient()
    output_formatter = OutputFormatter()
    stats = ExecutionStats()
    
    # Print header
    output_formatter.print_header(NUM_ITERATIONS, SEGMENT_URL)
    
    # Generate and send test data
    for i in range(1, NUM_ITERATIONS + 1):
        # Generate test data
        user_data = generator.generate()
        
        # Print user info
        output_formatter.print_user_info(user_data, i, NUM_ITERATIONS)
        
        # Send to Segment
        status_code, response_text = segment_client.send_identify(user_data)
        
        # Print result and update stats
        output_formatter.print_request_result(status_code, response_text)
        
        if status_code == 200:
            stats.record_success()
        else:
            stats.record_failure()
        
        # Add delay between requests (except for the last request)
        if i < NUM_ITERATIONS:
            print(f"   ⏱️  Waiting 300ms...")
            time.sleep(REQUEST_DELAY)
    
    # Print summary
    output_formatter.print_summary(stats.get_stats(NUM_ITERATIONS))

if __name__ == "__main__":
    main()