import mysql.connector

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Style


db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="root",  
    database="shop"
)
cursor = db.cursor()


root = Tk()
root.title("Online Shopping System")
root.geometry("900x700")

style = Style()
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
style.configure("TButton", font=("Helvetica", 10))


current_user = None


def clear_frame():
    """Clear the main frame content."""
    for widget in main_frame.winfo_children():
        widget.destroy()

def admin_dashboard():
    """Admin Dashboard."""
    clear_frame()
    Label(main_frame, text=f"Welcome, Admin {current_user[1]}", font=("Helvetica", 16, "bold")).pack(pady=20)
    Button(main_frame, text="View All Users", command=view_all_users, width=25).pack(pady=10)
    Button(main_frame, text="View All Orders", command=view_all_orders, width=25).pack(pady=10)
    Button(main_frame, text="Add Product", command=add_product_screen, width=25).pack(pady=10)
    Button(main_frame, text="Logout", command=logout, width=25).pack(pady=10)

def view_all_users():
    """View all user data."""
    clear_frame()
    Label(main_frame, text="All Users", font=("Helvetica", 16, "bold")).pack(pady=20)

    tree = Treeview(main_frame, columns=("User ID", "Name", "Address", "Role"), show="headings", height=15)
    tree.heading("User ID", text="User ID")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("Role", text="Role")
    tree.pack(fill=BOTH, expand=True)

    cursor.execute("SELECT user_id, name, address, role FROM users")
    users = cursor.fetchall()
    for user in users:
        tree.insert("", "end", values=user)

    Button(main_frame, text="Back", command=admin_dashboard, width=20).pack(pady=10)

def view_all_orders():
    """Admin screen to view all orders."""
    clear_frame()
    Label(main_frame, text="All Orders", font=("Helvetica", 16, "bold")).pack(pady=20)

    tree = Treeview(main_frame, columns=("Order ID", "User", "Product", "Quantity", "Total Price"), show="headings", height=15)
    tree.heading("Order ID", text="Order ID")
    tree.heading("User", text="User")
    tree.heading("Product", text="Product")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Total Price", text="Total Price")
    tree.pack(fill=BOTH, expand=True)

    cursor.execute("""
        SELECT o.order_id, u.name, p.prod_name, o.quantity, o.total_price
        FROM orders o
        JOIN users u ON o.user_id = u.user_id
        JOIN products p ON o.prod_id = p.prod_id
    """)
    orders = cursor.fetchall()
    for order in orders:
        tree.insert("", "end", values=order)

    Button(main_frame, text="Back", command=admin_dashboard, width=20).pack(pady=20)

def add_product_screen():
    """Admin screen to add new products."""
    clear_frame()
    Label(main_frame, text="Add New Product", font=("Helvetica", 16, "bold")).pack(pady=20)

    Label(main_frame, text="Product Name:", font=("Helvetica", 12)).pack(pady=5)
    prod_name_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    prod_name_entry.pack()

    Label(main_frame, text="Quantity:", font=("Helvetica", 12)).pack(pady=5)
    quantity_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    quantity_entry.pack()

    Label(main_frame, text="Price:", font=("Helvetica", 12)).pack(pady=5)
    price_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    price_entry.pack()

    def add_product():
        name = prod_name_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()

        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            cursor.execute("INSERT INTO products (prod_name, prod_quantity, price) VALUES (%s, %s, %s)",
                           (name, int(quantity), float(price)))
            db.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid inputs!")

    Button(main_frame, text="Add Product", command=add_product, width=20).pack(pady=20)
    Button(main_frame, text="Back", command=admin_dashboard, width=20).pack()

cart = [] 


def user_dashboard():
    """Display the dashboard for users."""
    clear_frame()
    Label(main_frame, text=f"Welcome, {current_user[1]}", font=("Helvetica", 16, "bold")).pack(pady=20)
    Button(main_frame, text="View Products", command=view_products, width=25).pack(pady=10)
    Button(main_frame, text="View Cart", command=view_cart, width=25).pack(pady=10)
    Button(main_frame, text="Checkout", command=checkout, width=25).pack(pady=10)
    Button(main_frame, text="Generate Invoice", command=show_invoice, width=20).pack(pady=10)
    Button(main_frame, text="Logout", command=logout, width=25).pack(pady=10)


