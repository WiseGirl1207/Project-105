import os
import cv2

images = []
path="Images"

for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name=path+"/"+file
        print(file_name)
        images.append(file_name)
count=len(images)

frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
out=cv2.VideoWriter("project.mp4",cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),0.8, size)
for i in range(0, count-1):
    frames=cv2.imread(images[i])
    out.write(frames)

out.release()
print("Done!")
