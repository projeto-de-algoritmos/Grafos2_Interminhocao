from tkinter import *
from PIL import Image, ImageTk
from funcoes import *



#teste();



janela = Tk()
janela.geometry("1280x680")
janela.title("Grafos 1 Projeto de Algoritmos")
janela.resizable(height=False, width=False)
texto = Text(janela)



mapa =  Image.open("assets/UnbMap2.png")
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

def noA(x,y):
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
    if(y > 1):
        for k in x:
            print(k)
            if(k == 'ICC SUL'):
                botaoA.config(image=btn_select)
            if(k == 'IB'):
                botaoB.config(image=btn_select)
            if(k == 'IDA'):
                botaoC.config(image=btn_select)
            if(k == 'REITORIA'):
                botaoD.config(image=btn_select)
            if(k == 'FT'):
                botaoE.config(image=btn_select)
            if(k == 'CEUBINHO'):
                botaoF.config(image=btn_select)
            if(k == 'FD'):
                botaoG.config(image=btn_select)
            if(k == 'BCE'):
                botaoH.config(image=btn_select)
            if(k == 'ICC NORTE'):
                botaoI.config(image=btn_select)
    else:
        if(x == 'ICC SUL'):
            botaoA.config(image=btn_select)
        if(x == 'FT'):
            botaoE.config(image=btn_select)
        if(x == 'IDA'):
            botaoC.config(image=btn_select)
        if(x == 'IB'):
            botaoB.config(image=btn_select)
        if(x == 'REITORIA'):
            botaoD.config(image=btn_select)
        if(x == 'FT'):
            botaoE.config(image=btn_select)
        if(x == 'CEUBINHO'):
            botaoF.config(image=btn_select)
        if(x == 'FD'):
            botaoG.config(image=btn_select)
        if(x == 'BCE'):
            botaoH.config(image=btn_select)
        if(x == 'ICC NORTE'):
            botaoI.config(image=btn_select)

    #k.config(image=btn_select)



def addNo(x):

    nos.append(x)
    print(nos,len(nos))
    if len(nos) < 2:
        noA(x,len(nos))
    if len(nos) == 2:
        print('Menor caminho entre',nos[0],' e ',nos[1])

        canvas.create_rectangle(50, 10, 550, 40, fill="black")
        bbox = canvas.bbox("all")
        canvas.create_rectangle(bbox, outline="white")

        canvas.create_text(300,30, text="Menor caminho entre {no1} e {no2}".format(no1=nos[0], no2=nos[1]), fill="white" ,font=('Helvetica 15 bold'))
        #canvas.create_rectangle(canvas.bbox())
        canvas.pack()

        canvas.create_rectangle(25, 50, 575, 80, fill="black")
        bbox = canvas.bbox("all")
        canvas.create_rectangle(bbox, outline="white")



        y = dijkstra(graphPeso,nos[0],nos[1])
        x = y[1]

        canvas.create_text(300,70, text="Menor caminho = {no2}".format(no2=x), fill="white" ,font=('Helvetica 15 bold'))
        #canvas.create_rectangle(canvas.bbox())
        canvas.pack()
        noA(x,len(nos))
    if len(nos) > 2:
        nos.clear()
        #print("len", len(nos))
        noA(0, len(nos))

botaoA = Button(janela, image=btn_no,command=lambda: addNo('ICC SUL'), bd=0, highlightthickness=0)
botaoA.pack()
botaoA.place(x=430,y=450, anchor=NW)

botaoB = Button(janela, image=btn_no,command=lambda: addNo('IB'), bd=0, highlightthickness=0)
botaoB.pack()
botaoB.place(x=325,y=480, anchor=NW)

botaoC = Button(janela, image=btn_no,command=lambda: addNo('IDA'), bd=0, highlightthickness=0)
botaoC.pack()
botaoC.place(x=326,y=350, anchor=NW)

botaoD = Button(janela, image=btn_no,command=lambda: addNo('REITORIA'), bd=0, highlightthickness=0)
botaoD.pack()
botaoD.place(x=680,y=650, anchor=NW)

botaoE = Button(janela, image=btn_no,command=lambda: addNo('FT'), bd=0, highlightthickness=0)
botaoE.pack()
botaoE.place(x=700,y=120, anchor=NW)

botaoF = Button(janela, image=btn_no,command=lambda: addNo('CEUBINHO'), bd=0, highlightthickness=0)
botaoF.pack()
botaoF.place(x=680,y=315, anchor=NW)

botaoG = Button(janela, image=btn_no,command=lambda: addNo('FD'), bd=0, highlightthickness=0)
botaoG.pack()
botaoG.place(x=980,y=140, anchor=NW)

botaoH = Button(janela, image=btn_no,command=lambda: addNo('BCE'), bd=0, highlightthickness=0)
botaoH.pack()
botaoH.place(x=1080,y=440, anchor=NW)

botaoI = Button(janela, image=btn_no,command=lambda: addNo('ICC NORTE'), bd=0, highlightthickness=0)
botaoI.pack()
botaoI.place(x=820,y=180, anchor=NW)



janela.mainloop()
