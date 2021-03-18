import tkinter as tk
from random import randint
from time import sleep


class Interface:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')

        self.primeriocontainer = tk.Frame(master)
        self.primeriocontainer['pady'] = 30
        self.primeriocontainer.pack()

        self.segundocontainer = tk.Frame(master)
        self.segundocontainer['padx'] = 30
        self.segundocontainer.pack()

        self.terceirocontainer = tk.Frame(master)
        self.terceirocontainer['padx'] = 30
        self.terceirocontainer.pack()

        self.quartocontainer = tk.Frame(master)
        self.quartocontainer['pady'] = 30
        self.quartocontainer.pack()

        self.quintocontainer = tk.Frame(master)
        self.quintocontainer['pady'] = 20
        self.quintocontainer.pack()

        self.sextocontainer = tk.Frame(master)
        self.sextocontainer['padx'] = 20
        self.sextocontainer.pack()

        self.setimocontainer = tk.Frame(master)
        self.setimocontainer['pady'] = 30
        self.setimocontainer.pack()

        self.oitavocontainer = tk.Frame(master)
        self.oitavocontainer['pady'] = 30
        self.oitavocontainer.pack()

        # Titulo
        self.titulo = tk.Label(self.primeriocontainer, text='ROLETA DECISIVA')
        self.titulo['font'] = ('Adigiana Toybox', '25', 'bold')
        self.titulo.pack()

        self.titulo_roleta = tk.Label(self.segundocontainer, text='Qual o titulo para a Roleta: ', font=self.fontePadrao)
        self.titulo_roleta.pack(side=tk.LEFT)

        self.campo_titulo = tk.Entry(self.segundocontainer)
        self.campo_titulo['width'] = 30
        self.campo_titulo['font'] = self.fontePadrao
        self.campo_titulo.pack(side=tk.LEFT)

        self.opcao = tk.Label(self.terceirocontainer, text=f'{"Opção:".center(9)}', font=self.fontePadrao)
        self.opcao.pack(side=tk.LEFT)

        self.campo_opcao = tk.Entry(self.terceirocontainer)
        self.campo_opcao['width'] = 15
        self.campo_opcao['font'] = self.fontePadrao
        self.campo_opcao.pack(side=tk.LEFT)

        self.quantos_resultados = tk.Label(self.quintocontainer, text='Quantos Resultados Quer: ', font=self.fontePadrao)

        self.campo_quantidade_resultados = tk.Entry(self.quintocontainer)
        self.campo_quantidade_resultados['width'] = 10
        self.campo_quantidade_resultados['font'] = self.fontePadrao

        opcoes = list()

        self.botao_adicionar = tk.Button(self.quartocontainer)
        self.botao_adicionar['text'] = 'Adicionar Opção'
        self.botao_adicionar['font'] = ('Calibri', '11', 'bold')
        self.botao_adicionar['width'] = 15
        self.botao_adicionar['height'] = 1
        self.botao_adicionar['command'] = lambda: self.adicionar(opcoes)
        self.botao_adicionar.pack(side=tk.LEFT)

        self.botao_decidir = tk.Button(self.quartocontainer)
        self.botao_decidir['text'] = 'Decidir'
        self.botao_decidir['font'] = ('Calibri', '11', 'bold')
        self.botao_decidir['width'] = 15
        self.botao_decidir['height'] = 1
        self.botao_decidir['command'] = lambda: self.decidir(opcoes)
        self.botao_decidir.pack(side=tk.LEFT)

        self.tituloRoleta = tk.Label(self.sextocontainer, text='')
        self.tituloRoleta['font'] = ('Arial', '16', 'bold')
        self.tituloRoleta.pack()

        self.resultado = tk.Label(self.setimocontainer, text='')
        self.resultado['font'] = ('Script MT', '9', 'bold')
        self.resultado.pack()

        self.mensagem = tk.Label(self.oitavocontainer, text='')
        self.mensagem['font'] = ('Arial', '10', 'bold')
        self.mensagem.pack()

    def adicionar(self, opcoes):
        opcao = self.campo_opcao.get()
        if opcao in opcoes:
            self.mensagem['fg'] = 'red'
            self.mensagem['text'] = 'ERROR: Está opção já está adicionada'
        else:
            self.mensagem['fg'] = 'green'
            self.mensagem['text'] = 'Adicionado com sucesso'
            opcoes.append(opcao)
            return opcoes

    def decidir(self, opcoes):
        self.mensagem['text'] = ''
        self.quantos_resultados.pack(side=tk.LEFT)
        self.campo_quantidade_resultados.pack(side=tk.LEFT)
        self.botao_decidir['text'] = 'Mostrar Resultados'
        if self.campo_quantidade_resultados.get() != '':
            resultado = list()
            self.tituloRoleta['text'] = self.campo_titulo.get()
            quantidade_resultados = int(self.campo_quantidade_resultados.get())
            for valor in range(0, quantidade_resultados):
                index = randint(0, len(opcoes) - 1)
                opcao = opcoes[index]
                while opcao in resultado:
                    index = randint(0, len(opcoes) - 1)
                    opcao = opcoes[index]
                resultado.append(opcao)
            self.resultado['text'] = str(resultado)
