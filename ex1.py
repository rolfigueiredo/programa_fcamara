from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, '')

print ("Calcular aumento de salário:")

now = datetime.now()
ano = now.year

ano_inicio=2005
aumento=0.015
salario=1000

print ("Salário inicial em ",ano_inicio,": R$ ",locale.format("%1.2f",salario,2))
ano_inicio+=1

while ano_inicio<=ano:
    salario+=(salario*aumento)
    aumento*=2
    ano_inicio+=1

print ("Salário em ",ano_inicio,": R$ ",locale.format("%1.2f",salario,2))
