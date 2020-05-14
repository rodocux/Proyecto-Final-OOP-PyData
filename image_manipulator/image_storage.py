import cv2


class ImageStorage:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            return img
        else:
            print("formato no valido")
            return None

    @staticmethod
    def save_img(img, name_img):
        """Recibe una imagen y una ruta de guardado con el nombre, solo acepta .jpg o .png"""
        # Escribe la imagen en disco, si es que esta termina en .jpg o .png
        pos_point = name_img.find(".")
        if pos_point == -1:
            print("Nombre no valido")
        else:
            termination = name_img[pos_point:]
            if termination == ".jpg" or termination == ".png":
                cv2.imwrite(name_img, img)
            else:
                print("Nombre no valido")
        