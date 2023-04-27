import os
import sys
import datetime
from getpass import getpass
from prettytable import PrettyTable

MASTER_PASSWORD = "fish"

def add_entry(data, website, username, password):
    if website not in data:
        data[website] = {"username": username, "password": password, "date_created": datetime.datetime.now()}
        return "Entry added successfully."
    else:
        return "Website already exists. Use another name or delete the existing entry."

def delete_entry(data, website):
    if website in data:
        del data[website]
        return "Entry deleted successfully."
    else:
        return "Website not found."

def get_password(data, website):
    if website in data:
        return data[website]["password"]
    else:
        return "Website not found."

def list_entries(data):
    table = PrettyTable(["Website", "Username"])
    for website in data:
        table.add_row([website, data[website]["username"]])
    return table

def change_master_password(new_password):
    global MASTER_PASSWORD
    if MASTER_PASSWORD != new_password:
        MASTER_PASSWORD = new_password
        return "Master password updated."
    else:
        return "New master password cannot be the same as the current password."

def master_unlock(data, master_password_attempt):
    if master_password_attempt != MASTER_PASSWORD:
        return "Incorrect master password."
    table = PrettyTable(["Website", "Username", "Password", "Date Created"])
    for website in data:
        entry = data[website]
        table.add_row([website, entry["username"], entry["password"], entry["date_created"].strftime('%Y-%m-%d %H:%M:%S')])
    return table

def main():
    data = {}

    print("Welcome to the Password Manager")
    master_pass_attempt = getpass("Enter the master password: ")

    if master_pass_attempt != MASTER_PASSWORD:
        print("Incorrect master password. Exiting...")
        sys.exit(0)

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("Options:\n1. Add\n2. Delete\n3. Get\n4. List\n5. Change Master Password\n6. Master Unlock\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website: ")
            website = website.strip()
            if website.startswith("www."):
                website = website[4:]
            if website.endswith(".com"):
                website = website[:-4]
            website = "www." + website + ".com"
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            print(add_entry(data, website, username, password))
        elif choice == "2":
            website = input("Enter website to delete: ")
            website = website.strip()
            if website.startswith("www."):
                website = website[4:]
            if website.endswith(".com"):
                website = website[:-4]
            website = "www." + website + ".com"
            print(delete_entry(data, website))
        elif choice == "3":
            website = input("Enter website to get password: ")
            website = website.strip()
            if website.startswith("www."):
                website = website[4:]
            if website.endswith(".com"):
                website = website[:-4]
            website = "www." + website + ".com"
            print(get_password(data, website))
        elif choice == "4":
            print(list_entries(data))
        elif choice == "5":
            new_password = getpass("Enter new master password")
            print(change_master_password(new_password))
        elif choice == "6":
            master_pass_attempt = getpass("Enter the master password: ")
            print(master_unlock(data, master_pass_attempt))
        elif choice == "7":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
