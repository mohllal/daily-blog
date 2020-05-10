#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from handlers.home import HomeHandler
from handlers.signup import SignupHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler

from handlers.postdetails import PostDetailsHandler
from handlers.newpost import NewPostHandler
from handlers.deletepost import DeletePostHandler
from handlers.editpost import EditPostHandler

from handlers.newcomment import NewCommentHandler
from handlers.deletecomment import DeleteCommentHandler
from handlers.editcomment import EditCommentHandler

from handlers.newlike import NewLikeHandler
from handlers.newdislike import NewDislikeHandler


app = webapp2.WSGIApplication([('/', HomeHandler),
                               ('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ('/blog/([0-9]+)', PostDetailsHandler),
                               ('/blog/newpost', NewPostHandler),
                               ('/blog/delete/([0-9]+)', DeletePostHandler),
                               ('/blog/edit/([0-9]+)', EditPostHandler),
                               ('/blog/([0-9]+)/newcomment', NewCommentHandler),
                               ('/blog/([0-9]+)/deletecomment/([0-9]+)', DeleteCommentHandler),
                               ('/blog/([0-9]+)/editcomment/([0-9]+)', EditCommentHandler),
                               ('/blog/([0-9]+)/newlike', NewLikeHandler),
                               ('/blog/([0-9]+)/newdislike', NewDislikeHandler),
                               ],
                              debug=True)
