"""
This module contains the Timeline class.

Author: Tomás Cardenas Benitez <20221020021> and Juan Jesus Poveda <20202020128>
"""

import json
import random

class Timeline:
    def __init__(self, users_file='users.json'):
        """
        This function initializes the Timeline object.

        Atributtes:
            users_file (str, optional): The path to the JSON file containing user profiles and posts. Defaults to 'users.json'.
            posts: The list of post returned form the file 'users.JSON'
            current_index: The index of a shuffled list of posts

        Methods:
            load_users(): This method loads user profiles from the JSON file.
            load_posts(): This method loads posts from user profiles.
            display_posts: This function displays the next post in the timeline.
            get_current_post_info: This function helps by getting information about the current post.

        """
        self.users_file = users_file
        self.posts = self.load_posts()
        self.current_index = -1  

    def load_users(self):
        """
        This method loads user profiles from the JSON file.

        Returns:
            list: A list of user profiles.
        """
        try:
            with open(self.users_file, 'r', encoding='UTF-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return []

    def load_posts(self):
        """
        This method loads posts from user profiles.

        Returns:
            list: A list of post dictionaries containing username, text, likes, saved, and comments.
        """
        users = self.load_users()
        posts = []

        for user in users:
            username = user.get('username')
            user_posts = user.get('profile', {}).get('posts', [])
            for post in user_posts:
                post['username'] = username
                posts.append(post)

        random.shuffle(posts)
        return posts

    def display_post(self):
        """
        This function displays the next post in the timeline.
        """
        self.current_index += 1

        if self.current_index >= len(self.posts):
            print("No hay más posts disponibles.")
            return

        post = self.posts[self.current_index]
        print(f"Post {self.current_index + 1}:")
        print(f"Username: {post['username']}")
        print(f"Text: {post['text']}")
        print(f"Likes: {post['likes']}")
        print(f"Saved: {post['saved']}")
        print("Comments:")
        for comment in post["comments"]:
            print(f"- {comment}")
        print("\n" + "-"*20 + "\n")

    def get_current_post_info(self):
        """
        This function helps by getting information about the current post.

        Returns:
            dict: A dictionary containing information about the current post (username, text, likes, saved, comments)
            None: if there are no more posts.
            
        """
        if self.current_index >= len(self.posts):
            print("No hay más posts disponibles.")
            return None

        post = self.posts[self.current_index]
        post_info = {
            "Username": post['username'],
            "Text": post['text'],
            "Likes": post['likes'],
            "Saved": post['saved'],
            "Comments": post["comments"]
        }
        return post_info

        