class Student:
    def __init__(self,name,first_name,number):
        self.__name=name
        self.__first_name=first_name
        self.__number=number
        self.__credit=0
        self.__level=self.call()
#je créé une class student avec 4 attributs privé

    def add_credits(self,credit):
        if credit>0:
            self.__credit+=credit
        else:
            print("Number of credits needs to be positive.")
        print(f"Credit number of {self.__first_name} {self.__name} is {self.__credit} points")
#je créé une méthode de mutateur qui ajoute des crédits a l'attribut après avoir
#vérififier que le nombre des crédit soit superieur a 0 grace a une condition if

    def get_student(self):
        return self.__name,self.__first_name,self.__number,self.__credit
#j'ai créé en plus uen methode accesseur pour pouvoir afficher le contenut de l'objet

    def __student_eval(self):
        if self.__credit>=90:
            self.__level="Excellent"
        elif self.__credit>=80:
            self.__level="Trés Bien"
        elif self.__credit>=70:
            self.__level="Bien"
        elif self.__credit>=60:
            self.__level="passable"
        elif self.__credit<60:
            self.__level="insuffisant"
        return self.__level
#je créé une méthode privé qui renvoie une note en valeur en fonction du nombre de crédit

    def call(self):
        return self.__student_eval()
#je créé cette méthode suplémentaire qui me permet d'appeller __student_eval que je ne peut
#pas appeler directement

    def student_info(self):
        print(f"""
        First name = {self.__first_name}
        Name = {self.__name}
        id = {self.__number}
        Level = {self.__level}
""")
# cette méthode permet d'afficher toutes les informations de l'étudiant




john_Doe=Student("Doe","John",145)
john_Doe.add_credits(100)  
john_Doe.add_credits(50)    
john_Doe.add_credits(10) 
print(john_Doe.get_student()) 
john_Doe.call() 
john_Doe.student_info()   


    



