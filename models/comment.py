from google.appengine.ext import db
from post import Post
from user import User


class Comment(db.Model):
    """
        This class represents comment entity in Google Datastore.
        Attributes:
            post (ReferenceProperty): This attribute represents post
                in which this comment is exists.
            user (ReferenceProperty): This attribute
                represents comment's owner.
            content (TextProperty): This attribute
                represents comment's content.
        Functions:
            render(): returns comment's content after replacing
                each linefeed with <br> HTML element.
    """
    post = db.ReferenceProperty(Post, collection_name='comment_post')
    user = db.ReferenceProperty(User, collection_name='comment_user')
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def render(self):
        return self.content.replace('\n', '<br>')
