class Livre:
    def __init__(self,title,autor,number_pages,):
        self.__title=title
        self.__autor=autor
        self.__number_pages=number_pages
        self.__disponible= True
    #je créé une class livre avec plusieur attributs, ces attributs sont privé grace au double underscore

    def get_title(self):
        return self.__title
    
    def get_autor(self):
        return self.__autor
    
    def get_number_pages(self):
        return self.__number_pages
    # je créé trois méthodes accesseurs qui me permettent de connaitre les attributs

    def set_title(self,title):
        self.__title=title

    def set_autor(self,autor):
        self.__autor=autor

    def set_number_pages(self,number_pages):
        if number_pages>0 and type(number_pages)==int:
            self.__number_pages=number_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
    #je créé trois méthodes mutateur qui me permettent de changer les attributs
    #je vérifie que le nombre de page entrer soit bien un entier positif avec une condition if et 
    #les fonctions type et int

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False
    #avec la fonction verification je test si l'attribut __disponible de self est True
    #puis je retourn True sinon je retourne False
        
    def borrow(self):
        if not self.verification :
            print("Book isn't available")
            return False
        else:
            self.__disponible=False
            return True
        
    #je verifie si le livre est disponible en testant directement la methode verification
    #avec une condition if puis je change l' attribut __disponible de self en false
    #j'afficihe un message d'erreur si le livre n'est pas disponible

    def give_back(self,):
        if self.borrow:
            self.__disponible=True
        else:
            print("No borrowing ongoing.")

    #je verifie si le livre a été emprunté en testant directement la methode emprunter()
    #avec la condition if
    

object=Livre("bon","rousseau",200)
print(object.get_number_pages())
object.set_number_pages(300)
print(object.get_number_pages()) #on créé un objet en tant que livre, on change son nombre de page 

print(object.verification())#on verifiy s'il est disponible
print(object.borrow())#on lance un emprunt
object.give_back()#on rend l'emprunt
print(object.verification())#on verifie que le livre est a nouveau disponible
 

