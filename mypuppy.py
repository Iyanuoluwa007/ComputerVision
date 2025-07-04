import cv2

img = cv2.imread('C:/Users/okeiy/Downloads/Computer_Vision/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy',img)
    
    # If we've waited at least 1 ms AND we've pressed the Esc or use can use any letter ord('any letter') i.e ord('q') 
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()