# Question 1
"""class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        self.email = self.first_name + '.' + self.last_name + "@imagine.com"

    def employee_details(self):
        return f"Name: {self.first_name} {self.last_name}\n" \
                f"Email: {self.email}\n" \
                f"Annual Salary: {self.salary:.2f}"


Employee1 = Employee("John", "Smith", 50000)
print(Employee1.employee_details())
"""


# Question 2
class LuxuryGood():
    def __init__(self, brand, name, purchase_date, price):
        if brand == "" or name == "" or purchase_date == "" or price == "":
            raise ValueError("brand, name, purchase_date, or price cannot be empty") 
               
        self.brand = brand
        self.name = name
        self.purchase_date = purchase_date
        self.price = price

    def employee_details(self):
        return f"Item: {self.brand} {self.name}\n" \
                f"Purchase Date: {self.purchase_date}\n" \
                f"Price: {self.price:.2f}"

class RichClient():
    def __init__(self):
        self.shopping_list = []
    
    def add_item(self, item):
        self.shopping_list.append(item)

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
    
    def print_list(self):
        if self.list_size() == 0:
            print("Shopping list is empty")
        else:
            for item in self.shopping_list:
                print(item.display_item())
    
    def list_size(self):
        return len(self.shopping_list)