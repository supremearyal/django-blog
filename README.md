This is a very basic blog web application written in Django.
Lots of things are missing like authentication.

How to run
==========

Create database (uses sqlite3 by default).

  $ python manage.py syncdb

Run server

  $ python manage.py runserver

The application should be running in localhost:8000.

Screenshots
===========

All entries:

![All blog entries.](https://raw.github.com/supremearyal/blog/master/screenshots/entries.png)

Single entry:

![Single blog entry.](https://raw.github.com/supremearyal/blog/master/screenshots/entry.png)

New entry:

![New blog entry.](https://raw.github.com/supremearyal/blog/master/screenshots/new_entry.png)
