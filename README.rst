====
utmp
====

Pure-Python library to decode/read utmp and wtmp files.
Please note that there is an alternative library which uses the underlying C API: pyutmp_

This package requires Python 3.4.

Usage
=====

The ``utmp.read`` function decodes a binary utmp/wtmp stream and yields record objects:

.. code-block:: python

    with open('/var/log/wtmp', 'rb') as fd:
        buf = fd.read()
        for entry in utmp.read(buf):
            print(entry.time, entry.type, entry)

.. _pyutmp: https://pypi.python.org/pypi/pyutmp
