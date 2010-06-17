JSPlot
======

JSPlot is a library with Matplotlib like API, except that the ``show()``
command launches a web server and you interact with the plot in the web
browser.

Example::

    >>> from jsplot import plot, show
    >>> plot([1, 2, 3], [1, 2, 1])
    >>> show()
    Server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Going to the url above will show something like the following screenshot, where
you can interactively zoom in/out.

.. image:: http://github.com/certik/jsplot/raw/master/doc/jsplot1.png


Development
-----------

To develop the plotserver, do::

    cd plotserver
    ./manage.py runserver

To develop the jsplot itself, just edit files in the ``jsplot`` directory.
