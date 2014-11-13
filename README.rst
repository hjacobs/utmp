====
utmp
====

Library to decode/read utmp and wtmp files.

Usage
=====

The ``utmp.read`` function decodes a binary utmp/wtmp stream and yields record objects:

.. code-block:: python

    with open('/var/log/wtmp', 'rb') as fd:
        buf = fd.read()
        for entry in utmp.read(buf):
            print(entry.time, entry.type, entry)
