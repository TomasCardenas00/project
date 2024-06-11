"""
This module contains the User and Authenticator classes.

Author: Tomás Cardenas Benitez <20221020021> and Juan Jesus Poveda <20202020128>
"""


import json

class User:
    """
    This class provides the basic definition of a user.

    Atributes:
        __username: A string conaining the user's username

    Methods:
        __init__: This method initializes an User object with the provided username.
        get_username: This method returns the username.
    """
    def __init__(self, username: str):
        self.__username = username

    def get_username(self):
        """
        This method returns the username.
        """
        return self.__username


class Authenticator:
    """
    This class provides methods in order to authenticate de log in of a user.

    Methods:
        __init__: This methodd initializes an Authenticator object with the provided username and password.
        authenticate: This class authenticates the user by comparing the provided credentials with those stored in a JSON file.
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def authenticate(self) -> bool:
        """
        This method authenticates the user by comparing the provided credentials with those stored in a JSON file.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            print("The user file was not found.")
            return False

        for user in users:
            if user["username"] == self.username and user["password"] == self.password:
                return True

        print("Incorrect username or password")
        return False

