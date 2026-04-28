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
# Reverse DNA
reverse = dna[::-1]
print("Reverse:", reverse)

# Complement DNA
complement = ""
for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

print("Complement:", complement)

# Reverse Complement
rev_comp = ""
for base in reverse:
    if base == "A":
        rev_comp += "T"
    elif base == "T":
        rev_comp += "A"
    elif base == "G":
        rev_comp += "C"
    elif base == "C":
        rev_comp += "G"

print("Reverse Complement:", rev_comp)
def count_all_bases(dna):
    counts = {
        "A": 0,
        "G": 0,
        "T": 0,
        "C": 0
    }
    for base in dna:
        if base in counts:
            counts[base] += 1
    return counts


dna = input("Enter Dna: ").upper()
result = count_all_bases(dna)

total = len(dna)

for base in result:
    percent = (result[base] / total) * 100
    print(base, "%:", percent)
