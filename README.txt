Bonjoir,

ce programme permet donc de :
  envoyer un mail (aux addresse précisée dans destinataires.txt) si une matière "objectif" a été notée sur le site 


#################
## Dépendances ##
#################

- requests
- BeautifulSoup


-------------------------------------------------------------------------------------
---   ENSUITE   ---

?? Comment ça marche ??

###########
## INPUT ##
###########
--- matieres.txt ---
contient les noms des matières, copiez-collez le nom exact donné dans la page de notes
Sautez un ligne entre chaque matière
/!\N'oubliez pas de sauter une ligne à la dernière matière aussi/!\

_ex:
matière 1
matière 2
Matière 3


--- destinataires.txt ---
Les e-mails des destinataires, un par ligne
/!\ N'oubliez pas de sauter une ligne au dernier e-mail /!\


--- ID_mail.txt --- 
La première ligne contient le protocole SMTP, 
en général, c'est smtp.après_arobase
si mon mail est mon_nom@gmail.com, alors le protocole sera smtp.gmail.com
si c'est mon_mail@domaine.fr, alors le protocole sera smtp.domaine.fr

La deuxième ligne contient votre e-mail ou un e-mail vous appartenant

La troisième ligne contient un mot de passe permettant d'accéder à la boîte mail

/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\
/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\
/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\


--- ID_univ.txt ---
La première ligne contient ton identifiant universitaire

La deuxième ton mot de passe universitaire

/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\
/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\
/!\/!\/!\ NE PARTAGEZ JAMAIS CE FICHIER /!\/!\/!\


############
## OUTPUT ##
############
--- log_Notes.txt ---
Il y est écrit quand le programme a été lancé


--- objectifs_atteints.txt ---
Il y est écrit quelles matières ont été notées, et quand


--- Notes.html ---
c'est la page des notes qui est téléchargée, puis analysée (vous pouvez la visualiser)

--------------------------------------------------------------------------------------


Le script principal Note-ify peut être éxécuté via le "task scheduler" de windows.
Pour l'éxécuter en silence, on utilise pythonw (et non pas 'simplement' python) !

########################################
## Set Up le "task scheduler" windows ##
########################################

- Cherchez le programme "task scheduler", en français "Planificateur de tâches"
à gauche, vous voyez des dossiers, vous pouvez en créer un autre, du genre "script-Notify"

- Clic droit sur ce dossier, puis "Créer un tâche" (pas "de base", sinon ils vous manquera quelques options intéressantes)

- Choisissez un nom, puis une description (pour vous rappeler à quoi sert cette tâche plus tard :p)



- Cochez "Éxécuter avec les autorisations maximales"
- Cochez "Masquer", et configurez pour "Windows 10"

Passez à l'onglet "Déclencheur"
-------------------------------
- Cliquez sur "Nouveau"
- Laissez "Lancer la tâche à l'heure programmée"

- Pour ses paramètres:
  - Cochez une fois par jour
  - Vous démarrez le jour que vous voulez, ça répètera tout les jours...
  - j'ai personnellement choisi 8h30

- Pour ses paramètres avancés:
  - Cochez "Répéter la tâche toutes les :"
  - J'ai choisi 20 minutes, pour cela sélectionnez un temps en minute et réécrivez "20 minutes" à la place
  - J'ai choisi une durée de "10 heures"

Ces paramètres auront pour effet de, une fois par jour, lancer une boucle qui lancera la commande toute les 20 minutes pendant 10 heures
  - Vous pouvez indiquez une date d'expiration, je le recommande, parce que sinon vous allez clairement oublier de la désactiver :)
  - Cochez "Activée"
  - Validez ce paramètre en cliquant dur "Ok"

Passez à l'onglet "Actions"
---------------------------
- Cliquez sur "Nouveau"
- Laissez l' "Action" "Démarrer un programme"

- Pour ses Paramètres:
  - Vous chosirez l'exécutable "pythonw.exe", vérifiez à bien spécifier son chemin, n'hésitez pas à utiliser l'option "Parcourir"
Ensuite, comme vous le souhaitez :
  - Soit vous spécifiez le chemin entier vers le script "Note-ify.py" dans "Ajouter des arguments"
  - Soit vous spécifiez dans "Ajouter des arguments" uniquement "./Note-ify.py", et dans "Commencer dans", vous mettez le dossier dans lequel se situe le script de Note-ify

Validez avec "Ok"
Re validez avec "OK"

Votre super tâche est Set up :D

maintenant, je vous propose une super vidéo pour mettre votre PC en AFk :D
https://youtu.be/1SLr62VBBjw
Ou celle là :D
https://youtu.be/_Den0fw2pQg




