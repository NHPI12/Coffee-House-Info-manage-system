from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


class ProductTable:
    def __init__(self,root):
        self.root = root
        self.root.title("Coffee House management system")
        self.root.geometry("1540x800+0+0")
        self.root.configure(bg = 'saddle brown')
        self.coffee_image = Image.open("d:/Python/Project/coffe_banner.jpg") #import image
        self.resized = self.coffee_image.resize((1000,260),Image.ANTIALIAS) #resized image
        self.new_coffee_img = ImageTk.PhotoImage(self.resized) #new resized image
        self.product_ID = StringVar()        #  
        self.product_name = StringVar()      #  
        self.product_type = StringVar()      # Variables
        self.product_price = StringVar()     # 
        lbltitle = Label(self.root,relief=FLAT, bd = 20,text = "Product Information Management System",fg = "white", bg= "saddle brown",font=("Arial",50))
        lbltitle.pack(side=TOP, fill = X)

        #Dataframe
        Dataframe = Frame(self.root,bd = 10,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530, height = 400)

        DataframeLeft = LabelFrame(Dataframe,bd =5,relief= RIDGE,padx=10,font=("Arial",12,"bold"),text="Product information")
        DataframeLeft.place(x = 0, y = 5, width =980, height=350)

        DataframeRight = LabelFrame(Dataframe,bd =5,relief= RIDGE,padx=10,font=("Arial",12,"bold"),text="Input bar")
        DataframeRight.place(x = 990, y = 5, width =460, height=350)

         #button frame
        Buttonframe = Frame(self.root,bd = 10,relief=RIDGE)
        Buttonframe.place(x=990,y=530,width=540, height = 260)   

        #banner frame
        bannerframe = Frame (self.root, bd = 10)
        bannerframe.place(x=-210,y=530,width=1200, height = 260)
        imageFrame = Label(bannerframe,image= self.new_coffee_img)
        imageFrame.place(x = 200, y = -20)

        #dataframeright
        lblNameID = Label(DataframeRight,font = ("arial",12,"bold"),text = "ID",padx =2, pady = 6)
        lblNameID.grid(row = 0, column=0, sticky = W)
        txtID = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.product_ID)
        txtID.grid(row = 0, column = 1)

        lblNameProduct = Label(DataframeRight,font = ("arial",12,"bold"),text = "Product Name",padx =2,pady=6)
        lblNameProduct.grid(row = 1, column=0, sticky = W)
        txtName = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.product_name)
        txtName.grid(row = 1, column = 1)

        lblNameType = Label(DataframeRight,font = ("arial",12,"bold"),text = "Type",padx =2,pady=6)
        lblNameType.grid(row = 2, column=0, sticky = W)
        txtType = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.product_type)
        txtType.grid(row = 2, column = 1)

        lblNamePrice = Label(DataframeRight,font = ("arial",12,"bold"),text = "Price",padx =2, pady=6)
        lblNamePrice.grid(row = 3, column=0, sticky = W)
        txtPrice = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.product_price)
        txtPrice.grid(row = 3, column = 1)

        
        #button
        
        btnLabelAdd = LabelFrame(Buttonframe,bd = 2, bg = "black")  #Add info button
        btnLabelAdd.grid(row = 0, column = 0, padx = 5, pady = 2)  
        btnAdd = Button(btnLabelAdd, text = "Add info",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6, command=self.Add_Data)
        btnAdd.grid(row = 0, column= 0, padx=2, pady= 2)
        
        btnLabelUpdate = LabelFrame(Buttonframe,bd = 2, bg = "black")   #Update info button
        btnLabelUpdate.grid(row = 0, column = 1, padx = 5, pady = 2)
        btnUpdate = Button(btnLabelUpdate,text = "Update info",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6,command= self.Update_data)
        btnUpdate.grid(row = 0, column= 1,padx=2, pady= 2)

        btnLabelDelete = LabelFrame(Buttonframe,bd = 2, bg = "black")   #Delete info button
        btnLabelDelete.grid(row = 1, column = 0, padx = 5, pady = 2)
        btnDelete = Button(btnLabelDelete,text = "Delete info",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6, command= self.Delete_data)
        btnDelete.grid(row = 1, column= 0,padx=2, pady= 2)

        btnLabelClear = LabelFrame(Buttonframe,bd = 2, bg = "black")    #Clear input button
        btnLabelClear.grid(row = 1, column = 1, padx = 5, pady = 2)
        btnClear = Button(btnLabelClear,text = "Clear input",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6, command= self.Clear_input)
        btnClear.grid(row = 1, column= 1,padx=2, pady= 2)

        #btnLabelSearch = LabelFrame(Buttonframe,bd = 2, bg = "black" )  #Search button
        #btnLabelSearch.grid(row = 2, column= 0, padx= 5, pady = 2)
        #btnSearch = Button(btnLabelSearch, text="Seach input",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6,command= self.Search_data)
        #btnSearch.grid(row=2, column=0,padx = 2, pady= 2)

        #btnLabelQuit = LabelFrame(Buttonframe,bd = 2, bg = "black")     #Quit Button
        #btnLabelQuit.grid(row = 2, column= 1, padx= 5, pady = 2 )
        #btnQuit = Button(btnLabelQuit,text = "Quit",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6,command= self.Quit_product )
        #btnQuit.grid(row=2,column=1,padx= 5, pady =2)


        
        #Scrollbar
        scroll_X = ttk.Scrollbar(DataframeLeft,orient= HORIZONTAL)
        scroll_Y = ttk.Scrollbar(DataframeLeft,orient= VERTICAL)
        self.Product_table=ttk.Treeview(DataframeLeft, column= ("ID","Product name","Type","Price"),xscrollcommand = scroll_Y.set,yscrollcommand = scroll_X.set)
        scroll_X.pack(side = BOTTOM, fill = X)
        scroll_Y.pack(side = RIGHT, fill = Y)

        scroll_X = ttk.Scrollbar(command= self.Product_table.xview)
        scroll_Y = ttk.Scrollbar(command= self.Product_table.yview)
        
        #Date table
        self.Product_table.heading("ID",text = "ID")
        self.Product_table.heading("Product name",text = "Product Name")
        self.Product_table.heading("Type",text = "Type")
        self.Product_table.heading("Price",text = "Price")

        self.Product_table["show"] = "headings"
        self.Product_table.column("ID", width=100)

        self.Product_table.pack(fill = BOTH, expand = 1)
        self.Product_table.bind("<ButtonRelease-1>",self.use_cursor)
        self.show_data()
        
    #Function
    def show_data(self):
        connect =mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        c.execute("SELECT * FROM product")
        rows = c.fetchall()
        if len(rows) != 0:
            self.Product_table.delete(*self.Product_table.get_children())
            for i in rows:
                self.Product_table.insert("",END,values = i)
            connect.commit()
        connect.close()
        
    def Add_Data(self):
        if self.product_ID.get() == "":
            messagebox.showerror("Error ,All fields must be filled")    
        else:
            connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
            c = connect.cursor()
            insert_query = "INSERT INTO `product`(`product_id`,`product_name`,`product_type`,`product_price`) VALUES (%s,%s,%s,%s)"
            vals = (self.product_ID.get(),self.product_name.get(),self.product_type.get(),self.product_price.get())
            c.execute(insert_query,vals)
                
            connect.commit()
            self.show_data()
            connect.close()
            messagebox.showinfo("success","record has been saved")
    def Update_data(self):
        connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        insert_query = "UPDATE product SET product_name = %s, product_type = %s, product_price = %s WHERE product_id = %s"
        vals = (self.product_name.get(),self.product_type.get(),self.product_price.get(),self.product_ID.get())
        c.execute(insert_query,vals)
        connect.commit()
        self.show_data()
        connect.close()
        messagebox.showinfo("Update","Successfully")

    def Delete_data(self):
        connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        insert_query = "DELETE FROM `product` WHERE `product_id` = %s"
        vals = (self.product_ID.get(),)
        c.execute(insert_query,vals)
        connect.commit()
        connect.close()
        self.show_data()
        messagebox.showinfo("Delete","Data successfully wiped")        

    def use_cursor(self,event = ""):
        cursor_row = self.Product_table.focus()
        contents = self.Product_table.item(cursor_row)
        row = contents["values"]
        self.product_ID.set(row[0])
        self.product_name.set(row[1])
        self.product_type.set(row[2])
        self.product_price.set(row[3])
    def Clear_input(self):
        self.product_ID.set("")
        self.product_name.set("")
        self.product_type.set("")
        self.product_price.set("")
        
    #def Search_data(self):
    #    connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
    #    c = connect.cursor(buffered=True)
    #    insert_query = "SELECT product_id,product_name,product_type,product_price FROM product WHERE product_id = %s"
    #    vals = (self.product_ID.get(),)
    #    c.execute(insert_query,vals)
    #    connect.commit()
    #    connect.close()

    #def Quit_product(self):
    #    messQuite = messagebox.showinfo("Coffee House Information Management System","Do you want to exit? ")
    #    if messQuite>0:
    #        root.destroy()
    #        return
