class Livre:
    def __init__(self,title,autor,number_pages):
        self.__title=title
        self.__autor=autor
        self.__number_pages=number_pages
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

object=Livre("bon","rousseau",200)
print(object.get_number_pages())
object.set_number_pages(300)
print(object.get_number_pages())

