import genanki

# Définir le modèle de carte
card_model = genanki.Model(
    1607392319,  # Identifiant unique pour le modèle
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
    ],
)

#    Materiales compuestos : Materiales compuestos
#    Los polímeros : Polímeros
#    Química general : Química general

# Créer un paquet pour les matériaux composites
composite_deck = genanki.Deck(
    2059400110,  # Identifiant unique pour le paquet
    'Materiales compuestos',
)

# Ajouter des cartes au paquet des matériaux composites
composite_cards = [
    {'Recto': 'Renfort', 'Verso': 'Refuerzo'},
    {'Recto': 'Matrice', 'Verso': 'Matriz'},
    {'Recto': 'Résine époxy', 'Verso': 'Resina epoxi'},
    {'Recto': 'Résine polyester', 'Verso': 'Resina de poliéster'},
    {'Recto': 'Résine thermodurcissable', 'Verso': 'Resina termoestable'},
    {'Recto': 'Moulage par injection', 'Verso': 'Moldeo por inyección'},
    {'Recto': 'Résistance mécanique', 'Verso': 'Resistencia mecánica'},
    {'Recto': 'Module d\'élasticité', 'Verso': 'Módulo de elasticidad'},
    {'Recto': 'Résistance à la corrosion', 'Verso': 'Resistencia a la corrosión'},
    {'Recto': 'Conductivité électrique', 'Verso': 'Conductividad eléctrica'},
    {'Recto': 'Composites thermoplastiques', 'Verso': 'Compuestos termoplásticos'},
    {'Recto': 'Composites thermodurcissables', 'Verso': 'Compuestos termoestables'},
    {'Recto': 'Matériaux composites à matrice métallique (MMC)', 'Verso': 'Materiales compuestos de matriz metálica (MMC)'},
    {'Recto': 'Matériaux composites à matrice céramique (CMC)', 'Verso': 'Materiales compuestos de matriz cerámica (CMC)'},
    {'Recto': 'Renforts céramiques', 'Verso': 'Refuerzos cerámicos'},
    {'Recto': 'Microscopie électronique à balayage (MEB)', 'Verso': 'Microscopía electrónica de barrido (MEB)'},
    {'Recto': 'Composites intelligents', 'Verso': 'Compuestos inteligentes'},
    {'Recto': 'Composites à auto-réparation', 'Verso': 'Compuestos de autorreparación'},
    {'Recto': 'Composites à mémoire de forme', 'Verso': 'Compuestos con memoria de forma'},
    {'Recto': 'Résistance à la fatigue', 'Verso': 'Resistencia a la fatiga'},
    {'Recto': 'Durabilité environnementale', 'Verso': 'Durabilidad ambiental'},
    {'Recto': 'Recyclage des matériaux composites', 'Verso': 'Reciclaje de materiales compuestos'},
    {'Recto': 'Fin de vie des composites', 'Verso': 'Fin de vida de los compuestos'},
]

for card_info in composite_cards:
    composite_note = genanki.Note(
        model=card_model,
        fields=[card_info['Recto'], card_info['Verso']],
    )
    composite_deck.add_note(composite_note)

# Créer un paquet pour les polymères
polymer_deck = genanki.Deck(
    2059400111,  # Identifiant unique pour le paquet
    'Polímeros',
)

# Ajouter des cartes au paquet des polymères
polymer_cards = [
    {'Recto': 'Polymérisation', 'Verso': 'Polimerización'},
    {'Recto': 'Monomère', 'Verso': 'Monómero'},
    {'Recto': 'Polymère thermoplastique', 'Verso': 'Polímero termoplástico'},
    {'Recto': 'Polymère thermodurcissable', 'Verso': 'Polímero termoestable'},
    {'Recto': 'Polyéthylène', 'Verso': 'Polietileno'},
    {'Recto': 'Polystyrène', 'Verso': 'Poliestireno'},
    {'Recto': 'Polypropylène', 'Verso': 'Polipropileno'},
    {'Recto': 'Polyvinylechlorure (PVC)', 'Verso': 'Policloruro de vinilo (PVC)'},
    {'Recto': 'Masse molaire moyenne', 'Verso': 'Masa molar media'},
    {'Recto': 'Taux de cristallinité', 'Verso': 'Tasa de cristalinidad'},
    {'Recto': 'Point de fusion', 'Verso': 'Punto de fusión'},
    {'Recto': 'Module d\'élasticité', 'Verso': 'Módulo de elasticidad'},
    {'Recto': 'Plastiques', 'Verso': 'Plásticos'},
    {'Recto': 'Fibres synthétiques', 'Verso': 'Fibras sintéticas'},
    {'Recto': 'Caoutchoucs synthétiques', 'Verso': 'Caucho sintético'},
    {'Recto': 'Adhésifs et colles', 'Verso': 'Adhesivos y pegamentos'},
    {'Recto': 'Polymérisation radicalaire', 'Verso': 'Polimerización radicalaria'},
    {'Recto': 'Polymérisation par ouverture d\'anneau', 'Verso': 'Polimerización por apertura de anillo'},
    {'Recto': 'Polymérisation par étapes', 'Verso': 'Polimerización por etapas'},
    {'Recto': 'Copolymères', 'Verso': 'Copolímeros'},
    {'Recto': 'Biopolymères', 'Verso': 'Biopolímeros'},
    {'Recto': 'Dégradation chimique', 'Verso': 'Degradación química'},
    {'Recto': 'Recyclage des plastiques', 'Verso': 'Reciclaje de plásticos'},
    {'Recto': 'Bioplastiques', 'Verso': 'Bioplásticos'},
    {'Recto': 'Réaction de polycondensation', 'Verso': 'Reacción de policondensación'},
    {'Recto': 'Réaction de polyaddition', 'Verso': 'Reacción de poliadición'},
    {'Recto': 'Polymérisation radicalaire en émulsion', 'Verso': 'Polimerización radicalaria en emulsión'},
    {'Recto': 'Polymérisation anionique', 'Verso': 'Polimerización aniónica'},
]

