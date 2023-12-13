from tkinter import *
from tkinter import messagebox

exp=""

def press(num):
    global exp
    exp=exp+str(num)
    a.set(exp)
    
def equal():
    global exp
    
    try:
        result=str(eval(exp))
        a.set(result)
        exp=""
        
    except:
        b='ERROR'
        a.set(b)
        exp=""

def clear():
    global exp
    exp=""
    a.set("")
    
if __name__ == '__main__':
    root=Tk()
    root.title('SIMPLE CALCULATOR')
    root.minsize(500,500)
    root.maxsize(500,500)
    root.iconbitmap('calc1.ico')
    frame=Frame(root,height=480,width=480,background='lightgreen',borderwidth=5)
    frame.place(x=10,y=10)
    f2=Frame(root,height=100,width=480,background='cyan',borderwidth=5,)
    f2.place(x=10,y=10)
    f3=Frame(frame,width=300,height=480,background='red')
    f3.place(x=0,y=20)

    a=StringVar()

    e1=Entry(f2,textvariable=a,width=60,bd=5,justify='right')
    e1.grid(columnspan=20,ipadx=50)
    
    
    ac=Button(frame,text='AC',height=4,width=8,borderwidth=5,command=clear)
    ac.place(x=305,y=290)

    eq=Button(frame,text='=',height=4,width=8,borderwidth=5,command=equal)
    eq.place(x=390,y=290)
            
    add=Button(frame,text='+',height=4,width=8,borderwidth=5,command=lambda:press('+'))
    add.place(x=305,y=110)

    sub=Button(frame,text='-',height=4,width=8,borderwidth=5,command=lambda:press('-'))
    sub.place(x=390,y=110)

    mul=Button(frame,text='x',height=4,width=8,borderwidth=5,command=lambda:press('*'))
    mul.place(x=305,y=200)

    div=Button(frame,text='/',height=4,width=8,borderwidth=5,command=lambda:press('/'))
    div.place(x=390,y=200)
    
    dot=Button(f3,text='.',height=5,width=10,borderwidth=5,command=lambda:press('.'),fg='blue')
    dot.place(x=200,y=330)

    b00=Button(f3,text='00',height=5,width=10,borderwidth=5,command=lambda:press('00'))
    b00.place(x=105,y=330)

    b0=Button(f3,text='0',height=5,width=10,borderwidth=5,command=lambda:press(0),fg='blue')
    b0.place(x=10,y=330)

    b1=Button(f3,text='1',height=5,width=10,borderwidth=5,command=lambda:press(1),fg='blue')
    b1.place(x=200,y=230)

    b2=Button(f3,text='2',height=5,width=10,borderwidth=5,command=lambda:press(2),fg='blue')
    b2.place(x=105,y=230)

    b3=Button(f3,text='3',height=5,width=10,borderwidth=5,command=lambda:press(3),fg='blue')
    b3.place(x=10,y=230)

    b4=Button(f3,text='4',height=5,width=10,borderwidth=5,command=lambda:press(4),fg='blue')
    b4.place(x=200,y=130)

    b5=Button(f3,text='5',height=5,width=10,borderwidth=5,command=lambda:press(5),fg='blue')
    b5.place(x=105,y=130)

    b6=Button(f3,text='6',height=5,width=10,borderwidth=5,command=lambda:press(6),fg='blue')
    b6.place(x=10,y=130)
    
    b7=Button(f3,text='7',height=5,width=10,borderwidth=5,command=lambda:press(7),fg='blue')
    b7.place(x=200,y=30)
    b8=Button(f3,text='8',height=5,width=10,borderwidth=5,command=lambda:press(8),fg='blue')
    b8.place(x=105,y=30)

    b9=Button(f3,text='9',height=5,width=10,borderwidth=5,command=lambda:press(9),fg='blue')
    b9.place(x=10,y=30)

    root.mainloop()
