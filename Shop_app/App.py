import mysql.connector
from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter.ttk import Treeview,Style

Conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Shop_appDB"
)

Cur = Conn.cursor()

Root = Tk()
Main_frame = Frame(Root)
Main_frame.pack(fill=BOTH, expand=True)
Root.title( " Online Shopping app " )
Root.geometry( "1200x600" )
Main_frame.configure( bg="#060201" )

Style = Style()
Style.configure( "TreeView.Heading", font = ( "Helvetica", 20, "bold"  ) )
Style.configure( " TreView", font = ( "Helvetica", 20 ), rowheight = 25 )
Style.configure( "Button", font = ("Helvetica", 20) )

Current_user = None

def Home():
    Label(Root, text = "Welcome to Online Shopping System", font = ("Helvetica 28"), bg = "#060201", fg = "yellow").place(x = 230, y = 20)
    
    Button(Root, text = "Admin Login", font = ( "Arial", 20 ), height = 5, width = 25, command = Admin_login, bg="#060201", fg="#fff").place(x = 86, y = 100)
    Button(Root, text = "Register", font = ( "Arial", 20 ), height = 5, width = 25, bg="#060201", fg="#fff", command = Register_user).place(x = 600, y = 100)
    Button(Root, text = "User Login", font = ( "Helvetica", 20 ), height = 5, width = 25, bg="#060201", fg="#fff", command = Login_user).place(x = 90,y = 300)
    Button(Root, text = "Exit", command = Root.destroy, font = ( "Helvetica", 20 ), height = 5, width = 25, bg="#060201", fg="#fff").place(x = 600, y = 300)

def Admin_login():
    Base = Tk()
    Base.geometry( "1500x900" )
    Base.configure( bg="#060201" )
    
    Label(Base, text = "Admin Login", font = ("Helvetica", 28, "bold"), bg = "#060201", fg="#F1AD12" ).place(x = 86, y = 20)

    Label(Base, text = "Name", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 100)
    NameValue = StringVar()
    NameEntry = Entry(Base, textvariable = NameValue, text = "", font = ("Helvetica", 20), width = 45 )
    NameEntry.place(x = 400, y = 100)

    Label(Base, text = "Username", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 200)
    UsernameValue = StringVar()
    UsernameEntry = Entry(Base, textvariable = UsernameValue ,text = "", font = ("Helvetica", 20), width = 45)
    UsernameEntry.place(x = 400, y = 200)
    
    Label(Base, text = "Email", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 300)            
    EmailValue = StringVar()
    EmailEntry = Entry(Base, textvariable = EmailValue ,text = "", font = ("Helvetica", 20), width = 45 )
    EmailEntry.place(x = 400, y = 300)
    
    Label(Base, text = "Password", font = ("Helvetica", 20), bg="#060201", fg="#fff" ).place(x = 86, y = 400)
    PasswordValue = StringVar()
    PasswordEntry = Entry(Base, textvariable = PasswordValue, text = "", font = ("Helvetica", 20), width = 45, show = "*")
    PasswordEntry.place(x = 400, y = 400)

    def Admin_login():
        Name = NameEntry.get()
        Usernamme = UsernameEntry.get()
        Email = EmailEntry.get()
        Password = PasswordEntry.get()
        
        if Name == "" or Usernamme == "" or Email == "" or Password == "":
            Messagebox.showerror("ALERT", "Please enter all fields")
        else:
            try:
                Cur.execute( "SELECT * FROM Admin_login WHERE Admin_name=%s AND Admin_username=%s AND Admin_email=%s AND Admin_password=%s",(Name,Usernamme,Email,Password) )
                Admin = Cur.fetchone()
                
                Messagebox.showinfo("Status","Data saved.")
                
                if Admin:
                    Current_user = Admin
                    Messagebox.showinfo("Success", f"Welcome, Admin {Admin}!")
                    Admin_Dashboard()
                else:
                    Messagebox.showerror("!Error","Invalid user or password entered.")
            except Exception as Err:
                Messagebox.showerror("ALERT", Err)

    Button(Base, text = "Login", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 65, command = Admin_login).place(x = 86, y = 500)
    Button(Base, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 65, command = Home).place(x = 86, y = 600)
        
    Base.mainloop()

