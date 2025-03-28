with open("6_  sequences.fa") as seqfa:
    
    counts = len([line.strip() for line in seqfa if line.strip().startswith(">")])
    
    print(f"\nEl archivo FASTA tiene {counts} secuencias.\n")