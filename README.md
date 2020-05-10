# Daily Blog

Daily Blog is a simple multi-user blog web application where users can sign in and post blog posts as well as like and comment on other posts made by other users.

This is my project for the [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) course [Intro to Backend](https://www.udacity.com/course/intro-to-backend--ud171).

Project Name: Multi User Blog.

You can view all of my Nanodegree projects from this repo [mohllal/udacity-fsnd](https://github.com/mohllal/udacity-fsnd).

### Prerequisites:
The application was built on [Google App Engine platform](https://cloud.google.com/appengine/docs/standard/python/download) using [Python 2.7](https://www.python.org/downloads/).
It uses [Google Cloud Datastore](https://cloud.google.com/appengine/docs/standard/python/datastore/) as the underlying database technology.

### Features:
 - Login/Signup.
 - CRUD Post operations.
 - CRUD Comment operations.
 - Like\Dislike to other posts.
 - Elegant UI.

### Usage:
1. Clone this repository to your desktop, go to the ```p3-daily-blog``` directory and run:
```python
dev_appserver.py .
```
**Note:** Ensure the you have both Python 2.7 and GAE SDK installed.

2. Go to [localhost:8080](http://localhost:8080) to see the application running and [localhost:8000](http://localhost:8000) for the admin console.

### Built With:
- [Bootstrap 3](http://getbootstrap.com/): Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.
- [JQuery](https://jquery.com/): jQuery is a fast, small, and feature-rich JavaScript library.
- [Milligram](http://milligram.io/): Milligram is a CSS framework that provides a minimal setup of styles for a fast and clean starting point.
- [Jinja2](http://jinja.pocoo.org/docs/2.9/): Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates.
- [webapp2](https://webapp2.readthedocs.io/en/latest/): webapp2 is a lightweight Python web framework compatible with Google App Engine’s webapp.

### License:
This software is licensed under the [Modified BSD License](https://opensource.org/licenses/BSD-3-Clause).