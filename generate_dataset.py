"""Generate test dataset in JSONL format compatible with Google BigQuery."""
import json
import argparse
import sys
from datetime import datetime
from pathlib import Path
from generators.data_generator import UserDataGenerator
from models.user_data import UserData

# Import configuration
try:
    from config import NUM_ITERATIONS
except ImportError:
    print("❌ ERROR: config.py not found. Please create it with your settings.")
    sys.exit(1)


class DatasetGenerator:
    """Generates test dataset in JSONL format for BigQuery."""
    
    def __init__(self, output_file: str = None):
        """Initialize the dataset generator.
        
        Args:
            output_file: Output filename. If None, generates timestamp-based filename.
        """
        self.generator = UserDataGenerator()
        self.output_file = output_file or self._generate_filename()
    
    def _generate_filename(self) -> str:
        """Generate timestamp-based filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"test_dataset_{timestamp}.jsonl"
    
    def _user_data_to_dict(self, user_data: UserData) -> dict:
        """Convert UserData object to dictionary for JSON serialization.
        
        Args:
            user_data: UserData instance to convert
            
        Returns:
            Dictionary representation of user data
        """
        return {
            "snid": user_data.unique_snid,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name,
            "email": user_data.unique_email,
            "hashed_email": user_data.hashed_email,
            "mkt_opt_in": user_data.mkt_opt_in,
            # "explicit_choice": user_data.explicit_choice,
            "advertising_opt_in": user_data.advertising_opt_in,
            "third_party_prom": user_data.third_party_prom,
            "role": user_data.role,
            "subjects": user_data.subjects,
            # "newsletters": user_data.newsletters,
            "nature_india": user_data.nature_india,
            "nature_middle_east": user_data.nature_middle_east,
            "nature_china": user_data.nature_china,
            "nature_newsletter": user_data.nature_newsletter,
            "generated_at": datetime.now().isoformat()  # Add timestamp for tracking
        }
    
    def generate_dataset(self, num_records: int) -> None:
        """Generate dataset and save to JSONL file.
        
        Args:
            num_records: Number of records to generate
        """
        print(f"🚀 Generating {num_records} test records...")
        print(f"📁 Output file: {self.output_file}")
        print("-" * 60)
        
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for i in range(1, num_records + 1):
                    # Generate test data
                    user_data = self.generator.generate()
                    
                    # Convert to dictionary
                    record = self._user_data_to_dict(user_data)
                    
                    # Write as JSONL (one JSON object per line)
                    f.write(json.dumps(record, ensure_ascii=False) + '\n')
                    
                    # Progress indicator
                    if i % 100 == 0 or i == num_records:
                        print(f"   ✅ Generated {i}/{num_records} records...")
            
            # Verify file was created
            file_path = Path(self.output_file)
            if file_path.exists():
                file_size = file_path.stat().st_size
                print("-" * 60)
                print(f"✅ Dataset generated successfully!")
                print(f"📄 File: {self.output_file}")
                print(f"📊 Records: {num_records}")
                print(f"💾 Size: {file_size:,} bytes")
                print(f"📋 Format: JSONL (BigQuery compatible)")
            else:
                print("❌ ERROR: File was not created successfully.")
                
        except Exception as e:
            print(f"❌ ERROR: Failed to generate dataset: {e}")
            sys.exit(1)
    
    def preview_sample(self, num_samples: int = 3) -> None:
        """Generate and display sample records without saving to file.
        
        Args:
            num_samples: Number of sample records to display
        """
        print(f"🔍 Generating {num_samples} sample records...")
        print("-" * 60)
        
        for i in range(1, num_samples + 1):
            user_data = self.generator.generate()
            record = self._user_data_to_dict(user_data)
            
            print(f"Sample {i}:")
            print(json.dumps(record, indent=2, ensure_ascii=False))
            if i < num_samples:
                print("-" * 40)


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate test dataset in JSONL format for Google BigQuery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_dataset.py                    # Generate default number of records
  python generate_dataset.py -n 1000           # Generate 1000 records
  python generate_dataset.py -o my_data.jsonl  # Custom output filename
  python generate_dataset.py --preview         # Preview sample records
        """
    )
    
    parser.add_argument(
        '-n', '--num-records',
        type=int,
        default=NUM_ITERATIONS,
        help=f'Number of records to generate (default: {NUM_ITERATIONS})'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Output filename (default: timestamp-based name)'
    )
    
    parser.add_argument(
        '--preview',
        action='store_true',
        help='Preview sample records without saving to file'
    )
    
    parser.add_argument(
        '--preview-count',
        type=int,
        default=3,
        help='Number of sample records to preview (default: 3)'
    )
    
    args = parser.parse_args()
    
    # Create dataset generator
    generator = DatasetGenerator(args.output)
    
    # Handle preview mode
    if args.preview:
        generator.preview_sample(args.preview_count)
        return
    
    # Validate number of records
    if args.num_records <= 0:
        print("❌ ERROR: Number of records must be greater than 0")
        sys.exit(1)
    
    # Generate dataset
    generator.generate_dataset(args.num_records)


if __name__ == "__main__":
    main()
