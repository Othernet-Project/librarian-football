==================
Librarian Football
==================

A librarian component for displaying football data such as leagues and scores.

Installation
------------

The component has the following dependencies:

- librarian-core_
- librarian-content_
- untangle_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_football

And to make the menuitem show up::

    [menu]
    +main =
        football

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _librarian-core: https://github.com/Outernet-Project/librarian-core
.. _librarian-content: https://github.com/Outernet-Project/librarian-core
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
.. _untangle: https://github.com/stchris/untangle