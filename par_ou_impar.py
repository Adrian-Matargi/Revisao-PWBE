laco = 's'

while laco == 's':
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("\nSeu número é par!")
    else:
        print("\nSeu número é impar!")
    print("\nDeseja continuar?")
    laco = input("s/n")