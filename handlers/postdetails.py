from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils


class PostDetailsHandler(Handler):
    """
        This class represents request handler for the main post page.
        It checks whether the specified post's id is valid or not.
        If it's valid it renders its content
            (subject, content, owner, likes, comments).
        It can handle two post requests (comment and like).
    """
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        # Check if the post id is valid
        if not post:
            self.error(404)
            return

        self.render("post-details.html", post=post,
                    user=self.user, comments=post.comment_post)
