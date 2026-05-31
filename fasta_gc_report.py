file = open("sample.fasta", "r")

total_gc = 0
total_bases = 0

for line in file:

    line = line.strip()

    if not line.startswith(">"):

        gc_count = line.count("G") + line.count("C")

        total_gc += gc_count

        total_bases += len(line)

file.close()

gc_percentage = (total_gc / total_bases) * 100

print("Total GC Bases :", total_gc)

print("Total Bases :", total_bases)

print("GC Content :", round(gc_percentage, 2), "%")
