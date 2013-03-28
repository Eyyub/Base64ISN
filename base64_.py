def initialize(pixels, pixels2, (w, h)):
  """Initialise la nouvelle matrice de pixel""" #C'est juste une copie qui ne perd pas la reference
	for y in range(h):
		for x in range(w):
			pixels2[x, y] = pixels[x, y]
	return pixels2

def miroir(pixels, pixels2, (w, h)):
	"""Miroir, symetrie verticale"""
	for y in range(h):
		for x in range(w):
			pixels2[x, y] = pixels[w-x-1, y]
	return pixels2

def reverse(pixels, pixels2, (w, h)):
	"""Renversement de l'image, rotation a 180 degres"""
	for y in range(h):
		for x in range(w):
			pixels2[x, y] = pixels[x, h-y-1]
	return pixels2

def neg(pixels, pixels2, (w, h)):
	"""Negatif de l'image"""
	r, g, b = 0, 0, 0 #Pour eviter l'allocation des variables a chaque boucles

	for y in range(h):
		for x in range(w):
			r, g, b = pixels[x, y]
			pixels2[x, y] = (255-r, 255-g, 255-b)
	return pixels2

def seuillage(pixels, pixels2, (w, h), seuil=60):
	pixel = 0 #Pour eviter l'allocation de la variable a chaque boucles
	
	for y in range(h):
		for x in range(w):
			if pixels[x, y] >= (seuil, seuil, seuil):
				pixel = 255
			pixels2[x, y] = (pixel, pixel, pixel)
			pixel = 0
	return pixels2

def gris(r, g, b):
	return (r*299 + g*587 + b*114)/1000

def to_gris(pixels, pixels2, (w, h)):
	r, g, b = 0, 0, 0 #Pour eviter l'allocation des variables a chaque boucles
	for y in range(h):
		for x in range(w):
			r, g, b = pixels[x, y]
			pixels2[x, y] = (gris(r, g, b), gris(r, g, b), gris(r, g, b))
	return pixels2
