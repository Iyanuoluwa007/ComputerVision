import cv2

img = cv2.imread('C:/Users/okeiy/Downloads/Computer_Vision/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy',img)
    # If waited for 1ms and Esc key is pressed or letter q (or ord('q'))
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cv2.destroyAllWindows()