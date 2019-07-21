import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
Width = int(cap.get(3))
Height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter('output.avi',fourcc, 30, (Width,Height))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

video_path = "output.avi"
cap = cv2.VideoCapture(video_path)

num = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite("picture{:0=3}".format(num)+".jpg",frame)
        print("save picture{:0=3}".format(num)+".jpg")
        num += 1
    else:
        break

cap.release()

num=0
x = []
list = []
for i in range(186):
 img = cv2.imread("picture{:0=3}".format(num)+".jpg")
 mean = np.mean(img)
 list.append(mean)
 x.append(num/20)
 num += 1


plt.plot(x,list)
plt.ylabel('luminance')
plt.xlabel('second')
plt.show()
