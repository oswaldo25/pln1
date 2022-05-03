import nltk
carpeta_nombre="F:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="Procesamiento de Lenguaje Natural 1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
lista_frecuencias=distribucion.most_common()
print(lista_frecuencias)

print("la frecuencia de la palabra procesamiento en el documento es de:",distribucion["procesamiento"])