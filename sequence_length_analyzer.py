dna_sequences = [
    "ATGCGA",
    "GGGCCC",
    "ATATTTAAA"
]

total_length = 0

for dna in dna_sequences:

    sequence_length = len(dna)

    total_length += sequence_length

    print("DNA Sequence :", dna)

    print("Length :", sequence_length)

    print("=" * 30)

print("Total Length of All Sequences :", total_length)
