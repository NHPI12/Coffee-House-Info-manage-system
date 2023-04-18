from tkinter import *

import tkinter as tk
from GUI_employee import EmployeeTable
from GUI_product import ProductTable

class main_menu:
    def __init__(self,root):
        self.root = root
        root.title("Coffee House Information Management System")
        root.geometry("600x400")

        #Titlte Frame:
        TitleFrame = Label(root,bd = 10, relief= RIDGE,bg = "saddle brown")
        TitleFrame.place (x = 0, y = 0, width = 500, height = 400)
        TitleLabel = Label(TitleFrame,text = "Coffee House\n\nInformation Management\n\nSystem",fg = "white",font = ("Arial",20,"bold"),bg = "saddle brown")
        TitleLabel.place (x=25,y=40)
        # Button Frame
        ButtonFrame = Frame(root,bd = 10,relief= RIDGE)
        ButtonFrame.place(x = 400,y = 0,width= 200, height= 400)

        #Button
        btnEmployeeLabel = LabelFrame(ButtonFrame,bd = 2, bg = "black")
        btnEmployeeLabel.place(x =30, y= 50, width = 122, height = 40)
        ButtonEmployee = Button(btnEmployeeLabel,text = "Employee",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 10,command=self.Employee_open)
        ButtonEmployee.grid(row=  0, column= 0, padx= 5, pady=2)
        btnProductLabel = LabelFrame(ButtonFrame,bd = 2, bg = "black")
        btnProductLabel.place(x =30, y= 150, width = 122, height = 40)
        ButtonProduct = Button(btnProductLabel,text = "Product",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 10,command=self.Product_open)
        ButtonProduct.grid(row= 0, column= 0, padx= 5, pady= 2)
        btnLabelQuit = LabelFrame(ButtonFrame,bd = 2, bg = "black")
        btnLabelQuit.place(x =30, y= 250, width = 122, height = 40)
        ButtonQuit = Button(btnLabelQuit,text = "Exit",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 10,command= root.quit)
        ButtonQuit.grid(row = 0, column = 0, padx =5, pady = 2)
    #Function
    def Employee_open(self):
        new_window = tk.Toplevel()
        EmployeeTable(new_window)
    def Product_open(self):
        product_window = tk.Toplevel()
        ProductTable(product_window)
    
    
root = Tk()
objs = main_menu(root)
root.mainloop()