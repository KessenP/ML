import genanki
import random

# Créer un modèle Anki
model = genanki.Model(
    1607392319,
    'Basique',
    fields=[
        {'name': 'Recto'},
        {'name': 'Verso'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Recto}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Verso}}',
        },
    ])

# Créer un paquet Anki
deck = genanki.Deck(
    random.randint(10**9, (10**10)-1),
    'vocabulario_alas')

# Liste des mots et traductions
word_pairs = [
    ('Indulgence', 'indulto.'),
    ('Eh bien', 'Pues'),
    ('Détruis-le', 'deshazlo'),
    ('Peau', 'piel'),
    ('Traître', 'traidor'),
    ('Mâchoire', 'quijada'),
    ('Lieutenant', 'Teniente.'),
    ('Se lève', 'yergue,'),
    ('Approuve', 'asiente'),
    ('Sac à dos', 'mochila'),
    ('Entrée', 'ingreso.'),
    ('Joue', 'mejilla,'),
    ('Il arque', 'Enarca'),
    ('Sourcil', 'ceja.'),
    ('Bien que', 'Aunque'),
    ('Coucher de soleil', 'atardecer'),
    ('Sac à dos', 'mochila'),
    ('Finition', 'remate'),
    ('Avait l\'habitude', 'solía'),
    ('Coin', 'esquina.'),
    ('Merde', 'Carajo,'),
    ('Poids', 'pesar,'),
    ('Libère', 'suelta'),
    ('Les jeter', 'tirarlos'),
    ('Coin', 'rincón'),
    ('Parapet', 'parapeto'),
    ('Large', 'ancho,'),
    ('Je me suis penché', 'asomé,'),
    ('Glissant', 'resbaloso,'),
    ('Cauchemar', 'pesadilla.'),
    ('Je livre', 'entrego.'),
    ('Mesure', 'medida.'),
    ('Côtes', 'costillas'),
    ('Miroir', 'espejo.'),
    ('Moitié', 'mitad'),
    ('Tirage', 'jalón'),
    ('Tresse', 'trenza.'),
    ('Mèches', 'mechones'),
    ('Tirer sur moi', 'jalarme'),
    ('Reste', 'Mantente'),
    ('Lien', 'vínculo'),
    ('Pièges', 'trampas'),
    ('Montes', 'subes'),
    ('Dehors', 'afuera'),
    ('En embrassant', 'abrazando'),
    ('Saisit', 'aferra'),
    ('Vides', 'vacíos'),
    ('Coin', 'esquina'),
    ('Folie', 'locura')
]

# Ajouter des cartes au paquet
for word, translation in word_pairs:
    note = genanki.Note(
        model=model,
        fields=[word, translation])
    deck.add_note(note)

# Créer le fichier du paquet Anki (.apkg)
genanki.Package(deck).write_to_file('vocabulario_alas.apkg')

print('Paquet Anki créé avec succès.')
