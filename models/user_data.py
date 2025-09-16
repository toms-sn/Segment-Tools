"""Data models for user information."""
from dataclasses import dataclass
from typing import List, Optional, Union

@dataclass
class UserData:
    """Represents a test user's data."""
    unique_snid: str
    first_name: str
    last_name: str
    unique_email: str
    hashed_email: str
    mkt_opt_in: Optional[bool]
    explicit_choice: bool
    advertising_opt_in: Optional[bool]
    third_party_prom: Optional[bool]
    role: str
    subjects: Optional[List[int]]
    newsletters: List[str]
    nature_india: Optional[bool]
    nature_middle_east: Optional[bool]
    nature_china: Optional[bool]
    nature_newsletter: Optional[bool]