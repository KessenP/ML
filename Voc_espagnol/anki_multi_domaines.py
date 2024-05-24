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



domains =[]

# Liste des mots et traductions
word_pairs_alimentation_et_cuisine = [
    ("Repas", "Comida"),
    ("Ingrédients", "Ingredientes"),
    ("Recette", "Receta"),
    ("Cuisine", "Cocina"),
    ("Plat", "Plato"),
    ("Cuisson", "Cocción"),
    ("Saveur", "Sabor"),
    ("Épices", "Especias"),
    ("Assiette", "Plato"),
    ("Ustensiles", "Utensilios"),
    ("Cuisiner", "Cocinar"),
    ("Manger", "Comer"),
    ("Préparer", "Preparar"),
    ("Assaisonner", "Condimentar"),
    ("Déguster", "Degustar"),
    ("Servir", "Servir"),
    ("Mixer", "Mezclar"),
    ("Griller", "Asar a la parrilla"),
    ("Fondre", "Derretir"),
    ("Bouillir", "Hervir"),
]

domains.append(word_pairs_alimentation_et_cuisine)

# Création du tableau pour le domaine transport
word_pairs_transport = [
    ("Voiture", "Coche"),
    ("Train", "Tren"),
    ("Avion", "Avión"),
    ("Bus", "Autobús"),
    ("Vélo", "Bicicleta"),
    ("Métro", "Metro"),
    ("Taxi", "Taxi"),
    ("Port", "Puerto"),
    ("Aéroport", "Aeropuerto"),
    ("Station", "Estación"),
    ("Conduire", "Conducir"),
    ("Voyager", "Viajar"),
    ("Embarquer", "Abordar"),
    ("Débarquer", "Desembarcar"),
    ("Atterrir", "Aterrizar"),
    ("Décoller", "Despegar"),
    ("Circuler", "Circular"),
    ("Accélérer", "Acelerar"),
    ("Freiner", "Frenar"),
    ("Descendre", "Bajar"),
]

domains.append(word_pairs_transport)

word_pairs_voyages_et_tourisme = [
    ("Destination", "Destino"),
    ("Hôtel", "Hotel"),
    ("Guide", "Guía"),
    ("Excursion", "Excursión"),
    ("Plage", "Playa"),
    ("Monument", "Monumento"),
    ("Carte", "Mapa"),
    ("Aventure", "Aventura"),
    ("Souvenir", "Recuerdo"),
    ("Itinéraire", "Itinerario"),
    ("Explorer", "Explorar"),
    ("Visiter", "Visitar"),
    ("Se détendre", "Relajarse"),
    ("Voyager", "Viajar"),
    ("Découvrir", "Descubrir"),
    ("Planifier", "Planificar"),
    ("Séjourner", "Quedarse"),
    ("Embrasser", "Besar"),
    ("Photographier", "Fotografiar"),
    ("S'émerveiller", "Maravillarse"),
]
domains.append(word_pairs_voyages_et_tourisme)

word_pairs_shopping_et_commerce = [
    ("Magasin", "Tienda"),
    ("Produit", "Producto"),
    ("Vêtement", "Ropa"),
    ("Prix", "Precio"),
    ("Soldes", "Rebajas"),
    ("Marque", "Marca"),
    ("Client", "Cliente"),
    ("Achats", "Compras"),
    ("Réduction", "Descuento"),
    ("Caissier", "Cajero"),
    ("Acheter", "Comprar"),
    ("Vendre", "Vender"),
    ("Payer", "Pagar"),
    ("Essayer", "Probar"),
    ("Choisir", "Elegir"),
    ("Négocier", "Negociar"),
    ("Magasiner", "Ir de compras"),
    ("Emballer", "Empaquetar"),
    ("Livrer", "Entregar"),
    ("Rembourser", "Reembolsar"),
]

domains.append(word_pairs_shopping_et_commerce)

