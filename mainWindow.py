from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget
from classePedido import Pedido
from itens import Itens, Hamburgeres, HamburgerCarne, Bebidas, Cocacola
from funcoes import addPedido, executaPedido, preparaPedido, pedidos, emPreparacao, pronto

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trabalho")
        self.pedido_atual = Pedido()

        self.setCentralWidget(QWidget())
        self.principal()

    def principal(self):
        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(50)

        label = QLabel('Bem vindo ao \nBar do Alemão')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        botao = QPushButton('Cardápio')
        botao.clicked.connect(self.cardapio)
        botao2 = QPushButton('Atendente')
        botao2.clicked.connect(self.pedido)
        botao3 = QPushButton('Cozinha')
        botao3.clicked.connect(self.cozinha)

        layout.addWidget(label)
        layout.addWidget(botao)
        layout.addWidget(botao2)
        layout.addWidget(botao3)

        self.setCentralWidget(base)
        base.setLayout(layout)

    def cardapio(self):
        base = QWidget()
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(50)

        label = QLabel('Cardápio')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(botao_voltar)

        self.setCentralWidget(base)
        base.setLayout(layout)

    def pedido(self):
        base = QWidget()
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(50)

        label = QLabel('Atendente')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        botao_hamburguer = QPushButton('Hamburger+1')
        botao_hamburguer.clicked.connect(self.add_hamburguer)
        
        botao_executar_pedido = QPushButton('Executar Pedido')
        botao_executar_pedido.clicked.connect(self.executar_pedido)
        
        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(botao_hamburguer)
        layout.addWidget(botao_executar_pedido)
        layout.addWidget(botao_voltar)

        self.setCentralWidget(base)
        base.setLayout(layout)

    def cozinha(self):
        base = QWidget()
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(50)

        label = QLabel('Cozinha')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        self.pedidos_list = QListWidget()
        self.em_preparacao_list = QListWidget()
        self.pronto_list = QListWidget()

        botao_preparar = QPushButton('Preparar Pedido')
        botao_preparar.clicked.connect(self.preparar_pedido)
        
        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(QLabel('Pedidos:'))
        layout.addWidget(self.pedidos_list)
        layout.addWidget(QLabel('Em Preparação:'))
        layout.addWidget(self.em_preparacao_list)
        layout.addWidget(QLabel('Pronto:'))
        layout.addWidget(self.pronto_list)
        layout.addWidget(botao_preparar)
        layout.addWidget(botao_voltar)

        self.setCentralWidget(base)
        base.setLayout(layout)
        self.update_lists()

    def add_hamburguer(self):
        item = HamburgerCarne("Hamburger de Carne", "P")
        self.pedido_atual.addItem(item, 1)

    def executar_pedido(self):
        addPedido(self.pedido_atual)
        self.pedido_atual = Pedido()
        executaPedido()

    def preparar_pedido(self):
        preparaPedido()
        self.update_lists()

    def update_lists(self):
        self.pedidos_list.clear()
        self.em_preparacao_list.clear()
        self.pronto_list.clear()

        self.pedidos_list.addItems([str(pedido) for pedido in pedidos])
        self.em_preparacao_list.addItems([str(pedido) for pedido in emPreparacao])
        self.pronto_list.addItems([str(pedido) for pedido in pronto])