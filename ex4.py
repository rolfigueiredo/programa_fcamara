import locale
locale.setlocale(locale.LC_ALL, '')

print ("Calcular área:")

area=float(input("Entre com o tamanho em metros quadrados da área: "))

valor_lata=80

qtd_tinta=area/3

qtd_latas=qtd_tinta//18

if qtd_tinta % 18:
    qtd_latas+=1

valor_total=qtd_latas*valor_lata

print ("Quantidades de latas de tinta a serem compradas: ", int(qtd_latas)," - valor: R$ ",locale.format("%1.2f",valor_total,2))