word_pairs_education = [
    ("École", "Escuela"),
    ("Étudiant", "Estudiante"),
    ("Professeur", "Profesor"),
    ("Cours", "Clase"),
    ("Matière", "Materia"),
    ("Diplôme", "Diploma"),
    ("Bibliothèque", "Biblioteca"),
    ("Examen", "Examen"),
    ("Leçon", "Lección"),
    ("Apprentissage", "Aprendizaje"),
    ("Apprendre", "Aprender"),
    ("Enseigner", "Enseñar"),
    ("Étudier", "Estudiar"),
    ("Réviser", "Revisar"),
    ("Partager", "Compartir"),
    ("Noter", "Tomar apuntes"),
    ("Comprendre", "Comprender"),
    ("S'inscrire", "Inscribirse"),
    ("Progresser", "Progresar"),
    ("Explorer", "Explorar"),
]

domains.append(word_pairs_education)

word_pairs_sante = [
    ("Médecin", "Médico"),
    ("Patient", "Paciente"),
    ("Hôpital", "Hospital"),
    ("Médicament", "Medicamento"),
    ("Symptôme", "Síntoma"),
    ("Diagnostique", "Diagnóstico"),
    ("Consultation", "Consulta"),
    ("Soins", "Cuidados"),
    ("Pharmacie", "Farmacia"),
    ("Vaccin", "Vacuna"),
    ("Soigner", "Curar"),
    ("Diagnostiquer", "Diagnosticar"),
    ("Prescrire", "Recetar"),
    ("Guérir", "Curarse"),
    ("Prendre", "Tomar"),
    ("Consulter", "Consultar"),
    ("Vacciner", "Vacunar"),
    ("Traiter", "Tratar"),
    ("Suivre", "Seguir"),
    ("Examiner", "Examinar"),
]

domains.append(word_pairs_sante)

word_pairs_meteo = [
    ("Temps", "Tiempo"),
    ("Soleil", "Sol"),
    ("Pluie", "Lluvia"),
    ("Vent", "Viento"),
    ("Nuage", "Nube"),
    ("Orage", "Tormenta"),
    ("Neige", "Nieve"),
    ("Tornade", "Tornado"),
    ("Prévision", "Previsión"),
    ("Climat", "Clima"),
    ("Briller", "Brillar"),
    ("Pleuvoir", "Llover"),
    ("Souffler", "Soplar"),
    ("Nuager", "Nublarse"),
    ("Orageux", "Tormentoso"),
    ("Tomber (neige)", "Caer (nieve)"),
    ("Prédire", "Predecir"),
    ("Varier", "Variar"),
    ("Rafraîchir", "Refrescar"),
    ("Chauffer", "Calentar"),
]

domains.append(word_pairs_meteo)

word_pairs_travail_et_emploi = [
    ("Emploi", "Empleo"),
    ("Bureau", "Oficina"),
    ("Collègue", "Colega"),
    ("Réunion", "Reunión"),
    ("Projet", "Proyecto"),
    ("Salaire", "Salario"),
    ("Carrière", "Carrera"),
    ("CV (Curriculum Vitae)", "CV (Currículum Vitae)"),
    ("Entretien", "Entrevista"),
    ("Mission", "Misión"),
    ("Travailler", "Trabajar"),
    ("Embaucher", "Contratar"),
    ("Licencier", "Despedir"),
    ("Réussir", "Tener éxito"),
    ("Promouvoir", "Ascender"),
    ("Postuler", "Solicitar"),
    ("Diriger", "Dirigir"),
    ("Collaborer", "Colaborar"),
    ("Gérer", "Gestionar"),
    ("Évoluer", "Evolucionar"),
]

domains.append(word_pairs_travail_et_emploi)

