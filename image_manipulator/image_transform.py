import cv2
import numpy as np

class ImageColor:

	@classmethod
	def gray_scale(cls,img):
		"""Convierte una imagen en color a uma imagen en blanco y negro"""
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return gray_img


	@classmethod
	def hsv(cls, img):
		"""Convierte una imagen en color a una imagen HSV"""
		hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		return hsv_img


class ImageTransform:

	@classmethod
	def resize(cls, img, percent_size):
		"""Redimensiona una imagen al porcentaje dado"""
		new_width = int(img.shape[1] * percent_size / 100)
		new_height = int(img.shape[0] * percent_size / 100)
		new_dimension = (new_width, new_height)
		resize_img = cv2.resize(img, new_dimension, interpolation = cv2.INTER_AREA)
		return resize_img

	@classmethod
	def traslation(cls, img, new_x, new_y):
		"""Realiza una traslacion de una imagen a las nuevas coordenadas
		x e y"""
		rows,cols = img.shape[0:2]
		matrix = np.float32([[1,0,new_x],[0,1,new_y]])
		tras_img = cv2.warpAffine(img,matrix,(cols,rows))
		return tras_img

	@classmethod
	def rotation(cls, img, grades):
		"""Realiza una rotacion de una imagen cierta cantidad de grados"""
		rows,cols = img.shape[0:2]
		M = cv2.getRotationMatrix2D((cols/2,rows/2),grades,1)
		rotate_img = cv2.warpAffine(img, M, (cols,rows))
		return rotate_img