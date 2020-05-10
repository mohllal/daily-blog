from google.appengine.ext import db
from handlers.handler import Handler
from utilities import Utils
from models.like import Like


class NewDislikeHandler(Handler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Utils.blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user.key().id():
            error = "You cannot dislike your own post."
            self.render('base.html', access_error=error)

        elif not self.user:
            self.redirect('/login')

        else:
            l = Like.all().filter('user =', self.user.key()).filter('post =', post.key()).get()

            if l:
                l.delete()
                post.likes -= 1
                post.put()

                self.redirect('/blog/' + str(post.key().id()))
            else:
                self.redirect('/blog/' + str(post.key().id()))
