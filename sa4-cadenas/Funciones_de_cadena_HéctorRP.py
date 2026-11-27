#Ejer1
cadena = input("Escriba una cadena, puede ser solo números si quiere. ")
cadena = cadena.strip()
print(f"La longitud de la cadena es: {len(cadena)}.")
print(f"¿Contiene la cadena la subcadena \'pe\'? {'pe' in cadena}. ")
print(f"¿Contiene la cadena la subcadena \'la\'? {'la' in cadena}. ")
print(f"¿La cadena es entera de números? {cadena.isdigit()}.")
print(f"¿La cadena es solo números y letras (sin símbolos)? {cadena.isalnum()}.")

#Ejer2
palabra_mod  = input("Dígame una palabra o frase cualquiera. ")
print(palabra_mod.lower())
print(palabra_mod.upper())
print(palabra_mod[2:-2:1])
print(palabra_mod[0:5:1])
print(palabra_mod[::-1])

#Ejer3
palabra_mod2  = input("Dígame otra palabra o frase cualquiera. ")
palabra_mod2 = palabra_mod2.lower()
vocales_debiles = palabra_mod2.count("u") + palabra_mod2.count("i") + palabra_mod2.count("ú") + palabra_mod2.count("ü") +palabra_mod2.count("í")
vocales_totales = vocales_debiles + palabra_mod2.count("a") + palabra_mod2.count("e") +  palabra_mod2.count("o") + palabra_mod2.count("á")  + palabra_mod2.count("é")  + palabra_mod2.count("ó")
print(f"La frase/palabra que has escrito tiene {vocales_debiles} vocal/es débiles (u/i).")
print(f"La frase/palabra que has escrito tiene {vocales_totales} vocal/es en total.")

#Ejer4
print(f"{'Carácter':<7} {'Código':^8} ")
print(f"{'0':<7} {ord('0'):^8} ")
print(f"{'1':<7} {ord('1'):^8} ")
print(f"{'9':<7} {ord('9'):^8} ")
print(f"{'@':<7} {ord('@'):^8} ")
print(f"{'A':<7} {ord('A'):^8} ")
print(f"{'Z':<7} {ord('Z'):^8} ")
print(f"{'a':<7} {ord('a'):^8} ")
print(f"{'z':<7} {ord('z'):^8} ")
print(f"{'Á':<7} {ord('Á'):^8} ")
print(f"{'Ñ':<7} {ord('Ñ'):^8} ")
print(f"{'à':<7} {ord('à'):^8} ")
print(f"{'á':<7} {ord('á'):^8} ")
print(f"{'ç':<7} {ord('ç'):^8} ")

#Ejer5
ciudad1 = input("Dígame el nombre de una ciudad. ")
ciudad2 = input("Dígame el nombre de otra ciudad. ")
print(f"¿Es la primera ciudad mayor alfabéticamente que la segunda? {ciudad1.lower() > ciudad2.lower()}.")
print(f"¿Es la primera ciudad menor alfabéticamente que la segunda? {ciudad1.lower() < ciudad2.lower()}.")
print(f"¿Es la primera ciudad igual alfabéticamente que la segunda? {ciudad1.lower() == ciudad2.lower()}.")