def Register_user():
    Base = Tk()
    Base.geometry( "1500x850" )
    Base.configure( bg="#060201" )

    Label(Base, text = "User Register", font = ("Helvetica", 28, "bold"), bg = "#060201", fg="#F1AD12" ).place(x = 86, y = 20)
    
    Label(Base, text = "First-name:", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 100)
    First_nameValue = StringVar()
    First_nameEntry = Entry(Base, textvariable = First_nameValue, text = "", font = ("Helvetica", 20), width = 45 )
    First_nameEntry.place(x = 400, y = 100)

    Label(Base, text = "Last-name:", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 200)
    LastnameValue = StringVar()
    LastnameEntry = Entry(Base, textvariable = LastnameValue, text = "", font = ("Helvetica", 20), width = 45 )
    LastnameEntry.place(x = 400, y = 200)
    
    Label(Base, text = "User-name:", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 300)
    UsernameValue = StringVar()
    UsernameEntry = Entry(Base, textvariable = UsernameValue, text = "", font = ("Helvetica", 20), width = 45 )
    UsernameEntry.place(x = 400, y = 300)
    
    Label(Base, text = "Email:", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 400)        
    EmailValue = StringVar()
    EmailEntry = Entry(Base, textvariable = EmailValue, text = "", font = ("Helvetica", 20), width = 45 )
    EmailEntry.place(x = 400, y = 400)
    
    Label(Base, text = "Password:", font = ("Helvetica", 20), bg="#060201", fg="#fff" ).place(x = 86, y = 500)
    PasswordValue = StringVar()
    PasswordEntry = Entry(Base, textvariable = PasswordValue, text = "", font = ("Helvetica", 20), width = 45, show = "*")
    PasswordEntry.place(x = 400, y = 500)
    
    Label(Base, text = "Confirm-password:", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 600)    
    Confirm_passwordValue = StringVar()
    Confirm_passwordEntry = Entry(Base, textvariable = Confirm_passwordValue, text = "", font = ("Helvetica", 20), width = 45, show = "*")
    Confirm_passwordEntry.place(x = 400, y = 600)
    
    def Register():
        First_name = First_nameEntry.get()
        Lastname = LastnameEntry.get()
        Username = UsernameEntry.get()
        Email = EmailEntry.get()
        Password = PasswordEntry.get()
        Confirm_password = Confirm_passwordEntry.get()
        
        if(First_name == "" or Lastname == "" or Username == "" or Email == "" or Password == "" or Confirm_password == ""):
            Messagebox.showerror("ALERT", "Please enter all fields")
        else:
            try:
                Q = "INSERT INTO User_credential VALUES('"+First_name+"','"+Lastname+"','"+Username+"','"+Email+"','"+Password+"','"+Confirm_password+"')"

                Cur.execute(Q)

                Conn.commit()

                Messagebox.showinfo("Status","Data saved.")
            except Exception as Err:
                Messagebox.showerror("!ALERT", Err)
    
    Button(Base, text = "Submit", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 10, command = Register ).place(x = 86, y = 700)
    Button(Base, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 10, command = Home ).place(x = 400, y = 700)
    
    Base.mainloop()

def Login_user():
    Base = Tk()
    Base.geometry( "1200x600" )
    Base.configure( bg="#060201" )
    
    Label(Base, text = "Admin Login", font = ("Helvetica", 28, "bold"), bg = "#060201", fg="#F1AD12" ).place(x = 86, y = 20)
    Label(Base, text = "Email", font = ("Helvetica", 20, "bold"), bg="#060201", fg="#fff" ).place(x = 86, y = 100)
    Label(Base, text = "Password", font = ("Helvetica", 20), bg="#060201", fg="#fff" ).place(x = 86, y = 200)
    
    EmailValue = StringVar()
    EmailEntry = Entry(Base, textvariable = EmailValue,text = "", font = ("Helvetica", 20), width = 45 )
    EmailEntry.place(x = 400, y = 100)
    PasswordValue = StringVar()
    PasswordEntry = Entry(Base, textvariable = PasswordValue,text = "", font = ("Helvetica", 20), width = 45)
    PasswordEntry.place(x = 400, y = 200)

    def Login():
        Email = EmailEntry.get()
        Password = PasswordEntry.get()
        
        if Email == "" or Password == "":
            Messagebox.showerror("ALERT", "Please enter all fields")
        else:
            try:
                Cur.execute( "SELECT * FROM User_credential WHERE User_email=%s AND User_password=%s",(Email,Password) )
                User = Cur.fetchone()
                
                if User:
                    Current_user = User
                    Messagebox.showinfo("Status",f"Welcome { Current_user[1] }")
                    Dashboard()
                else:
                    Messagebox.showerror("!Error","Invalid user or password entered.")

                Messagebox.showinfo("Status","Data saved.")
            except Exception as Err:
                Messagebox.showerror("ALERT", Err)

    Button(Base, text = "Login", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Login ).place(x = 86, y = 300)
    Button(Base, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Home ).place(x = 86, y = 400)
        
    Base.mainloop()

