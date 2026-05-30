dna_sequences = [
    "ATGC",
    "GGCC",
    "ATGC",
    "TTAA",
    "GGCC",
    "ATGC"
]

frequency = {}

for dna in dna_sequences:

    if dna in frequency:

        frequency[dna] += 1

    else:

        frequency[dna] = 1

print("Sequence Frequency Table")

print("=" * 30)

for dna, count in frequency.items():

    print(dna, ":", count)
most_common = max(frequency, key=frequency.get)

print("Most Common Sequence :", most_common)
