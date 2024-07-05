from PySide6.QtWidgets import QApplication
from mainWindow import Window

app = QApplication()
janela = Window()
janela.show()

app.exec()