word_pairs_loisirs_et_divertissements = [
    ("Loisirs", "Ocio"),
    ("Sport", "Deporte"),
    ("Cinéma", "Cine"),
    ("Musique", "Música"),
    ("Lecture", "Lectura"),
    ("Spectacle", "Espectáculo"),
    ("Jeu", "Juego"),
    ("Exposition", "Exposición"),
    ("Art", "Arte"),
    ("Loisir", "Pasatiempo"),
    ("Pratiquer", "Practicar"),
    ("Regarder", "Mirar"),
    ("Écouter", "Escuchar"),
    ("Lire", "Leer"),
    ("Participer", "Participar"),
    ("Jouer", "Jugar"),
    ("Détendre", "Relajarse"),
    ("Créer", "Crear"),
    ("Visiter", "Visitar"),
    ("Apprécier", "Disfrutar"),
]

domains.append(word_pairs_loisirs_et_divertissements)

word_pairs_technologie = [
    ("Ordinateur", "Ordenador"),
    ("Smartphone", "Teléfono inteligente"),
    ("Internet", "Internet"),
    ("Logiciel", "Software"),
    ("Réseau", "Red"),
    ("Appareil", "Dispositivo"),
    ("Données", "Datos"),
    ("Écran", "Pantalla"),
    ("Batterie", "Batería"),
    ("Application", "Aplicación"),
    ("Naviguer", "Navegar"),
    ("Programmer", "Programar"),
    ("Télécharger", "Descargar"),
    ("Connecter", "Conectar"),
    ("Charger", "Cargar"),
    ("Partager", "Compartir"),
    ("Surfer", "Navegar"),
    ("Mettre à jour", "Actualizar"),
    ("Téléphoner", "Llamar"),
    ("Utiliser", "Usar"),
]

domains.append(word_pairs_technologie)

word_pairs_relations_et_communication = [
    ("Relation", "Relación"),
    ("Amitié", "Amistad"),
    ("Famille", "Familia"),
    ("Conversation", "Conversación"),
    ("Sentiment", "Sentimiento"),
    ("Opinion", "Opinión"),
    ("Communication", "Comunicación"),
    ("Confiance", "Confianza"),
    ("Respect", "Respeto"),
    ("Conseil", "Consejo"),
    ("Parler", "Hablar"),
    ("Écouter", "Escuchar"),
    ("Comprendre", "Entender"),
    ("Partager", "Compartir"),
    ("Exprimer", "Expresar"),
    ("Aimer", "Amar"),
    ("Conseiller", "Asesorar"),
    ("Respecter", "Respetar"),
    ("Échanger", "Intercambiar"),
    ("Ressentir", "Sentir"),
]

domains.append(word_pairs_relations_et_communication)

word_pairs_logement = [
    ("Maison", "Casa"),
    ("Appartement", "Apartamento"),
    ("Chambre", "Habitación"),
    ("Cuisine", "Cocina"),
    ("Salle de bain", "Baño"),
    ("Salon", "Salón"),
    ("Meuble", "Mueble"),
    ("Bail", "Contrato de alquiler"),
    ("Voisin", "Vecino"),
    ("Propriétaire", "Propietario"),
    ("Vivre", "Vivir"),
    ("Louer", "Alquilar"),
    ("Décorer", "Decorar"),
    ("Nettoyer", "Limpiar"),
    ("Déménager", "Mudarse"),
    ("Acheter", "Comprar"),
    ("Installer", "Instalar"),
    ("Partager", "Compartir"),
    ("Visiter", "Visitar"),
    ("Réparer", "Reparar"),
]

domains.append(word_pairs_logement)

