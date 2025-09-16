"""Generates test user data."""
import random
import uuid
from faker import Faker
from typing import Optional, List
from models.user_data import UserData
from config import (
    SNID_PREFIX, 
    EMAIL_DOMAIN, 
    BOOLEAN_NULL_DISTRIBUTION,
    AVAILABLE_ROLES,
    AVAILABLE_SUBJECTS,
    AVAILABLE_NEWSLETTERS
)

fake = Faker()

class UserDataGenerator:
    """Generates realistic test user data."""
    
    @staticmethod
    def generate_boolean_or_null() -> Optional[bool]:
        """Generate boolean or null values based on configured distribution."""
        rand = random.random()
        
        true_prob = BOOLEAN_NULL_DISTRIBUTION['true_probability']
        false_prob = BOOLEAN_NULL_DISTRIBUTION['false_probability']
        
        if rand < true_prob:
            return True
        elif rand < (true_prob + false_prob):
            return False
        else:
            return None
    
    def generate_subjects(self) -> Optional[List[int]]:
        """Generate random subjects array (0-20 subjects)."""
        num_subjects = random.randint(0, 20)
        if num_subjects == 0:
            return None
        return random.sample(AVAILABLE_SUBJECTS, min(num_subjects, len(AVAILABLE_SUBJECTS)))
    
    def generate_newsletters(self) -> List[str]:
        """Generate random newsletters array."""
        num_newsletters = random.randint(0, len(AVAILABLE_NEWSLETTERS))
        return random.sample(AVAILABLE_NEWSLETTERS, num_newsletters)
    
    def generate(self) -> UserData:
        """Generate complete test user data."""
        # Generate unique SNID
        unique_snid = f"{SNID_PREFIX}{uuid.uuid4()}_SN"
        
        # Generate names
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Generate unique email
        random_number = random.randint(1000, 9999)
        unique_email = f"{first_name.lower()}.{last_name.lower()}{random_number}{EMAIL_DOMAIN}"
        
        # Generate hashed email
        hashed_email = str(uuid.uuid4())
        
        return UserData(
            unique_snid=unique_snid,
            first_name=first_name,
            last_name=last_name,
            unique_email=unique_email,
            hashed_email=hashed_email,
            mkt_opt_in=self.generate_boolean_or_null(),
            explicit_choice=random.choice([True, False]),
            advertising_opt_in=self.generate_boolean_or_null(),
            third_party_prom=self.generate_boolean_or_null(),
            role=random.choice(AVAILABLE_ROLES),
            subjects=self.generate_subjects(),
            newsletters=self.generate_newsletters(),
            nature_india=self.generate_boolean_or_null(),
            nature_middle_east=self.generate_boolean_or_null(),
            nature_china=self.generate_boolean_or_null(),
            nature_newsletter=self.generate_boolean_or_null()
        )