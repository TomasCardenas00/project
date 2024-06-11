"""
This module contains the Post and PostFactory classes and
VideoPost, TextPost and VideoPost subclasses.

Author: Tomás Cardenas Benitez <20221020021> and Juan Jesus Poveda <20202020128>
"""


class Post:
    """
    This class provides the basic definition of a user.

    Atributes:
        text: An string containing information about the post made.
        likes: An int containing the amount of likes made to a post.
        comments: A list containing the comments made to a post.
        saved: An int containing the amount of saves made to a post.
        reports: An int containing the amount of reports made to a post.

    Methods:
        __init__: This method initializes an User object with the provided username.
        to_dict: This method converts the post object to a dictionary.
        convert_dict_to_post: This method converts a dictionary to a Post object.
        like_post: This method increments the number of likes for the post.
        save_post: This method increments the number of saves for the post.
        add_comment: This method adds a comment to the comments' list
        report_post: This method increments the number of reports for the post.
    """
    def __init__(self, text: str, likes: int, comments: list, saved: int, reports:int):
        self.text = text
        self.likes = likes
        self.comments = comments
        self.saved = saved
        self.reports = reports

    def to_dict(self):
        """
        This method converts the post object to a dictionary.

        Returns:
            dict: A dictionary representation of the post.
        """
        return {
            "text": self.text,
            "likes": self.likes,
            "comments": self.comments,
            "saved": self.saved
        }
    
    def convert_dict_to_post(self, post_dict):
        """
        This method converts a dictionary to a Post object.

        Args:
            post_dict (dict): A dictionary containing post information.

        Returns:
            Post: A Post object created from the dictionary.
        """
        text = post_dict.get('Text', '')
        likes = post_dict.get('Likes', 0)
        comments = post_dict.get('Comments', [])
        saved = post_dict.get('Saved', 0)

        return Post(text, likes, comments, saved)
    
    def like_post(self):
        """This method increments the number of likes for the post."""
        self.likes += 1

    def save_post(self):
        """This method increments the number of saves for the post."""
        self.saved += 1

    def add_comment(self, comment: str):
        """This method adds a comment to the comments' list"""
        self.comments.append(comment)

    def report_post(self):
        """This method increments the number of reports for the post."""
        self.reports += 1
    
class TextPost(Post):
    """This class represents a subclass representing a text post."""

class ImagePost(Post):
    """This class represents a subclass representing a image post."""

class VideoPost(Post):
    """This class represents a subclass representing a video post."""

class PostFactory:
    """This class creates a post object based on the provided post type."""
    @staticmethod
    def create_post(post_type: str, text:str) -> Post:
        """
        This class creates a post object based on the provided post type.

        Args:
            post_type (str): The type of post to create.
            text (str): The text content of the post.

        Returns:
            Post: A Post object of the specified type.
        
        Raises:
            ValueError: If an invalid post type is provided.
        """
        if post_type == "1":
            return TextPost(text, 0, [], 0, 0)
        elif post_type == "2":
            return ImagePost(text, 0, [], 0, 0)
        elif post_type == "3":
            return VideoPost(text, 0, [], 0, 0)
        else:
            raise ValueError("Tipo de publicación no válido")
        
