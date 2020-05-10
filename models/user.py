from google.appengine.ext import db
from utilities import Utils


class User(db.Model):
    """
        User class represents user entity in Google Datastore
        Attributes:
            name (StringProperty): This attribute represents user's name
            pw_hash (StringProperty): This attribute represents hashed
                user's password
            phone (PhoneNumberProperty): This attribute represents user's phone
            address (StringProperty): This attribute represents user's address
            email (StringProperty): This attribute represents user's email
        Functions:
            by_id(cls, uid): returns a user instance with id = uid
            by_name(cls, name): returns the first user
                instance with name = name
            by_address(cls, address): returns users instances
                with address = address
            register(cls, name, pw, phone=None, address=None, email=None):
                returns a new user instance to register
            login(cls, name, pw): returns a user instance after
                verifying his name and password
    """
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    phone = db.StringProperty()
    address = db.StringProperty()
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent=Utils.users_key())

    @classmethod
    def by_name(cls, name):
        return cls.all().filter('name =', name).get()

    @classmethod
    def by_address(cls, address):
        cls.all().filter('address =', address)

    @classmethod
    def register(cls, name, pw, phone=None, address=None, email=None):
        pw_hash = Utils.make_pw_hash(name, pw)
        return cls(parent=Utils.users_key(),
                   name=name,
                   pw_hash=pw_hash,
                   phone=phone,
                   address=address,
                   email=email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and Utils.valid_pw(name, pw, u.pw_hash):
            return u