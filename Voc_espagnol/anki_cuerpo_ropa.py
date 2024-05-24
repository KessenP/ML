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
    'vocabulario_cuerpo_y_ropa')

# Liste des mots et traductions
word_pairs = [
    ('Tête', 'Cabeza'),
    ('Yeux', 'Ojos'),
    ('Oreilles', 'Orejas'),
    ('Nez', 'Nariz'),
    ('Bouche', 'Boca'),
    ('Cou', 'Cuello'),
    ('Épaules', 'Hombros'),
    ('Bras', 'Brazos'),
    ('Mains', 'Manos'),
    ('Doigts', 'Dedos'),
    ('Poitrine', 'Pecho'),
    ('Dos', 'Espalda'),
    ('Estomac', 'Estómago'),
    ('Jambes', 'Piernas'),
    ('Pieds', 'Pies'),
    ('Chemise', 'Camisa'),
    ('Pantalons', 'Pantalones'),
    ('Robe', 'Vestido'),
    ('Chaussures', 'Zapatos'),
    ('Chaussettes', 'Calcetines'),
    ('Casquette', 'Gorra'),
    ('Chapeau', 'Sombrero'),
    ('Écharpe', 'Bufanda'),
    ('Gants', 'Guantes'),
    ('Manteau', 'Abrigo'),
    ('Jupe', 'Falda'),
    ('Cravate', 'Corbata'),
    ('Veste', 'Chaqueta'),
    ('Pull', 'Jersey'),
    ('T-shirt', 'Camiseta'),
]

# Ajouter des cartes au paquet
for word, translation in word_pairs:
    note = genanki.Note(
        model=model,
        fields=[word, translation])
    deck.add_note(note)

# Créer le fichier du paquet Anki (.apkg)
genanki.Package(deck).write_to_file('vocabulario_cuerpo_y_ropa.apkg')

print('Paquet Anki créé avec succès.')
