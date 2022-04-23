# Projeto 5 - decida por mim
# Faça uma pergunta para o programa e ele terá que te dar uma resposta 
import random
import PySimpleGUI as sg
class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Não sei, você sabe!',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!',layout=layout)
        while True:
            # ler os valores
            self.eventos, self.valores = self.janela.Read()
            # fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                

decida = DecidaPorMim()
decida.Iniciar()