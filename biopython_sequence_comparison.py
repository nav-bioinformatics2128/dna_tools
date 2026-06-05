from Bio.Seq import Seq

seq1 = Seq("ATGCGA")
seq2 = Seq("ATGCCA")

differences = 0

for i in range(len(seq1)):

    if seq1[i] != seq2[i]:

        differences += 1

print("Differences:", differences)
