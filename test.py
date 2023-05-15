from tkinter import *
from PIL import Image, ImageTk
from funcoes import *



#teste();
#x = bfs(graph, "A", "E")


janela = Tk()
janela.geometry("1280x680")
janela.title("Grafos 1 Projeto de Algoritmos")
janela.resizable(height=False, width=False)
texto = Text(janela)



mapa =  Image.open("assets/UnBgrafo.png")
img_no = Image.open("assets/square.png")
img_no_selecionado = Image.open("assets/greensquare.png")

canvas = Canvas(janela, width=1280, height=720)
canvas.pack()


resized_image = mapa.resize((1280,680), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

canvas.create_image(0,0,anchor=NW, image=new_image)

resized_btn = img_no.resize((30,30))
btn_no = ImageTk.PhotoImage(resized_btn)

resized_green_btn = img_no_selecionado.resize((30,30))
btn_select = ImageTk.PhotoImage(resized_green_btn)

nos = []

def no(x):
    #print("A")

    if x == 0:
        botaoA.config(image=btn_no)
        botaoB.config(image=btn_no)
        botaoC.config(image=btn_no)
        botaoD.config(image=btn_no)
        botaoE.config(image=btn_no)
        botaoF.config(image=btn_no)
        botaoG.config(image=btn_no)
        botaoH.config(image=btn_no)
        botaoI.config(image=btn_no)
    else:
        for k in x:
            if(k[0] == 'A'):
                botaoA.config(image=btn_select)
            if(k[0] == 'B'):
                botaoB.config(image=btn_select)
            if(k[0] == 'C'):
                botaoC.config(image=btn_select)
            if(k[0] == 'D'):
                botaoD.config(image=btn_select)
            if(k[0] == 'E'):
                botaoE.config(image=btn_select)
            if(k[0] == 'F'):
                botaoF.config(image=btn_select)
            if(k[0] == 'G'):
                botaoG.config(image=btn_select)
            if(k[0] == 'H'):
                botaoH.config(image=btn_select)
            if(k[0] == 'I'):
                botaoI.config(image=btn_select)

    #k.config(image=btn_select)



def addNo(x):

    nos.append(x)
    #print(nos)
    if len(nos) < 2:
        no(x)
    if len(nos) == 2:
        print('Menor caminho entre',nos[0],' e ',nos[1])

        canvas.create_rectangle(100, 10, 500, 40, fill="black")
        bbox = canvas.bbox("all")
        canvas.create_rectangle(bbox, outline="white")

        canvas.create_text(300,30, text="Menor caminho entre {no1} e {no2}".format(no1=nos[0], no2=nos[1]), fill="white" ,font=('Helvetica 15 bold'))
        #canvas.create_rectangle(canvas.bbox())
        canvas.pack()

        canvas.create_rectangle(100, 100, 500, 70, fill="black")
        bbox = canvas.bbox("all")
        canvas.create_rectangle(bbox, outline="white")

        x = bfs(graph,nos[0],nos[1])
        canvas.create_text(300,90, text="Menor caminho = {no2}".format(no2=x), fill="white" ,font=('Helvetica 15 bold'))
        #canvas.create_rectangle(canvas.bbox())
        canvas.pack()
        no(x)
    if len(nos) > 2:
        nos.clear()
        #print("len", len(nos))
        no(0)


class Pesos:
    peso = 0

pesosA = Pesos()
pesosB = Pesos()
pesosC = Pesos()
pesosD = Pesos()
pesosE = Pesos()
pesosF = Pesos()
pesosG = Pesos()
pesosH = Pesos()
pesosI = Pesos()

pesos = locals()
botao = locals()

def weight(y):
    p = pesos["pesos" + y]
    b = botao["botao"+y]
    b.config(image=btn_select)
    p.peso += 1
    if p.peso > 4:
        p.peso = 0
        b.config(image=btn_no)
    print(y)
    print(p.peso)



botaoA = Button(janela, image=btn_no,command=lambda: addNo('A'), bd=0, highlightthickness=0)
botaoA.pack()
botaoA.place(x=430,y=450, anchor=NW)
botaoA.bind("<Button-2>", lambda event: weight('A'))
botaoA.bind("<Button-3>", lambda event: weight('A'))

botaoB = Button(janela, image=btn_no,command=lambda: addNo('B'), bd=0, highlightthickness=0)
botaoB.pack()
botaoB.place(x=325,y=480, anchor=NW)
botaoB.bind("<Button-2>", lambda event: weight('B'))
botaoB.bind("<Button-3>", lambda event: weight('B'))

botaoC = Button(janela, image=btn_no,command=lambda: addNo('C'), bd=0, highlightthickness=0)
botaoC.pack()
botaoC.place(x=326,y=350, anchor=NW)
botaoC.bind("<Button-2>", lambda event: weight('C'))
botaoC.bind("<Button-3>", lambda event: weight('C'))

botaoD = Button(janela, image=btn_no,command=lambda: addNo('D'), bd=0, highlightthickness=0)
botaoD.pack()
botaoD.place(x=680,y=650, anchor=NW)
botaoD.bind("<Button-2>", lambda event: weight('D'))
botaoD.bind("<Button-3>", lambda event: weight('D'))

botaoE = Button(janela, image=btn_no,command=lambda: addNo('E'), bd=0, highlightthickness=0)
botaoE.pack()
botaoE.place(x=700,y=120, anchor=NW)
botaoE.bind("<Button-2>", lambda event: weight('E'))
botaoE.bind("<Button-3>", lambda event: weight('E'))

botaoF = Button(janela, image=btn_no,command=lambda: addNo('F'), bd=0, highlightthickness=0)
botaoF.pack()
botaoF.place(x=725,y=335, anchor=NW)
botaoF.bind("<Button-2>", lambda event: weight('F'))
botaoF.bind("<Button-3>", lambda event: weight('F'))

botaoG = Button(janela, image=btn_no,command=lambda: addNo('G'), bd=0, highlightthickness=0)
botaoG.pack()
botaoG.place(x=980,y=140, anchor=NW)
botaoG.bind("<Button-2>", lambda event: weight('G'))
botaoG.bind("<Button-3>", lambda event: weight('G'))

botaoH = Button(janela, image=btn_no,command=lambda: addNo('H'), bd=0, highlightthickness=0)
botaoH.pack()
botaoH.place(x=1080,y=440, anchor=NW)
botaoH.bind("<Button-2>", lambda event: weight('H'))
botaoH.bind("<Button-3>", lambda event: weight('H'))

botaoI = Button(janela, image=btn_no,command=lambda: addNo('I'), bd=0, highlightthickness=0)
botaoI.pack()
botaoI.place(x=820,y=180, anchor=NW)
botaoI.bind("<Button-2>", lambda event: weight('I'))
botaoI.bind("<Button-3>", lambda event: weight('I'))



janela.mainloop()
