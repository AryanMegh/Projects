import sqlite3
import re

# Connect to SQLite database (or create it if it doesn't exist)
Conn = sqlite3.connect('MiniprojDB.db')
Cursor = Conn.cursor()

# Create a table for vehicles
Cursor.execute('''
CREATE TABLE IF NOT EXISTS Vechile_detail(
     Id INTEGER PRIMARY KEY AUTOINCREMENT,
     Vechile_making_name TEXT NOT NULL,
     Vechile_model TEXT NOT NULL,
     Vechile_identification_num TEXT NOT NULL UNIQUE,
     Seller_name TEXT,
     Price_paid REAL,
     Sale_price REAL NOT NULL,
     Vechile_description TEXT
)
''')
Conn.commit()

def Validate_vechilemakingname(Vechilemakingname):
     return Vechilemakingname.isalpha()

def Validate_vechilemodel(V_model):
     return bool( re.match("^[A-Za-z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$", V_model)) and not re.search("[!\"#$]", V_model )

def Validate_vechileidentificationum(Vechile_identification_num):
     return bool( re.match("^[A-Za-z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$", Vechile_identification_num ) ) and not re.search("[!\"#$]", Vechile_identification_num )

def Show_data():
     Cursor.execute( " select * from Vechile_detail" )
     Vehicles = Cursor.fetchall()
     if Vehicle:
            for Vehicle in Vehicles:
                print(f"ID: { Vehicle[0] }, \n Vechile Making Name: { Vehicle[1] }, \n Vechile Model: { Vehicle[2] }, \n Vechile Identifictiona Number: { Vehicle[3] }, "
                  f"\n Seller Name: { Vehicle[4] }, \n Price Paid: { Vehicle[5] }, \n Sales Price: { Vehicle[6] }, "
                  f"\n Vechile Description: { Vehicle[7] }")
     else:
             print( " No vehicles found. " )

def Add_data():
     Vechile_id = int( input( " Enter ID: " ) )
     Vechile_making_name = str( input( " Enter your Vehicle Making Name: " ) )
     if not Validate_vechilemakingname(Vechile_making_name):
             print( " Invalid Vehicle Make. It must contain letters only." )
             return
     Vechile_model = str( input( " Enter Vehicle Model Name: " ) )
     if not Validate_vechilemodel(Vechile_model):
             print( " Invalid Vehicle Model. It must not contain ! \" # $ and can have special characters." )
             return
     Vechile_identification_num = str( input( " Enter Vehicle Identification Number (VIN): " ) )
     if not Validate_vechileidentificationum(Vechile_identification_num):
          print( " Invalid Vehicle Identification number. It must not contain a-z and 0-9. " )
          return
     Seller_name = str( input( " Enter Seller Name (optional): " ) )
     Price_paid = str( input( " Enter Price Paid (optional, leave blank if not applicable): " ) )
     Sale_price = int( input( " Enter Sales Price: " ) )
     Vechile_description = str( input("Enter Vehicle Description: ") )

     # Insert vehicle into the database
     Cursor.execute('''
     insert into Vechile_detail (Vechile_making_name, Vechile_model, Vechile_identification_num, Seller_name, Price_paid, Sale_price, Vechile_description)
     VALUES (?, ?, ?, ?, ?, ?, ?)
     ''', (Vechile_making_name, Vechile_model, Vechile_identification_num, Seller_name, Price_paid if Price_paid else None, Sale_price, Vechile_description))
     Conn.commit()
     print( " Vehicle data saved successfully." )

def Edit_data():
     Vehicle_id = input( " Enter the ID of the vehicle to edit: " )
     Cursor.execute( " select * from Vechile_datail where Id = ?", (Vehicle_id) )
     Vehicle = Cursor.fetchone()

     if not Vehicle:
        print( " Vehicle not found." )
        return

     print( f" Current details: {Vehicle} " )
     Vechile_making_name = input( " Enter new Vehicle Make (leave blank to keep current): " ) or Vehicle[1]
     if not Validate_vechilemakingname(Vechile_making_name):
        print( " Invalid Vehicle Make. It must contain letters only." )
        return

     Vechile_model = str( input( " Enter Vehicle Model: " ) )
     if not Validate_vechilemodel(Vechile_model):
          print("Invalid Vehicle Model. It must not contain ! \" # $ and can have special characters.")
          return

     Vechile_identification_num = str( input( " Enter Vehicle Identification Number (VIN): " ) )
     Seller_name = str( input( " Enter Seller Name (optional): " ) )
     Price_paid = str( input( " Enter Price Paid (optional, leave blank if not applicable): " ) )
     Sale_price = int( input( " Enter Sales Price: " ) )
     V_description = str( input("Enter Vehicle Description: ") )

     # Update vehicle in the database
     Cursor.execute('''
     UPDATE vehicles
     SET make = ?, model = ?, vin = ?, seller_name = ?, price_paid = ?, sales_price = ?, description = ?
     WHERE id = ?
     ''', (Vechile_making_name, Vechile_model, Vechile_identification_num, Seller_name, Price_paid if Price_paid else None, Sale_price, V_description, Vehicle_id) )
     Conn.commit()
     print( " Vehicle updated successfully." )

def Remove_data():
     Vehicle_id = input( " Enter the ID of the vehicle to remove: " )
     Cursor.execute( " delete from Vehicle_datail where Dd = ? ", (Vehicle_id) )
     Conn.commit()
     print( " Vehicle removed successfully." )

def main():
     while True:
             print( " 1. Add a vehicle data" )
             print( " 2. Show all vehicle data" )
             print( " 3. Edit a vehicle " )
             print( " 4. Remove a vehicle " )
             print( " 5. Exit program " )
             
             Choice = input( " Select an option (1-5): " )
             
             if Choice == '1':
               Add_data()
             elif Choice == '2':
               Show_data()
             elif Choice == '3':
                Edit_data()
             elif Choice == '4':
                Remove_data()
             elif Choice == '5':
               print( " Exiting program. " )
               break
             else:
               print( " Invalid option. Please try again." )

if __name__ == "__main__":
     main()

# Close the database connection
Conn.close()