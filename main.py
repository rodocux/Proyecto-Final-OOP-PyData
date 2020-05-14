import cv2
from image_manipulator.image_storage import ImageStorage
from image_manipulator.image_transform import ImageTransform


if __name__ == '__main__':
    img = ImageStorage.read_image("images/profile.jpg")
    
    img_gray = ImageTransform.gray_scale(img)
    ImageStorage.save_img(img=img_gray, name_img="images/profile_gray.jpg")

    img_hsv = ImageTransform.hsv(img)
    ImageStorage.save_img(img=img_hsv, name_img="images/profile_hsv.jpg")