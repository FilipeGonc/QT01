from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from Cadastro import cadastrar

class TelaCadastro(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregarTela = QUiLoader()
        self.tela = carregarTela.load('Tarefa.ui')
        self.componentes()
    
    def componentes(self):
        self.caixaDesc = self.tela.findChild(QtWidgets.QLineEdit, "caixaDesc")
        self.dateIni = self.tela.findChild(QtWidgets.QDateEdit, "dateIni")
        self.dateFim = self.tela.findChild(QtWidgets.QDateEdit, "dateFim")
        self.caixaResp = self.tela.findChild(QtWidgets.QComboBox, "caixaResp")
        self.caixaPrio = self.tela.findChild(QtWidgets.QComboBox, "caixaPrio")
        self.caixaObs = self.tela.findChild(QtWidgets.QTextEdit, "caixaObs")
        self.btnCad = self.tela.findChild(QtWidgets.QPushButton, "btnCad")

        self.btnCad.clicked.connect(self.funcaoCadastrar)


    def funcaoCadastrar(self):
        desc = self.caixaDesc.text()
        dataI = self.dateIni.text()
        dataF = self.dateFim.text()
        resp = self.caixaResp.currentText()
        prio = self.caixaPrio.currentText()
        obs = self.caixaObs.toPlainText()
        
        cadastrar(desc,dataI,dataF,resp,prio,obs)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaCadastro()
    interface.tela.show()
    app.exec()
    
