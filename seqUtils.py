# substitution matrix
def score(base1,base2):
    import sys
    base1=base1.upper()
    base2=base2.upper()
    if base1 not in 'ACTG' or base2 not in 'ACTG':
        print 'Not DNA base!'
        sys.exit()
    elif base1==base2:
        return 2
    else:
        return -1

# generate matrix of appropriate size
def make_matrix(seq1, seq2, gap, align):
    matrix = []
    mRows = len(seq1)
    nCols = len(seq2)
    for x in range(mRows + 1): # fill with zeros
        matrix.append([])
        for y in range(nCols + 1):
            matrix[x].append(0)
    if align.lower() == 'global': # fill first row and column with gap penalties
        for x in range(mRows + 1):
            matrix[x][0] = gap*x
        for y in range(nCols + 1):
            matrix[0][y] = gap*y
    return matrix

# choose local or global and populate matrix
def make_align(seq1, seq2, matrix, gap, align):
    import sys
    mRows = len(seq1)
    nCols = len(seq2)
    for i in range(1, mRows + 1): 
        for j in range(1, nCols + 1):
            dscore = matrix[i-1][j-1] + score(seq1[i-1], seq2[j-1])
            vscore = matrix[i-1][j] + gap
            hscore = matrix[i][j-1] + gap
            if align.lower() == 'local':
                matrix[i][j]=max(0, vscore, hscore, dscore)
            elif align.lower() == 'global':
                matrix[i][j]=max(vscore, hscore, dscore)
            else: 
                print 'Choose either a local or global programming matrix'
                sys.exit()
    return matrix

# print matrix separated by tabs
def print_matrix(matrix):
    for line in matrix:
        line = str(line).strip('[]').replace(', ', '\t')
        print line
