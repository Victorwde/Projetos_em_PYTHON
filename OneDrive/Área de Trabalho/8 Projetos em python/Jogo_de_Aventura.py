# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa
# qual é o cenário: eu estou numa guerra entre duas nações, e nós temos dois lados: lado A e lado B. Somente o lado A ira vencer, eo lado B ira perder! então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente o lado A irá conseguir!
import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul ? (n/s)' # norte = lado A, sul = lado B
        self.pergunta2 = 'Você prefere a espada ou escudo ? (espada/escudo)' # espada = lado A, escudo = lado B
        self.pergunta3 = 'Qual é a sua especialidade ? (linha de frente/tático)' # linha de frente = lado A, tático = lado B
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'
        
    def Iniciar(self):
        # layout
        layout = [
            [sg.Output(size=(50,0),key='respostas')],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!',layout=layout)
        while True :
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.eventos == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tático':
                        print(self.finalHistoria4)
    
    def LerValores(self):
        self.eventos, self.valores = self.janela.Read()




jogo = JogoDeAventura()
jogo.Iniciar()
