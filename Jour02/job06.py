class Commande:
    def __init__(self,nb_commande):
        self.__nb_commande=nb_commande
        self.__list_plats={}
        self.__statut_commande="en cours"
        self.__total=self.total_prix()
        # je créé mon constructeur avec les attributs demandé

    def add_commande(self,nom_plat,new_prix):
        self.__list_plats[nom_plat]=new_prix
        return self.__list_plats
        #je créé une méthode quime permet tout simplemetn d'ajouter un element a mon dictionnaire

    def annuler_commande(self):
        if self.__statut_commande=="en cours":
            self.__statut_commande="annulée"
        else:
            print("La commande a été terminée ou annulée")
        #je créé une méthode qui détermine si l'attribut commance est "en cour" ou "annulé"
        #dans le cas ou l'attribut n'est pas trouvé j'affiche un message d'erreur

    def total_prix(self):
        total=sum(self.__list_plats.values())
        return total
        #cette méthode permet de faire le total à payer grçacea une commande sum() et .value()
    
    def get_commande(self):
        return f""" 
        numéro de commande : {self.__nb_commande}
        liste de plats : {self.__list_plats}
        statut de la commande : {self.__statut_commande}
        total à payer : {self.__total + self.calcul_TVA()}
"""
#une méthode accesseur pour tout les attribut de notre objet

    def calcul_TVA(self):
        tva= self.total_prix()*0.2
        return tva
    # calcule du prix a payer pour une tva à 20%

object=Commande(110)
object.add_commande("steak",15)
object.add_commande("burger",22)
print(object.total_prix())
print(object.calcul_TVA())
print(object.get_commande())

