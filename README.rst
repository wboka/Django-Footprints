=====
Footprints
=====

Footprints is a simple Django app to record page access.

Features
--------

- Page tracking by IP and logged in user
- Templatetags for viewing page hits (excluding admin site).
- Full test suite!

Installing
----------
Install from PyPi:

You can pip install the app directly from GitHub:

::

    $ pip install git+git://github.com/wboka/django-footprints.git#egg=DjangoFootprints

Quick start
-----------
0. Add "'footprints'" to your INSTALLED_APPS setting like this:
::
    INSTALLED_APPS = [
        ...
        'footprints',    
    ]
1. Add "'footprints.middleware.footprints_middleware.FootprintMiddleware'" to your MIDDLEWARE
2. Run `python manage.py migrate` to create the footprints models.
3. Start the development server and visit http://127.0.0.1:8000/admin/   to view a accessed pages (you'll need the Admin app enabled).
4. Visit http://127.0.0.1:8000/ to record page access.
