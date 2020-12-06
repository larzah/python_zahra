# Programme Interactif
# Par Zahra Larche-Sheikh, larzah20@ecolecatholique.ca
# 2020/12/03

print("Bienvenue, pour commencer le jeux s'il vous plaît écrire start")
choice = input()
if choice == "start":
    print(
        "Tu te retrouve dans un fôret sombre, deux chemain sont situé devant vous. Est-ce que vous aller sur la chemain droite ou gauche?"
    )
    choice = input()
    if choice == "droite":
        print(
            "Vous avez choisi la chemain droite. Tu continue sur cette route et retrouve une verre de lait. Est-ce que tu le bois? Oui ou non?"
        )
        choice = input()
        if choice == "oui":
            print("Tu bois le lait. Aucun changement est arriver.")
        if choice == "non":
            print("Vous ignorez le lait et continue sur la route.")
        print(
            "En poursuivant votre route, vous rencontrez un monstre. Est-ce que vous a) fuyez ou b) Le combattre avec vos poings?"
        )
        choice = input()
        if choice == "a":
            print("Vous avez décider de vous fuire. Malheureusement, le monstre a couru après vous et vous a tué. [Jeu terminé, merci d'avoir joué]")
        if choice == "b":
            print("Vous avez choisi b! Tout en combattant le monstre, une autre personne se joint à vous et ensemble vous le battez!")
            print("Bonjour, je m'appelle Eyra! C'est quoi ton nom?")
            name = input()
            print("Bonjour", name, "Pour vous aider à traverser cette forêt, prenez cette épée!")
            print("Vous prenez l'épée d'Eyra et continuez votre chemin. Bientôt, il commence à faire noir. Voulez vous a) Utilisez votre épée pour obtenir du bois pour un feu, ou b) Continuez à marcher. [Veuillez choisir a ou b]")
            choice = input()
            if choice == "a":
              print("Vous avez décidé d'aller chercher du bois de chauffage. Malheureusement, en ramassant le bois, vous trébuchez sur une branche et vous poignardez. [Jeu Terminé, merci d'avoir joué.]")
            if choice == "b":
              print("Vous avez choisi de continuer votre promenade. En trébuchant dans la forêt sombre, vous tombez dans un trou profond sans issue. [Jeu Terminé, merci d'avoir joué.]")
if choice == "gauche":
  print("Vous avez décidé d'aller à gauche, ce chemin est plein de pierres et de champignons. Prenez-vous une bouchée des champignons? Oui ou non?")
  choice = input()
  if choice == "oui":
    print("Vous prenez une bouchée du champignon et commencez à vous sentir étourdi. Vous continuez à marcher sur le chemin, puis vous vous évanouissez. En s'évanouissant, un monstre vous trouve et vous mange. [Jeu Terminé, merci d'avoir joué.]")
  if choice =="non":
    print("Vous avez décidé de ne pas manger les champignons. Vous voyez un bug en sortir et vous vous sentez chanceux. En continuant sur le chemin, vous apercevez un petit chalet avec de la fumée sortant de la cheminée. Vous décidez de frapper et d'entrer dans la maison. Personne ne semble être à la maison. Il y a un bol chaud de flocons d'avoine sur la table, tu le manges? Oui ou non?")
    if choice == "oui":
      print("Vous commencez à vous sentir mal à l'aise après avoir pris votre première bouchée, vous regardez de plus près le gruau et voyez qu'il a une teinte verte. Vous regardez par-dessus votre épaule et voyez une bouteille à moitié vide étiquetée «poison». [Jeu Terminé, merci d'avoir joué.]")
      if choice == "non":
        print("Vous choisissez de ne pas manger le bol de gruau et de quitter la maison. Vous choisissez de ne pas manger le bol de gruau et de quitter le chalet. En quittant le gîte, le propriétaire du chalet vous repère et vous accuse de vol. Il vous saisit et vous enferme au sous-sol. Sans échappatoire, vous vivez au sous-sol pour le reste de votre courte vie.[Jeu Terminé, merci d'avoir joué.]")


