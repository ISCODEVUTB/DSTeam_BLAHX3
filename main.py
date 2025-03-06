from typing import List
from flask import Flask
from Gestion_Paquete.users import User
from Gestion_Paquete.location import Location
from Gestion_Paquete.package import Package
from Gestion_Paquete.order import Order


app = Flask(__name__)
@app.route("/")

in_user: User = [None]
recipient_list: List[User] = []
order_list: List[Order] = []

def main():
    """
    Main entry point of the program.

    This function serves as the starting point of execution.
    """
    app.run(host="0.0.0.0", port=9876)   
    main_menu()

def main_menu() -> None:
    """
    Displays the main menu and handles user input.

    The user can choose to create a new order or exit the program.
    If an invalid option is entered, the user is prompted again.
    """
    while True:
        menu = (
            "\tMenu\n"
            "\t1.\tCreate Order\n"
            "\t2.\tExit\n"
        )
        print(menu)

        try:
            option = int(input("Type a number: "))
            if option == 1:
                new_order()
                break  # Exit loop after handling the option
            elif option == 2:
                break  # Exit function
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def order_menu() -> int:
    """
    Displays the order menu and handles user input.

    The user can choose to create, view, delete packages, generate a receipt,
    or exit the order menu. If an invalid option is entered, the user is prompted again.

    Returns:
        int: The selected menu option (1-5).
    """
    while True:
        menu = (
            "\tMenu\n"
            "\t1.\tNew package\n"
            "\t2.\tShow packages\n"
            "\t3.\tDelete package\n"
            "\t4.\tGenerate receipt\n"
            "\t5.\tExit"
        )
        print(menu)

        try:
            option = int(input("Type a number: "))
            if option >= 1 or option <= 5:
                return option
            print("Invalid option. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def new_user(user_type: str) -> User:
    """
    Creates a new user by prompting for user details.

    Args:
        user_type (str): The type of user being created.

    Returns:
        User: A new User instance with the provided details.
    """
    print(f"Creating {user_type} user")

    name = input("Name: ")
    last_name = input("Last name: ")
    national_id = input("National Identification: ")
    email = input("Email: ")
    location = new_location(name)

    return User(name, last_name, national_id, email, location, "BLAHX3")

def new_location(user_name: str) -> Location:
    """
    Creates a new location by prompting the user for details.

    Args:
        user_name (str): The name of the user associated with the location.

    Returns:
        Location: A Location instance with the provided details.
    """
    print(f"Address for {user_name}")

    country = input("Country: ")
    department = input("Department: ")
    city = input("City: ")
    address1 = input("Address 1: ")
    address2 = input("Address 2: ")

    zip_code = None
    while zip_code is None:
        try:
            zip_code = int(input("Zip Code: "))
            if zip_code <= 0:
                print("Invalid value. Zip Code must be a positive number.")
                zip_code = None
        except ValueError:
            print("Invalid input. Please enter a numeric zip code.")

    return Location(country, department, city, address1, address2, zip_code)

def new_package() -> Package:
    """
    Creates a new package by prompting the user for weight and dimensions.

    Returns:
        Package: A Package instance with the provided weight and dimensions.
    """
    print("New package")

    # Function to validate numeric positive input
    def get_positive_value(prompt: str) -> float:
        """
        Prompts the user for a positive float value.

        Args:
            prompt (str): The input message displayed to the user.

        Returns:
            float: A positive numeric value entered by the user.
        """
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    raise ValueError("Value must be a positive number.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}")

    # Get and validate inputs
    weight = get_positive_value("Weight (Kg): ")
    length = get_positive_value("Length (m): ")
    width = get_positive_value("Width (m): ")
    height = get_positive_value("Height (m): ")

    return Package(weight, length, width, height)

def show_packages(package_list: list, receiver: User = None) -> None:
    """
    Displays the list of packages. If a receiver is provided, 
    it shows the recipient's information.

    Args:
        package_list (list): A list of Package objects to display.
        receiver (User, optional): The recipient of the packages. Defaults to None.
    """
    if receiver is not None:
        print(f"Packages due to be sent to: {receiver.name} ({receiver.user_id})")

    for index, package in enumerate(package_list, start=1):
        print(f"Package {index}")
        print(package)
        print()

def delete_package(package_list: list) -> int:
    """
    Removes a package from the package list based on user input.

    Args:
        package_list (list): A list of Package objects.

    Returns:
        int: 1 if the package was successfully deleted, 0 if the package was not found.
    """
    if not package_list:
        print("No packages available to delete.")
        return 0

    # Display available packages
    show_packages(package_list)

    # Extract package IDs
    package_list_id = [package.package_id for package in package_list]

    package_deleted = input("Select package ID to delete: ")

    try:
        index = package_list_id.index(package_deleted)
        package_list.pop(index)
        return 1
    except ValueError:
        return 0

def new_order():
    """
    Handles the process of creating a new order.

    - Ensures a sender is registered.
    - Creates a new receiver.
    - Manages package operations (adding, showing, deleting).
    - Generates a receipt or exits the order process.
    """
    if in_user[0] is None:
        in_user[0] = new_user("sender")

    print()
    receiver: User = new_user("receiver")
    recipient_list.append(receiver)

    package_list: list = []

    while True:
        option: int = order_menu()

        if option == 1:
            package: Package = new_package()
            print(f"Package created ({package.package_id})")
            package_list.append(package)
        elif option == 2:
            show_packages(package_list, receiver)
        elif option == 3:
            if delete_package(package_list) == 1:
                print("Package deleted successfully")
            else:
                print("Invalid package ID. No package deleted.")
        elif option > 3 and package_list is not None:
            order_list.append(Order(in_user[0], recipient_list[0], package_list))
            if option == 4:
                receipt()
                return
            elif option == 5:
                print(order_list[0])
                option = 0
                while option not in ('y', 'n'):
                    option = input("Quieres parar la Orden? (Y/N)").lower()
                    if option == "y":
                        return
                    elif option == "n":
                        continue

def receipt():
    """
    Generates and prints a detailed receipt for the first order in the `order_list`.

    This function calculates the total price for all packages in the first order, then 
    prints relevant details, including:
    - Order ID
    - Receiver's name, user ID, and address
    - A list of packages included in the order
    - Sender's name, user ID, and address
    - The total price of all packages in the order
    
    Assumes that:
    - `order_list` contains at least one order.
    - `recipient_list` and `in_user` contain at least one recipient and one sender respectively.
    - Each package in `order_list[0].packages` has a `calculate_price()` method.
    - `recipient_list[0]` and `in_user[0]` have attributes such as `name`, `user_id`, and `address`.
    """
    package_info = ', '.join(str(pkg) for pkg in order_list[0].packages)
    total = 0
    for pkg in order_list[0].packages:
        total = total + pkg.calculate_price()

    print()
    print("\t*****  RECEIPT  *****")
    print(f"\nOrder ID: {order_list[0].order_id}")
    print(f"\n\nRECEIVER: {recipient_list[0].name} ({recipient_list[0].user_id})")
    print(f"RECEIVER ADDRESS: {recipient_list[0].address.city + ',' + recipient_list[0].address.address1}")
    print(f"\n\n\tPACKEGES")
    print(package_info)
    print(f"\n\nSENDER: {in_user[0].name} ({in_user[0].user_id})")
    print(f"RECEIVER ADDRESS: {in_user[0].address.city + ',' + in_user[0].address.address1}")
    print("\n-----------------------------------")
    print(f"Total: {total} USD")


if __name__ == '__main__':
    main()
