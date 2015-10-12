# sequence-alignment
Align two DNA sequences in either a global or dynamic programming matrix

This program takes in two sequences as command line arguments, a third argument that is either 'local' or 'global',
and a fourth argument that is a gap penalty. It fills in either a local or global dynamic programming 
matrix depending on the third argument. Functions can be found in "seqUtils.py"

Run example:

C:\>alignment.py ACTGTGCCGA AGTCTTCCGA global -1
