from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


class EmployeeTable:
    def __init__(self,root):
        self.root = root
        self.root.title("Coffee House management system")
        self.root.geometry("1540x800+0+0")
        self.root.configure(bg = 'saddle brown')
        self.coffee_image = Image.open("d:/Python/Project/coffe_banner.jpg") #import image
        self.resized = self.coffee_image.resize((1000,260),Image.ANTIALIAS) #resized image
        self.new_coffee_img = ImageTk.PhotoImage(self.resized) #new resized image
        self.employee_ID = StringVar()        #  
        self.employee_name = StringVar()      #  
        self.employee_DOB = StringVar()       # Variables
        self.employee_position = StringVar()  #
        self.employee_phone_number = StringVar()
        lbltitle = Label(self.root,relief=FLAT, bd = 20,text = "Employee Information Management System",fg = "white", bg= "saddle brown",font=("Arial",50))
        lbltitle.pack(side=TOP, fill = X)

        #Dataframe
        Dataframe = Frame(self.root,bd = 10,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530, height = 400)

        DataframeLeft = LabelFrame(Dataframe,bd =5,relief= RIDGE,padx=10,font=("Arial",12,"bold"),text="Employee information")
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
        txtID = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.employee_ID)
        txtID.grid(row = 0, column = 1)

        lblNameEmployee = Label(DataframeRight,font = ("arial",12,"bold"),text = "Employee Name",padx =2,pady=6)
        lblNameEmployee.grid(row = 1, column=0, sticky = W)
        txtName = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.employee_name)
        txtName.grid(row = 1, column = 1)

        lblNameDOB = Label(DataframeRight,font = ("arial",12,"bold"),text = "Date of Birth",padx =2,pady=6)
        lblNameDOB.grid(row = 2, column=0, sticky = W)
        txtDOB = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.employee_DOB)
        txtDOB.grid(row = 2, column = 1)

        lblNamePosition = Label(DataframeRight,font = ("arial",12,"bold"),text = "Position",padx =2, pady=6)
        lblNamePosition.grid(row = 3, column=0, sticky = W)
        txtPosition = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.employee_position)
        txtPosition.grid(row = 3, column = 1)

        lblNumbPhone = Label(DataframeRight,font = ("arial",12,"bold"),text = "Phone number",padx =2, pady = 6)
        lblNumbPhone.grid(row = 4, column=0, sticky = W)
        txtNumbPhone = Entry(DataframeRight,font = ("arial",12,"bold"),width = 30,textvariable=self.employee_phone_number)
        txtNumbPhone.grid(row = 4, column = 1)

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

        btnLabelQuit = LabelFrame(Buttonframe,bd = 2, bg = "black")     #Quit Button
        btnLabelQuit.grid(row = 2, column= 0, padx= 5, pady = 2 )
        btnQuit = Button(btnLabelQuit,text = "Quit",bg = "saddle brown",fg = "white",font = ("arial", 12,"bold"),width = 15,padx = 10,pady = 6,command= root.destroy)
        btnQuit.grid(row=2,column=0,padx= 2, pady =2)


        
        #Scrollbar
        scroll_X = ttk.Scrollbar(DataframeLeft,orient= HORIZONTAL)
        scroll_Y = ttk.Scrollbar(DataframeLeft,orient= VERTICAL)
        self.Employee_table=ttk.Treeview(DataframeLeft, column= ("ID","Name","Date of Birth","Position","Phone number"),xscrollcommand = scroll_Y.set,yscrollcommand = scroll_X.set)
        scroll_X.pack(side = BOTTOM, fill = X)
        scroll_Y.pack(side = RIGHT, fill = Y)

        scroll_X = ttk.Scrollbar(command= self.Employee_table.xview)
        scroll_Y = ttk.Scrollbar(command= self.Employee_table.yview)
        
        #Date table
        self.Employee_table.heading("ID",text = "ID")
        self.Employee_table.heading("Name",text = "Name")
        self.Employee_table.heading("Date of Birth",text = "Date of Birth")
        self.Employee_table.heading("Position",text = "Position")
        self.Employee_table.heading("Phone number",text = "Phone number")

        self.Employee_table["show"] = "headings"
        self.Employee_table.column("ID", width=100)

        self.Employee_table.pack(fill = BOTH, expand = 1)
        self.Employee_table.bind("<ButtonRelease-1>",self.use_cursor)
        self.show_data()
        
    #Function
    def show_data(self):
        connect =mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        c.execute("SELECT * FROM employee")
        rows = c.fetchall()
        if len(rows) != 0:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for i in rows:
                self.Employee_table.insert("",END,values = i)
            connect.commit()
        connect.close()
        
    def Add_Data(self):
        if self.employee_ID.get() == "":
            messagebox.showerror("Error ,All fields must be filled")    
        else:
            connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
            c = connect.cursor()
            insert_query = "INSERT INTO `employee`(`employee_id`,`employee_name`,`employee_dob`,`employee_position`,`employee_phone_number`) VALUES (%s,%s,%s,%s,%s)"
            vals = (self.employee_ID.get(),self.employee_name.get(),self.employee_DOB.get(),self.employee_position.get(),self.employee_phone_number.get())
            c.execute(insert_query,vals)
                
            connect.commit()
            self.show_data()
            connect.close()
            messagebox.showinfo("success","record has been saved")
    def Update_data(self):
        connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        insert_query = "UPDATE employee SET employee_name = %s, employee_dob = %s, employee_position = %s, employee_phone_number = %s WHERE employee_id = %s"
        vals = (self.employee_name.get(),self.employee_DOB.get(),self.employee_position.get(),self.employee_phone_number.get(),self.employee_ID.get())
        c.execute(insert_query,vals)
        connect.commit()
        self.show_data()
        connect.close()
        messagebox.showinfo("Update","Update Successfully")

    def Delete_data(self):
        connect = mysql.connector.connect(host = "127.0.0.1", username= "root", password = "123456789", database= "mydata")
        c = connect.cursor()
        insert_query = "DELETE FROM `employee` WHERE `employee_id` = %s"
        vals = (self.employee_ID.get(),)
        c.execute(insert_query,vals)
        connect.commit()
        connect.close()
        self.show_data()
        messagebox.showinfo("Delete","Data successfully wiped")        

    def use_cursor(self,event = ""):
        cursor_row = self.Employee_table.focus()
        contents = self.Employee_table.item(cursor_row)
        row = contents["values"]
        self.employee_ID.set(row[0])
        self.employee_name.set(row[1])
        self.employee_DOB.set(row[2])
        self.employee_position.set(row[3])
        self.employee_phone_number.set(row[4])
    def Clear_input(self):
        self.employee_ID.set("")
        self.employee_name.set("")
        self.employee_DOB.set("")
        self.employee_position.set("")
        self.employee_phone_number.set("")
    



