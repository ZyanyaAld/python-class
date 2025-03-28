
secuencias = input ("Dame secuancias separadas por coma").upper().split(",")

stop_codons = {"TAA", "TAG", "TGA"}

seq = [secuencia for secuencia in secuencias if any(codon in secuencia for codon in stop_codons)]

print(seq)