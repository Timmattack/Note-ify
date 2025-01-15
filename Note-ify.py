import envoie_mail
import analyse_page
from datetime import datetime

def log(file: str = "output/log_Notes.txt"):
    
    lheure = datetime.now()
    dt_string = lheure.strftime("%Y/%m/%d, %H:%M:%S")
    
    with open(file, 'a') as f:
        f.write("loggé à : "+dt_string+"\n")


def main():
    
    log()
    
    res = analyse_page.Analyse_plus_resultats()
    
    if(res != []):
        destinataires = envoie_mail.Init_destinataires()
        
        msg = "Matières concernées: \n\n-"
        msg += "\n-".join(res)
        
        envoie_mail.envoie_notif(msg, destinataires)
    
    
    
    

if __name__ == "__main__":
    main()