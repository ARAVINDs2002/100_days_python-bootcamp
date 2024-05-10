# Define a function to get a specific contact
contact_list={}
def add_contact(contact_list,name,number):
    contact_list[name]=number
def get_contact(contact_list, name):
    # Check if the contact exists in the contact list
    if name in contact_list:
        phone = contact_list[name]  # Retrieve the phone number
        return f"Name: {name}, Phone: {phone}"
    else:
        return f"Contact '{name}' not found"

#add contacts here ok
add_contact(contact_list,"John Doe","5123456")
add_contact(contact_list,"pokerboy","12345")
add_contact(contact_list,"daniel","654321")
#retrieve contact
res=get_contact(contact_list, "John Doe") 
print(res)
res=get_contact(contact_list, "pokerboy") 
print(res)
res=get_contact(contact_list, "mamon") 
print(res)