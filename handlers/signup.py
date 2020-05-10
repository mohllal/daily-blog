from handlers.handler import Handler
from models.user import User
from utilities import Utils


class SignupHandler(Handler):
    """
        This class represents request handler for signup form.
        Attributes:
            username (String): This attribute represents inputted username.
            password (String): This attribute represents inputted password.
            verify (String): This attribute represents inputted
                verification password.
            phone (String): This attribute represents inputted phone.
            address (String): This attribute represents inputted address.
            email (String): This attribute represents inputted email.
    """

    def get(self):
        # Redirect if the user is already logged in
        if self.user:
            return self.redirect('/')

        self.render("signup-form.html")

    def post(self):
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.phone = self.request.get('phone')
        self.address = self.request.get('address')
        self.email = self.request.get('email')

        params = dict(username=self.username,
                      email=self.email, phone=self.phone,
                      address=self.address)

        if not Utils.valid_username(self.username):
            params['error'] = "That's not a valid username."
            have_error = True

        if not Utils.valid_password(self.password):
            params['error'] = "That wasn't a valid password."
            have_error = True

        elif self.password != self.verify:
            params['error'] = "Your passwords didn't match."
            have_error = True

        if not Utils.valid_email(self.email):
            params['error'] = "That's not a valid email."
            have_error = True

        if not Utils.valid_phone(self.phone):
            params['error'] = "That's not a valid phone number."
            have_error = True

        if not Utils.valid_address(self.address):
            params['error'] = "That's not a valid address."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()

    def done(self):
        # Check if the user is already exists
        user = User.by_name(self.username)
        if user:
            msg = 'That user is already exists!'
            self.render('signup-form.html', error=msg)
        else:
            user = User.register(self.username, self.password, self.email)
            user.put()
            self.login(user)
            self.redirect('/')
