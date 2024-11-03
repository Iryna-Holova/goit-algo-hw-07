"""
This module implements a comment system for a blog post.

Classes:
    Comment: Represents a comment on a blog post.
"""


class Comment:
    """
    Represents a comment on a blog post.

    Attributes:
        text (str): The text of the comment.
        author (str): The author of the comment.
        replies (list): A list of replies to the comment.
        is_deleted (bool): Whether the comment is deleted or not.
    """

    def __init__(self, text, author):
        """
        Create a new comment with given text and author.

        Args:
            text (str): The text of the comment.
            author (str): The author of the comment.
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply_comment):
        """
        Add a reply to the comment.

        Args:
            reply_comment (Comment): The reply to add.
        """
        self.replies.append(reply_comment)

    def remove_reply(self):
        """
        Remove the last reply from the comment.
        """
        self.text = "This comment has been removed."
        self.is_deleted = True

    def display(self, level=0):
        """
        Display the comment with indentation and replies.

        Args:
            level (int): The indentation level.
        """
        indent = '    ' * level
        display_text = (
            f"{self.author}: {self.text}"
            if not self.is_deleted
            else f"[deleted]: {self.text}"
        )
        print(f"{indent}{display_text}")
        for reply in self.replies:
            reply.display(level + 1)


# Test example:
if __name__ == "__main__":
    root_comment = Comment("What a wonderful book!", "John")
    reply1 = Comment("The book was a disappointment :(", "Jane")
    reply2 = Comment("What's so wonderful about it?", "Mary")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("It was a waste of paper...", "Bill")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
