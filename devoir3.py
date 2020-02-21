# je crois avoir réussi l'entièreté de mon travail sauf pour une chose : la dernière balise que je devrais trouver pour pouvoir imprimer le titre des articles et non seulement les liens. Comme je suis aux jeux de la communication, je n'ai pas eu l'opportunité de le travailer plus tard que mardi le 18.


# coding : utf-8

import requests, csv 
from bs4 import BeautifulSoup

with open('spotmini.csv', 'w', newline='') as csvfile:   

# mon objectif est de moissonner tous les articles de The Verge qui traitent du chien-robot de la firme Boston Dynamics : le Spot Mini

    url = "https://www.theverge.com/tech/archives/"

entetes = {
     "User-Agent":"Félix Pedneault - 514/778-4207 : requête envoyée dans le cadre d'un cours de journalisme pour un reportage numérique",
     "From":"felix.pedneault21@gmail.com"}

# je dois créer un moyen de fouiller toutes les pages d'archives de la section Tech de The Verge. C'est 15 pages. La première page des archives s'appellent url/archives/ par contre, son numéro n'est donc pas 1, ce qui pourrait causer problème à mon code. 

page = list(range(2,16))

for numero in page:
    if numero < 2:
        numero = "" + str(numero)
    urlpage = url + str(numero)
    print(urlpage)
    
r = requests.get(url)
section1 = BeautifulSoup(r.text, "html.parser")
section2 = ""

n = 0 
numero = 1
while section2 != section1:
    # print(section1)
    numero = numero +1
    section2 = section1
    urlpage = url + str(numero)

    r = requests.get(urlpage)
    section1 = BeautifulSoup(r.text, "html.parser")

    articles = section1.find_all("h2", class_="c-entry-box--compact__title")

    #ici je cherche des caractères clés dans les titres d'articles

    for article in articles: 
            n += 1
            
            articleurl = article.find("a")["href"]
            print(n, articleurl)
            print("."*10)   

            articletitre = section1.find(, class_="c-entry-box--compact__title").text.strip()
            if "SpotMini" in articletitre or "spotmini" in articletitre or "spot" in articletitre or "Spot" in articletitre or "Boston Dynamics" in articletitre:
                print(articletitre)   
                print("."*10)
                spamwriter = csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([articletitre] + [articleurl])
