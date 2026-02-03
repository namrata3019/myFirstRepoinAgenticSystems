print("Enter your age")
age = int(input())
print("Do you have an ID card? (true/false)")
has_id=bool(input())
if age>=18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")