def Admin_Dashboard():
    R = Tk()
    R.geometry( "950x599" )
    R.configure( bg="#060201" )

    Label(R, text = f"Welcome {Current_user[1]}", font = ("Helvetica 28"), bg = "#060201", fg = "yellow").place(x = 86, y = 20)
    Button(R, text = "Add New Product", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 45, command = Add_product).place(x = 86, y = 100)
    Button(R, text = "View all Users", font = ("Helvetica",20), bg = "#060201", fg = "#fff", width = 45, command = View_user).place(x = 86, y = 200)
    Button(R, text = "View all Order History", font = ("Helvetica",20), bg = "#060201", fg = "#fff", width = 45, command = View_order).place(x = 86, y = 300)
    Button(R, text = "Logout", font = ("Helvetica",20), bg = "#060201", fg = "#fff", width = 45, command = Dashboard).place(x = 86, y = 400)
    
    R.mainloop()

def Dashboard():
    R = Tk()
    R.geometry( "950x599" )
    R.configure( bg="#060201" )

    Label(R, text = f"Welcome, {Current_user[1]}", font = ("Helvetica 28"), bg = "#060201", fg = "yellow").place(x = 86, y = 20)
    
    Button(R, text = "View product", font = ( "Arial 20" ), width = 45, bg="#060201", fg="#fff", command = View_product).place(x = 86, y = 100)
    Button(R, text = "View cart", font = ( "Arial 20" ), width = 45, bg="#060201", fg="#fff", command = View_cart).place(x = 86, y = 200)
    Button(R, text = "Generate Invoice", font = ( "Arial 20" ), width = 45, bg="#060201", fg="#fff", command = Generate_invoice).place(x = 86, y = 300)
    Button(R, text = "Checkout", font = ( "Helvetica 20" ), width =  45, bg="#060201", fg="#fff", command = Checkout_product).place(x = 86,y = 400)
    Button(R, text = "Logout", font = ( "Helvetica 20" ), width =  45, bg="#060201", fg="#fff", command = Logout_user).place(x = 86, y = 500)    
    
    R.mainloop()

def Add_product():
    B = Tk()
    B.geometry( "1000x850" )
    B.configure( bg="#060201" )

    Label(B, text = "Avaliable Prodcut", font = ("Helvetica 28"), bg="#060201", fg = "yellow").place(x = 86, y = 20)

    Label(B, text = "Prouduct Name", font = ("Helvetica 28"), bg="#060201", fg="yellow").place(x = 86, y = 100)
    NameValue = StringVar()
    NameEntry = Entry(B, textvariable= NameValue, text = "", bg="#060201", fg="#fff")
    NameEntry.place(x = 400, y = 100)

    Label(B, text = "Quantity", font = ("Helvetica 28"), bg="#060201", fg="#fff").place(x = 86, y = 200)
    QuantityValue = StringVar()
    QuantityEntry = Entry(B, textvariable = QuantityValue, text = "", bg="#060201", fg="#fff")
    QuantityEntry.place(x = 400, y = 200)

    Label(B, text = "Price", font = ("Helvetica 28"), bg="#060201", fg="#fff").place(x = 86, y = 300)
    PriceValue = StringVar()
    PriceEntry = Entry(B, textvariable = PriceValue, text = "", bg="#060201", fg="#fff")
    PriceEntry.place(x = 400, y = 300)

    def Add_product():
        Name = NameEntry.get()
        Quantity = QuantityEntry.get()
        Price = PriceEntry.get()

        if Name == "" and Quantity.isdigit == "" and Price.replace('.','',1).isdigit == "":
            Cur.execute( "INSERT INTO Product_detail(Prod_name,Prod_quantity,Prod_price) VALUES(%s,%s,%s)",(Name,int(Quantity),float(Price)) )
            Conn.commit()
            Admin_Dashboard()
            Messagebox.showinfo("Success", "Product added successfully!")
        else:
            Messagebox.showinfo("ALERT", "Please enter all fields")
    
    Button(B, text = "Submit", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Add_product ).place(x = 86, y = 400)
    Button(B, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Dashboard ).place(x = 86, y = 500)

    B.mainloop()

