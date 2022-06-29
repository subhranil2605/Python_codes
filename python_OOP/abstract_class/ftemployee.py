from employee import Employee



class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary



if __name__ == "__main__":
    e = FullTimeEmployee("Subhranil", "sarkar", 50000)
    print(e)
