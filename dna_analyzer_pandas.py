import pandas as pd 

def complement_dna(dna):
    comp = ""
    for base in dna:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A" 
        elif base == "G":
            comp += "C"
        elif base == "C":
            comp += "G"
    return comp 

df = pd.read_csv("dna.txt", header=None)

for seq in df[0]:
    dna = seq.strip().upper()
    print("Sequence:", dna)

    bases = list(dna)

    counts = pd.Series(bases).value_counts()
    percent = pd.Series(bases).value_counts(normalize=True) * 100

    counts = counts.reindex(["A","C","G","T"], fill_value=0)
    percent = percent.reindex(["A","C","G","T"], fill_value=0)

    print("Counts:")
    for base, value in counts.items():
        print(base, ":", value)

    print("Percentages:")
    for base, value in percent.items():
        print(base, "%:", value)

    reverse = dna[::-1]
    print("Reverse:", reverse)

    comp = complement_dna(dna)
    print("Complement:", comp)

    print("-" * 30)