def View_user():
    Frame = Tk()
    Frame.geometry("1200x500")
    Frame.configure("#060201")

    Label(Frame, text="User History", font = ("Helvetica",20), bg = "#060201", fg = "yellow").place(x = 86, y = 20)

    Tree = Treeview( columns=("User_name","User_lasname","User_username","User_email","User_password","User_confirmpassword"), show = "headings", height = 15 )
    Tree.heading("User_name", text="User_name")
    Tree.heading("User_lastname", text="User_lastname")
    Tree.heading("Tree_username", text="Tree_username")
    Tree.heading("User_email", text="User_email")
    Tree.heading("Tree_password", text="Tree_password")
    Tree.heading("Tree_confirmpassword", text="Tree_confirmpassword")
    Tree.pack(fill=BOTH, expand=True)

    Cur.execute( "SELECT User_name, User_lastname, User_username, User_email, User_email, User_password, User_confirmpassword FROM User_credential" )
    User = Cur.fetchall()

    for U in User:
        Tree.insert("","end",values = User)

    Button(Frame, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Admin_Dashboard ).place(x = 86, y = 100)

    Frame.mainloop()

def View_order():
    Label(Frame, text="User History", font = ("Helvetica",20), bg = "#060201", fg = "yellow").place(x = 86, y = 20)

    Tree = Treeview( column = ("Order_id","User_id","Prod_id","Quantity","Total_price"), show = "headings", height = 15 )
    Tree.heading("Order_id", text="Order_id")
    Tree.heading("User_id", text="User_id")
    Tree.heading("Prod_id", text="Prod_id")
    Tree.heading("Quantity", text="Quantity")
    Tree.heading("Total_price", text="Total_price")

    Cur.execute("""SELECT O.Order_id, U.User_name, P.Prod_name, O.Quantity, O.Total_price
    FROM Order_detail O
    JOIN User_credential U ON O.User_id = U.User_id 
    JOIN Product P ON O.Prod_id = P.Prod_id""")
    Order = Cur.fetchall()
    for Ord in Order:
        Tree.insert("", "end", values = Ord)

    Button(Frame, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Admin_Dashboard ).place(x = 86, y = 100)

Cart = []

def View_product():
    Page_frame = Tk()
    Page_frame.geometry( "1000x850" )
    Page_frame.configure( bg="#060201" )

    Tree = Treeview( columns=("Prod_id","Prod_name","Prod_quantity","Prod_price"), show="headings", height=15 )
    Tree.heading("Pod_id", text="Prod_id")
    Tree.heading("Prod_name", text="Prod_name")
    Tree.heading("Prod_quantity", text="Prod_quantity")
    Tree.heading("Prod_price", text="Prod_price")
    Tree.pack(fill=BOTH, expand=True)

    Label(Page_frame, text = "Product Details", font = ("Helvetica 28"), bg="#060201", fg = "yellow").place(x = 86, y = 20)

    Cur.execute( "SELECT * FROM Product" )
    Products = Cur.fetchall()
    for Product in Products:
        Tree.insert("", "end", values = Product)

    Label(Page_frame, text = "Prouduct ID", font = ("Helvetica 28"), bg="#060201", fg="yellow").place(x = 86, y = 100)
    NameValue = StringVar()
    IDEntry = Entry(Page_frame, textvariable= NameValue, text = "", bg="#060201", fg="#fff")
    IDEntry.place(x = 400, y = 100)

    Label(Page_frame, text = "Product Quantity", font = ("Helvetica 28"), bg="#060201", fg="#fff").place(x = 86, y = 200)
    QuantityValue = StringVar()
    QuantityEntry = Entry(Page_frame, textvariable = QuantityValue, text = "", bg="#060201", fg="#fff")
    QuantityEntry.place(x = 400, y = 200)

    def Addprod_cart():
        ID = IDEntry.get()
        Quantity = QuantityEntry.get()

        if ID.isdigit() and Products.isdigit():
            Cur.execute( "SELECT * FROM Product WHERE Prod_id=%s AND Prod_quantity=%s",(ID,Quantity) )
            Cur.fetchone()
            if Product:
                Cart.append( ( Product[0], Product[1], int(Quantity), Product[3] * int(Quantity) ) )
                Messagebox.showinfo("Success", f"{Product[1]} added to cart!")            
                View_prodcut()
            else:
                Messagebox.showerror("Error", "Quantity exceeds available stock.")
        else:
            Messagebox.showinfo("Alert","Enter valid data.")    

    Button(Page_frame, text = "Submit", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Addprod_cart ).place(x = 86, y = 400)
    Button(Page_frame, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Dashboard ).place(x = 86, y = 500)

    Page_frame.mainloop()

