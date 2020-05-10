from google.appengine.ext import db
from post import Post
from user import User


class Like(db.Model):
    """
        This class represents like entity in Google Datastore.
        Attributes:
            post (ReferenceProperty): This attribute represents
                post in which this like is exists.
            user (ReferenceProperty): This attribute represents like's owner.
            content (TextProperty): This attribute represents
                like's content. (liked or not)
    """
    post = db.ReferenceProperty(Post, collection_name='like_post')
    user = db.ReferenceProperty(User, collection_name='like_user')
    created = db.DateTimeProperty(auto_now_add=True)
