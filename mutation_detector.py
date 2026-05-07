normal_dna = "ATGCTA"
mutated_dna = "ATGATA"

print("Normal DNA:", normal_dna)
print("Mutated DNA:", mutated_dna)
print("=" * 40)

if len(normal_dna) != len(mutated_dna):

    print("Sequences must have same length")

else:

    for i in range(len(normal_dna)):

        if normal_dna[i] != mutated_dna[i]:

            print(f"Position {i+1}: {normal_dna[i]} → {mutated_dna[i]}")
