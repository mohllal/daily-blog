from google.appengine.ext import db
from models.comment import Comment
from handlers.handler import Handler
from utilities import Utils


class NewCommentHandler(Handler):

    def get(self, post_id):
        if not self.user:
            self.redirect('/login')
        else:
            self.render("comment-form.html", post_id=post_id)

    def post(self, post_id):
        if not self.user:
            self.redirect('/login')
            return

        content = self.request.get('content')

        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        c = Comment(parent=key, user=self.user, content=content, post=post)
        post.comments += 1

        c.put()
        post.put()

        self.redirect('/blog/' + str(post_id))
