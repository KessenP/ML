# pip install beautifulsoup4
from bs4 import BeautifulSoup

def extraire_mots(html_content):
    # Charger le contenu HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver toutes les balises <div> avec la classe "noteText"
    balises_div = soup.find_all('div', class_='noteText')

    # Initialiser une liste pour stocker les mots extraits
    mots_extraits = []

    # Parcourir toutes les balises <div> trouvées
    for div in balises_div:
        # Extraire le texte contenu dans la balise
        texte = div.get_text(strip=True)
        
        # Diviser le texte en mots
        mots = texte.split()

        # Ajouter les mots à la liste
        mots_extraits.extend(mots)

    return mots_extraits

# Lire le contenu du fichier HTML
chemin_fichier = 'alas_chap1.html'

with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
    contenu_html = fichier.read()

# Appeler la fonction avec le contenu du fichier HTML
mots_extraits = extraire_mots(contenu_html)

# Afficher les mots extraits
print(mots_extraits)