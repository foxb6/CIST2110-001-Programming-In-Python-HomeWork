# Project 2
# Name: Bodhi Fox
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
from datetime import datetime, timedelta
from tabulate import tabulate

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.

def import_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            contacts = {}
            for row in reader:
                name = row[0]
                phone = row[1]
                email = row[2]
                birthday = datetime.strptime(row[3], '%m/%d/%Y')
                contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday}
            print(f"Contacts imported successfully from {file_name}")
            return contacts
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return {}

# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]

def add_contact(name, phone, email, birthday, contacts):
    if name in contacts:
        print(f"Error: Contact {name} already exists.")
        return False
    else:
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': datetime.strptime(birthday, '%m/%d/%Y')}
        print(f"Contact {name} added successfully.")
        return True

# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    contacts_list = [{'Name': name, 'Phone': contact['Phone'], 'Email': contact['Email'],
                      'Birthday': contact['Birthday'].strftime('%m/%d/%Y')} for name, contact in contacts.items()]
    print(tabulate(sorted(contacts_list, key=lambda x: x['Name']),
                   headers='keys', tablefmt='grid'))

# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.

def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
        return True
    else:
        print(f"Error: Contact {name} not found.")
        return False

# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.

def next_birthday(contacts):
    if not contacts:
        print("No contacts found.")
        return
    today = datetime.now()
    next_birthday_contacts = []
    for name, contact in contacts.items():
        contact_birthday = contact['Birthday'].replace(year=today.year)
        if today <= contact_birthday <= today + timedelta(days=30):
            next_birthday_contacts.append({'Name': name, 'Next Birthday': contact_birthday.strftime('%m/%d')})
    if next_birthday_contacts:
        print("Next Birthdays:")
        print(tabulate(sorted(next_birthday_contacts, key=lambda x: x['Next Birthday']),
                       headers='keys', tablefmt='grid'))
    else:
        print("No birthdays in the next 30 days.")

# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.

def save_csv(file_name, contacts):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            for name, contact in contacts.items():
                writer.writerow([name, contact['Phone'], contact['Email'], contact['Birthday'].strftime('%m/%d/%Y')])
        print(f"Contacts saved successfully to {file_name}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    contacts = import_csv("contact.csv")
    
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Next Birthday")
        print("5. Save Contacts to CSV")
        print("0. Quit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            birthday = input("Enter birthday (MM/DD/YYYY): ")
            add_contact(name, phone, email, birthday, contacts)
            
        elif choice == '2':
            view_contacts(contacts)
            
        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name, contacts)
            
        elif choice == '4':
            next_birthday(contacts)
            
        elif choice == '5':
            file_name = input("Enter the filename to save contacts: ")
            save_csv(file_name, contacts)
            
        elif choice == '0':
            save_csv("contact.csv", contacts)  # Save contacts before quitting
            print("Exiting program. Contacts saved.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

  
    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?

names_starting_with_a = sum(1 for name in contacts.keys() if name.startswith('A'))
print("Names starting with A:", names_starting_with_a)

    # How many emails are yahoo emails?
yahoo_emails = sum(1 for contact in contacts.values() if 'yahoo.com' in contact['Email'])
print("Yahoo emails:", yahoo_emails)
    # How many .org emails are there?
org_emails = sum(1 for contact in contacts.values() if contact['Email'].endswith('.org'))
print(".org emails:", org_emails)
    # How many contacts have a birthday in January?
january_birthdays = sum(1 for contact in contacts.values() if contact['Birthday'].month == 1)
print("Contacts with January birthdays:", january_birthdays)

if __name__ == "__main__":
    main()
