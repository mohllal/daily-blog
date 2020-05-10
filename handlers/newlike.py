from google.appengine.ext import db
from handlers.handler import Handler
from models.like import Like
from utilities import Utils


class NewLikeHandler(Handler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user.key().id():
            error = "You cannot like your own post."
            self.render('base.html', access_error=error)

        elif not self.user:
            self.redirect('/login')

        else:
            like = Like.all().filter('user =', self.user).filter('post =', post).get()

            if like:
                self.redirect('/blog/' + str(post.key().id()))

            else:
                like = Like(parent=key, user=self.user,
                            post=post)

                post.likes += 1

                like.put()
                post.put()

                self.redirect('/blog/' + str(post.key().id()))
