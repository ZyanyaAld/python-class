
secuencias = input ("Dame secuancias separadas por coma").split(",")

secuencias_arn = [secuencia.replace("T", "U") for secuencia in secuencias] 

print(secuencias_arn)