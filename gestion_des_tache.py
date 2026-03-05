taches=["1.Faire les courses","2.Reviser le python","3.sortir le chien"]
taches_termine=[]
while True:
    
    print("""
=== MENU GESTIONNAIRE DE TACHES ===
1.Afficher les tache 
2.Ajouter une tache 
3.Supprime une tache
4.Marque une tache comme terminee
5.reset
6.quitter
""")
    print("------------------------------------")
    choix=int(input("==> votre choix : "))
    print("------------------------------------")
    print("------------------------------------")
    if  choix == 1 :
        nbr_taches = len(taches)
        nbr_taches_termine = len(taches_termine)
        print("==== votre taches sont ====")
        for i in range(nbr_taches):
            print(taches[i])
        print("------------------------------------")
        print("==== votre taches termine sont ====")
        for i in range(nbr_taches_termine):
            print(taches_termine[i])
    elif choix == 2 :
        tache=input("enterez une tache a ajouter : ")
        taches.append(tache)
    elif choix == 3 :
        index=int(input("enterez le num de votre tache a supprime : "))
        taches.pop(index-1)
    elif choix == 4 :
        index=int(input("enterez le numero de la tache terminee : "))
        tache_t=taches[index-1]
        taches_termine.append(tache_t)       
        taches.pop(index-1)
    elif choix == 5:
        print("vous voulez supri;e tout les taches")
        validation = input("oui/non")
        if validation == "oui":
            taches.clear()
            taches_termine.clear()
    elif choix == 6:
        print("Au revoir")
        break

    

        

    