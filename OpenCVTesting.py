import cv2

# Connecting to Laptop Camera
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Wndows *DIVX or Linux *XVID
writer = cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height)) # 20 fps 

while True:
    ret,frame = cap.read()

    # Operations (Drawing)
    writer.write(frame)
    
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow('frame',frame) #frame or gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
