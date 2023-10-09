def main():
    map_chars = "aeiou "
    texto = input("Ingrese un texto: ").lower()
    print(f"Texto sin vocales: {twttr(texto, map_chars)}")
    
def twttr(texto, chars):
    return ''.join(char for char in texto if char not in chars)

if __name__ == "__main__":
    main()