nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))
nota4 = float(input("Digite a nota: "))
nota5 = float(input("Digite a nota: "))

soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma / 5

print(f"\nA media desse aluno é {media}")

if media >= 5:
    print("\nAluno aprovado!")
elif media >= 2.5 and media < 5:
    print("\nAluno de Recuperação!")
elif media < 2.5:
    print("\nAluno Reprovado!")