# Simuldor de dados
# Simular o uso de um dado, gerando um valor de 1 ate 6
import random 
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado ?"
        # layout
        self.layout = [
            [sg.Text("Jogar o Dado?")],
            [sg.Button("sim"),sg.Button("não")]
        ]
    
    def Iniciar(self):
         # criar um janela 
        self.janela = sg.Window("simulador de Dado",layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa som esses valores
        try:
            if self.eventos == "sim" or self.eventos == "s":
                self.gerarvalordodado()
            elif self.eventos == "não" or self.eventos == "n":
                print("Agradecemos a sua participação!")
            else:
                print("Favor digitar sim ou não")
        except:
            print("Ocorreu um erro ao receber sua resposta!")
    
    def gerarvalordodado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

Simulador = SimuladorDeDado()
Simulador.Iniciar()

    