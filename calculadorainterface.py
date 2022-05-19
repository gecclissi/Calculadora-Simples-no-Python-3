from tkinter import *

top=Tk()
caixa =Frame(top)
caixa.pack()
top1 =Frame(top)
top1.pack()

def inselimp(): z.delete(0, END)

def inseigual():
    sinal = "".join(list(filter(lambda l: l in "+-*/", z.get())))
    print(sinal)
    numeros = z.get().split(sinal)
    exec(f'resultado = float(numeros[0]) {sinal} float(numeros[1])\nz.delete(0, END)\nz.insert(INSERT, str(round(resultado, 2)))')


z = Entry(caixa, width=40)
z.pack()

# o quadro de botoes
mat = [
    ['7','8','9','-'],
    ['4','5','6','/'],
    ['1','2','3','+'],
    ['c','0','*','=']
]
# a lista para armazenar os botoes (inicialmente vazia)
buttons = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        element = mat[i][j]
        btn = Button(top1, text=element, relief='groove', border=10, font='Times 24 bold')
        btn.grid(
                   row=i + 1, column=j + 1, stick=N + S + W + E, pady=3
               )

        if element == '=':
            # coloco o b=btn, para ele passar como parametro do lambda, sem matar o btn de origem
            btn.configure(command=lambda b=btn: inseigual())
        elif element == 'c':
            btn.configure(command=lambda b=btn: inselimp())
        else:
            # cget pega o valor do texto de dentro do botao
            btn.configure(command=lambda b=btn: z.insert(INSERT, b.cget('text')))
        # O append eh para os botoes ficarem registrados na memoria, assim eles nao se perdem, e nao se sobreescrevem
        buttons.append(btn)


top.title('fiec')
top.geometry("390x720+200+200")
top.mainloop()