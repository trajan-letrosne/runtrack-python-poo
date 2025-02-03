class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #j'initialise x et y dans le constructeur

    def afficherLesPoints(self):
        return f"Point x = {self.x} point y = {self.y}"
    
    def afficherX(self):
        return f"x= {self.x}"
    
    def afficherY(self):
        return f"y={self.y}"
    # je créé trois methodes qui retourne x, y puis x et y

    def changerX(self):
        new=int(input("Enter votre nouvel x comme étant un entier :"))
        self.x = new
        return self.x
    
    def changerY(self):
        new=int(input("Enter votre nouvel y comme étant un entier :"))
        self.y = new
        return self.y
    # je créé deux methode qui entre un nouvel entier dans self.x puis retourn x
a=Point(1,2)
print(a.afficherLesPoints())
print(a.changerX())
print(a.afficherX())
    