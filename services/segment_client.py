"""Segment API client for sending identify calls."""
import requests
import base64
from typing import Tuple, Optional
from models.user_data import UserData
from config import SEGMENT_WRITE_KEY, SEGMENT_URL

class SegmentClient:
    """Client for interacting with Segment API."""
    
    def __init__(self, write_key: str = SEGMENT_WRITE_KEY, url: str = SEGMENT_URL):
        self.write_key = write_key
        self.url = url
        self.headers = self._build_headers()
    
    def _build_headers(self) -> dict:
        """Build authorization headers for Segment API."""
        auth_string = f"{self.write_key}:"
        encoded_auth = base64.b64encode(auth_string.encode()).decode()
        
        return {
            "Content-Type": "application/json",
            "Authorization": f"Basic {encoded_auth}"
        }
    
    def _build_payload(self, user_data: UserData) -> dict:
        """Build Segment identify payload from user data."""
        return {
            "userId": user_data.unique_snid,
            "traits": {
                "snid": user_data.unique_snid,
                "first_name": user_data.first_name,
                "last_name": user_data.last_name,
                "email": user_data.unique_email,
                "hashed_email": user_data.hashed_email,
                "mkt_pref_opt_in": user_data.mkt_opt_in,
#                "explicit_user_choice": user_data.explicit_choice,
                "advertising_opt_in": user_data.advertising_opt_in,
                "third_party_prom": user_data.third_party_prom,
                "role": user_data.role,
                "subjects": user_data.subjects,
 #               "newsletters": user_data.newsletters,
                "nature_india": user_data.nature_india,
                "nature_middle_east": user_data.nature_middle_east,
                "nature_china": user_data.nature_china,
                "nature_newsletter": user_data.nature_newsletter
            }
        }
    
    def send_identify(self, user_data: UserData) -> Tuple[Optional[int], str]:
        """Send Identify call to Segment."""
        payload = self._build_payload(user_data)
        
        try:
            response = requests.post(
                self.url,
                json=payload,
                headers=self.headers,
                verify=False,  # Disable SSL verification for testing
                timeout=30
            )
            return response.status_code, response.text
        except Exception as e:
            return None, str(e)