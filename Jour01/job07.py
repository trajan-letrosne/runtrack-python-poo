class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0
# j'initialise le personnage avec les atribut x et y

    def gauche(self):
        self.y-=1

    def droite(self):
        self.y+=1

    def bas(self):
        self.x-=1

    def haut(self):
        self.x +=1
#je créé 4 methodes qui permettent de deplacer mon personnage sur les axe x et y
#en ajoutant ou retirant 1 pour chaque mouvement

    def position(self):
        return self.x, self.y
# je renvoie la position qui va se mettre automatiquement sous la forme d'un tuple

object= Personnage()
object.gauche()
print( object.position())
    