for card_info in polymer_cards:
    polymer_note = genanki.Note(
        model=card_model,
        fields=[card_info['Recto'], card_info['Verso']],
    )
    polymer_deck.add_note(polymer_note)

# Créer un paquet pour la chimie
chemistry_deck = genanki.Deck(
    2059400112,  # Identifiant unique pour le paquet
    'Química general',
)

# Ajouter des cartes au paquet de chimie
chemistry_cards = [
    {'Recto': 'Réaction d\'oxydoréduction', 'Verso': 'Reacción de oxidación-reducción'},
    {'Recto': 'Synthèse organique', 'Verso': 'Síntesis orgánica'},
    {'Recto': 'Substitution nucléophile', 'Verso': 'Sustitución nucleofílica'},
    {'Recto': 'Réaction d\'hydrolyse', 'Verso': 'Reacción de hidrólisis'},
    {'Recto': 'Hydrocarbures', 'Verso': 'Hidrocarburos'},
    {'Recto': 'Alcools et phénols', 'Verso': 'Alcoholes y fenoles'},
    {'Recto': 'Amines', 'Verso': 'Aminas'},
    {'Recto': 'Amides', 'Verso': 'Amidas'},
    {'Recto': 'Orbitales atomiques', 'Verso': 'Orbitales atómicos'},
    {'Recto': 'Nombre quantique', 'Verso': 'Número cuántico'},
    {'Recto': 'Fonction d\'onde', 'Verso': 'Función de onda'},
    {'Recto': 'Équation de Schrödinger', 'Verso': 'Ecuación de Schrödinger'},
    {'Recto': 'Isomérie', 'Verso': 'Isomería'},
    {'Recto': 'Tautomérie', 'Verso': 'Tautomería'},
    {'Recto': 'Coordination des composés', 'Verso': 'Coordinación de compuestos'},
    {'Recto': 'Complexes de métaux de transition', 'Verso': 'Complejos de metales de transición'},
    {'Recto': 'Ligands', 'Verso': 'Ligandos'},
    {'Recto': 'Cristallographie', 'Verso': 'Cristalografía'},
    {'Recto': 'Enthalpie', 'Verso': 'Entalpía'},
    {'Recto': 'Entropie', 'Verso': 'Entropía'},
    {'Recto': 'Équilibre chimique', 'Verso': 'Equilibrio químico'},
    {'Recto': 'Ordre de réaction', 'Verso': 'Orden de reacción'},
    {'Recto': 'Constante de vitesse', 'Verso': 'Constante de velocidad'},
    {'Recto': 'Facteurs affectant la vitesse de réaction', 'Verso': 'Factores que afectan la velocidad de reacción'},
    {'Recto': 'Spectroscopie UV-visible', 'Verso': 'Espectroscopía UV-visible'},
    {'Recto': 'RMN (Résonance Magnétique Nucléaire)', 'Verso': 'RMN (Resonancia Magnética Nuclear)'},
    {'Recto': 'Chromatographie en phase liquide', 'Verso': 'Cromatografía en fase líquida'},
    {'Recto': 'Spectroscopie infrarouge (IR)', 'Verso': 'Espectroscopía infrarroja (IR)'},
    {'Recto': 'Méthodes de titrage', 'Verso': 'Métodos de titulación'},
    {'Recto': 'Chromatographie en phase gazeuse', 'Verso': 'Cromatografía en fase gaseosa'},
    {'Recto': 'Spectrométrie de masse', 'Verso': 'Espectrometría de masas'},
    {'Recto': 'Polluants atmosphériques', 'Verso': 'Contaminantes atmosféricos'},
    {'Recto': 'Déchets chimiques', 'Verso': 'Residuos químicos'},
    {'Recto': 'Gestion durable des ressources', 'Verso': 'Gestión sostenible de recursos'},
]

for card_info in chemistry_cards:
    chemistry_note = genanki.Note(
        model=card_model,
        fields=[card_info['Recto'], card_info['Verso']],
    )
    chemistry_deck.add_note(chemistry_note)

# Créer et sauvegarder les paquets
genanki.Package(composite_deck).write_to_file('Matériaux_Composites.apkg')
genanki.Package(polymer_deck).write_to_file('Polymères.apkg')
genanki.Package(chemistry_deck).write_to_file('Chimie.apkg')
