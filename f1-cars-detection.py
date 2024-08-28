# --------------- F1 Cars Detection -------------------
from ultralytics import YOLO
import cv2
import pandas as pd


video = cv2.VideoCapture(r'C:\Users\osama\OneDrive\Desktop\Moahmmed Upwork\-THROUGH GOES HAMILTON!- #Shorts.mp4')
model = YOLO(r'C:\Users\osama\Downloads\detection f1 cars.pt')
class_list = {0: 'Ferrari', 1: 'Mclaren', 2: 'Mercedes', 3: 'Redbull'}

person_axis = []
count = 0

while True:
    _, image = video.read()
    image_copy = image.copy()
    h, w, c = image.shape

    image = cv2.flip(image, 1)
    result = model.predict(image)

    a = result[0].boxes.data
    px = pd.DataFrame(a).astype(float)

    for index, row in px.iterrows():
        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
        cls = class_list[int(row[5])]
        confidence = row[4]


        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 165, 255), 2)
        cv2.rectangle(image, (x1, y1 - 25), (x1 + 200, y1), (0, 165, 255), -1)

        cv2.putText(image, f'id:{index}', (x1, y1 - 10), cv2.FONT_ITALIC, 0.7,
                    (0, 0, 0), 1)
        cv2.putText(image, f'{cls}', (x1+55, y1 - 10), cv2.FONT_ITALIC, 0.7,
                    (0, 0, 0), 1)
        cv2.putText(image, f'{round(confidence, 2)}', (x1 + 150, y1 - 10), cv2.FONT_ITALIC, 0.7,
                    (0, 0, 0), 1)


    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('o'):
        break

cv2.destroyAllWindows()
video.release()
