import cv2
from image_manipulator.image_storage import ImageStorage
from image_manipulator.image_transform import *


if __name__ == '__main__':
    img = ImageStorage.read_image("images/profile.jpg")
    
    img_gray = ImageColor.gray_scale(img)
    ImageStorage.save_img(img=img_gray, name_img="images/profile_gray.jpg")

    img_hsv = ImageColor.hsv(img)
    ImageStorage.save_img(img=img_hsv, name_img="images/profile_hsv.jpg")

    image_50 = ImageTransform.resize(img, 50)
    ImageStorage.save_img(img = image_50, name_img="images/profile_50.jpg")

    image_tras = ImageTransform.traslation(img, 200, 150)
    ImageStorage.save_img(img = image_tras, name_img="images/profile_tras.jpg")

    image_rot = ImageTransform.rotation(img, 45)
    ImageStorage.save_img(img = image_rot, name_img="images/profile_rot.jpg")

    print("All transformations done")