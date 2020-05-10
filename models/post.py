from google.appengine.ext import db
from user import User
from utilities import Utils


class Post(db.Model):
    """
        This class represents post entity in Google Datastore.
        Attributes:
            subject (StringProperty): This attribute represents post's subject.
            content (TextProperty): This attribute represents post's content.
            created (DateTimeProperty): This attribute represents
                post's create time.
            last_modified (DateTimeProperty): This attribute represents
                post's modify time.
            user (ReferenceProperty): This attribute represents post's owner.
            likes (IntegerProperty): This attribute represents number of likes on post.
            comments (IntegerProperty): This attribute represents number of comments on post.
        Functions:
            render(): returns post's content after replacing each
                linefeed with <br> HTML element.
    """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user = db.ReferenceProperty(User, collection_name='User.post_set')
    likes = db.IntegerProperty(default=0)
    comments = db.IntegerProperty(default=0)

    def render(self, current_user_id):
        key = db.Key.from_path('User', int(self.user.key().id()), parent=Utils.users_key())
        user = db.get(key)

        self._render_text = self.content.replace('\n', '<br>')
        return Utils.render_str("single-post.html", post=self, current_user_id=current_user_id, author=user.name)

    @classmethod
    def by_id(cls, uid):
        return Post.get_by_id(uid, parent=Utils.blog_key())
