from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

similarities = []

total_similarity = 0

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    similarities.append({
        "Pair": records[i].id + " vs " + records[i + 1].id,
        "Similarity": similarity
    })

    total_similarity += similarity

average_similarity = total_similarity / len(similarities)

closest_pair = similarities[0]

smallest_distance = abs(
    similarities[0]["Similarity"] - average_similarity
)

for item in similarities:

    distance = abs(
        item["Similarity"] - average_similarity
    )

    if distance < smallest_distance:

        smallest_distance = distance

        closest_pair = item

print("Average Similarity:",
      round(average_similarity, 2))

print("Closest Pair:")

print(closest_pair)
