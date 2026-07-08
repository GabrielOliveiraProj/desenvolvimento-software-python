def add(a, b):
    return a + b

     # colete os números
while True: # ---> precisei adicionar para a calculadora rodar sem interruoções até o final e voltar.
    while True: # ---> rodando dentro do principal "while true"
       try:
           numero1 = int(input("Digite o primeiro número: ")) # ---> coletou o número.
           break # ---> "break" fechou; interrupção
       except ValueError:
           print("Erro: Digite números! ") # ---> desceu...

    while True:
        try:
           numero2 = int(input("digite o segundo número: "))
           break
        except ValueError:
           print("Erro: Digite número! ")

     # soma o resultado e volta rodar novamente.
    result = add(numero1, numero2)  # ---> ficou dentro do "while true" para voltar para o principal...
    print(f"{numero1} + {numero2} = {result}")