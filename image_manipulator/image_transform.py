import cv2

class ImageTransform:

	@classmethod
	def gray_scale(self,img):
		"""Convierte una imagen en color a uma imagen en blanco y negro"""
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return gray_img


	@classmethod
	def hsv(self, img):
		"""Convierte una imagen en color a una imagen HSV"""
		hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		return hsv_img