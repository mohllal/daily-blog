from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils


class EditPostHandler(Handler):
    """
        This class represents request handler for post edit action.
        It checks if the requested post id is valid and if
            the logged in user has this permission.
        It handles one post request to edit post (subject and content).
    """
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        # Check if the post id is valid and if
        # the logged in user has the permission to edit it
        if not post or \
                not post.user.key().id() == self.user.key().id():
            self.error(404)
            return

        self.render("post-form.html", subject=post.subject,
                    content=post.content)

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/')

        # Check if the post id is valid
        # or the logged in user has this permission
        if not post or not post.user.key().id() == self.user.key().id():
            self.error(404)
            return

        # Get form input values (subject and content)
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            post.subject = subject
            post.content = content
            post.put()
            return self.redirect('/blog/' + str(post_id))
        else:
            error = "Subject and content must be provided!"
            self.render("post-form.html", subject=subject,
                        content=content, error=error)
