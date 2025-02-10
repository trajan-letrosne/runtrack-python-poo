class Animal:
    def __init__(self):
        self.age=0
        self.prenom=str()
#j'initialise avec des attribut vides
    
    def afficher_age(self):
        return f"L'age de l'animal est {self.age}"
#je créé une methode qui retourne l'age

    def viellir(self):
        self.age+=1
        return f"l'age de l'animal est {self.age}"
#je créé une methode qui ajoute +1 à l'age puis retourne l'age

    def nommer(self):
        self.prenom=input("Entrez le nom de l'animal :")
        return f"L'animal se nomme {self.prenom}"
#je créé une methode qui ajoute un nom a l'animal puis retourne son nom

object=Animal()
object.afficher_age()
object.viellir()
object.nommer()
