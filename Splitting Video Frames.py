import cv2

source_video = ''
save_directory = ''

frequency = 201

cap = cv2.VideoCapture(source_video)
frames = (cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("===Generating " + str(int(frames / frequency)) + " Frames===")

i, image = cap.read()
count = 0

while i:
    count += 1
    i, image = cap.read()

    if count % frequency == 0:
        cv2.imwrite(save_directory + 'Video Frames ' + str(count) + '.jpg', image)
        print("Frame " + str(count) + " out of " + str(frames) + str("(") + str((count / frames) * 100) + "%)")


print('Done. Saved to ' + save_directory)
