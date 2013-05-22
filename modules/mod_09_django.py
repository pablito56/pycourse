#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod: django module
'''
#==========================================================================================
#
#  WARNING!
#
#    All sentences that start with '>>>' should be executed from a command-line
#
#==========================================================================================
try:
    import shutil; shutil.rmtree('mysite')
except OSError:
    pass


#==========================================================================================
#
#  "Django is a high-level Python Web framework that encourages rapid development and clean,
#   pragmatic design" - www.djangoproject.com
#
#  There are many other web-frameworks like flask, bottle, etc. Django is the one that it is
#  in the current Tech Plan.
#
#  1. Installation
#  2. Creating an Application
#  3. manage.py script
#  4. settings
#  5. models
#  6. url dispatching
#  7. views
#  8. middlewares
#  9. unit testing
# 10. django rest framework
#
#==========================================================================================



#==========================================================================================
#
#   1. Installation
#
#==========================================================================================


# just as simple as any other python module, use pip to install it
# from a bash console within the python activated
# >>> pip install django


# Once installed check that it is properly installed
import django;
print(django.get_version())


#==========================================================================================
#
#  2. Creating an Application
#
#       - An app in django is a module that does something
#       - A project is a configuration with some related apps that makes a web site
#
#   WARNING: check out the recommended folder structure in a Django project
#       https://colabora.pdi.inet/kbportal/PLCwiki/Guidelines/DEV/Standard%20directory%20structure%20for%20projects/in%20Python/Django.aspx
#
#==========================================================================================

# To create the scaffold for a django project, use the django-admin.py script
# >>> django-admin.py startproject mysite


# It generates the following tree structure
# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py


#==========================================================================================
#
#   3. The django-admin.py and manage.py scripts
#
#   - django-admin.py is an admin command-line utility for administrative tasks.
#       - It is on your path if django has been installed with setup.py utility (like pip does)
#   - when creating an project, manage.py is created providing a thin layer for django-admin.py
#       - it puts your project on sys.path
#       - it sets DJANGO_SETTINGS_MODULE environment variable so it points to your project settings.py
#
#   More Info: https://docs.djangoproject.com/en/1.5/ref/django-admin/
#==========================================================================================


#==========================================================================================
#
#  most important comamnds
#    manage.py startapp
#       Creates a Django app directory structure for the given app name in the current
#       directory or the given destination.
#
#    manage.py sqlall
#       Prints the CREATE TABLE and initial-data SQL statements for the given app name(s).
#
#    manage.py shell
#       Starts the Python interactive interpreter
#
#    manage.py syncdb
#       Creates the database tables for all apps in INSTALLED_APPS whose tables have not
#       already been created.
#       Use this command when you’ve added new applications to your project and want to install
#       them in the database.
#       This includes any apps shipped with Django that might be in INSTALLED_APPS by default.
#       WARNING: syncdb will only create tables for models which have not yet been installed.
#           It will never issue ALTER TABLE statements to match changes made to a model class
#           after installation. Check South 3rd party package ( http://south.aeracode.org/ )
#
#    manage.py test
#       Runs tests for all installed models.
#==========================================================================================


# let's create an application inside the project

# >>> python manage.py startapp polls


# This has created the following structure
#
# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py
#         polls/
#           __init__.py
#           models.py
#           tests.py
#           views.py


#==========================================================================================
#
#  4. settings
#
#==========================================================================================


# A settings file is just a Python module with module-level variables
# When you use Django, you have to tell it which settings you’re using.
# Do this by using an environment variable, DJANGO_SETTINGS_MODULE.

# The value of DJANGO_SETTINGS_MODULE should be in Python path syntax, e.g. mysite.settings.
# Note that the settings module should be on the Python import search path.

# Let's setup a proper configuration for production and development configuration


# 1. Identify a global settings file and split different conf in a production.py and development.py
# mod_django_example/
#     manage.py
#     mod_django_example/
#         __init__.py
#         settings.py
#         development.py
#         production.py
#         urls.py
#         wsgi.py


# 2. remove DATABASES section from settings.py and add it to development.py with sqllite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mod_django_example.db',
    }
}


# 3. and production.py with mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mod_django_example',
        'USER': 'user',
        'PASSWORD': 'user',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# 4. if using mysql, database should be created manually before using it

"""
CREATE DATABASE IF NOT EXISTS mod_django_example DEFAULT CHARACTER SET 'UTF8' DEFAULT COLLATE 'UTF8_GENERAL_CI';
GRANT ALL PRIVILEGES ON mod_django_example.* TO 'user'@'localhost' IDENTIFIED BY 'user';
"""


# 5. run your server with your custom settings

# >>> python manage.py runserver --settings=mod_django_example.development


# 6. modify manage.py to make development as the default settings


#==========================================================================================
#
#  5. Models
#       A model is the single, definitive source of data about your data.
#       It contains the essential fields and behaviors of the data you’re storing.
#
#
#==========================================================================================

# define a Model. Inside models.py from the polls app


#from django.db import models
#
#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#
#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)


# - Each model is represented by a class that subclasses django.db.models.Model.


# class Poll(models.Model):


# - Each model has a number of class variables, each of which represents a database
#   field in the model. Each field is represented by an instance of a Field class – e.g.,
#   CharField for character fields and DateTimeField for datetimes.

#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


# - The name of each Field instance (e.g. question or pub_date ) is the field’s name.

# - Finally, note a relationship is defined, using ForeignKey.
#   That tells Django each Choice is related to a single Poll.

"""
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
"""
#   Django supports all the common database relationships: many-to-ones,
#   many-to-manys and one-to-ones.


# Models should be activated to be included


# In your settings.py
#   INSTALLED_APPS = (
#            'django.contrib.auth',
#            'django.contrib.contenttypes',
#            'django.contrib.sessions',
#            'django.contrib.sites',
#            'django.contrib.messages',
#            'django.contrib.staticfiles',
#            'polls',
#        )


# to create tables
# >>> python manage.py syncdb


# Remember that this will not update already created models


#==========================================================================================
#
#  6. url dispatching
#
#==========================================================================================


#   How Django processes a request
#       When a user requests a page from your Django-powered site, this is the algorithm the
#       system follows to determine which Python code to execute:


#         - Django determines the root URLconf module to use. Ordinarily, this is the value
#           of the ROOT_URLCONF setting.

#   >>> cat mod_django_example/settings.py | grep ROOT


#         - Django loads that Python module and looks for the variable urlpatterns. This should
#           be a Python list, in the format returned by the function django.conf.urls.patterns().

#   >>> cat mod_django_example/urls.py


#         - Django runs through each URL pattern, in order, and stops at the first one that
#           matches the requested URL.
#
#         - Once one of the regexes matches, Django imports and calls the given view, which is
#           a simple Python function (or a class based view). The view gets passed an HttpRequest
#           as its first argument and any values captured in the regex as remaining arguments.
#
#         - If no regex matches, or if an exception is raised during any point in this process,
#           Django invokes an appropriate error-handling view. See Error handling below.


#   >>> cat polls/urls.py
#   >>> cat polls/views.py


# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.


#urlpatterns = patterns('',
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),)


# regex
#    a regular expression for matching patterns in strings, or in this case, url patterns.


# view
#   When Django finds a regular expression match, Django calls the specified view function,
#   with an HttpRequest object as the first argument and any “captured” values from the regular
#   expression as other arguments. If the regex uses simple captures, values are passed as
#   positional arguments; if it uses named captures, values are passed as keyword arguments.


# kwargs
#   Arbitrary keyword arguments can be passed in a dictionary to the target view.


# name
#   Naming your URL lets you refer to it unambiguously from elsewhere in Django especially templates.
#   This powerful feature allows you to make global changes to the url patterns of your project while
#   only touching a single file.


#==========================================================================================
#
#  7. views
#       A view function is simply a Python function that takes a Web request and returns a Web response.
#       This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document...
#       The view itself contains whatever arbitrary logic is necessary to return that response.
#
#
#
#==========================================================================================


# The simplest view

# def vote(request, poll_id):
#    return HttpResponse("You're voting on poll %s." % poll_id)


# for common operations like:
#   "getting data from the database according to a parameter passed in the URL, loading a template and returning the
#   rendered template"
#
#  Django provides some Generic View to spare us some time

# Generic views abstract common patterns to the point where you don’t even need to write Python code to write an app.


#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'
#    context_object_name = 'latest_poll_list'
#
#    def get_queryset(self):
#        # Return the last five published polls.
#        return Poll.objects.order_by('-pub_date')[:5]
#
#
#class DetailView(generic.DetailView):
#    model = Poll
#    template_name = 'polls/detail.html'


# We’re using two generic views here: ListView and DetailView.
# Respectively, those two views abstract the concepts of “display a list of objects”
# and “display a detail page for a particular type of object.”


# Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
# The DetailView generic view expects the primary key value captured from the URL to be called "pk",
# so we’ve changed poll_id to pk for the generic views.


#==========================================================================================
#
#  8. middlewares
#
#    Middleware is a framework of hooks into Django’s request/response processing.
#    It’s a light, low-level “plugin” system for globally altering Django’s input or output.
#
#==========================================================================================


# https://docs.djangoproject.com/en/dev/topics/http/middleware/


# Middlewares should be activated into settings file


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


# In the request_phase: two hooks are available


#  process_request(self, request)
#    It should return either None or HttpResponse.
#    If None process will continue to next stage


#  process_view(self, request, view_func, view_args, view_kwargs)
#    will be called after process_request
#    view_func -> the view function that django is about to use


# In the response


#  process_exception(self, request, exception)
#    only called when a view raises an exception


#  process_template_response(self, request, response)
#    is called just after the view has finished executing, if the response instance
#    has a render() method, indicating a TemplateResponse or equivalent


#  process_response(self, request, response)
#     request -> HttpRequest object
#     response -> HttpResponse returned by Django view or by a middleware
#


# Example  <https://pdihub.hi.inet/TDAF/tdaf-ebooks-python/blob/develop/ebooks/commons/middleware.py>
#
#
#    class RequestTransactionIDMiddleware(object):
#    """
#    Middleware class to add to local thread a unique transaction id to be used
#    in logging.
#    REQUEST_TRANSACTION_ID_HEADER value can be set in settings, by default is HTTP_X_TRANSACTION_ID.
#    When the REQUEST_TRANSACTION_ID_HEADER is provided in request, that value is used, otherwise a unique
#    identifier is generated.
#    """
#
#    def __init__(self):
#        self.request_transaction_id_header = getattr(settings, 'REQUEST_TRANSACTION_ID_HEADER',
#                                                               'HTTP_X_TRANSACTION_ID')
#
#    def process_request(self, request):
#        request_transaction_id = self._get_request_transaction_id(request)
#        local_context.transaction_id = request_transaction_id
#        return None
#
#    def _get_request_transaction_id(self, request):
#        meta = request.META
#        return getattr(meta, self.request_transaction_id_header, self._generate_id())
#
#    def _generate_id(self):
#        return uuid.uuid4().hex


#==========================================================================================
#
#  9. unit testing
#
#   https://docs.djangoproject.com/en/dev/intro/tutorial05/
#   https://docs.djangoproject.com/en/dev/topics/testing/overview/
#
#==========================================================================================


# In Django, it is recommended to subclass django.test.TestCase class


#import datetime
#from django.utils import timezone
#from django.test import TestCase
#from polls.models import Poll
#
#class PollMethodTests(TestCase):
#
#    def test_was_published_recently_with_future_poll(self):
#        """
#        was_published_recently() should return False for polls whose
#        pub_date is in the future
#        """
#        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
#        self.assertEqual(future_poll.was_published_recently(), False)


# in order to launch the test

# >>> python manage.py test polls
# >>> python manage.py test polls.tests.test_polls
# >>> python manage.py test polls.tests.test_polls.PollMethodTests.test_was_published_recently_with_future_poll


# When you run your tests, the default behavior of the test utility is to find all the test
# cases (that is, subclasses of unittest.TestCase) in any file whose name begins with test,
# automatically build a test suite out of those test cases, and run that suite.


# In order to test view Django provides a test Client to simulate a user interacting with the
# code at the view level. We can use it in our TestCases or even in the shell.


#==========================================================================================
#
#  10. Django REST Framework
#
#       django plugin than eases the development of Web API
#
#     There is a framework in-house which everyone should follow:
#        https://pdihub.hi.inet/TDAF/tdaf-ebooks-python
#
#==========================================================================================


# 1. Request objects
#       .DATA   - returns the parsed content of the request body
#               - it supports flexible request parsing. not just form data
#       .QUERY_PARAMS
#               - a more clear way to refer to query params than request.GET
#
#  more info:
#       http://django-rest-framework.org/api-guide/requests.html


# 2. Response objects
#       - return content that can be rendered into multiple content types
#       - objects are initialised with data, which should consists of native python primitives
#       - with standard HTTP content negotiation it will be determined how it should render the response
#
# more info:
#       http://django-rest-framework.org/api-guide/responses.html


# 3. APIView model
#       APIView is a class based view which subclasses django's View class
#           - Requests passed to the handler will be REST's frameworks Requests instances
#           - Handler methods may return REST framework's Response
#           - the incoming requests is dispatched to the appropiate get/post/put/delete methods


# 4. Serializers
#       Allow complex data to be converted to native python datatypes
#       Serializers also provide deserialization, allowing parsed data to be
#           converted back into complex types, after first validating the incoming data.
#       It provides a Serializer class which gives you a powerful, generic way to control
#         the output of your responses, as well as a ModelSerializer class which provides a useful
#         shortcut for creating serializers that deal with model instances and querysets.
