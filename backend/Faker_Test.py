import json
from datetime import datetime
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Predefined list of comments
comments_list = [
    "Disappointing.", "Not impressed.", "Boring.", "Poorly written.", "I expected more.", "Lacks detail.", "Not engaging.", "Needs improvement.", # Negative Comments
    "Informative.", "Decent read.", "Not bad.", "It's okay.", "Average content.", "Could be better.", "Standard post.", "Thanks for sharing.", # Neutral Comments
    "Good post!", "Amazing!", "Love it!", "Very interesting.", "Great job!", "Fantastic!", "Excellent!", "Inspiring!" # Positive Comments
]

# Predefined list of passwords
password_list = [
    'danish', 'cheesecake', 'sugar',
    'Lollipop', 'wafer', 'Gummies',
    'sesame', 'Jelly', 'beans',
    'pie', 'bar', 'Ice', 'oat'
]

def create_person_name():
    """
    This fucntion generates a fake person's name using Faker.

    Returns:
        str: A fake name.
    """
    return fake.name()

def create_person_post():
    """
    This fucntion generates a fake post text using Faker.

    Returns:
        str: A fake sentence.
    """
    return fake.sentence()

def generate_likes():
    """
    This fucntion generates a random number of likes between 0 and 1,000,000.

    Returns:
        int: A random number of likes.
    """
    return random.randint(0, 1000000)

def generate_saves():
    """
    This fucntion generates a random number of saves between 0 and 10,000.

    Returns:
        int: A random number of saves.
    """
    return random.randint(0, 10000)

def create_comments():
    """
    This fucntion selects a random comment from the predefined comments list.

    Returns:
        str: A random comment.
    """
    return random.choice(comments_list)

def create_birthdate():
    """
    This fucntion generates a fake birthdate using Faker.

    Returns:
        datetime.date: A fake date of birth.
    """
    return fake.date_of_birth()

def create_password():
    """
    This fucntion selects a random password from the predefined password list.

    Returns:
        str: A random password.
    """
    return random.choice(password_list)

def add_fake_users(num_users=10):
    """
    This fucntion generates a list of fake users with random attributes and saves it to a JSON file.

    Args:
        num_users (int): The number of fake users to generate. Default is 10.
    """
    users = []

    for _ in range(num_users):
        user = {
            "username": create_person_name().replace(" ", "_"),
            "password": create_password(),
            "profile": {
                "bio": fake.text(),
                "pfp": fake.image_url(),
                "birthday": str(create_birthdate()),
                "posts": [
                    {
                        "text": create_person_post(),
                        "likes": generate_likes(),
                        "comments": [create_comments() for _ in range(random.randint(0, 5))],
                        "saved": generate_saves(),
                    } for _ in range(random.randint(1, 5))
                ]
            }
        }
        users.append(user)

    with open("users.json", "w", encoding="UTF-8") as file:
        json.dump(users, file, indent=4)

