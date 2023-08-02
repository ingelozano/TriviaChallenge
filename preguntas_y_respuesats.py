#Importamos el modulo random para hacer uso de funciones relacionadas con numeros aleatoreos
import random
#Definimos un diccionario llamado preguntas, donde cada pregunta esta asociada a una categoria y dentro de cada categoria
#hay una lista de preguntas, donde cada pregunta es un diccionario que contiene la pregunta en si, las opciones de respuesta
#las respuestas correctas y los puntos que vale la pregunta.
preguntas = {
    'Deportes': [
        {
            'pregunta': '¿En qué deporte se utiliza un bate y una pelota?',
            'opciones': ['Fútbol', 'Béisbol', 'Baloncesto', 'Tenis'],
            'respuesta': 'Béisbol',
            'puntos': 5
        },
        {
            'pregunta': '¿Cuál es el deporte más popular en Estados Unidos?',
            'opciones': ['Fútbol', 'Béisbol', 'Baloncesto', 'Hockey'],
            'respuesta': 'Fútbol',
            'puntos': 6
        },
        {
            'pregunta': '¿En qué deporte se puede hacer un "birdie"?',
            'opciones': ['Golf', 'Tenis', 'Voleibol', 'Rugby'],
            'respuesta': 'Golf',
            'puntos': 4
        },
        {
            'pregunta': '¿Quién es considerado el mejor jugador de baloncesto de todos los tiempos?',
            'opciones': ['Michael Jordan', 'LeBron James', 'Kobe Bryant', 'Magic Johnson'],
            'respuesta': 'Michael Jordan',
            'puntos': 7
        },
        {
            'pregunta': '¿Qué país ganó la Copa Mundial de la FIFA 2018?',
            'opciones': ['Brasil', 'Alemania', 'Francia', 'Argentina'],
            'respuesta': 'Francia',
            'puntos': 5
        },
        {
            'pregunta': '¿En qué ciudad se celebraron los Juegos Olímpicos de Verano en 2016?',
            'opciones': ['Londres', 'Pekín', 'Río de Janeiro', 'Tokio'],
            'respuesta': 'Río de Janeiro',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el equipo de fútbol más laureado de España?',
            'opciones': ['Barcelona', 'Real Madrid', 'Atlético de Madrid', 'Valencia'],
            'respuesta': 'Real Madrid',
            'puntos': 5
        },
        {
            'pregunta': '¿Cuál es el país de origen del tenista Rafael Nadal?',
            'opciones': ['España', 'Argentina', 'Francia', 'Suiza'],
            'respuesta': 'España',
            'puntos': 4
        },
        {
            'pregunta': '¿En qué deporte se destaca Usain Bolt como uno de los mejores atletas?',
            'opciones': ['Natación', 'Atletismo', 'Ciclismo', 'Gimnasia'],
            'respuesta': 'Atletismo',
            'puntos': 7
        },
        {
            'pregunta': '¿Cuál es el país de origen del piloto de Fórmula 1 Lewis Hamilton?',
            'opciones': ['Reino Unido', 'Estados Unidos', 'Alemania', 'Brasil'],
            'respuesta': 'Reino Unido',
            'puntos': 6
        },
    ],
    'Ciencia': [
        {
            'pregunta': '¿Cuál es el símbolo químico del oro?',
            'opciones': ['Au', 'Ag', 'Fe', 'Cu'],
            'respuesta': 'Au',
            'puntos': 5
        },
        {
            'pregunta': '¿Cuál es el planeta más grande del Sistema Solar?',
            'opciones': ['Tierra', 'Júpiter', 'Saturno', 'Marte'],
            'respuesta': 'Júpiter',
            'puntos': 7
        },
        {
            'pregunta': '¿Qué tipo de animal es el delfín?',
            'opciones': ['Pez', 'Mamífero', 'Ave', 'Reptil'],
            'respuesta': 'Mamífero',
            'puntos': 6
        },
        {
            'pregunta': '¿Qué científico propuso la famosa ecuación E=mc^2?',
            'opciones': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Charles Darwin'],
            'respuesta': 'Albert Einstein',
            'puntos': 8
        },
        {
            'pregunta': '¿Cuál es la principal función del ADN en los seres vivos?',
            'opciones': ['Respiración', 'Digestión', 'Reproducción', 'Crecimiento'],
            'respuesta': 'Reproducción',
            'puntos': 5
        },
        {
            'pregunta': '¿Cuál es el elemento químico más abundante en el Universo?',
            'opciones': ['Hidrógeno', 'Oxígeno', 'Helio', 'Carbono'],
            'respuesta': 'Hidrógeno',
            'puntos': 7
        },
        {
            'pregunta': '¿Qué animal fue el primero en viajar al espacio exterior?',
            'opciones': ['Perro', 'Mono', 'Gato', 'Ratón'],
            'respuesta': 'Perro',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es la capa más externa de la Tierra?',
            'opciones': ['Núcleo', 'Manto', 'Corteza', 'Núcleo externo'],
            'respuesta': 'Corteza',
            'puntos': 4
        },
        {
            'pregunta': '¿Cuál es el elemento químico más pesado?',
            'opciones': ['Uranio', 'Plutonio', 'Oro', 'Mercurio'],
            'respuesta': 'Plutonio',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el planeta más cercano al Sol?',
            'opciones': ['Venus', 'Mercurio', 'Marte', 'Júpiter'],
            'respuesta': 'Mercurio',
            'puntos': 5
        },
    ],
    'Astronomía': [
        {
            'pregunta': '¿Cuál es el nombre de nuestra galaxia?',
            'opciones': ['Andrómeda', 'Vía Láctea', 'Sombrero', 'Elíptica'],
            'respuesta': 'Vía Láctea',
            'puntos': 7
        },
        {
            'pregunta': '¿Cuál es el nombre del telescopio espacial lanzado por la NASA en 1990?',
            'opciones': ['Hubble', 'Kepler', 'Galileo', 'Chandra'],
            'respuesta': 'Hubble',
            'puntos': 9
        },
        {
            'pregunta': '¿Cuál es el nombre del primer ser humano en viajar al espacio?',
            'opciones': ['Neil Armstrong', 'Yuri Gagarin', 'Buzz Aldrin', 'Alan Shepard'],
            'respuesta': 'Yuri Gagarin',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el nombre de la luna más grande de Júpiter?',
            'opciones': ['Io', 'Europa', 'Ganímedes', 'Calisto'],
            'respuesta': 'Ganímedes',
            'puntos': 8
        },
        {
            'pregunta': '¿Cuál es el nombre del planeta conocido como el "planeta rojo"?',
            'opciones': ['Júpiter', 'Venus', 'Marte', 'Mercurio'],
            'respuesta': 'Marte',
            'puntos': 7
        },
        {
            'pregunta': '¿Qué astro es conocido como "la estrella del Norte"?',
            'opciones': ['Venus', 'Júpiter', 'Sirio', 'Polaris'],
            'respuesta': 'Polaris',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el nombre del primer telescopio espacial lanzado al espacio?',
            'opciones': ['Hubble', 'Kepler', 'Galileo', 'Chandra'],
            'respuesta': 'Hubble',
            'puntos': 8
        },
        {
            'pregunta': '¿Cuál es el nombre de la agencia espacial estadounidense?',
            'opciones': ['ESA', 'NASA', 'ISRO', 'Roscosmos'],
            'respuesta': 'NASA',
            'puntos': 5
        },
        {
            'pregunta': '¿Qué planeta es conocido como "el gigante helado"?',
            'opciones': ['Neptuno', 'Urano', 'Saturno', 'Júpiter'],
            'respuesta': 'Neptuno',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el nombre del primer satélite artificial lanzado al espacio?',
            'opciones': ['Sputnik 1', 'Explorer 1', 'Vanguard 1', 'Luna 2'],
            'respuesta': 'Sputnik 1',
            'puntos': 7
        },
    ],
    'Cultura General': [
        {
            'pregunta': '¿Cuál es la capital de Italia?',
            'opciones': ['Roma', 'París', 'Madrid', 'Londres'],
            'respuesta': 'Roma',
            'puntos': 5
        },
        {
            'pregunta': '¿En qué país se encuentra la Torre Eiffel?',
            'opciones': ['Francia', 'Italia', 'Alemania', 'España'],
            'respuesta': 'Francia',
            'puntos': 4
        },
        {
         
            'pregunta': '¿Quién escribió la obra literaria "Don Quijote de la Mancha"?',
            'opciones': ['Miguel de Cervantes', 'William Shakespeare', 'Gabriel García Márquez', 'Jorge Luis Borges'],
            'respuesta': 'Miguel de Cervantes',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el río más largo del mundo?',
            'opciones': ['Amazonas', 'Nilo', 'Misisipi', 'Yangtsé'],
            'respuesta': 'Amazonas',
            'puntos': 7
        },
        {
            'pregunta': '¿En qué país se encuentra la Gran Muralla China?',
            'opciones': ['Japón', 'China', 'India', 'Corea del Sur'],
            'respuesta': 'China',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el nombre del famoso cuadro pintado por Leonardo da Vinci que se encuentra en el Museo del Louvre?',
            'opciones': ['La última cena', 'El Grito', 'La Gioconda', 'La noche estrellada'],
            'respuesta': 'La Gioconda',
            'puntos': 8
        },
        {
            'pregunta': '¿En qué país se encuentra el Taj Mahal?',
            'opciones': ['India', 'Egipto', 'Turquía', 'México'],
            'respuesta': 'India',
            'puntos': 7
        },
        {
            'pregunta': '¿Cuál es el océano más grande del mundo?',
            'opciones': ['Atlántico', 'Pacífico', 'Índico', 'Ártico'],
            'respuesta': 'Pacífico',
            'puntos': 5
        },
        {
            'pregunta': '¿En qué continente se encuentra el desierto del Sahara?',
            'opciones': ['África', 'Asia', 'América del Norte', 'Europa'],
            'respuesta': 'África',
            'puntos': 6
        },
        {
            'pregunta': '¿Cuál es el monte más alto del mundo?',
            'opciones': ['Everest', 'Kilimanjaro', 'Aconcagua', 'Monte McKinley'],
            'respuesta': 'Everest',
            'puntos': 7
        },
    ],
}
#Colocamos la funcion de obtener_preguntas_y_respuestas para seleccionar una pregunta aleatoria disponible 
#en el diccionario de preguntas y luego las remueve para que no se repitan las preguntas en la misma partida
def obtener_pregunta_y_respuesta(preguntas_hechas):
    categoria = random.choice(list(preguntas.keys()))
    while len(preguntas[categoria]) == 0:
        categoria = random.choice(list(preguntas.keys()))
    pregunta_info = random.choice(preguntas[categoria])
    preguntas[categoria].remove(pregunta_info)
    pregunta = pregunta_info['pregunta']
    opciones = pregunta_info['opciones']
    respuesta_correcta = opciones.index(pregunta_info['respuesta']) + 1
    return categoria, pregunta, opciones, respuesta_correcta, pregunta_info['puntos']
