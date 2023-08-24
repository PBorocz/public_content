#!/usr/bin/env python
"""Org Post-process for Pandoc to Markdown.

Usage:
  org_preprocessor.py -i INPUT_FILE [-o OUTPUT_FILE]  [--verbose]

Options:
  -h --help                   Show this screen.
  -i <file>, --input <file>   Input file.
  -o <file>, --output <file>  Output file.
"""
import sys
from pathlib import Path

from docopt import docopt


def main(args):
    fh_out = open(args["--output"], 'w') if args["--output"] else sys.stdout

    # Write header first..
    fh_out.write("---\n")
    fh_out.write("tags:\n")
    fh_out.write("  - python\n")
    fh_out.write("---\n\n")

    # Followed by the rest of the file
    for line in open(args["--input"], "r"):
        fh_out.write(line)

    fh_out.close()
    exit(0)


if __name__ == "__main__":
    args = docopt(__doc__, version="pandoc-org postprocessor")

    if not Path(args["--input"]).exists():
        sys.stderr.write(f"Sorry, couldn't find '{args['--input']}'\n")
        exit(1)

    main(args)
