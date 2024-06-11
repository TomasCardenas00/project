import json
from datetime import datetime
from faker import Faker
import random

fake = Faker()

comments_list = [
    "Disappointing.", "Not impressed.", "Boring.", "Poorly written.", "I expected more.", "Lacks detail.", "Not engaging.", "Needs improvement.", #Negative Comments
    "Informative.", "Decent read.", "Not bad.", "It's okay.", "Average content.", "Could be better.", "Standard post.", "Thanks for sharing.", #Neutral Comments
    "Good post!", "Amazing!", "Love it!", "Very interesting.", "Great job!", "Fantastic!", "Excellent!", "Inspiring!" #Positive Comments
]

password_list = [
    'danish','cheesecake','sugar',
    'Lollipop','wafer','Gummies',
    'sesame','Jelly','beans',
    'pie','bar','Ice','oat'
]

def create_person_name():
    return fake.name()

def create_person_post():
    return fake.sentence()

def generate_likes():
    return random.random(0,1000000)

def generate_saves():
    return random.random(0,10000)

def create_comments():
    return random.choice(comments_list)

def create_birhtdate():
    return fake.date_of_birth()

def create_password():
    return random.choice(password_list)

def add_fake_users(num_users=10):
    users = []

    for _ in range(num_users):
        user = {
            "username": create_person_name().replace(" ", "_"),
            "password": create_password(),
            "profile": {
                "bio": fake.text(),
                "pfp": fake.image_url(),
                "birthday": str(create_birhtdate()),
                "posts": [
                    {
                        "text": create_person_post(),
                        "likes": generate_likes(),
                        "comments": [create_comments() for _ in range(random.randint(0, 5))],
                        "saved": generate_saves(),
                    } for _ in range(random.randint(1, 5))]
            }
        }
        users.append(user)

    with open("users.json", "w", encoding="UTF-8") as file:
        json.dump(users, file, indent=4)


