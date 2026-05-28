dna_sequences = [
    "ATGCGA",
    "GGGCCC",
    "ATATTTAAA",
    "ATGCGCTAGCTA"
]

longest_sequence = ""

for dna in dna_sequences:

    if len(dna) > len(longest_sequence):

        longest_sequence = dna

print("Longest DNA Sequence :")

print(longest_sequence)

print("Length :", len(longest_sequence))
