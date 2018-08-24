import locale
locale.setlocale(locale.LC_ALL, '')

print ("Calcular salário:")

horas=int(input("Entre com as horas trabalhadas: "))
salario_minimo=float(input("Entre com o valor do salario mínimo: "))

valor_hora=salario_minimo*0.1
imposto=0.03

salario=valor_hora*horas
imposto=salario*imposto

salario-=imposto
print("Salário `a receber: R$ ",locale.format("%1.2f",salario,2))
