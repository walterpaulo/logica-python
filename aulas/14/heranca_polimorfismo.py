class Dispositivo():
  def __init__(self):
    self.nome = ""
    self.chip = ""

    def ligar(self):
      return f"Estou ligando o disposito #{self.nome}"

    def desliga(sef):
      return f"estou desligando o dispositivo #{self.nome} do chip {self.chip}"

class Celular(Dispositivo):
  # método reservado, chamamos construtor
    def __init__(self):
        # propriedades, "self" é o objeto do escopo e chama propriedade dentro da estância.
        self.capa = ""
        self.cor = ""
        self.botoes = ""

    def liga(self):
      # ligar_base = Dispositivo.ligar(self)
      return f"Estou ligando o celular com capa({self.capa}) nos botões({self.botoes_formatados}))"

    def botoes_formatados(self):
      return ', '.join(self.botoes)
      


sansung = Celular()
sansung.capa = "B3G-TTT"
sansung.cor = "Preta"
sansung.botoes = ["Ligar", "Volume UP", "Volume Down"]
print(sansung.liga())
# print(sansung.)