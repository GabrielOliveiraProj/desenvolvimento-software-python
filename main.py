import sympy as sp
x, y = sp.symbols('x y')
expressao = x**2 + 2*x*y + y**2
expressao_otimizada = sp.factor(expressao)
while True:
    try:
        numero_x = float(input("Digite o número de x: "))
        break
    except ValueError:
        print("Erro: Digite apenas números!")
while True:
    try:
        numero_y = float(input("Digite o número de y: "))
        break
    except ValueError:
        print("Erro: Digite apenas números!")
resultado_otimizado = expressao_otimizada.subs({x: numero_x, y: numero_y})
print(resultado_otimizado)