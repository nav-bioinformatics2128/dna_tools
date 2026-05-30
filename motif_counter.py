dna_sequences = [
    "ATGCGA",
    "GGGCCC",
    "ATGTTTAAA",
    "CCCATGGA"
]

motif = "ATG"

count = 0

for dna in dna_sequences:

    if motif in dna:

        count += 1

        print("Motif found in :", dna)

print("=" * 30)

print("Total sequences containing motif :", count)
