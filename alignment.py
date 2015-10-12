import sys
import seqUtils

seq1 = sys.argv[2]
seq2 = sys.argv[1]
align = sys.argv[3]
gap = int(sys.argv[4])

# print(programming_matrix(empty matrix of appropriate size))
seqUtils.print_matrix(seqUtils.make_align(seq1,seq2,seqUtils.make_matrix(seq1,seq2,gap,align),gap,align))

