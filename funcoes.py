from collections import deque


pedidos = deque()
emPreparacao = deque()
pronto = deque()
# Função para adicionar pedido à fila de pedidos
def addPedido(pedido):
    pedidos.append(pedido)

# Função para transferir pedidos entre filas
def executaPedido():
    if pedidos:
        emPreparacao.append(pedidos.popleft())

def preparaPedido():
    if emPreparacao:
        pronto.append(emPreparacao.popleft())