def View_cart():
    Frame = Tk()
    Frame.geometry( "1000x850" )
    Frame.configure( bg="#060201" )

    Tree = Treeview( columns=("Prod_id","Prod_name","Prod_quantity","Prod_price"), show="headings", height=15 )
    Tree.heading("Pod_id", text="Prod_id")
    Tree.heading("Prod_name", text="Prod_name")
    Tree.heading("Prod_quantity", text="Prod_quantity")
    Tree.heading("Prod_price", text="Prod_price")
    Tree.pack(fill=BOTH, expand=True)
    
    for Item in Cart:
        Tree.insert("","end", values=Item)

    Button(Frame, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Dashboard ).place(x = 86, y = 100)

    Frame.mainloop()

def Generate_invoice():
    F = Tk()
    F.geometry( "1000x850" )
    F.configure( bg="#060201" )

    Tree = Treeview( columns = ("Order_id,Usr_id,Prod_id,Quantity,Total_price"), show="headings", height=15 )
    Tree.heading("Order_id", text="Order_id")
    Tree.heading("User_id",text="User_id")
    Tree.heading("Prod_id", text="Prod_id")
    Tree.heading("Quantity", text="Quantity")
    Tree.heading("Total_price", text="Total_price")

    Cur.execute("""
        SELECT O.Order_id, P.Prod_name, O.Quantity, O.Total_price
        FROM Order_detail O
        JOIN Product P ON O.Prod_id = P.Prod_id
        WHERE O.User_id = %s
    """, ( Current_user[0] ) )
    Order = Cur.fetchall()
    for Ord in Order:
        Tree.insert("","end",values=Ord)

    Button(Frame, text = "Back", font = ("Helvetica", 20), bg="#060201", fg="#fff", width = 55, command = Dashboard ).place(x = 86, y = 500)
        
    F.mainloop()

def Checkout_product():
    B = Tk()
    B.geometry( "1500x850" )
    B.configure( bg="#060201" )

    global Cart
    
    if not Cart:
        Messagebox.showwarning("Warning", "Your cart is empty!")
        return
    
    try:
        for Item in Cart:
            Prod_id, Prod_quantity, Total_price = Item
            
            Cur.execute( "SELECT Prod_id,Prod_name,Prod_price FROM Product WHERE Prod_id=%s",(Prod_id) )
            Stock = Cur.fetchone()
            if Prod_quantity > Stock:
                Messagebox.showerror("Error", f"Not enough stock for product ID {Prod_id}.")
                return

            Cur.execute( "UPDATE Product SET Prod_quantity = Prod_quantity - % WHERE Product_id=%s",(Prod_quantity,Prod_id) )
            Conn.commit()

            Cur.execute( "INSERT INTO Order_detail(User_id,Prod_id,Quantity,Total_price) VALUES(%s,%s,%s,%s,%s)",(Current_user[ 0 ], Prod_id, Prod_quantity, Total_price) )
            Conn.commit()
            Dashboard()
    except Exception as Err:
        Messagebox.showwarning("!ALERT",Err)
        
    B.mainloop()

def Logout_user():
    global Current_user
    
    Current_user = None
    
    Messagebox.showinfo("Status", F"{Current_user[1]} Logged out successfully!")
    Home()

Home()

Root.mainloop()