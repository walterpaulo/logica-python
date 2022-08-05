class Celular():
    # método reservado, chamamos construtor
    def __init__(self):
        # propriedades, "self" é o objeto do escopo e chama propriedade dentro da estância.
        self.capa = ""
        self.cor = ""
        self.botoes = ""

    # métodos personalizados
    def liga(self):
      return f"Estou ligando o celular com capa({self.capa}) nos botões({self.botoes_formatados}))"

    def botoes_formatados(self):
      return ', '.join(self.botoes)

sansung = Celular()
sansung.capa = "B3G-TTT"
sansung.cor = "Preta"
sansung.botoes = ["Ligar", "Volume UP", "Volume Down"]
print(sansung.liga())

lg = Celular()
lg.capa = "KG-TTT"
lg.cor = "Azul"
lg.botoes = ["Ligar", "Volume UP", "Volume Down"]


iphone = Celular()
iphone.capa = "IP-ttt"
iphone.cor = "Preta"
