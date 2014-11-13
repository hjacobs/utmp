import utmp
import pytest
import struct

def test_read_empty():
    for entry in utmp.read(b''):
        pass

def test_read_fail():
    with pytest.raises(struct.error):
        for entry in utmp.read(b'123'):
            pass
