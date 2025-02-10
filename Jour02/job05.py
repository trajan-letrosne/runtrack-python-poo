class Voiture:
    def __init__(self,model,marque,année,kilo):
        self.__model=model
        self.__marque=marque
        self.__année=année
        self.__kilo=kilo
        self.en_marche=False
        self.__reservoir=50
    #je créé une class voiture avec cinq attributs

    def get_model(self):
        return self.__model
    
    def get_marque(self):
        return self.__marque
    
    def get_année(self):
        return self.__année
    
    def get_kilo(self):
        return self.__kilo
    
    def get_marche(self):
        return self.en_marche
    #je créé un accesseur pour chaque attributs

    def set_model(self,model):
        self.__model=model

    def set_marque(self,marque):
        self.__marque=marque

    def set_année(self,année):
        self.__année=année

    def set_kilo(self,kilo):
        self.__kilo=kilo

    def set_marche(self,marche):
        self.en_marche=marche
    #je créé mutateur pour chaque attributs

    def demarrer(self):
        k = self.__verifier_plein()
        if k>5:
            self.en_marche=True
        else:
            print("Il n'y a pas assez d'essence.")
            # j'utilisa dans la méthode démarrer le retour de la méthode vérifier
            #plein et ensuite je compare s'il est supérieur a 5 à l'aide d'une
            #condition if
            #s'il nest pas assez plein je renvoie un message d'erreur
    
    def arreter(self):
        self.en_marche=False
    #je créé deux méthode pour arreter et demarrer la voiture en utilisant 
    #l'attribut en_marche

    def __verifier_plein(self):
        return self.__reservoir
    #je créé une methode qui me renvoie l'état du réservoire que je vais pouvoir
    #utiliser dans la méthode démarrer

    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self,reservoir):
        self.reservoir=reservoir
    #je créé aussi un mutateur et accesseur pour le nouvel attribut __reservoir


object=Voiture("208","peugeot","2015",12000)
print(object.get_model())
object.set_model(207)
print(object.get_model())
object.demarrer()
print(object.get_marche())

    