#Colocamos la funcion jugar solicita el numero de participantes y sus nombres y despues hace un ciclo donde cada jugador
#tiene su turno en la partida iniciada
def jugar():
    print("Bienvenido al juego de preguntas y respuestas")
    num_jugadores = int(input("Ingresa el número de jugadores: "))
    jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Jugador {i + 1}, ingresa tu nombre: ")
        jugadores.append({'nombre': nombre, 'puntos': 0})
    
    while True:
        for jugador in jugadores:
            print(f"\nTurno de {jugador['nombre']}:")
            categoria, pregunta, opciones, respuesta_correcta, puntos = obtener_pregunta_y_respuesta(preguntas)
            print(f"Categoría: {categoria}")
            print(f"Pregunta: {pregunta}")
            for i, opcion in enumerate(opciones):
                print(f"{i + 1}. {opcion}")
            
            respuesta = int(input("Ingresa el número de la opción correcta: "))
            if respuesta == respuesta_correcta:
                jugador['puntos'] += puntos
                print("¡Respuesta correcta!")
            else:
                print("Respuesta incorrecta.")
                print(f"La respuesta correcta es la opción {respuesta_correcta}: {opciones[respuesta_correcta-1]}")
            
            print(f"Puntos de {jugador['nombre']}: {jugador['puntos']}")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            break

if __name__ == "__main__":
    jugar()