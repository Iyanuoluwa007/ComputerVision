import cv2 
import numpy as np
import matplotlib.pyplot as plt


full = cv2.imread(r"C:\Users\okeiy\Downloads\Computer_Vision\Computer-Vision-with-Python\DATA\sammy.jpg")
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

face = cv2.imread(r"C:\Users\okeiy\Downloads\Computer_Vision\Computer-Vision-with-Python\DATA\sammy_face.jpg")
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    # Create a copy of the full image
    full_copy = full.copy()

    method = eval(m)
    
    # Template Mathching
    res = cv2.matchTemplate(full_copy, face, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    height, width, channels = face.shape

    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(full_copy, top_left,bottom_right,(255,0,0),10)

    # Plot and show the image
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Heatmap of template matching')
    
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detection of Template')
    # Title with the method usesd
    plt.suptitle(m)

    plt.show()

    print('\n')
    print('\n')