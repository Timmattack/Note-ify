Bonjoir,

?? Comment ça marche ??

###########
## INPUT ##
###########

--- destinataires.txt ---
Les e-mails des destinataires, un par ligne
/!\ N'oubliez pas de sauter une ligne au dernier e-mail /!\


--- TOUCHE_PAS_CA_mail.txt --- 
La première ligne contient le protocole SMTP, 
en général, c'est smtp.après_arobase
si mon mail est mon_nom@mail.com, alors le protocole sera smtp.gmail.com
si c'est mon_mail@domaine.fr, alors le protocole sera smtp.domaine.fr


La deuxième ligne contient votre e-mail ou un e-mail vous appartenant ;)


La troisième ligne contient un mot de passe permettant d'accéder à la boîte mail


--- CA_NON_PLUS_univ.txt ---
La première ligne contient ton identifiant universitaire

La deuxième ton mot de passe universitaire


--- matières.txt ---
contient les noms des matières, copiez-collez le nom exact donné dans la page de notes
Sautez un ligne entre chaque matière
/!\N'oubliez pas de sauter une ligne à la dernière matière aussi/!\

_ex:
matière1
matière2
Matière 3


############
## OUTPUT ##
############

--- log_Notes.txt ---
Il y est écrit quand le programme a été lancé


--- objectifs_atteints.txt ---
Il y est écrit quelles matières ont été notées




Le script principal (Note-ify) peut être éxécuté via le "task scheduler" de windows !

Pour l'éxécuter en silence, on utilise pythonw !



un mail est envoyé (aux addresse précisée dans destinataires.txt) si une matière "objectif" a été notée sur le site 