from PIL import Image

if __name__ == '__main__':

	try:
		wallpaper = Image.open('images/wallpaper.jpg')
		wp = wallpaper.crop(
			(2500, 1500, 3400, 2180) # LURB
		)
		wp.save('images/wp.jpg')
	except FileNotFoundError as e:
		print('No es posible obtener la imagen.')