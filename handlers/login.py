from models.user import User
from handlers.handler import Handler


class LoginHandler(Handler):
    """
        This class represents request handler for login form.
        It checks the inputted user information (username
        and password) against Google Datastore
    """
    def get(self):
        # Redirect if the user is already logged in
        if self.user:
            return self.redirect('/')

        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        # check if the user is already registered
        u = User.login(username, password)
        if u:
            self.login(u)
            return self.redirect('/')
        else:
            msg = 'Invalid login!'
            self.render('login-form.html', error=msg)
