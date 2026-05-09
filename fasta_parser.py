file = open("sample.fasta")

for line in file:

    line = line.strip()

    if line.startswith(">"):

        print("Header:", line[1:])

    else:

        print("DNA Sequence:", line)
