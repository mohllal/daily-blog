from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils


class EditCommentHandler(Handler):
    """
        This class represents request handler for comment edit action.
        It checks if the requested comment id is valid and
            if the logged in user has this permission.
        It handles one post request to edit comment (content).
    """
    def get(self, post_id, comment_id):
        # Check if the user is currently logged in
        if not self.user:
            return self.redirect("/login")

        postKey = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())

        commentKey = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(commentKey)

        # Check if the comment id is valid and if
        # the logged in user has the permission to edit it
        if not comment or \
                not comment.user.key().id() == self.user.key().id():
            self.error(404)
            return

        self.render("comment-form.html",
                    content=comment.content, post_id=post_id)

    def post(self, post_id, comment_id):
        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        postKey = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())

        commentKey = db.Key.from_path('Comment', int(comment_id), parent=postKey)
        comment = db.get(commentKey)

        # Check if the comment id is valid and if
        # the logged in user has the permission to edit it
        if not comment or \
                not comment.user.key().id() == self.user.key().id():
            self.error(404)
            return

        # Get form input value (content)
        content = self.request.get('content')

        if content:
            comment.content = content
            comment.put()
            return self.redirect('/blog/' + str(post_id))
        else:
            error = "Content must be provided!"
            self.render("comment-form.html",
                        content=content, error=error, post_id=post_id)
