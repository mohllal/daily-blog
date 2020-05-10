from handlers.handler import Handler


class LogoutHandler(Handler):
    """
        This class represents request handler for logout.
        It deletes user cookie from the browser.
    """
    def get(self):
        # Check if the user is currently logged in
        if not self.user:
            return self.redirect('/login')

        self.logout()
        return self.redirect('/')
