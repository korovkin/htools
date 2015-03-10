# line.py


Usage:
```
Usage: line.py [options]

   Process the stdin line by line. apply the following operators on each line.

Options:
  -h, --help         show this help message and exit
  --version          print version number
  --Prefix=PREFIX    prefix each line with the given string
  --Postfix=POSTFIX  postfix each line with the given string
  --Grep=GREP        output lines containing the given RE
  --Splice=SPLICE    Output the given RE
  --Replace=REPLACE  Replace --Replace RE with --With
  --With=WITH        Replace --Replace RE with --With
```


Examples:

```
cat lines.txt
A
B
C

cat lines.txt | ./line.py --Prefix "prefix: " --Postfix ": postfix"
prefix: A: postfix
prefix: B: postfix
prefix: C: postfix

 # cat lines.txt | ./line.py --Splice "A|B"
A
B

``

