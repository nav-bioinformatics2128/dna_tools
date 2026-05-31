file = open("dna_sequences.txt", "r")

total_gc = 0
total_bases = 0

for line in file:

    dna = line.strip()

    gc_count = dna.count("G") + dna.count("C")

    total_gc += gc_count

    total_bases += len(dna)

file.close()

gc_percentage = (total_gc / total_bases) * 100

print("Total GC Bases :", total_gc)

print("Total Bases :", total_bases)

print("GC Content :", round(gc_percentage, 2), "%")
