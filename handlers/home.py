from handlers.handler import Handler
from models.post import Post


class HomeHandler(Handler):
    """
        This class represents request handler for main blog page.
        It fetches all posts from Google Datastore and renders it.
    """
    def get(self):
        posts = Post.all().order('-created')
        self.render('home.html', posts=posts)
