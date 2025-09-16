"""Output and logging utilities."""
import time
from typing import Dict
from models.user_data import UserData

class OutputFormatter:
    """Handles formatted output for the application."""
    
    @staticmethod
    def print_header(num_iterations: int, segment_url: str):
        """Print application header."""
        print(f"🚀 Starting generation of {num_iterations} test users...")
        print(f"📡 Target: {segment_url}")
        print(f"⏱️  Delay: 300ms between requests")
        print("=" * 80)
    
    @staticmethod
    def print_user_info(user_data: UserData, iteration: int, total: int):
        """Print user information."""
        print(f"\n📝 Generating test user {iteration}/{total}...")
        print(f"   SNID: {user_data.unique_snid}")
        print(f"   Name: {user_data.first_name} {user_data.last_name}")
        print(f"   Email: {user_data.unique_email}")
        print(f"   Role: {user_data.role}")
        print(f"   Subjects: {user_data.subjects}")
        print(f"   Newsletters: {user_data.newsletters}")
    
    @staticmethod
    def print_request_result(status_code: int, response_text: str):
        """Print request result."""
        print(f"   📤 Sending to Segment...")
        if status_code == 200:
            print(f"   ✅ SUCCESS - Status: {status_code}")
        else:
            print(f"   ❌ FAILED - Status: {status_code}, Response: {response_text}")
    
    @staticmethod
    def print_summary(stats: Dict[str, any]):
        """Print execution summary."""
        print("\n" + "=" * 80)
        print(f"🎯 SUMMARY:")
        print(f"   ✅ Successful requests: {stats['successful']}")
        print(f"   ❌ Failed requests: {stats['failed']}")
        print(f"   📊 Success rate: {stats['success_rate']:.1f}%")
        print(f"   ⏱️  Total execution time: {stats['total_time']:.2f} seconds")
        print(f"   🕐 Average time per request: {stats['avg_time']:.2f} seconds")
        

class ExecutionStats:
    """Tracks execution statistics."""
    
    def __init__(self):
        self.successful = 0
        self.failed = 0
        self.start_time = time.time()
    
    def record_success(self):
        """Record a successful request."""
        self.successful += 1
    
    def record_failure(self):
        """Record a failed request."""
        self.failed += 1
    
    def get_stats(self, total_iterations: int) -> Dict[str, any]:
        """Get execution statistics."""
        total_time = time.time() - self.start_time
        success_rate = (self.successful / total_iterations) * 100 if total_iterations > 0 else 0
        avg_time = total_time / total_iterations if total_iterations > 0 else 0
        
        return {
            'successful': self.successful,
            'failed': self.failed,
            'total_time': total_time,
            'success_rate': success_rate,
            'avg_time': avg_time
        }