import feedparser
import requests
from bs4 import BeautifulSoup
import ssl

# Bypass SSL verification (temporal)
ssl._create_default_https_context = ssl._create_unverified_context

# Parsear el feed RSS
url = 'https://www.jotdown.es/feed/'
d = feedparser.parse(url)

# Verificar si el feed se cargó correctamente
if not d.bozo:  # `d.bozo` es False si el feed se cargó sin errores
    print("\nFeed cargado correctamente\n")
else:
    print(f"\nError al cargar el feed: {d.bozo_exception}\n")
    exit()

# Verificar si hay artículos en el feed
if len(d.entries) == 0:
    print("No se encontraron artículos en el feed.")
    exit()

# Acceder a los artículos dentro de la etiqueta <item> del feed
articles = {}
for i, entry in enumerate(d.entries):
    title = entry.title
    link = entry.link
    articles[i] = link  # Guardar el enlace de cada artículo
    print(f'{i}: {title}')  # Mostrar título del artículo

# Función para mostrar el contenido del artículo
def show_content(article_url):
    try:
        response = requests.get(article_url)
        response.raise_for_status()  # Verificar errores HTTP
        soup = BeautifulSoup(response.text, 'html.parser')
        search_content = soup.select_one(".entry-content")
        if search_content:
            print(search_content.get_text().strip())
        else:
            print("No se pudo extraer el contenido del artículo. Verifica el selector CSS.")
    except Exception as e:
        print(f"Error al obtener el artículo: {e}")

# Bucle principal
while True:
    try:
        art = int(input('\n¿Qué artículo quieres leer? (número): '))
        if art not in articles:
            print("Índice fuera de rango. Intenta de nuevo.")
            continue
        show_content(articles[art])
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    x = input('¿Leer otro? (y/n): ').strip().lower()
    if x != 'y':
        print("¡Adiós!")
        break
