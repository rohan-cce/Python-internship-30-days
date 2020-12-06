from tkinter import * 

m = Tk()

m.title("COFFEE SHOP")



wel=Label(m,text="THE MACHINE WILL SERVE THE CUSTOMERS FOR 1000 TIMES..... ENJOY THE COFFEE")
wel.grid(column=0,row=0)

sts=Label(m,text="STATUS OF THE MACHINE (ON/OFF)")
sts.grid(column=0,row=3)

def on_clicked():
    on.configure(text=" THE MACHINE IS STARTED")
    on.grid(column=0,row=4)

    c_1=Label(text="***ENTER 1 FOR ESPRESSO")
    c_1.grid(column=0,row=5)
    c_2=Label(text="***ENTER 2 FOR LATTEE")
    c_2.grid(column=0,row=6)
    c_3=Label(text="***ENTER 3 FOR CAPPUCCINO")
    c_3.grid(column=0,row=7)

def choi_clicked():
    cof=Label(text="YOU HAVE CHOOSED YOUR DRINK")
    cof.grid(column=1,row=11)

    rep=Label(text="*****The report of the coffee machine *****")
    rep.grid(column=1,row=12)

    cur=Label(text="Current resource values are :")
    cur.grid(column=1,row=13)
    w=Label(text="----WATER = 500 ml")
    w.grid(column=1,row=14)
    m=Label(text="----MILK = 500 ml")
    m.grid(column=1,row=15)
    c=Label(text="----COFFEE = 500 ml")
    c.grid(column=1,row=16)
    mo=Label(text="----MONEY = $10")
    mo.grid(column=1,row=17)

    
    
    
            
on=Button(m,text="ON",bg="yellow",command=on_clicked)
on.grid(column=1,row=3)

def off_clicked():
    off.configure(text="PLEASE TURN ON THE MACHINE TO START THE SERVICE")
    off.grid(column=1,row=4)

off=Button(m,text="OFF",bg="red",command=off_clicked)
off.grid(column=2,row=3)


choi=Entry(m,width=20)
choi.grid(column=1,row=9)

choi_button=Button(m,text="OK",bg="pink",command=choi_clicked)
choi_button.grid(column=2,row=9)
   
   
def l_choose():
    l_w=Label(text="ENTER THE AMOUNT OF WATER YOU WANT TO ADD IN YOUR DRINK(in ml) :")
    l_w.grid(column=0,row=22)
    l_ws=Entry(m,width=20)
    l_ws.grid(column=1,row=22)
    l_m=Label(text="ENTER THE AMOUNT OF MILK YOU WANT TO ADD IN YOUR DRINK(in ml) :")
    l_m.grid(column=0,row=23)
    l_ms=Entry(m,width=20)
    l_ms.grid(column=1,row=23)
    l_c=Label(text="ENTER THE AMOUNT OF COFFEE YOU WANT TO ADD IN YOUR DRINK(in ml) :")
    l_c.grid(column=0,row=24)
    l_cs=Entry(m,width=20)
    l_cs.grid(column=1,row=24)

sk=Radiobutton(m,text="PRESS HERE TO CHOOSE YOUR INGREDIENTS TO YOUR COFFEE",command=l_choose)
sk.grid(column=0,row=19)
    
cos=Label(text="THE COST OF YOUR COFFEE IS $10")
cos.grid(column=1,row=26)

mon=Label(text="ENTER THE AMOUNT IN THE BELOW TEXT BOX")
mon.grid(column=1,row=27)

def money():
    l_q=Label(text="ENTER THE AMOUNT OF MONEY IN TERMS OF QUARTER($ 0.25):")
    l_q.grid(column=0,row=28)
    l_qs=Entry(m,width=10)
    l_qs.grid(column=1,row=28)
    l_d=Label(text="ENTER THE AMOUNT OF MONEY IN TERMS OF DIMES($0.10).IF ENTERED SUFFICIENT AMOUNT ENTER 0:")
    l_d.grid(column=0,row=29)
    l_ds=Entry(m,width=10)
    l_ds.grid(column=1,row=29)
    l_n=Label(text="ENTER THE AMOUNT OF MONEY IN TERMS OF NICKEL($0.05).IF ENTERED SUFFICIENT AMOUNT ENTER 0 :")
    l_n.grid(column=0,row=30)
    l_ns=Entry(m,width=10)
    l_ns.grid(column=1,row=30)
    l_p=Label(text="ENTER THE AMOUNT OF MONEY IN TERMS OF PENNIES($0.01).IF ENTERED SUFFICIENT AMOUNT ENTER 0 :")
    l_p.grid(column=0,row=31)
    l_ps=Entry(m,width=10)
    l_ps.grid(column=1,row=31)
    res=Label(text="MONEY RECEIVED \n ENJOY YOUR COFFEE \n THANK YOU!!!!!!!!!!!!!")
    res.grid(column=1,row=35)
    
set=Radiobutton(m,text="OK",command=money)
set.grid(column=2,row=27)


m.mainloop()