word_pairs_mathematiques = [
    ("Nombre", "Número"),
    ("Addition", "Suma"),
    ("Soustraction", "Resta"),
    ("Multiplication", "Multiplicación"),
    ("Division", "División"),
    ("Équation", "Ecuación"),
    ("Géométrie", "Geometría"),
    ("Calcul", "Cálculo"),
    ("Algèbre", "Álgebra"),
    ("Formule", "Fórmula"),
    ("Calculer", "Calcular"),
    ("Résoudre", "Resolver"),
    ("Additionner", "Sumar"),
    ("Soustraire", "Restar"),
    ("Multiplier", "Multiplicar"),
    ("Diviser", "Dividir"),
    ("Mesurer", "Medir"),
    ("Équilibrer", "Equilibrar"),
    ("Appliquer", "Aplicar"),
    ("Comprendre", "Comprender"),
]


domains.append(word_pairs_mathematiques)

word_pairs_ingenierie = [
    ("Ingénieur", "Ingeniero"),
    ("Projet", "Proyecto"),
    ("Conception", "Diseño"),
    ("Technologie", "Tecnología"),
    ("Innovation", "Innovación"),
    ("Prototype", "Prototipo"),
    ("Matériau", "Material"),
    ("Mécanisme", "Mecanismo"),
    ("Test", "Prueba"),
    ("Structure", "Estructura"),
    ("Concevoir", "Diseñar"),
    ("Tester", "Probar"),
    ("Construire", "Construir"),
    ("Innover", "Innovar"),
    ("Développer", "Desarrollar"),
    ("Améliorer", "Mejorar"),
    ("Réparer", "Reparar"),
    ("Analyser", "Analizar"),
    ("Programmer", "Programar"),
    ("Évaluer", "Evaluar"),
]

domains.append(word_pairs_ingenierie)

word_pairs_environnement = [
    ("Environnement", "Medio ambiente"),
    ("Écologie", "Ecología"),
    ("Nature", "Naturaleza"),
    ("Pollution", "Contaminación"),
    ("Ressource", "Recurso"),
    ("Biodiversité", "Biodiversidad"),
    ("Énergie", "Energía"),
    ("Déchet", "Residuo"),
    ("Climat", "Clima"),
    ("Conservation", "Conservación"),
    ("Protéger", "Proteger"),
    ("Recycler", "Reciclar"),
    ("Préserver", "Preservar"),
    ("Polluer", "Contaminar"),
    ("Consommer", "Consumir"),
    ("Agir", "Actuar"),
    ("S'engager", "Comprometerse"),
    ("Sensibiliser", "Sensibilizar"),
    ("Économiser", "Ahorrar"),
    ("Observer", "Observar"),
]

domains.append(word_pairs_environnement)


#print(domains)






# Créer un paquet Anki

liste_decks=[]

for domain in domains:
    # domain contient un tableau avec les doublets de mots
    nom_domaine = [name for name, value in globals().items() if value is domain][0]
    nom_domaine = nom_domaine [11:]

    # on spécifie le nom du deck
    nom_domaine = f'vocabulario_{nom_domaine}'
    nom_package =f'{nom_domaine}.apkg'

    print(domain)
    print(nom_domaine)
    print(nom_package)

    #on crée le deck
    nombre_aleatoire = random.randint(10**9, (10**10)-1)
    print(nombre_aleatoire)
    deck = genanki.Deck(nombre_aleatoire
        ,
        nom_domaine)
    
    # Ajouter des cartes au deck, model est une variable global

    for word, translation in domain:
        note = genanki.Note(
            model=model,
            fields=[word, translation])
        deck.add_note(note)

 
    # créer le package

    
    genanki.Package(deck).write_to_file(nom_package)

    print(f'Paquet Anki {nom_package} créé avec succès.')

"""
    domain = 
    deck = genanki.Deck(
        
        2059400110,
        'cuerpo y ropa vocabulario')

# Ajouter des cartes au paquet

for domain in domains:
    for word, translation in domain:
        note = genanki.Note(
            model=model,
            fields=[word, translation])
        deck.add_note(note)

# Créer le fichier du paquet Anki (.apkg)
genanki.Package(deck).write_to_file('Espagnol_.apkg')

print('Paquet Anki créé avec succès.')
"""



