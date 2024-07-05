from collections import deque

pedidos = deque()
emPreparacao = deque()
pronto = deque()

def addPedido(pedido):
    pedidos.append(pedido)

def executaPedido():
    if pedidos:
        emPreparacao.append(pedidos.popleft())

def preparaPedido():
    if emPreparacao:
        pronto.append(emPreparacao.popleft())