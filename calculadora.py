
## pyinstaller --onefile --windowed 'NOME DO ARQUIVO' --> Esse comando é para tornar executável
from ast import Del
from cProfile import label
from tkinter import *
from turtle import end_fill

global anterior, operaçao
anterior = None
operaçao = None

def AC(visor):
    global anterior, operaçao
    visor.delete('1.0',END)
    visor.insert(INSERT,'0')
    anterior = None
    operaçao = None

def num(n):
    x = visor.get('1.0',END)
    if x =='0\n':
        visor.delete('1.0',END)
        visor.insert(INSERT,n)
    else:
        visor.insert(INSERT,n)


def cal(simbolo, visor):
    global anterior, operaçao
    if anterior == None:
        if simbolo == '<--':
           atual = visor.get("1.0",END)
           visor.delete('1.0',END)
           visor.insert(INSERT, atual[:-2])
        
        elif simbolo == 'x²':
            atual = visor.get('1.0',END)
            visor.delete('1.0',END)
            visor.insert(INSERT,float(atual)*float(atual))
        
        else:
           anterior = visor.get('1.0', END)
           visor.delete('1.0', END)
           operaçao = simbolo
        
    elif simbolo == "=":
        proximo = visor.get('1.0',END)
        if len(proximo) > 0:
            if operaçao == '+':
                visor.delete('1.0',END)
                visor.insert(INSERT,float(anterior)+float(proximo))
            elif operaçao == '-':
                visor.delete('1.0',END)
                visor.insert(INSERT,float(anterior)-float(proximo))
            elif operaçao == '*':
                visor.delete('1.0',END)
                visor.insert(INSERT,float(anterior)*float(proximo))
            elif operaçao == '/':
                visor.delete('1.0',END)
                visor.insert(INSERT,float(anterior) /float(proximo))
            elif operaçao == '√':
                visor.delete('1.0',END)
                visor.insert(INSERT,float(anterior)**(1/2))
            
                



    
janela = Tk()
janela.geometry('245x370')
janela.title('Calculadora')
visor = Text(janela, height=2.4, width=16,font='Arial 19 bold')
visor.place(x = '5', y = '5')

visor.insert(INSERT,'0')

btn = Button(janela, width=3,font='Arial 18 bold',text = 'AC', command=lambda: AC(visor))
btn.place(x = '5', y = '95')

btn2 = Button(janela,width=3,font='Arial 18 bold', text = 'x²', command=lambda:cal('x²',visor))
btn2.place(x = '65', y = '95')

btn3 = Button(janela,width=3,font='Arial 18 bold', text = '√', command=lambda:cal('√',visor))
btn3.place(x = '125', y = '95')

btn4 = Button(janela,width=3,font='Arial 18 bold', text = '/', command=lambda:cal('/',visor))
btn4.place(x = '185', y = '95')

btn5 = Button(janela,width=3,font='Arial 18 bold', text = '7', command=lambda:num('7'))
btn5.place(x = '5', y = '150')

btn6 = Button(janela,width=3,font='Arial 18 bold', text = '8', command=lambda:num('8'))
btn6.place(x = '65', y = '150')

btn7 = Button(janela,width=3,font='Arial 18 bold', text = '9', command=lambda:num('9'))
btn7.place(x = '125', y = '150')

btn8 = Button(janela,width=3,font='Arial 18 bold', text = '*', command=lambda:cal('*',visor))
btn8.place(x = '185', y = '150')

btn9 = Button(janela,width=3,font='Arial 18 bold', text = '4', command=lambda:num('4'))
btn9.place(x = '5', y = '205')

btn10 = Button(janela,width=3,font='Arial 18 bold', text = '5', command=lambda:num('5'))
btn10.place(x = '65', y = '205')

btn11 = Button(janela,width=3,font='Arial 18 bold', text = '6', command=lambda:num('6'))
btn11.place(x = '125', y = '205')

btn12 = Button(janela,width=3,font='Arial 18 bold', text = '-', command=lambda:cal('-',visor))
btn12.place(x = '185', y = '205')

btn13 = Button(janela,width=3,font='Arial 18 bold', text = '1', command=lambda:num('1'))
btn13.place(x = '5', y = '260')

btn14 = Button(janela,width=3,font='Arial 18 bold', text = '2', command=lambda:num('2'))
btn14.place(x = '65', y = '260')

btn15 = Button(janela,width=3,font='Arial 18 bold', text = '3', command=lambda:num('3'))
btn15.place(x = '125', y = '260')

btn16 = Button(janela,width=3,font='Arial 18 bold', text = '+', command=lambda:cal('+',visor))
btn16.place(x = '185', y = '260')

btn17 = Button(janela,width=3,font='Arial 18 bold', text = '0', command=lambda:num('0'))
btn17.place(x = '5', y = '315')

btn18 = Button(janela,width=3,font='Arial 18 bold', text = '.',command=lambda:num('.'))
btn18.place(x = '65', y = '315')

btn19 = Button(janela,width=3,font='Arial 18 bold', text = '<--', command=lambda:cal('<--',visor))
btn19.place(x = '125', y = '315')

btn20 = Button(janela,width=3,font='Arial 18 bold', text = '=', command=lambda:cal('=',visor))
btn20.place(x = '185', y = '315')

janela.mainloop()   







