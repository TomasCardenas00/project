"""
This module contains the SocialMedia Facade class, making use of the facade pattern design.

Author: Tomás Cardenas Benitez <20221020021> and Juan Jesus Poveda <20202020128>
"""

import json
from Post import Post, PostFactory
from TimeLine import Timeline
from User import Authenticator


class SocialMediaFacade:
    """
    This class provides the basic definition of a user.

    Attributes:
        None

    Methods:
        __init__: This method initializes a SocialMediaFacade object with the provided username and password.
        login: This method authenticates the user.
        create_post: This method creates a new post.
        add_post: This method adds a post to a user's profile.
        add_user: This method adds a new user to the platform.
        like_post: This method increments the like count for a post.
        save_post: This method increments the save count for a post.
        add_comment: This method adds a comment to a post.
        report_post: This method reports a post.
        block_user: This method blocks a user.
        quote_post: This method quotes a post.
        report_user: This method reports a user.
        repost_post: This method reposts a post.
        mute_user: This method mutes a user.
        show_posts: This method displays posts in the timeline.
        get_current_post: This method returns information about the current post.
        get_current_user: This method returns the username of the current user.
    """
    def __init__(self,username,password):
        self.authenticator = Authenticator(username,password)
        self.timeline = Timeline()
        self.postFactory = PostFactory

    def login(self):
        """This method authenticates the user."""
        return self.authenticator.authenticate()

    def create_post(self, post_type:str, text:str):
        """
        This method creates a new post.
        Args:
            post_type (str): The type of post (e.g., text, image, video).
            text (str): The content of the post.

        Returns:
            Post: The created post object.
        """
        post = self.postFactory.create_post(post_type,text)
        return post

    def add_post(self,username, post: Post):
        """
        This method adds a post to a user's profile
        Args:
            username (str): The username of the user.
            post (Post): The post object to add.
        """
        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return

        for user in users:
            if user["username"] == username:
                user["profile"]["posts"].append(post.to_dict())
                break
        else:
            print("Usuario no encontrado.")
            return

    def add_user(self, username: str, password: str, bio: str, pfp: str, birthday: str, posts=[]):
        """
        This method adds a new user to the platform.
         Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            bio (str): The biography of the new user.
            pfp (str): The profile picture URL of the new user.
            birthday (str): The birthday of the new user.
            posts (list, optional): The list of posts of the new user. Defaults to an empty list.
        """
        new_user = {
            "username": username,
            "password": password,
            "profile": {"bio": bio, "pfp": pfp, "birthday": birthday, "posts": posts},
        }

        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        if not users:
            users.append(new_user)
            print("Usuario posible")        
        else:
            for user in users:
                if new_user["username"] == user["username"]:
                    print("Usuario ya existente")
                else:
                    users.append(new_user)
                    print("Usuario posible")
            
        with open("users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)
        print("Usuario añadido exitosamente")

    def add_post(self, username:str, post: Post):
        """
        This method adds a post to a user's profile.
        Args:
            username (str): The username of the user.
            post (Post): The post object to add.
        """
        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return

        for user in users:
            if user["username"] == username:
                user["profile"]["posts"].append(post.to_dict())
                break
        else:
            print("Usuario no encontrado.")
            return

        with open("users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)
        print("Post añadido exitosamente")        

    def like_post(self, post: Post):
        """
        This method increments the like count for a post.

        Args:
            post (Post): The post object to like.
        """
        post.like_post()

    def save_post(self, post: Post):
        """
        This method increments the saves count for a post.

        Args:
            post (Post): The post object to save.
        """
        post.save_post()

    def add_comment(self, post: Post, comment: str):
        """
        This method adds a comment to a post.

        Args:
            post (Post): The post object to comment on.
            comment (str): The comment to add.
        """
        post.add_comment(comment)

    def report_post(self, post: Post):
        """
        This method reports a post.

        Args:
            post (Post): The post object to report.
        """
        post.report_post()

    def block_user(self, username: str, blckd_username: str, blocked_users=[]):
        """
        This method blocks a user.

        Args:
            username (str): The username of the user performing the block action.
            blckd_username (str): The username of the user to be blocked.
            blocked_users (list, optional): A list of previously blocked users. Defaults to an empty list.
        """
        new_format = {
            "username": username,
            "blocked_users": blocked_users
        }
        try:
            with open("blocked_users.json", "r", encoding="UTF-8") as file:
                blck_users = json.load(file)
        except FileNotFoundError:
            blck_users = []

        if not blck_users:
            blck_users.append(new_format)
        else:
            for user in blck_users:
                if new_format["username"] == username:
                    user["blocked_users"].append(blckd_username)
                    break
                else:
                    print("Usuario no encontrado.")
                    return
        
        with open("blocked_users.json", "w", encoding="UTF-8") as file:
            json.dump(blck_users, file, indent=4)
        print("Usuario bloqueado")

    def quote_post(self, username: str, post:Post, citation: str):
        """This method quotes a post.

        Args:
            username (str): The username of the user quoting the post.
            post (Post): The post object to be quoted.
            citation (str): The citation or additional text accompanying the quoted post.
        """

        new_cited_post = {
            "username": post.username,
            "text": post.text,
            "likes": post.likes,
            "comments": post.comments,
            "saved": post.saved,
            "citation": citation
        }
        
        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return

        for user in users:
            if user["username"] == username:
                user["profile"]["posts"].append(new_cited_post)
                break
        else:
            print("Usuario no encontrado.")
            return

        with open("users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)
        print("Post añadido exitosamente")
    
    def report_user(self, reported_username: str, reason: str):
        """
        This method reports a user.

        Args:
            reported_username (str): The username of the user being reported.
            reason (str): The reason for reporting the user.
        """
        report = {
            "reported_username": reported_username,
            "reason": reason
        }

        try:
            with open("reports.json", "r", encoding="UTF-8") as file:
                reports = json.load(file)
        except FileNotFoundError:
            reports = []

        reports.append(report)

        with open("reports.json", "w", encoding="UTF-8") as file:
            json.dump(reports, file, indent=4)
        print("Usuario reportado exitosamente")

    def repost_post(self, username : str, original_user: str, post: Post):
        """
        This method reposts a post.

        Args:
            username (str): The username of the user reposting the post.
            original_user (str): The username of the original poster of the post.
            post (Post): The post object to be reposted.
        """

        new_repost = {
            "username": username,
            "original_user": original_user,
            "post": {
                "text": post.text,
                "likes": post.likes,
                "comments": post.comments,
                "saved": post.saved
            }
        }
        try:
            with open("users.json", "r", encoding="UTF-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return

        for user in users:
            if user["username"] == username:
                user["profile"]["posts"].append(new_repost)
                break
        else:
            print("Usuario no encontrado.")
            return

        with open("users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, indent=4)
        print("Post añadido exitosamente")

    def mute_user(self, username: str, muted_username: str):
        """
        This method mutes a user.

        Args:
            username (str): The username of the user performing the mute action.
            muted_username (str): The username of the user to be muted.
        """
        new_mute_entry = {
            "username": username,
            "muted_users": [muted_username]
        }

        try:
            with open("muted_users.json", "r", encoding="UTF-8") as file:
                muted_users = json.load(file)
        except FileNotFoundError:
            muted_users = []

        for user in muted_users:
            if user["username"] == username:
                user["muted_users"].append(muted_username)
                break
        else:
            muted_users.append(new_mute_entry)

        with open("muted_users.json", "w", encoding="UTF-8") as file:
            json.dump(muted_users, file, indent=4)
        print("Usuario silenciado exitosamente")

    def show_posts(self):
        """
        This method displays posts in the timeline.
        """
        self.timeline.display_post()

    def get_current_post(self):
        """
        This method returns information about the current post

        Returns:
            Post: The current post object.
        """
        post_info = self.timeline.get_current_post_info()

        if post_info is None:
            print("No hay un post disponible en el timeline.")
            return None

        current_post = Post(
            text=post_info['Text'],
            likes=post_info['Likes'],
            comments=post_info['Comments'],
            saved=post_info['Saved'],
            reports=0
        )

        return current_post
    
    def get_current_user(self):
        """
        This method returns the username of the user who made the current post.

        Returns:
            str: The username of the current post's author.
        """
        user_info = self.timeline.get_current_post_info()
        username = user_info['Text']
        return username

