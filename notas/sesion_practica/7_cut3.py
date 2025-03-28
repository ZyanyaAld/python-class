
secuencias = input ("Dame secuancias separadas por coma").split(",")

codones_inicio= [secuencia.strip()[:3] for secuencia in secuencias]

print(codones_inicio)