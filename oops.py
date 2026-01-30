class company:
    def __init__(self):
        self.__company="google"
    def display(self):
        print(self.__company)
s1=company()
s1.__company="gooogle"
s1.display()