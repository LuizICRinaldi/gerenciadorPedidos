from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget
from classePedido import Pedido
from itens import HamburgerCarne, Cocacola
from funcoes import addPedido, executaPedido, preparaPedido, pedidos, emPreparacao, pronto

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trabalho Grau B")
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
        fontText = QFont()
        fontText.setPixelSize(25)

        label = QLabel('Cardápio')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        hamburger = QLabel('Hamburger      35R$')
        hamburger.setAlignment(Qt.AlignLeft)
        hamburger.setFont(fontText)

        coca = QLabel('Coca-cola        5R$')
        coca.setAlignment(Qt.AlignLeft)
        coca.setFont(fontText)


        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(hamburger)
        layout.addWidget(coca)
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

        botao_hamburguer = QPushButton('Adicionar Hamburger')
        botao_hamburguer.clicked.connect(self.add_hamburguer)

        botao_coca = QPushButton('Adicionar Coca-cola')
        botao_coca.clicked.connect(self.add_coca)
        
        botao_fazer_pedido = QPushButton('Fazer Pedido')
        botao_fazer_pedido.clicked.connect(self.fazer_pedido)
        
        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(botao_hamburguer)
        layout.addWidget(botao_coca)
        layout.addWidget(botao_fazer_pedido)
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

        botao_comecar = QPushButton('comecar Pedido')
        botao_comecar.clicked.connect(self.comecar_pedido)

        botao_preparar = QPushButton('Preparar Pedido')
        botao_preparar.clicked.connect(self.preparar_pedido)
        
        botao_voltar = QPushButton('Voltar')
        botao_voltar.clicked.connect(self.principal)

        layout.addWidget(label)
        layout.addWidget(QLabel('Pedidos:'))
        layout.addWidget(self.pedidos_list)
        layout.addWidget(botao_comecar)
        layout.addWidget(QLabel('Em Preparação:'))
        layout.addWidget(self.em_preparacao_list)
        layout.addWidget(botao_preparar)
        layout.addWidget(QLabel('Pronto:'))
        layout.addWidget(self.pronto_list)
        
        layout.addWidget(botao_voltar)

        self.setCentralWidget(base)
        base.setLayout(layout)
        self.update_lists()

    def add_hamburguer(self):
        item = HamburgerCarne("Hamburger de Carne", "P")
        self.pedido_atual.addItem(item, 1)

    def add_coca(self):
        item = Cocacola("Coquinha")
        self.pedido_atual.addItem(item, 1)

    def fazer_pedido(self):
        addPedido(self.pedido_atual)
        self.pedido_atual = Pedido()

    def comecar_pedido(self):
        executaPedido()
        self.update_lists()
    
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