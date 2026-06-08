from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

all_summaries = []

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    summary = {
        "Pair": records[i].id + " vs " + records[i + 1].id,
        "Similarity": round(similarity, 2)
    }

    all_summaries.append(summary)

all_summaries.sort(
    key=lambda x: x["Similarity"],
    reverse=True
)

for item in all_summaries:

    print(item)
