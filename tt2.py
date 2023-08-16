import cv2

input_file = "ankara messi chiquito (1).mp4"
cap = cv2.VideoCapture(input_file)
fps = cap.get(cv2.CAP_PROP_FPS)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame_counter = total_frames - 1

check , vid = cap.read()
counter = 0
check = True
frame_list = []
while(check == True):
    cv2.imwrite("frame%d.jpg" %counter , vid)
    check , vid = cap.read()
    frame_list.append(vid)

    counter += 1

frame_list.pop()
frame_list.reverse()
  
for frame in frame_list:
    if frame_counter % 2 == 0:
       cv2.imshow("Slow Motion Video", frame)
       if cv2.waitKey(int(1000 / (fps / 2))) & 0xFF == 27:  # Press ESC to exit
          break
    frame_counter = frame_counter - 1
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break
