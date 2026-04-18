# Parent class
class Emp:
    def __init__(self, ecode, ename, sal):
        self.ecode = ecode
        self.ename = ename
        self.sal = sal
    
    def takeLeave(self):
        print(f"{self.ename} is on leave")
    
    def display(self):
        print(f"Employee Code: {self.ecode}")
        print(f"Employee Name: {self.ename}")
        print(f"Salary: {self.sal}")


# Subclass - Developer
class Developer(Emp):
    def __init__(self, ecode, ename, sal, programming_language):
        super().__init__(ecode, ename, sal)
        self.programming_language = programming_language
    
    def takeLeave(self):
        print(f"{self.ename} (Developer) is on leave for bug fixing")
    
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


# Subclass - Manager
class Manager(Emp):
    def __init__(self, ecode, ename, sal, department):
        super().__init__(ecode, ename, sal)
        self.department = department
    
    def takeLeave(self):
        print(f"{self.ename} (Manager) is on leave, delegating responsibilities")
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Usage Example
if __name__ == "__main__":
    # Create Developer object
    dev = Developer("E001", "Alice", 75000, "Python")
    dev.display()
    dev.takeLeave()
    
    print("\n" + "="*40 + "\n")
    
    # Create Manager object
    mgr = Manager("E002", "Bob", 95000, "IT")
    mgr.display()
    mgr.takeLeave()