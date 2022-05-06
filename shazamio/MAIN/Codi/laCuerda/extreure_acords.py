from bs4 import BeautifulSoup
from normalitzar_lacuerda import normalitzar_lacuerda

song = 'Hasta la raíz'
artist = 'Natalia Lafourcade'
url = normalitzar_lacuerda(song, artist)
url_soup = url[8:]+'.html'

soup = BeautifulSoup(open(url_soup), features="lmxl")

print(soup.prettify())
