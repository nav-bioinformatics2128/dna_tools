dna1 = "ATGCGA"
dna2 = "ATGAGA"

print("DNA 1:", dna1)
print("DNA 2:", dna2)
print("=" * 40)

matches = 0

if len(dna1) != len(dna2):

    print("Sequences must have same length")

else:

    for i in range(len(dna1)):

        if dna1[i] == dna2[i]:

            matches += 1

    similarity = (matches / len(dna1)) * 100

    print("Matches:", matches)
    print("Similarity Percentage:", round(similarity, 1), "%")
