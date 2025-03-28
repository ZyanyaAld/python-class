
secuencias = input ("Dame secuancias separadas por coma").split(",")

secuencia_invertida = [secuencia[::-1] for secuencia in secuencias] 

print(secuencia_invertida)