class Itens:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}: R${self.getPreco():.2f}"

    def getPreco(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse")

class Hamburgeres(Itens):
    def __init__(self, nome, tamanho):
        super().__init__(nome)
        self.tamanho = tamanho

class HamburgerCarne(Hamburgeres):
    preco = 35.00
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)

    def getPreco(self):
        return HamburgerCarne.preco

class Bebidas(Itens):
    def __init__(self, nome):
        super().__init__(nome)

class Cocacola(Bebidas):
    preco = 5.00
    def __init__(self, nome):
        super().__init__(nome)

    def getPreco(self):
        return Cocacola.preco