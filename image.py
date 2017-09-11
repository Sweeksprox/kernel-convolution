from PIL import Image
from random import randint
import math

def Nearest_Neighbor(img_src):
	pixels_src = img_src.load()
	img_nearest = Image.new('LA', (img_src.size[0], img_src.size[1]), 'black')
	pixels_nearest = img_nearest.load()

	kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
	for i in range(1, img_src.size[0] - 1):
		for j in range(1, img_src.size[1] - 1):
			neighbor_total = 0
			neighbor_count = 0
			for x in range(-1, 2):
				for y in range(-1, 2):
					neighbor_total += pixels_src[i + x, j + y][0] * kernel[x][y]
					neighbor_count += 1 * kernel[x][y]
			neighbor_total = neighbor_total / neighbor_count
			pixels_nearest[i, j] = (int(neighbor_total), 255)

	return img_nearest

def Black_White(img_src):
	pixels_src = img_src.load()

	img_new = Image.new('LA', (img_src.size[0], img_src.size[1]), 'black')
	pixels_new = img_new.load()

	for i in range(img_src.size[0]):
		for j in range(img_src.size[1]):
			p = pixels_src[i, j][0]
			if p >= 40:
				pixels_new[i, j] = (255, 255)
			else:
				pixels_new[i, j] = (0, 255)
	return img_new

def Sobel_Edge(img_src):
	pixels_src = img_src.load()

	img_x = Image.new('LA', (img_src.size[0], img_src.size[1]), 'black')
	pixels_x = img_x.load()

	kernel_x = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
	kernel_y = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

	for i in range(1, img_src.size[0] - 1):
		for j in range(1, img_src.size[1] - 1):
			neighbor_total = 0
			neighbor_count = 0
			for x in range(-1, 2):
				for y in range(-1, 2):
					neighbor_total += pixels_src[i + x, j + y][0] * (kernel_x[y][x] + kernel_y[y][x])
					neighbor_count += 1 * (kernel_x[y][x] + kernel_y[y][x])
			if neighbor_count == 0: 
				neighbor_count = 1
			neighbor_total = neighbor_total
			pixels_x[i, j] = (int(neighbor_total), 255)
	return img_x

def Scale_Resolution(img_src, scale):
	pixels_src = img_src.load()

	width = math.floor(img_src.size[0]/scale)
	height = math.floor(img_src.size[1]/scale)
	img_new = Image.new('LA', (width, height), 'black')
	pixels_new = img_new.load()

	kernel = [[0 for n in range(scale * 2 + 2)] for m in range(scale * 2 + 2)]
	for i in range(-scale, scale + 1):
		for j in range(-scale, scale + 1):
			kernel[i][j] = i * j
	print(kernel)
	for i in range(0, width):
		for j in range(0, height):
			pixels_new[i, j] = pixels_src[i * scale, j * scale]
	img_new.show()


img_src = Image.open('road_0.jpg').convert('LA')
img_src.show()
#Scale_Resolution(img_src, 10)
#img_black_white = Black_White(img_src)
#img_black_white.show()
#img_nearest = Nearest_Neighbor(img_src)
#img_nearest.show()

img_sobel = Sobel_Edge(img_src)
img_sobel.show()
