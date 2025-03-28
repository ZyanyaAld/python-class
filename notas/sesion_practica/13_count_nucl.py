secuencias = input ("Dame secuancias separadas por coma").upper().split(",")


nucleotides = [(secuencia.count("A"), secuencia.count("T"), secuencia.count("C"), secuencia.count("G"))  for secuencia in secuencias]

print(nucleotides)