import argparse
import utmp

def main():
    with open('/var/log/wtmp', 'rb') as fd:
        buf = fd.read()
        for entry in utmp.read(buf):
            print(entry.time, entry.type, entry)


if __name__ == '__main__':
    main()
