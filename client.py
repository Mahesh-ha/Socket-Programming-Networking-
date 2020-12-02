# importing Tkinter and math
from tkinter import *
import math
from socket import *


# calc class
class calc:
    def send(self):
        serverName = '127.0.0.1'
        serverPort = 1206
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        self.ex = self.e.get()
        clientSocket.send((self.ex).encode())
        self.result = clientSocket.recv(1024).decode()
        self.mylist.insert(END, self.ex)
        self.mylist.insert(END, self.result)
        self.mylist.insert(END, "\n")
        self.mylist.yview('end')
        self.e.delete(0, END)
        self.e.insert(0, self.result)
        clientSocket.close()


    def clearall(self):
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0, END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END, argi)



    def __init__(self, master):
        """Constructor method"""
        master.title('Calulator')
        #label frame
        self.labels=Frame(master)
        label1 = Label(self.labels, text="CALCULATOR", font=("arial", 16, "bold"),bg="yellow",fg="red",relief="solid")
        label1.pack(side=LEFT)

        #scrollbar frame
        self.list = Frame(master)
        scrollbar = Scrollbar(self.list)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        self.mylist = Listbox(self.list,width=30,height=5, yscrollcommand=scrollbar.set)
        self.mylist.pack(side=RIGHT, fill=BOTH)
        scrollbar.config(command=self.mylist.yview)


        self.e = Entry(master)
        self.e.grid(row=3, column=0, columnspan=5, pady=5)
        self.e.focus_set() # Sets focus on the input text areas

        self.labels.grid(row=0, column=1, columnspan=10, sticky="ew")
        self.list.grid(row=1, column=0,columnspan=5, sticky="nsew")

        # Generating Buttons
        #row =5
        Button(master, text="log", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('log(')).grid(
            row=5, column=0)
        Button(master, text="ln", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('ln(')).grid(
            row=5, column=1)
        Button(master, text='AC', width=5, height=3, fg="red",
               bg="light green", command=lambda: self.clearall()).grid(
            row=5, column=2)
        Button(master, text='C', width=12, height=3, fg="red",
               bg="light green", command=lambda: self.clear1()).grid(
            row=5, column=3, columnspan=2)

        # row =6
        Button(master, text="y^x", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('^(')).grid(
            row=6, column=0)
        Button(master, text="X!", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('!')).grid(
            row=6, column=1)
        Button(master, text="e", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('e(')).grid(
            row=6, column=2)
        Button(master, text="(", width=5, height=3, fg="orange",
                bg="black", command=lambda: self.action('(')).grid(
            row=6, column=3)
        Button(master, text=")", width=5, height=3, fg="orange",
                bg="black", command=lambda: self.action(')')).grid(
            row=6, column=4)

        # row =7
        Button(master, text="7", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('7')).grid(
            row=7, column=0)
        Button(master, text="8", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('8')).grid(
            row=7, column=1)
        Button(master, text="9", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('9')).grid(
            row=7, column=2)
        Button(master, text='x²', width=5, height=3, fg="red",
               bg="green",command=lambda: self.action("\u00b2")).grid(
            row=7, column=3)
        Button(master, text="sqroot", width=5, height=3, fg="red",
               bg="green", command=lambda: self.action('**0.5')).grid(
            row=7, column=4)

        # row =8
        Button(master, text="4", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('4')).grid(
            row=8, column=0)
        Button(master, text="5", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('5')).grid(
            row=8, column=1)
        Button(master, text="6", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('6')).grid(
            row=8, column=2)
        Button(master, text='x', width=5, height=3,fg="red",
               bg="green", command=lambda: self.action('x')).grid(
            row=8, column=3)
        Button(master, text="÷", width=5, height=3, fg="red",
               bg="green", command=lambda: self.action('/')).grid(
            row=8, column=4)
        # row =9
        Button(master, text="1", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('1')).grid(
            row=9, column=0)
        Button(master, text="2", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('2')).grid(
            row=9, column=1)
        Button(master, text="3", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('3')).grid(
            row=9, column=2)
        Button(master, text='+', width=5, height=3, fg="red",
               bg="green",command=lambda: self.action('+')).grid(
            row=9, column=3)
        Button(master, text="-", width=5, height=3, fg="red",
               bg="green", command=lambda: self.action('-')).grid(
            row=9, column=4)
        # row =10
        Button(master, text="0", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('0')).grid(
            row=10, column=0)
        Button(master, text=".", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('.')).grid(
            row=10, column=1)
        Button(master, text="x10^n", width=5, height=3, fg="gray",
               bg="black", command=lambda: self.action('x10^(')).grid(
            row=10, column=2)
        Button(master, text='=', width=12, height=3,fg="red",
               bg="light green", command=lambda: self.send()).grid(
            row=10, column=3, columnspan=2)


    # Driver Code


root = Tk()

obj = calc(root)  # object instantiated

root.mainloop()