# Segment Configuration
SEGMENT_WRITE_KEY = "insert yours here"  # HTTP API Source
SEGMENT_URL = "https://events.eu1.segmentapis.com/v1/identify/"

# Test Data Configuration
NUM_ITERATIONS = 5
SNID_PREFIX = "TEST_"
EMAIL_DOMAIN = "@test.nature.com"
REQUEST_DELAY = 0.3

# Data Generation Configuration
BOOLEAN_NULL_DISTRIBUTION = {
    'true_probability': 0.23,
    'false_probability': 0.23,
    'null_probability': 0.54
}

AVAILABLE_ROLES = [
    "Researcher", 
    "Lecturer", 
    "Healthcare professional", 
    "Librarian", 
    "Research manager", 
    "Other"
]

AVAILABLE_SUBJECTS = [
    2954, 3274, 37114, 10615, 41467, 12345, 23456, 34567, 45678, 56789,
    11234, 22567, 33891, 44123, 55678, 67890, 78123, 89456, 90789, 13579,
    24681, 35792, 46803, 57914, 68025
]

AVAILABLE_NEWSLETTERS = [
    "nature_india", 
    "nature_middle_east", 
    "nature_china", 
    "nature_newsletter", 
    "source_newsletter"
]