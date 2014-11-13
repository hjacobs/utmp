import argparse
import utmp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', metavar='FILE', help='Files (utmp/wtmp/btmp) to read from', nargs='+')
    args = parser.parse_args()

    for fn in args.files:
        with open(fn, 'rb') as fd:
            buf = fd.read()
            for entry in utmp.read(buf):
                print(entry.time, entry.type, entry)


if __name__ == '__main__':
    main()
