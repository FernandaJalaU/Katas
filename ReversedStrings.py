def reverse_string(s):
    return s[::-1]

# Pedir al usuario que ingrese la palabra
input_word = input("Ingresa una palabra: ")

# Invertir la palabra ingresada por el usuario
reversed_word = reverse_string(input_word)

# Mostrar la palabra invertida
print("La palabra invertida es:", reversed_word)
