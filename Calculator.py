from tkinter import * 
from tkinter import messagebox
import tkinter.messagebox


def space(row,col): 
    Label(main,text=" ").grid(column=col,row=row)

main=Tk()
main.title('Calculator')
main.geometry('{}x{}'.format(310,245))
main.resizable(False,False)

space(0,0)
global e
e=Entry(main,width=40,borderwidth=3)
e.grid(row=1,column=0,columnspan=5)
space(2,0)


def operation(par):
	global f
	f=par
	global fnum
	fnum=e.get()
	e.delete(0,END)

def equal():
	if f=='add':
		snum=e.get()
		e.delete(0,END)
		e.insert(0,float(fnum)+float(snum))
	elif f=='multiply':
		snum=e.get()
		e.delete(0,END)
		e.insert(0,float(fnum)*float(snum))
	elif f=='divide':
		snum=e.get()
		e.delete(0,END)
		e.insert(0,float(fnum)/float(snum))
	elif f=='subtract':
		snum=e.get()
		e.delete(0,END)
		e.insert(0,float(fnum)-float(snum))
	elif f=='root':
		e.insert(0,float(fnum)**(0.5))
	elif f=='square':
		e.insert(0,float(fnum)**2)
	elif f=='power':
		snum=e.get()
		e.delete(0,END)
		e.insert(0,float(fnum)**float(snum))

def click(num):
	global c
	c=e.get()
	e.delete(0,END)
	e.insert(0,c+str(num))

# **** BUTTONS *****
decimal=Button(main,text='.',command=lambda:click('.'),padx=25,pady=10).grid(row=3,column=0)
root=Button(main,text='Sq root',command=lambda:operation('root'),padx=8,pady=10).grid(row=3,column=1)
square=Button(main,text='Square',command=lambda:operation('square'),padx=10,pady=10).grid(row=3,column=2)
power=Button(main,text='Power',command=lambda:operation('power'),padx=10,pady=10).grid(row=3,column=3)
clear=Button(main,text='CLR',command=lambda:e.delete(0,END),padx=14, pady=10).grid(row=3,column=4)


b7=Button(main,text='7',bg='#b8b8b8',command=lambda:click(7),padx=24,pady=10).grid(row=4,column=0)
b8=Button(main,text='8',bg='#b8b8b8',command=lambda:click(8),padx=24,pady=10).grid(row=4,column=1)
b9=Button(main,text='9',bg='#b8b8b8',command=lambda:click(9),padx=24,pady=10).grid(row=4,column=2)
mult=Button(main,text='*',command=lambda:operation('multiply'),padx=23,pady=10).grid(row=4,column=3)
div=Button(main,text='/',command=lambda:operation('divide'),padx=23,pady=10).grid(row=4,column=4)


b6=Button(main,text='6',bg='#b8b8b8',command=lambda:click(6),padx=24,pady=10).grid(row=5,column=0)
b5=Button(main,text='5',bg='#b8b8b8',command=lambda:click(5),padx=24,pady=10).grid(row=5,column=1)
b4=Button(main,text='4',bg='#b8b8b8',command=lambda:click(4),padx=24,pady=10).grid(row=5,column=2)
add=Button(main,text='+',command=lambda:operation('add'),padx=20,pady=10).grid(row=5,column=3)
subt=Button(main,text='-',command=lambda:operation('subtract'),padx=23,pady=10).grid(row=5,column=4)


b3=Button(main,text='3',bg='#b8b8b8',command=lambda:click(3),padx=24,pady=10).grid(row=6,column=0)
b2=Button(main,text='2',bg='#b8b8b8',command=lambda:click(2),padx=24,pady=10).grid(row=6,column=1)
b1=Button(main,text='1',bg='#b8b8b8',command=lambda:click(1),padx=24,pady=10).grid(row=6,column=2)
equal=Button(main,text='=',command=equal,padx=50,pady=10).grid(row=6,column=3,columnspan=2,rowspan=2)

main.mainloop()
