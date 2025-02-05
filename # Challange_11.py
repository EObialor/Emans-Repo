# Challange_11

'''
Person and Customer classes

'''
# Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nphone: {self.phone}"

# Customer Subclass
class Customer(Person):
    def __init__(self, name, address, phone, customer_ID, mailing_list):
        super().__init__(name, address, phone)
        self.customer_ID = customer_ID
        self.mailing_list = mailing_list 

    def __str__(self):
        mailing_list_status = "Yes" if self.mailing_list else "No"
        return f"{super().__str__()}\nCustomer Number: {self.customer_ID}\nOn Mailing List: {mailing_list_status}"

if __name__ == "__main__":
    customer1 = Customer(name="Emmanuel Obialor", address="1500 Park row Blvd", phone="123-456-7890", customer_ID="C123456", 
     mailing_list=True)
    
    print(customer1)
