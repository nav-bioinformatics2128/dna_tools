from Bio.Seq import Seq

seq1 = Seq("ATGCGAGA")
seq2 = Seq("ATGCCATA")

mutations = []

for i in range(len(seq1)):

    if seq1[i] != seq2[i]:

        mutation = "Position " + str(i) + ": " + str(seq1[i]) + "->" + str(seq2[i])

        mutations.append(mutation)

print("MUTATION REPORT")

print("Total Mutations:", len(mutations))

for mutation in mutations:

    print(mutation)
