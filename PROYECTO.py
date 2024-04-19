# MENÚ 
 
print("*** ----------------------- MENÚ DE OPCIONES ----------------------- *** ")
print("1. Comprimir un texto")
print("2. Comprimir una colección de archivos en un directorio") 
print("3. Descomprimir un texto")
print("4. Descomprimir una colección de archivos en un directorio")
print("5. Comprimir una imagen")
print("6. Descomprimir una imagen") 
print("7. Salir")
print("--------------------------------------------------------------------------")

opcionSeleccionada = int(input("Seleccione una opción. Indique el número (del 1 al 7): "))

if(opcionSeleccionada == 1): 
    print("¿Qué algoritmo desea utilizar para comprimir un texto?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 2):
    print("¿Qué algoritmo desea utilizar para comprimir una colección de archivos en un directorio?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 3):    
    print("¿Qué algoritmo desea utilizar para descomprimir un texto?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 4):
    print("¿Qué algoritmo desea utilizar para descomprimir una colección de archivos en un directorio?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 5):
    print("¿Qué algoritmo desea utilizar para comprimir una imagen?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 6):
    print("¿Qué algoritmo desea utilizar para descomprimir una imagen?")
    print("1. Utilizar algoritmo Lempel-Ziv-Welch (LZW)")
    print("2. Utilizar algoritmo Run-Length Encoding (RLE)")
    print("3. Utilizar algoritmo Algoritmo de compresión por diccionario simple")
    print("4. Utilizar algoritmo Codificación densa post etiquetado")

    algoritmoSeleccionado = int(input("Seleccione una opción. Indique el número (del 1 al 4): "))

if(opcionSeleccionada == 7): 
    print("Has salido del software.")