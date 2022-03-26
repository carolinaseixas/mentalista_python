#Jogo do mentalista
#Jogo contra a máquina no qual a máquina sorteia um número inteiro de 0 a 10, o usuário dá um palpite sobre qual é o número, se errar ganha uma dica e tem mais 2 chances para acertar

import tkinter as tk
from tkinter import ttk
import random


def verifica_resposta():
    tentativas = tk_tentativas.get()
    palpite = int(palpites.get())
    num = maquina.get()

    if tentativas > 1 and palpite != num:
        if palpite < num:
            resultado["text"] = "O número que voce escolheu é menor que o escolhido pela máquina. Tente novamente."
            diminui_tentativa()
        else:
            resultado["text"] = "O número que voce escolheu é maior que o escolhido pela máquina. Tente novamente."
            diminui_tentativa()
    elif tentativas > 0 and palpite == num:
        resultado["text"] = f"Parabéns! Você acertou! A máquina escolheu o número {num}."
    elif tentativas == 1 and palpite != num:
        resultado["text"] = f"Você errou e não possui mais tentativas. O número escolhido pela máquina foi {num}. Fim de jogo..."
        diminui_tentativa()


def diminui_tentativa():
    tentativas = tk_tentativas.get()
    tentativas_restantes = tentativas - 1
    tk_tentativas.set(tentativas_restantes)
    n_tentativas["text"] = f"Tentativas restantes: {tk_tentativas.get()}"


def reiniciar():
    maquina.set(random.randint(1, 10))
    tk_tentativas.set(3)
    n_tentativas["text"] = f"Tentativas restantes: {tk_tentativas.get()}"
    resultado["text"] = ""


# *****CRIAÇÃO DA INTERFACE GRÁFICA*****

janela = tk.Tk()
janela.title("Jogo do mentalista")
janela.resizable(False, False)

titulo = tk.Label(text="Jogo do mentalista", padx=10, pady=10, bg="black", fg="white", font=("Montserrat", 20), width=70, height=5)
titulo.grid(row=0, column=0, columnspan=3)

maquina = tk.IntVar(value=random.randint(1,11))

instrucao = tk.Label(text="A máquina escolheu um número inteiro entre 1 e 10. Qual número você acha que é? "
                          "Selecione seu palpite e clique em enviar.", padx=10, pady=15, font="Montserrat", height=3)
instrucao.grid(row=2, column=0, columnspan=3)

tk_tentativas = tk.IntVar(value=3)
n_tentativas = tk.Label(text=f"Tentativas restantes: {tk_tentativas.get()}", padx=10, pady=20, height=3)
n_tentativas.grid(row=4, column=0, sticky="E")

info_palpite = tk.Label(text="Selecione seu palpite:", padx=10, pady=20, font="Montserrat", height=3)
info_palpite.grid(row=4, column=1, sticky="E")

lista_palpites = [str(num + 1) for num in range(10)]
palpites = ttk.Combobox(janela, values=lista_palpites, state="readonly")
palpites.current(0)
palpites.grid(row=4, column=2, sticky="W")

enviar_palpite = tk.Button(text="Enviar palpite", command=verifica_resposta, pady=10, font="Montserrat", bg="gray", width=20)
enviar_palpite.grid(row=6, column=1, ipadx=8)

resultado = tk.Label(text="", padx=10, pady=15, font="Montserrat", height=3)
resultado.grid(row=8, column=0, columnspan=3)

enviar_palpite = tk.Button(text="Reiniciar", command=reiniciar, pady=8, bg="#ccc", width=10)
enviar_palpite.grid(row=9, column=2, ipadx=4)

janela.mainloop()

