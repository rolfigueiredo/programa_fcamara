class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
     
    def setBase(self, base):
        self.base = base
     
    def setAltura(self, altura):
        self.conta = altura
    
    def getBase(self):
        return self.base
    
    def getAltura(self):
        return self.altura
    
    def calcularArea(self):
        return float(self.base*self.altura)
    
    def calcularPerimetro(self):
        return float(self.base*3)

print ("Retângulo:")

retangulo=Retangulo(float(input("Entre com a base do RETÂNGULO: ")),float(input("Entre com a altura do RETÂNGULO: ")))
#cada piso tem como medida 45cm x 45cm
pisos=retangulo.calcularArea()*(0.45*2)
rodape=pisos*0.1

print ("Tamanho da área: ",retangulo.calcularArea())
print ("Quantidade de pisos: ",pisos)
print ("Quantidade de rodapes: ",rodape)
