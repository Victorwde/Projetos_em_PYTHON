# chute o numero
# criar um algoritimo que gera um valor aleatorio e eu tenho que ficar chutando o numero ate acertar
import random 
import PySimpleGUI as sg
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True 

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text("Seu Chute: ",size=(39,0))],
            [sg.Input(size=(18,0),key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(39,10))]
        ]
        self.janela = sg.Window("Chute o Número!!!",layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # criar uma janela
                # receber os valores 
                self.eventos, self.valores = self.janela.Read()
                # fazer alguma coisa com estes valores
                if self.eventos == "Chutar!":
                    self.valor_do_chute = self.valores["ValorChute"]
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("chute um valor mais alto!")
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente == False
                            print("PARABÉNS VOCÊ ACERTOU!!!")
                            break
        except:
            print("Favor digitar apenas números")
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()