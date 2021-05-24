from typing import List


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, salary):
        self.__salary = salary


    @property
    def bonus(self):
        return self.__bonus


    @bonus.setter
    def bonus(self, bonus):
        self.__bonus += bonus


    def to_pay(self):
        return self.__salary + self.bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        self.__percent = percent
        self.__bonus = 0


    @property
    def bonus(self):
        return self.__bonus


    @bonus.setter
    def bonus(self, bonus):
        if self.__percent > 200:
            self.__bonus = bonus * 3
        elif self.__percent > 100:
            self.__bonus = bonus * 2
        else:
            self.__bonus = bonus


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(name, salary)
        self.__client_number = client_number
        self.__bonus = 0


    @property
    def bonus(self):
        return self.__bonus


    @bonus.setter
    def bonus(self, bonus):
        if self.__client_number > 150:
            self.__bonus = bonus + 1000
        elif self.__client_number > 100:
            self.__bonus = bonus + 500
        else:
            self.__bonus = bonus


class Company:
    def __init__(self, *args: List[Employee], n: int = 0):
        self.__employees: List[Employee] = []

        if args:
            for arg in args[0]:
                if isinstance(arg, Employee):
                    self.__employees.append(arg)


    @property
    def employees(self):
        return self.__employees


    def give_everybody_bonus(self, company_bonus):
        for employee in self.__employees:
            employee.bonus = company_bonus

    def total_to_pay(self):
        return sum(employee.to_pay() for employee in self.__employees)


    def name_max_salary(self):
        maxs = -1
        name = ''
        for employee in self.__employees:
            if employee.to_pay() > maxs:
                maxs = employee.to_pay()
                name = employee.name
        return name



# a = SalesPerson('Alex', 10, 50)
# b = SalesPerson('Victor', 10, 150) # *2=300
# c = SalesPerson('Dima', 10, 300) # *3=900

# d = Manager('Stepan', 10, 50)
# e = Manager('Gavr', 10, 125) #+500=625
# f = Manager('John', 10, 200) #+1000=1200

# mac = Company([a, b, c, d, e, f], n=6)
# #mac = Company([e], n=1)

# mac.give_everybody_bonus(150)
# print(mac.total_to_pay())
# print(mac.name_max_salary())
