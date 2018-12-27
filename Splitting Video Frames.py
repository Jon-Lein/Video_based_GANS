import cv2

source_video = 'SampleVideo.mp4'
save_directory = 'C:\\Users\\User\\Desktop\\Video Frames\\'

cap = cv2.VideoCapture(source_video)

i, image = cap.read()
count = 0

while i:
    cv2.imwrite(save_directory + 'Video Frames '+ str(count) + '.jpg', image)
    count += 1
    i, image = cap.read()

print('Total Frames: ' + str(count))
