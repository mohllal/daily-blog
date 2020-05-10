from handlers.handler import Handler
from models.post import Post
from utilities import Utils


class NewPostHandler(Handler):
    """
        This class represents request handler for the new post form.
        It checks whether the user is logged in or not.
        If the user is logged in, it takes form input
            values and create a new post.
    """
    def get(self):
        # Check if the user is logged in or not
        if self.user:
            self.render("post-form.html")
        else:
            return self.redirect("/login")

    def post(self):
        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        # Get form input values (subject - content)
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            post = Post(parent=Utils.blog_key(), subject=subject,
                        content=content, user=self.user)
            post.put()
            return self.redirect('/blog/%s' % str(post.key().id()))
        elif not subject:
            error = "Subject must be provided!"
            self.render("post-form.html", subject=subject,
                        content=content, error=error)
        elif not content:
            error = "Content must be provided!"
            self.render("post-form.html", subject=subject,
                        content=content, error=error)
        else:
            error = "Subject and content must be provided!"
            self.render("post-form.html", subject=subject,
                        content=content, error=error)
