=====
Footprints
=====

Footprints is a simple Django app to record page access.

Quick start
-----------
0. Add "'footprints'" to your INSTALLED_APPS setting like this:
    INSTALLED_APPS = [        ...        'footprints',    ]
1. Add "'footprints.middleware.footprints_middleware.FootprintMiddleware'" to your MIDDLEWARE
2. Run `python manage.py migrate` to create the footprints models.
3. Start the development server and visit http://127.0.0.1:8000/admin/   to view a accessed pages (you'll need the Admin app enabled).
4. Visit http://127.0.0.1:8000/ to record page access.
