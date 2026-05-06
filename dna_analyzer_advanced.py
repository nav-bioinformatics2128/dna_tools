import pandas as pd
import matplotlib.pyplot as plt


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

total_gc = 0
count_seq = 0

print(df)

for i, seq in enumerate(df[0]):
    dna = seq.strip().upper()

    valid_bases = ["A", "C", "G", "T"]

    # ✅ Proper validation (skip invalid sequence completely)
    if any(base not in valid_bases for base in dna):
        print("Invalid DNA sequence:", dna)
        continue

    print("\n" + "=" * 40)
    print(f"Sequence {i + 1}")
    print("=" * 40)

    print("DNA:", dna)

    length = len(dna)
    print("Length:", length)

    rna = dna.replace("T", "U")
    print("RNA:", rna)

    reverse = dna[::-1]
    print("Reverse:", reverse)

    rev_comp = complement_dna(reverse)
    print("Reverse Complement:", rev_comp)

    bases = list(dna)

    counts = pd.Series(bases).value_counts()
    percent = pd.Series(bases).value_counts(normalize=True) * 100

    counts = counts.reindex(["A", "C", "G", "T"], fill_value=0)
    percent = percent.reindex(["A", "C", "G", "T"], fill_value=0)

    gc = percent["G"] + percent["C"]
    at = percent["A"] + percent["T"]

    total_gc += gc
    count_seq += 1

    print("GC Content:", round(gc, 1))
    print("AT Content:", round(at, 1))

    print("Counts:")
    for base, value in counts.items():
        print(base, ":", value)

    print("Percentages:")
    for base, value in percent.items():
        print(base, "%:", round(value, 1))

    print("-" * 30)

    # 📊 Plot
    plt.figure(figsize=(6, 4))
    plt.bar(percent.index, percent.values)

    for j, value in enumerate(percent.values):
        plt.text(j, value + 1, str(round(value, 1)) + "%", ha='center')

    plt.title(f"Sequence {i + 1}: {dna}")
    plt.xlabel("Bases")
    plt.ylabel("Percentage")
    plt.grid(axis='y')

    plt.tight_layout()
    plt.savefig("dna_" + dna + ".png")
    plt.show()


print("\n" + "=" * 40)
print("FINAL SUMMARY")
print("=" * 40)

if count_seq > 0:
    avg_gc = total_gc / count_seq
    print("Total sequences:", count_seq)
    print("Average GC Content:", round(avg_gc, 1))
