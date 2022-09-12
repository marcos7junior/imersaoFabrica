
import calculadoraPython

valor_inteiro = 2
valor_float = 3.3
valor_string = "resultado"
valor_booleano = True

print("Hello, Fábrica!")

print(calculadoraPython.soma(valor_inteiro, valor_inteiro))
print(calculadoraPython.subtracao(valor_inteiro, valor_inteiro))
print(calculadoraPython.multiplicacao(valor_float, valor_inteiro))
print(calculadoraPython.multiplicacao(valor_string + " ", valor_inteiro))

if(valor_booleano):
    print(calculadoraPython.potencia(valor_inteiro, valor_inteiro))

print("Fim!")