def view_products():
    """Display all available products for users."""
    clear_frame()
    Label(main_frame, text="Available Products", font=("Helvetica", 16, "bold")).pack(pady=20)

    tree = Treeview(main_frame, columns=("Product ID", "Name", "Quantity", "Price"), show="headings", height=15)
    tree.heading("Product ID", text="Product ID")
    tree.heading("Name", text="Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.pack(fill=BOTH, expand=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        tree.insert("", "end", values=product)

    Label(main_frame, text="Enter Product ID to Add to Cart:", font=("Helvetica", 12)).pack(pady=10)
    prod_id_entry = Entry(main_frame, font=("Helvetica", 12), width=20)
    prod_id_entry.pack()

    Label(main_frame, text="Enter Quantity:", font=("Helvetica", 12)).pack(pady=5)
    quantity_entry = Entry(main_frame, font=("Helvetica", 12), width=20)
    quantity_entry.pack()

    def add_to_cart():
        prod_id = prod_id_entry.get()
        quantity = quantity_entry.get()

        if prod_id.isdigit() and quantity.isdigit():
            cursor.execute("SELECT * FROM products WHERE prod_id = %s", (prod_id,))
            product = cursor.fetchone()
            if product:
                if int(quantity) <= product[2]:
                    cart.append((product[0], product[1], int(quantity), product[3] * int(quantity)))
                    messagebox.showinfo("Success", f"{product[1]} added to cart!")
                    view_products()
                else:
                    messagebox.showerror("Error", "Quantity exceeds available stock.")
            else:
                messagebox.showerror("Error", "Invalid Product ID.")
        else:
            messagebox.showerror("Error", "Invalid inputs. Enter valid Product ID and Quantity.")

    Button(main_frame, text="Add to Cart", command=add_to_cart, width=20).pack(pady=20)
    Button(main_frame, text="Back", command=user_dashboard, width=20).pack()


def view_cart():
    """View the products in the cart."""
    clear_frame()
    Label(main_frame, text="Your Cart", font=("Helvetica", 16, "bold")).pack(pady=20)

    tree = Treeview(main_frame, columns=("Product ID", "Name", "Quantity", "Total Price"), show="headings", height=15)
    tree.heading("Product ID", text="Product ID")
    tree.heading("Name", text="Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Total Price", text="Total Price")
    tree.pack(fill=BOTH, expand=True)

    for item in cart:
        tree.insert("", "end", values=item)

    Button(main_frame, text="Back", command=user_dashboard, width=20).pack(pady=20)


def checkout():
    """Process the checkout and place the order."""
    global cart

    if not cart:
        messagebox.showwarning("Warning", "Your cart is empty!")
        return

    try:
        for item in cart:
            prod_id, _, quantity, total_price = item

            # Check stock availability
            cursor.execute("SELECT prod_quantity FROM products WHERE prod_id = %s", (prod_id,))
            stock = cursor.fetchone()[0]
            if quantity > stock:
                messagebox.showerror("Error", f"Not enough stock for product ID {prod_id}.")
                return

            # Deduct stock
            cursor.execute("UPDATE products SET prod_quantity = prod_quantity - %s WHERE prod_id = %s", (quantity, prod_id))
            db.commit()

            # Insert into orders
            cursor.execute(
                "INSERT INTO orders (user_id, prod_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                (current_user[0], prod_id, quantity, total_price))
            db.commit()

        cart = []  # Clear the cart after successful checkout
        messagebox.showinfo("Success", "Order placed successfully!")
        user_dashboard()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def show_invoice():
    """Generate and display the user's invoice."""
    clear_frame()
    Label(main_frame, text="Your Invoice", font=("Helvetica", 16, "bold")).pack(pady=20)

    tree = Treeview(main_frame, columns=("Order ID", "Product", "Quantity", "Total Price"), show="headings", height=15)
    tree.heading("Order ID", text="Order ID")
    tree.heading("Product", text="Product")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Total Price", text="Total Price")
    tree.pack(fill=BOTH, expand=True)

    cursor.execute("""
        SELECT o.order_id, p.prod_name, o.quantity, o.total_price
        FROM orders o
        JOIN products p ON o.prod_id = p.prod_id
        WHERE o.user_id = %s
    """, (current_user[0],))
    orders = cursor.fetchall()
    for order in orders:
        tree.insert("", "end", values=order)

    Button(main_frame, text="Back", command=user_dashboard, width=20).pack(pady=20)
    
def show_register():
    """Display the registration screen."""
    clear_frame()
    Label(main_frame, text="Register New Account", font=("Helvetica", 16, "bold")).pack(pady=20)

    Label(main_frame, text="Name:", font=("Helvetica", 12)).pack(pady=5)
    name_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    name_entry.pack()

    Label(main_frame, text="Address:", font=("Helvetica", 12)).pack(pady=5)
    address_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    address_entry.pack()

    Label(main_frame, text="Password:", font=("Helvetica", 12)).pack(pady=5)
    password_entry = Entry(main_frame, font=("Helvetica", 12), width=30, show="*")
    password_entry.pack()

    def register_user():
        name = name_entry.get()
        address = address_entry.get()
        password = password_entry.get()
        if name and address and password:
            try:
                cursor.execute("INSERT INTO users (name, address, password, role) VALUES (%s, %s, %s, 'user')",
                               (name, address, password))
                db.commit()
                messagebox.showinfo("Success", "Registration successful!")
                show_home()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database error: {e}")
        else:
            messagebox.showerror("Error", "All fields are required!")

    Button(main_frame, text="Register", command=register_user, width=20).pack(pady=20)
    Button(main_frame, text="Back", command=show_home, width=20).pack()

def show_home():
    """Display the home screen."""
    clear_frame()  # Clear the main frame before displaying the home screen

    # Welcome Label
    Label(main_frame, text="Welcome to the Online Shopping System", font=("Helvetica", 16, "bold")).pack(pady=20)

    # Buttons for navigation
    Button(main_frame, text="Admin Login", command=show_admin_login, width=25).pack(pady=10)
    Button(main_frame, text="Register", command=show_register, width=20).pack(pady=10)
    Button(main_frame, text="User Login", command=show_user_login, width=25).pack(pady=10)
    Button(main_frame, text="Exit", command=root.quit, width=25).pack(pady=10)

def show_user_login():
    """Display the user login screen."""
    clear_frame()

    # Login Screen
    Label(main_frame, text="User Login", font=("Helvetica", 16, "bold")).pack(pady=20)

    # Login form
    Label(main_frame, text="Name:", font=("Helvetica", 12)).pack(pady=5)
    name_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    name_entry.pack()

    Label(main_frame, text="Password:", font=("Helvetica", 12)).pack(pady=5)
    password_entry = Entry(main_frame, font=("Helvetica", 12), width=30, show="*")
    password_entry.pack()

    def login_user():
        """Log in the user and redirect to the dashboard."""
        global current_user
        name = name_entry.get()
        password = password_entry.get()

        if not name or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (name, password))
        user = cursor.fetchone()

        if user:
            current_user = user  # Save current user details
            messagebox.showinfo("Success", f"Welcomes, {user[1]}!")
            user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    # Login Button
    Button(main_frame, text="Login", command=login_user, width=20).pack(pady=20)

    # Back Button
    Button(main_frame, text="Back", command=show_home, width=20).pack()
 
# Authentication Functions
def logout():
    """Log out the current user."""
    global current_user
    current_user = None
    messagebox.showinfo("Success", "Logged out successfully!")
    show_home()

def show_admin_login():
    """Display the admin login screen."""
    clear_frame()  # Clear the main frame

    # Title
    Label(main_frame, text="Admin Login", font=("Helvetica", 16, "bold")).pack(pady=20)

    # Login form
    Label(main_frame, text="Admin Name:", font=("Helvetica", 12)).pack(pady=5)
    admin_name_entry = Entry(main_frame, font=("Helvetica", 12), width=30)
    admin_name_entry.pack()

    Label(main_frame, text="Password:", font=("Helvetica", 12)).pack(pady=5)
    admin_password_entry = Entry(main_frame, font=("Helvetica", 12), width=30, show="*")
    admin_password_entry.pack()

    def login_admin():
        """Validate admin credentials and show the admin dashboard."""
        admin_name = admin_name_entry.get()
        admin_password = admin_password_entry.get()

        # Query to verify admin credentials
        cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s AND role = 'admin'",
                       (admin_name, admin_password))
        admin = cursor.fetchone()

        if admin:
            global current_user
            current_user = admin  # Set current user as admin
            messagebox.showinfo("Success", f"Welcome, Admin {admin_name}!")
            show_admin_dashboard()  # Redirect to the admin dashboard
        else:
            messagebox.showerror("Error", "Invalid admin credentials!")

    # Buttons
    Button(main_frame, text="Login", command=login_admin, width=20).pack(pady=20)
    Button(main_frame, text="Back", command=show_home, width=20).pack()


def show_admin_dashboard():
    """Display the admin dashboard."""
    clear_frame()

   
    Label(main_frame, text=f"Welcome, Admin {current_user[1]}", font=("Helvetica", 16, "bold")).pack(pady=20)

  
    Button(main_frame, text="Add New Product", command=add_product_screen, width=25).pack(pady=10)
    Button(main_frame, text="View All Users", command=view_all_users, width=25).pack(pady=10)
    Button(main_frame, text="View Order History", command=view_all_orders, width=25).pack(pady=10)
    Button(main_frame, text="Logout", command=admin_logout, width=25).pack(pady=10)

def admin_logout():
    """Log out the admin."""
    global current_user
    current_user = None
    messagebox.showinfo("Success", "Logged out successfully!")
    show_home()

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)


show_home()

root.mainloop()
