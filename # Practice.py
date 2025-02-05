# Practice 
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    
    def display_info(self):
        print(f"This car is a {self.make} {self.model} {self.year} {self.color}.") 
        
    
    def start_engine(self):
        print(f"The engine of {self.make} is now running") 
        
        


if __name__ == "__main__":
        car1 = Car("Chevy", "sportage", 2021, "green")
        car2 = Car("Toyota", "sienna", 2024, "Blue")
        car3 = Car("Ford", "Mustang", 2022, "black")
        
  
car1.display_info()
car2.display_info()
car3.display_info()  




class Book:
    def __init__(self, title, author, price, isbn):
        self.title = title 
        self.author = author 
        self.__price = price
        self.__isbn = isbn
        
    def set_price(self, price):
        self.__price = price     
        
    def set_isbn(self, isbn):
        self.__isbn = isbn
        
        
    def get_price(self):
        return self.__price    
    
    
    def get_isbn(self):
        return self.__isbn
    
    
    def display_info(self):
     print(f"This book is {self.title}, {self.author}, {self.__price}, {self.__isbn}.")    
     
     
     
if __name__ == "__main__":
    book1 = Book("Naruto", "Kishimoto", 50, "1234567891234" )
    
    
book1.display_info()    