#!/usr/bin/env python
"""Org Preprocess for Pandoc to Markdown.

Usage:
  org_preprocessor.py -i INPUT_FILE [-o OUTPUT_FILE]  [--verbose]

Options:
  -h --help                   Show this screen.
  -i <file>, --input <file>   Input file.
  -o <file>, --output <file>  Output file.
  -v, --verbose               Verbose [default: False].
"""
import re
import sys
from pathlib import Path

from docopt import docopt

RE_ORG_DATESTAMP = re.compile(r"([^\n]*)(<\d{4}-\d{2}-\d{2} \w{3}> )([^\n]*)")

def datestamp_to_markup(line: str) -> str:
    match = RE_ORG_DATESTAMP.match(line)
    if not match:
        return line
    datestamp = " (/" + match[2][1:-1] + "/)"
    return ''.join((match[1], match[3], datestamp))


def main(args):
    fh_out = open(args["--output"], 'w') if args["--output"] else sys.stdout
    with open(args["--input"], "r") as fh_in:
        # Write header first..
        # fh_out.write("---\n")   # Why are these lines munged??
        # fh_out.write("tags:\n")
        # fh_out.write("  - Tech\n")
        # fh_out.write("  - Python\n")
        # fh_out.write("---\n\n")
        for line in fh_in:
            line = datestamp_to_markup(line)
            fh_out.write(line)
    fh_out.close()
    exit(0)


if __name__ == "__main__":
    args = docopt(__doc__, version="pandoc-org preprocessor")

    if not Path(args["--input"]).exists():
        sys.stderr.write(f"Sorry, couldn't find '{args['--input']}'\n")
        exit(1)

    main(args)
