# import random
from flask import Flask
from flask_wtf import CSRFProtect
from Gestion_Paquete.users import User
from Gestion_Paquete.location import Location
from Gestion_Paquete.package import Package

in_user: User = [None]
recipient_list: list = []
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app) 
@app.route("/")

def main():
    app.run(host="0.0.0.0", port=9876)    
    """
    Main entry point of the program.

    This function serves as the starting point of execution.
    """
    menu_principal()

def menu_principal() -> None:
    """
    """

    print("""
\tMenu
\t1.\tCrear orden
\t2.\tSalir
""")

    option=0
    try:
        while option < 1 or option > 3:
            option = int(input("Type a number: "))
    except ValueError:
        print("Invalid value")
        menu_principal()

    if option == 1:
        new_order()
    elif option == 2:
        return

def menu_orden() -> int:
    """
    """
    print("""
\tMenu
\t1.\tNew package
\t2.\tShow packages
\t3.\tDelete package
\t4.\tGenerate receipt
\t5.\tExit
""")

    option=0
    while option < 1 or option > 5:
        try:
            option = int(input("Type a number: "))
        except ValueError:
            print("Invalid value")

    return option

def new_user(user_type: str) -> User:
    """
    """
    print(f"Creating {user_type} user")
    name: str = input("Name: ")
    last_name: str = input("Last name: ")
    national_id: str = input("National Identification: ")
    email: str = input("Email: ")
    location: Location = new_location(name)

    return User(name, last_name, national_id, email, location)

def new_location(user_name: str):
    """
    """
    print(f"Direccion ({user_name})")
    country = input("Country: ")
    department = input("Departament: ")
    city = input("City: ")
    address1 = input("Address 1: ")
    address2 = input("Address 2: ")
    
    zip_code = None
    while zip_code is None:
        try:
            zip_code = int(input("Zip Code: "))
        except ValueError:
            print("Invalid value")
            zip_code = None

def new_package() -> Package:
    """
    """
    print("New packege")

    weight = None
    while weight is None:
        try:
            weight = int(input("Weight (Kg): "))
        except ValueError:
            print("Invalid value")
            weight = None
    
    length = input("Length (m): ")
    width = input("Width (m): ")
    height = input("Height (m): ")

    dimensions = length + 'x' + width + 'x' + height

    return Package(weight, dimensions)

def show_packages(package_list: list, receiver: User = None) -> None:
    """
    """
    if receiver is not None:
        print(f"Packeges due to sent to: {receiver.name} ({receiver.user_id})")
    for i in range(len(package_list)):
        print(f"Package {i+1}")
        for item in str(package_list[i]).split(','):
            print(item)
        print()

def delete_package(package_list: list) -> int:
    """
    """
    def extract_id(package: Package):
        return package.package_id
    package_list_id = list(map(extract_id, package_list))

    show_packages(package_list)

    package_deleted = input("Select package: ")

    try:
        index = package_list_id.index(package_deleted)
        package_list.pop(index)
        return 1

    except ValueError:
        index = None
        return 0

def new_order():
    """
    """
    if in_user[0] == None:
        in_user[0] = new_user("sender")

    print()
    receiver: User = new_user("receiver")
    recipient_list.append(receiver)

    package_list: list = []

    option = 0
    while True:
        option: int = menu_orden()

        if option == 1:
            package: Package = new_package()
            print(f"Paquete creado ({package.package_id})")
            package_list.append(package)
        elif option == 2:
            show_packages(package_list, receiver)
        elif option == 3:
            if delete_package(package_list) == 1:
                print("Package deleted succesfully")
            else:
                print("Package not deleted")
        elif option == 4:
            receipt()
        elif option == 5:
            break

def receipt():
    """
    """
    pass


if __name__ == '__main__':
    main()
