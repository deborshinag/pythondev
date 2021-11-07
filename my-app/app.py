from helper import util

class myapp:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def print_age(self):
        print(f"My age is {self.age}")


app = myapp("deborshi", 47) 

app.print_age()
util.show_name(app.name)