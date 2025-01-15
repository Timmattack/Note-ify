import requests
from bs4 import BeautifulSoup

from datetime import datetime



def mes_infos_univ(file: str = "input/CA_NON_PLUS_univ.txt") -> tuple[str]:
    with open(file, 'r') as f:
        infos = f.readlines()
    
    #      id           , mdp
    return infos[0][:-1], infos[1]


def connect_et_sauve_notes_html(id: str, mdp: str, site_login = "https://casv6.univ-angers.fr/cas/login?service=https%3A%2F%2Fvosnotes.univ-angers.fr%2Fvosnotes%2F", site_notes = "https://vosnotes.univ-angers.fr/vosnotes/", fichier: str = "output/Notes.html") -> bool:
    
    with requests.Session() as session:
        
        response = session.post(site_login)
        soup = BeautifulSoup(response.text, "html.parser")
        
        #On trouve un 'cookie' dans une balise input, avec dans l'argument name='execution'
        code_execution = soup.find("input", {"name": "execution"})["value"]
    
    
        requete = {
            "username": id,
            "password": mdp,
            "execution": code_execution,
            "_eventId": "submit",
            "geolocation": ""
        }
        
        response = session.post(site_login, data=requete)
        
        #print(f"Status code: {response.status_code}")
        
        if(response.status_code != 200):
            return False
        
        else:
            
            if not "Affichage Vos Notes" in response.text:
                print("grr >:( (pas de \"Affichage Vos Notes\")")
                return False
    
            page_notes = session.get(site_notes)
            with open(fichier, 'w', encoding='utf-8') as f:
                f.write(page_notes.text)
            
            return True


def Init_objectifs(fichier: str = "input/matieres.txt"):
    with open(fichier, 'r') as f:
        matieres = f.readlines()
    
    # les lignes finissent par \n, on retire alors ce dernier caractère
    return [m[:-1] for m in matieres]


def change_objectifs(objectifs: list[str], fichier: str = "input/matieres.txt"):
    objectifs = [m+'\n' for m in objectifs]
    
    with open(fichier, 'w', encoding='utf-8') as f:
        f.writelines(objectifs)
    
    objectifs = [m[:-1] for m in objectifs]

def ecrit_objectif_atteint(objectifs: list[str], fichier: str = "output/objectifs_atteints.txt"):
    
    lheure = datetime.now()
    dt_string = lheure.strftime("%Y/%m/%d, %H:%M:%S")
    
    objectifs = [obj+" | "+dt_string+'\n' for obj in objectifs]
    
    with open(fichier, 'a', encoding='utf-8') as f:
        f.writelines(objectifs)

def actualise_matieres_et_objectifs_atteints(obj_notes: list[str], objectifs: list[str]):
    ecrit_objectif_atteint(obj_notes)
    
    for obj in obj_notes:
        objectifs.remove(obj)
    
    change_objectifs(objectifs)
    


def extrait_soup(fichier: str = "output/Notes.html"): # renvoie la soupe
    with open(fichier, 'r') as f:
        page = f.read()
    
    soup = BeautifulSoup(page, 'html.parser')
    
    return soup

def objectifs_notes(objectifs: list[str], soup) -> list[str]:
    
    #La table des notes est la seule à contenir la class border :D
    la_table = soup.find("table", attrs={"class": "border"})
    lignes = la_table.find_all("tr")
    
    obj_notes = []
    
    for tr in lignes:
        
        datas = tr.find_all("td")
        
        if(len(datas) == 0):
            continue
        elif(not datas[0].string in objectifs):
            continue
        elif(datas[1].get_text(strip=True) == ''):
            continue
        else:
            obj_notes.append(datas[0].string)
    
    return obj_notes


def proto_CEST_IMPERDABE_PUTAIN():
    objectifs = Init_objectifs()
    
    obj_notes = objectifs_notes(objectifs, extrait_soup())
    
    print(f"{objectifs}")
    print(f"{obj_notes}")
    
    if not(obj_notes == []):
        actualise_matieres_et_objectifs_atteints(obj_notes, objectifs)

#se connecte, sauvegarde la page, la lis, regarde les matières notées, actualise les matières notées / non notées
def Analyse_plus_resultats() -> list[str]:
    
    id, id_mdp = mes_infos_univ()
    connect_et_sauve_notes_html(id, id_mdp)
    
    
    objectifs = Init_objectifs()
    
    obj_notes = objectifs_notes(objectifs, extrait_soup())
    
    #print(f"{objectifs}")
    #print(f"{obj_notes}")
    
    if not(obj_notes == []):
        actualise_matieres_et_objectifs_atteints(obj_notes, objectifs)
    
    return obj_notes



def main():
    
    """
    id, mdp = mes_infos_univ()
    
    site_login = "https://casv6.univ-angers.fr/cas/login?service=https%3A%2F%2Fvosnotes.univ-angers.fr%2Fvosnotes%2F"
    site_notes = "https://vosnotes.univ-angers.fr/vosnotes/"
    
    
    if(connect_et_sauve_notes_html(id, mdp)):
        print("ayé :D")
    else:
        print("aïe !!")
    """
    
    """
    matieres = Init_objectifs()
    
    obj_notes = objectifs_notes(matieres, extrait_soup())
    
    print(obj_notes)
    print(matieres)
    """
    
    proto_CEST_IMPERDABE_PUTAIN()
    
    
    

if __name__ == "__main__":
    main()
