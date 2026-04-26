dna = input("Enter DNA: ").upper()

counts = {
    "A": 0,
    "T": 0,
    "G": 0,
    "C": 0
}

for base in dna:
    if base in counts:
        counts[base] += 1

total = len(dna)

print("Base counts:", counts)

for base in counts:
    percent = (counts[base] / total) * 100
    print(base + "%:", percent)
