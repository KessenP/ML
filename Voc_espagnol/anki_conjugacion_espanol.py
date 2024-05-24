import genanki

# Définir le modèle de carte
card_model = genanki.Model(
    1607392319,  # Identifiant unique pour le modèle
    'Verbes Espagnols',
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

# Créer le paquet pour les verbes espagnols
spanish_verbs_deck = genanki.Deck(
    2059400112,  # Identifiant unique pour le paquet
    'Verbes Espagnols',
)

# Ajouter des cartes au paquet
spanish_verbs_cards = [
    {'Recto': 'Je danse', 'Verso': 'yo bailo (Présent, Groupe 1)'},
    {'Recto': 'Tu as parlé', 'Verso': 'tú has hablado (Passé Composé, Groupe 1)'},
    {'Recto': 'Il/Elle/On danse', 'Verso': 'él/ella/on baila (Présent, Groupe 1)'},
    {'Recto': 'Nous dansons', 'Verso': 'nosotros bailamos (Présent, Groupe 1)'},
    {'Recto': 'Vous dansez', 'Verso': 'vosotros bailáis (Présent, Groupe 1)'},
    {'Recto': 'Je chanterai', 'Verso': 'yo cantaré (Futur Simple, Groupe 1)'},
    {'Recto': 'Il/Elle/On chantera', 'Verso': 'él/ella/on cantará (Futur Simple, Groupe 1)'},
    {'Recto': 'Vous apprendriez (vouvoiement)', 'Verso': 'ustedes aprenderían (Conditionnel, Groupe 2)'},
    {'Recto': 'Vous apprendriez (tutoiement)', 'Verso': 'vosotros aprenderíais (Conditionnel, Groupe 2)'},
    {'Recto': 'Nous apprenions', 'Verso': 'nosotros aprendíamos (Imparfait, Groupe 2)'},
    {'Recto': 'Tu manges', 'Verso': 'tú comes (Présent, Groupe 2)'},
    {'Recto': 'Il/Elle/On boit', 'Verso': 'él/ella/on bebe (Présent, Groupe 2)'},
    {'Recto': 'Ils/Elles boivent', 'Verso': 'ellos/ellas beben (Présent, Groupe 2)'},
    {'Recto': 'Vous écriviez (vouvoiement) ', 'Verso': 'ustedes escriban (Subjonctif Présent, Groupe 3)'},
    {'Recto': 'Tu vivras', 'Verso': 'tú vivirás (Futur Simple, Groupe 3)'},
    {'Recto': 'Nous avons vécu', 'Verso': 'nosotros hemos vivido (Passé Composé, Groupe 3)'},
    {'Recto': 'Je dansai', 'Verso': 'yo bailé (Prétérit, Groupe 1)'},
    {'Recto': 'Tu dansas', 'Verso': 'tú bailaste (Prétérit, Groupe 1)'},
    {'Recto': 'Il/Elle/On dansa', 'Verso': 'él/ella/on bailó (Prétérit, Groupe 1)'},
    {'Recto': 'Nous dansâmes', 'Verso': 'nosotros bailamos (Prétérit, Groupe 1)'},
    {'Recto': 'Vous dansâtes (vouvoiement)', 'Verso': 'vosotros bailasteis (Prétérit, Groupe 1)'},
    {'Recto': 'Je chanterais', 'Verso': 'yo cantaría (Conditionnel, Groupe 1)'},
    {'Recto': 'Il/Elle/On chanterait', 'Verso': 'él/ella/on cantaría (Conditionnel, Groupe 1)'},
    {'Recto': 'Vous apprendriez (vouvoiement)', 'Verso': 'ustedes aprenderían (Conditionnel, Groupe 2)'},
    {'Recto': 'Tu apprendrais', 'Verso': 'tú aprenderías (Conditionnel, Groupe 2)'},
    {'Recto': 'Nous apprenions', 'Verso': 'nosotros aprendíamos (Imparfait, Groupe 2)'},
    {'Recto': 'Tu manges', 'Verso': 'tú comes (Présent, Groupe 2)'},
    {'Recto': 'Il/Elle/On boit', 'Verso': 'él/ella/on bebe (Présent, Groupe 2)'},
    {'Recto': 'Ils/Elles boivent', 'Verso': 'ellos/ellas beben (Présent, Groupe 2)'},
    {'Recto': 'Vous écriviez', 'Verso': 'ustedes escriban (Subjonctif Présent, Groupe 3)'},
    {'Recto': 'Tu écrirais', 'Verso': 'tú escribirías (Conditionnel, Groupe 3)'},
    {'Recto': 'Tu vivras', 'Verso': 'tú vivirás (Futur Simple, Groupe 3)'},
    {'Recto': 'Nous avons vécu', 'Verso': 'nosotros hemos vivido (Passé Composé, Groupe 3)'},
]

for card_info in spanish_verbs_cards:
    spanish_verb_note = genanki.Note(
        model=card_model,
        fields=[card_info['Recto'], card_info['Verso']],
    )
    spanish_verbs_deck.add_note(spanish_verb_note)

# Créer et sauvegarder le paquet
genanki.Package(spanish_verbs_deck).write_to_file('Verbes_Espagnols.apkg')

