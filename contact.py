contacts = {}  # Dictionary to store contacts
current_id = 0  # Auto-incrementing ID for contacts

def main_menu():
  """Displays the main menu and returns the user's choice."""
  print("\nContact Book")
  print("1. Add Contact")
  print("2. View Contact List")
  print("3. Search Contact")
  print("4. Update Contact")
  print("5. Delete Contact")
  print("6. Exit")
  choice = input("Enter your choice: ")
  return choice

def add_contact():
  """Adds a new contact to the contact book."""
  global current_id, contacts
  name = input("Enter Name: ")
  phone = input("Enter Phone Number: ")
  email = input("Enter Email (optional): ")
  address = input("Enter Address (optional): ")
  contact_info = {"name": name, "phone": phone, "email": email, "address": address}
  current_id += 1
  contacts[current_id] = contact_info
  print("Contact added successfully!")

def view_contacts():
  """Displays a list of all saved contacts."""
  if not contacts:
    print("No contacts found!")
    return
  print("\nContact List:")
  for contact_id, info in contacts.items():
    print(f"ID: {contact_id}")
    print(f"Name: {info['name']}")
    print(f"Phone: {info['phone']}")
    if info.get("email"):
      print(f"Email: {info['email']}")
    if info.get("address"):
      print(f"Address: {info['address']}")
    print("-" * 20)

def search_contact():
  """Searches for a contact by name or phone number."""
  search_term = input("Enter name or phone number to search: ")
  found = False
  for contact_id, info in contacts.items():
    if search_term.lower() in info["name"].lower() or search_term in info["phone"]:
      print(f"\nID: {contact_id}")
      print(f"Name: {info['name']}")
      print(f"Phone: {info['phone']}")
      if info.get("email"):
        print(f"Email: {info['email']}")
      if info.get("address"):
        print(f"Address: {info['address']}")
      print("-" * 20)
      found = True
  if not found:
    print("Contact not found!")

def update_contact():
  """Updates the details of an existing contact."""
  contact_id = int(input("Enter contact ID to update: "))
  if contact_id not in contacts:
    print("Contact not found!")
    return
  print("Update details (leave blank to keep unchanged):")
  new_name = input("Name: ") or contacts[contact_id]["name"]
  new_phone = input("Phone Number: ") or contacts[contact_id]["phone"]
  new_email = input("Email (optional): ") or contacts.get(contact_id, {}).get("email", "")
  new_address = input("Address (optional): ") or contacts.get(contact_id, {}).get("address", "")
  contacts[contact_id] = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
  print("Contact updated successfully!")

def delete_contact():
  """Deletes a contact from the contact book."""
  contact_id = int(input("Enter contact ID to delete: "))
  if contact_id not in contacts:
    print("Contact not found!")
    return
  confirm = input(f"Are you sure you want to delete contact {contact_id} (y/n)? ")
  if confirm.lower() == "y":
    del contacts[contact_id]
    print("Contact deleted successfully!")

# Main loop
while True:
  choice = main_menu()
  if choice == '1':
    add_contact()
  elif choice == '2':
    view_contacts()
  elif choice == '3':
    search_contact()
  elif choice == '4':
    update_contact()
  elif choice == '5':
    delete_contact()
