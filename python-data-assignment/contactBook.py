contacts={
 "Ravi": "9876543210",
 "Anita": "9123456780",
"Suresh": "9988776655",
"Priya": "9876501234",
}

print("all contacts: ", contacts)
name=input("Enter the name to search: ")
if name in contacts:
    print(f"{name}'s contact number is: {contacts[name]}")  
else:    print(f"Contact not found")