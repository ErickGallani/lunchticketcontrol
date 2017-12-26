import argparse
from subprocess import call

parser = argparse.ArgumentParser(description='Create a new database migration.')
parser.add_argument('--m', type=str, help='Database migration message')

args = parser.parse_args()

if args.m and isinstance(args.m, str) and args.m.strip():
    call('flask db migrate --message "{}"'.format(args.m))
