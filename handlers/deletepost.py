from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils


class DeletePostHandler(Handler):
    """
        This class represents request handler for post delete action.
        It checks if the requested post id is valid and
        if the logged in user has this permission.
    """
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        # Check if the post id is valid or
        # the logged in user has this permission
        if not post or \
                not post.user.key().id() == self.user.key().id():
            self.error(404)
            return

        post.delete()
        self.redirect('/')
