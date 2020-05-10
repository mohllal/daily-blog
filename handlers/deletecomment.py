from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils


class DeleteCommentHandler(Handler):
    """
        This class represents request handler for comment delete action.
        It checks if the requested comment id is valid and
        if the logged in user the permission to do this.
    """
    def get(self, post_id, comment_id):
        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        postKey = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(postKey)

        commentKey = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(commentKey)

        # Check if the comment id is valid and
        # if the logged in user has the permission to edit it
        if not comment or \
                not comment.user.key().id() == self.user.key().id():
            self.error(404)
            return

        post.comments -= 1

        comment.delete()
        post.put()

        self.redirect('/blog/' + str(post_id))
