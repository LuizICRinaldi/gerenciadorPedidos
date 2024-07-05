class Pedido:
    id_counter = 1

    def __init__(self):
        self.id = Pedido.id_counter
        Pedido.id_counter += 1
        self.itens = []
        self.preco = 0

    def addItem(self, item, qtd):
        self.itens.append((item, qtd))
        self.calcularPreco()

    def calcularPreco(self):
        self.preco = 0
        for item, qtd in self.itens:
            self.preco += item.getPreco() * qtd

    def __str__(self):
        itens_str = "\n".join([f"{item} x {qtd}" for item, qtd in self.itens])
        return f"Pedido ID: {self.id}\nItens:\n{itens_str}\nTotal: R${self.preco:.2f}\n"