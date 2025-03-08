import _sqlite3
import re

conn = _sqlite3.connect('pudocodedb.db')
cursor = conn.cursor()

# Create a table for vehicles
cursor.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     make TEXT NOT NULL,
     model TEXT NOT NULL,
     vin TEXT NOT NULL UNIQUE,
     seller_name TEXT,
     price_paid REAL,
     sales_price REAL NOT NULL,
     description TEXT
)
''')
conn.commit()

def is_valid_make(make):
     return make.isalpha()

def is_valid_model(model):
     return bool(re.match("^[A-Za-z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$", model))

def show_vehicles():
     cursor.execute("SELECT * FROM vehicles")
     vehicles = cursor.fetchall()
     if vehicles:
             for vehicle in vehicles:
                     print(f"ID: {vehicle[0]}, \n Make: {vehicle[1]}, \n Model: {vehicle[2]}, \n VIN: {vehicle[3]}, "
                                 f"\n Seller: {vehicle[4]},\n Price Paid: {vehicle[5]},\n Sales Price: {vehicle[6]}, "
                                 f"\n Description: {vehicle[7]}")
     else:
             print("No vehicles found.")

def add_vehicle():
     make = input("Enter Vehicle Make: ")
     if not is_valid_make(make):
             print("Invalid Vehicle Make. It must contain letters only.")
             return

     model = input("Enter Vehicle Model: ")
     if not is_valid_model(model):
             print("Invalid Vehicle Model. It can contain letters, numbers, and some special characters, "
                         "but cannot contain ! \" @ # $")
             return

     vin = input("Enter Vehicle Identification Number (VIN): ")
     seller_name = input("Enter Seller Name (optional): ")
     price_paid = input("Enter Price Paid (optional, leave blank if not applicable): ")
     sales_price = input("Enter Sales Price: ")
     description = input("Enter Vehicle Description: ")

     price_paid = float(price_paid) if price_paid else None
     sales_price = float(sales_price)

     try:
             cursor.execute("INSERT INTO vehicles (make, model, vin, seller_name, price_paid, sales_price, description) "
                                           "VALUES (?, ?, ?, ?, ?, ?, ?)",
                                           (make, model, vin, seller_name, price_paid, sales_price, description))
             conn.commit()
             print("Vehicle added successfully.")
     except _sqlite3.IntegrityError:
             print("Error: VIN must be unique.")

def edit_vehicle():
     vehicle_id = input("Enter the ID of the vehicle to edit: ")
     cursor.execute("SELECT * FROM vehicles WHERE id = ?", (vehicle_id,))
     vehicle = cursor.fetchone()

     if vehicle:
             print(f"Editing Vehicle: {vehicle}")
             make = input("Enter new Vehicle Make (leave blank to keep current): ") or vehicle[1]
             if not is_valid_make(make):
                     print("Invalid Vehicle Make. It must contain letters only.")
                     return

             model = input("Enter new Vehicle Model (leave blank to keep current): ") or vehicle[2]
             if not is_valid_model(model):
                     print("Invalid Vehicle Model. It can contain letters, numbers, and some special characters, "
                                 "but cannot contain ! \" @ # $")
                     return

             vin = input("Enter new Vehicle VIN (leave blank to keep current): ") or vehicle[3]
             seller_name = input("Enter new Seller Name (leave blank to keep current): ") or vehicle[4]
             price_paid = input("Enter new Price Paid (leave blank to keep current): ") or vehicle[5]
             sales_price = input("Enter new Sales Price (leave blank to keep current): ") or vehicle[6]
             description = input("Enter new Vehicle Description (leave blank to keep current): ") or vehicle[7]

             price_paid = float(price_paid) if price_paid else vehicle[5]
             sales_price = float(sales_price) if sales_price else vehicle[6]

             cursor.execute("UPDATE vehicles SET make = ?, model = ?, vin = ?, seller_name = ?, price_paid = ?, "
                                           "sales_price = ?, description = ? WHERE id = ?",
                                           (make, model, vin, seller_name, price_paid, sales_price, description, vehicle_id))
             conn.commit()
             print("Vehicle updated successfully.")
     else:
             print("Vehicle not found.")

def remove_vehicle():
     vehicle_id = input("Enter the ID of the vehicle to remove: ")
     cursor.execute("DELETE FROM vehicles WHERE id = ?", (vehicle_id,))
     conn.commit()
     if cursor.rowcount > 0:
             print("Vehicle removed successfully.")
     else:
             print("Vehicle not found.")

def main():
     while True:
             print("\nOptions:")
             print("1. Show all vehicles")
             print("2. Add a vehicle")
             print("3. Edit a vehicle")
             print("4. Remove a vehicle")
             print("5. Exit program")
             
             choice = input("Select an option: ")

             if choice == '1':
                     show_vehicles()
             elif choice == '2':
                     add_vehicle()
             elif choice == '3':
                     edit_vehicle()
             elif choice == '4':
                     remove_vehicle()
             elif choice == '5':
                     print("Exiting program.")
                     break
             else:
                     print

if __name__ == "__main__":
     main()

# Close the database connection
conn.close()