dna1 = "ATGCGC"
dna2 = "ATATGC"

gc1 = dna1.count("G") + dna1.count("C")
gc2 = dna2.count("G") + dna2.count("C")

percent1 = (gc1 / len(dna1)) * 100
percent2 = (gc2 / len(dna2)) * 100

print("DNA 1 GC%:", round(percent1, 1))
print("DNA 2 GC%:", round(percent2, 1))

if percent1 > percent2:

    print("DNA 1 has higher GC content")

elif percent2 > percent1:

    print("DNA 2 has higher GC content")

else:

    print("Both sequences have equal GC content")
