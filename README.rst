=============================
django-drylinks
=============================

.. image:: https://badge.fury.io/py/django-drylinks.png
    :target: http://badge.fury.io/py/django-drylinks
    
.. image:: https://travis-ci.org/raphigaziano/django-drylinks.png?branch=master
        :target: https://travis-ci.org/raphigaziano/django-drylinks

.. image:: https://pypip.in/d/django-drylinks/badge.png
        :target: https://crate.io/packages/django-drylinks?version=latest


**Django Drylink** is a set of model mixins and utilities to help you easily
manager various links in your django application.

It doesn't do much by itself, but rather provides a handfull of predefined
and extensible building blocks so that you can keep things
`DRY <http://c2.com/cgi/wiki?DontRepeatYourself>`_ 
when dealing with internal or external links.

Documentation
-------------

The full documentation is at http://django-drylinks.rtfd.org.

Quickstart
----------

Install django-drylinks::

    pip install django-drylinks

Then use it in a project::

	import drylinks

Features
--------

* Model Mixins, along with a few simple absract model, to quickly build your 
  own Link objects.

* Convenient admin classes for basic links.

* Handle external or internal urls (ie, provides an easy way to link to various
  internal urls from your application).

* Easy to extend: Just define your own mixins or override the abstract models
  to add your own custom functionalities.
