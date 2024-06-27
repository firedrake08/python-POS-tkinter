import tkinter as tk
from tkinter import ttk
import items

currentCode = ""
currentBillItems = []
totalBill = 0
billframe = None
totalLabel = None

def setCurrentCode(code):
    global currentCode
    currentCode+=code

def getItem():
    global currentCode
    global currentBillItems
    itemlist = list(filter(lambda x:x['code']==currentCode,items.items))
    if(len(itemlist)):
        currentBillItems.append(itemlist[0])
        display['text']  = f"{list(itemlist)[0]['item']}   {list(itemlist)[0]['price']}"
        currentCode = ""
    else:
        currentCode = ""


def totalPrice():
    global totalBill
    global billframe
    global totalLabel
    global currentBillItems
    totalBill = sum(item['price'] for item in currentBillItems)
    display['text'] = f"Total:  {totalBill}"
    billframe = tk.Frame(invoice,relief="solid",bg="khaki")
    billframe.grid(column=0,row=1)
    for billIndex,billItem in enumerate(currentBillItems):
        billItemLabel = tk.Label(billframe,text=f"{billItem['item']}",bg="khaki",anchor="w")
        billItemLabel.grid(column=0,row=billIndex,sticky=tk.W+tk.E)
        billPriceLabel = tk.Label(billframe,text=f"{billItem['price']}",bg="khaki",anchor="e")
        billPriceLabel.grid(column=1,row=billIndex,sticky=tk.W+tk.E)
    totalLabel = tk.Label(invoice,text=f"Total:    {totalBill}",bg="khaki")
    totalLabel.grid(row=2,column=0)
    currentBillItems = []

def reset():
    global totalBill
    global billframe
    global totalLabel
    totalBill = 0
    display['text'] = totalBill
    billframe.destroy()
    totalLabel.destroy()

window = tk.Tk()
window.title("Counter")

frame = tk.Frame(
    window,
    padx=100,
    pady=100)
frame.pack()

display = tk.Label(frame,padx=20,bg="lightgreen",width=6,height=2)
display.grid(column=0,row=0,columnspan=3,sticky=tk.W+tk.E,pady=10)


seven = tk.Button(frame,text="7",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('7'))
seven.grid(column=0, row=1)
eight = tk.Button(frame,text="8",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('8'))
eight.grid(column=1, row=1)
nine = tk.Button(frame,text="9",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('9'))
nine.grid(column=2, row=1)
four = tk.Button(frame,text="4",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('4'))
four.grid(column=0, row=2)
five = tk.Button(frame,text="5",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('5'))
five.grid(column=1, row=2)
six = tk.Button(frame,text="6",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('6'))
six.grid(column=2, row=2)
one = tk.Button(frame,text="1",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('1'))
one.grid(column=0, row=3)
two = tk.Button(frame,text="2",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('2'))
two.grid(column=1, row=3)
three = tk.Button(frame,text="3",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('3'))
three.grid(column=2, row=3)
zero = tk.Button(frame,text="0",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('0'))
zero.grid(column=0, row=4)
enter = tk.Button(frame,text="Enter",bg="skyblue",width=6,font=3,command=getItem)
enter.grid(column=1,row=4,columnspan=2,sticky=tk.W+tk.E)
total = tk.Button(frame,text="Total",bg="orangered",font=3,command=totalPrice)
total.grid(column=0, row=5,columnspan=3,sticky=tk.W+tk.E)
reset = tk.Button(frame,text="reset",bg="pink",font=3,command=reset)
reset.grid(column=0, row=6,columnspan=3,sticky=tk.W+tk.E)

invoice =  tk.Frame(
frame,relief='solid',bd=1,bg="khaki")
invoice.grid(column=0,row=7,sticky=tk.W+tk.E,pady=10,columnspan=3)
invoice.grid_columnconfigure(0, weight=1)

bill = tk.Label(invoice,bg="khaki", text="Invoice", font=2)
bill.grid(column=0,row=0,sticky="ew")

window.mainloop()



