import random
import string

# Función para generar la contraseña
def generar_contraseña(longitud, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_letters  # Incluye letras mayúsculas y minúsculas

    if incluir_numeros:
        caracteres += string.digits  # Añade números
    
    if incluir_simbolos:
        caracteres += string.punctuation  # Añade símbolos

    # Generar una contraseña aleatoria de la longitud indicada
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

# Función principal
def main():
    print("¡Bienvenido al generador de contraseñas seguras!")
    
    longitud = int(input("¿Cuál es la longitud de la contraseña que deseas generar? "))
    incluir_numeros = input("¿Quieres incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Quieres incluir símbolos? (s/n): ").lower() == 's'
    
    contraseña = generar_contraseña(longitud, incluir_numeros, incluir_simbolos)
    print(f"Tu contraseña generada es: {contraseña}")

if __name__ == "__main__":
    main()
