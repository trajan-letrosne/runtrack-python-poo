class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
#je créé une class rectangle avec length et width en attributs

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
# je créé deux méthodes accesseur qui me permette de connaitre la valeurs des attributs
    
    def set_length(self,length):
        self.length=length
   
    def set_width(self,width):
        self.width=width
#je créé deux mutateur qui me permette de modifier la valeur des attributs

object=Rectangle(10,5)
print(object.get_length(),object.get_width())
object.set_length(45)
object.set_width(23)
print(object.get_length(),object.get_width())
#je créé un objet, j'affiche ses attributs, je rentre des nouvelles valeurs dans les attributs puis j'affiche a nouveau


    