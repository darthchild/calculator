from tkinter import * 
from math import *
from tkinter import messagebox


main=Tk()
main.title('Calculator')
main.geometry('{}x{}'.format(316,287))
main.resizable(False,False)

Label(main,text=" ").grid(column=0,row=0)
entryF=Entry(main,width=40,borderwidth=3)
entryF.grid(row=1,column=0,columnspan=5)
Label(main,text=" ").grid(column=0,row=2)
fontTuple=('Corbel',10,'bold')

def initialize(par):
	global operation,firstNumber

	operation=par
	firstNumber=entryF.get()  #gets first number form the entry field
	entryF.delete(0,END)

def calculate():
	try:
		if operation =='add':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)+float(secondNumber))

		elif operation =='multiply':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)*float(secondNumber))

		elif operation =='divide':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)/float(secondNumber))

		elif operation =='subtract':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)-float(secondNumber))

		elif operation =='root':
			entryF.insert(0,float(firstNumber)**(0.5))

		elif operation =='square':
			entryF.insert(0,float(firstNumber)**2)

		elif operation =='power':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)**float(secondNumber))

		elif operation =='percent':
			secondNumber=entryF.get()
			entryF.delete(0,END)
			entryF.insert(0,float(firstNumber)/100)

		elif operation =='ln':
			answer= log( int(firstNumber) )
			entryF.insert(0,float(answer))

	# FACTORIAL FUNCTION NOT WORKING 
		elif operation =='factorial':
			print(firstNumber)
			answer= factorial( int(firstNumber) )
			entryF.insert(0,float(answer))
	except:
		messagebox.showerror('Error','Inavlid request')


def clickButton(num):
	global c
	c=entryF.get()
	entryF.delete(0,END)
	entryF.insert(0,c+str(num))

# **** BUTTONS *****

percent=Button(main,text='%',font=fontTuple,command=lambda:initialize('percent'),padx=22,pady=10).grid(row=3,column=0)
root=Button(main,text='√',font=fontTuple,command=lambda:initialize('root'),padx=23,pady=10).grid(row=3,column=1)
square=Button(main,text='x²',font=fontTuple,command=lambda:initialize('square'),padx=22,pady=10).grid(row=3,column=2)
power=Button(main,text='xⁿ',font=fontTuple,command=lambda:initialize('power'),padx=20,pady=10).grid(row=3,column=3)
clear=Button(main,text='CLR',font=fontTuple,command=lambda:entryF.delete(0,END),padx=14, pady=10).grid(row=3,column=4)


b7=Button(main,text='7',bg='#b8b8b8',command=lambda:clickButton(7),padx=24,pady=10).grid(row=4,column=0)
b8=Button(main,text='8',bg='#b8b8b8',command=lambda:clickButton(8),padx=24,pady=10).grid(row=4,column=1)
b9=Button(main,text='9',bg='#b8b8b8',command=lambda:clickButton(9),padx=24,pady=10).grid(row=4,column=2)
ln=Button(main,text='ln',font=fontTuple,command=lambda:initialize('ln'),padx=21,pady=10).grid(row=4,column=3)
factorial=Button(main,text='n!',font=fontTuple,command=lambda:initialize('factorial'),padx=20,pady=10).grid(row=4,column=4)


b4=Button(main,text='4',bg='#b8b8b8',command=lambda:clickButton(4),padx=24,pady=10).grid(row=5,column=0)
b5=Button(main,text='5',bg='#b8b8b8',command=lambda:clickButton(5),padx=24,pady=10).grid(row=5,column=1)
b6=Button(main,text='6',bg='#b8b8b8',command=lambda:clickButton(6),padx=24,pady=10).grid(row=5,column=2)
mult=Button(main,text='×',font=fontTuple,command=lambda:initialize('multiply'),padx=23,pady=10).grid(row=5,column=3)
div=Button(main,text='÷',font=('Corbel',12,'bold'),command=lambda:initialize('divide'),padx=20,pady=7).grid(row=5,column=4)


b1=Button(main,text='1',bg='#b8b8b8',command=lambda:clickButton(1),padx=24,pady=10).grid(row=6,column=0)
b2=Button(main,text='2',bg='#b8b8b8',command=lambda:clickButton(2),padx=24,pady=10).grid(row=6,column=1)
b3=Button(main,text='3',bg='#b8b8b8',command=lambda:clickButton(3),padx=24,pady=10).grid(row=6,column=2)
add=Button(main,text='+',font=fontTuple,command=lambda:initialize('add'),padx=23,pady=10).grid(row=6,column=3)
subt=Button(main,text='-',font=('Corbel',14,'bold'),command=lambda:initialize('subtract'),padx=20,pady=3).grid(row=6,column=4)

decimal=Button(main,text='.',font=fontTuple,command=lambda:clickButton('.'),padx=25,pady=10).grid(row=7,column=0)
b0=Button(main,text='0',bg='#b8b8b8',command=lambda:clickButton(0),padx=24,pady=10).grid(row=7,column=1)
pi=Button(main,text='π',command=lambda:clickButton('3.14159'),padx=24,pady=10).grid(row=7,column=2)
calculate=Button(main,text='=',font=fontTuple,command=calculate,padx=53,pady=10).grid(row=7,column=3,columnspan=2,rowspan=1)


main.mainloop()