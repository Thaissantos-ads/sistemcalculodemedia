# Projetos Exemplos: calcularadora de media do lundo
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2 

print("== Sistema de nota do aluno ===")
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a seginda nota"))
media = calcular_media(n1,n2)
print (f"A media final é: {media:.2f}")

if media >= 7.0:
    print ("status: APROVADO!")
else:
     print("status: REPROVADO!")