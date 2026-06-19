from Bio import SeqIO

results = []

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    g_count = sequence.count("G")

    c_count = sequence.count("C")

    gc_percent = ((g_count + c_count)
                  / len(sequence)) * 100

    results.append({
        "ID": record.id,
        "GC": gc_percent
    })

results.sort(
    key=lambda item: item["GC"],
    reverse=True
)

print("Top 3 GC-Rich Sequences")

for item in results[:3]:

    print(
        item["ID"],
        round(item["GC"], 2)
    )
