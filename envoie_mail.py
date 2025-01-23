import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mes_infos_mail(file: str = "input/ID_mail.txt") -> tuple[str]:
    with open(file, 'r', encoding='utf-8') as f:
        infos = f.readlines()
    
    #      smtp            , email           , mdp
    return infos[0].strip(), infos[1].strip(), infos[2].strip()


def Init_destinataires(file: str = "input/destinataires.txt") -> list[str]:
    with open(file, 'r', encoding='utf-8') as f:
        destinataires = f.readlines()
    
    return [m.strip() for m in destinataires if m.strip()]
    


def envoie_mail_par_univ_angers(smtp: str, expediteur: str, mdp: str, destinataires: list[str], sujet: str, titre: str, msg: str) -> int:
    
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = ", ".join(destinataires)
    message["Subject"] = sujet
    
    html = "<h2>"+ titre +"</h2><p><a href=\"https://dossetud.univ-angers.fr/dossetud/etud/ficheEtud\">Vos Notes</a></p>"
    
    message.attach(MIMEText(html, "html"))
    message.attach(MIMEText(msg, "plain"))
    
    try:
        # Connexion au serveur SMTP
        with smtplib.SMTP(smtp, 587) as server:
            server.starttls()  # Sécurise la connexion
            server.login(expediteur, mdp)  # Authentification
            server.sendmail(expediteur, destinataires, message.as_string())
            
        print("E-mail envoyé avec succès !")
        return 0
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
        return 1
    

def envoie_notif(msg: str, destinataires: list[str]):
    
    smtp, expediteur, mdp = mes_infos_mail()
    
    sujet = "Des Notes !!!"
    
    titre = "Bon bah aujourdhui, IL Y A DES NOTES !!"
    
    envoie_mail_par_univ_angers(smtp, expediteur, mdp, destinataires, sujet, titre, msg)



def main():
    
    destinataires = Init_destinataires("input/test_mail.txt")
    
    msg = "Bip Boup test 1 2\nwow le saut de ligne de fou"
    
    envoie_notif(msg, destinataires)






if __name__ == "__main__":
    main()
