#!/usr/bin/python

import sys
import re
import optparse

def main():
  parser = optparse.OptionParser()
  parser.add_option("", "--version",
                    action="store_true",
                    help="print version number",
                    dest="version", default=False)
  (options, filenames) = parser.parse_args()

  if options.version:
    print("version!")
    sys.exit(0)

  for filename in filenames:
    read_data = []
    if filename == "-":
      sys.stderr.write("reading from stdin...\n")
      read_data = sys.stdin.read()
      print read_data,
    else:
      read_data = open(filename).read()

    output_data = re.sub("[ \t]+\n", "\n", read_data)
    if read_data != output_data:
      sys.stderr.write("updated: " + filename + "\n")
      open(filename, "w").write(output_data)
    else:
      pass
if __name__ == "__main__":
  main()
