from google.appengine.ext import db
import jinja2
import os
import random
import re
import hmac
import hashlib
from string import letters


class Utils:
    """
        This class contains all the static helper functions.
    """

    # Setup Jinja2 environment and specify templates folder
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        autoescape=True)

    # Random string (10 characters) which used in hashing cookies.
    secret = ''.join(random.choice(letters) for count in xrange(10))

    # Render template with the given parameters
    @staticmethod
    def render_str(template, **params):
        t = Utils.jinja_env.get_template(template)
        return t.render(params)

    # Model keys
    @staticmethod
    def users_key(group='default'):
        return db.Key.from_path('users', group)

    @staticmethod
    def blog_key(name='default'):
        return db.Key.from_path('blogs', name)

    # Hash cookie value using HMAC algorithm
    @staticmethod
    def make_secure_val(val):
        return '%s|%s' % (val, hmac.new(Utils.secret, val).hexdigest())

    # Check if the cookie value is valid
    @staticmethod
    def check_secure_val(secure_val):
        val = secure_val.split('|')[0]
        if secure_val == Utils.make_secure_val(val):
            return val

    # Generate random salt string (5 characters)
    @staticmethod
    def make_salt(length=5):
        return ''.join(random.choice(letters) for count in xrange(length))

    # Hash user password using sha256 algorithm
    @staticmethod
    def make_pw_hash(name, pw, salt=None):
        if not salt:
            salt = Utils.make_salt()
        h = hashlib.sha256(name + pw + salt).hexdigest()
        return '%s|%s' % (salt, h)

    # Check password hash value
    @staticmethod
    def valid_pw(name, password, h):
        salt = h.split('|')[0]
        return h == Utils.make_pw_hash(name, password, salt)

    # Organize user entities under an ancestor element
    @staticmethod
    def users_key(group='default'):
        return db.Key.from_path('users', group)

    # Check the username value against regular expression
    @staticmethod
    def valid_username(username):
        # Username regular expression
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username and USER_RE.match(username)

    # Check the password value against regular
    @staticmethod
    def valid_password(password):
        # Password regular expression
        PASS_RE = re.compile(r"^.{3,20}$")
        return password and PASS_RE.match(password)

    # Check the phone value against regular expression
    @staticmethod
    def valid_phone(phone):
        # Phone regular expression
        PHONE_RE = re.compile(r"^[0-9]+.{6,10}$")
        return not phone or PHONE_RE.match(phone)

    # Check the address value against regular expression
    @staticmethod
    def valid_address(address):
        # Address regular expression
        ADDRESS_RE = re.compile(r"^[a-zA-Z]{4,20}$")
        return not address or ADDRESS_RE.match(address)

    # check the email value against regular expression
    @staticmethod
    def valid_email(email):
        # Email regular expression
        EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return not email or EMAIL_RE.match(email)
