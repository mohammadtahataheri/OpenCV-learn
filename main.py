import cv2
import numpy as np


cap = cv2.VideoCapture(0)


templates = [
    "images.png",
    "images (1).png",
    "Free_parking_sign_cropped.jpg",
    "Pasted image.png",
    "download.jpeg",
    "download1.jpeg",
    "download2.jpeg",
    "download3.jpeg",
    "download4.jpeg",
    "OIP-2000455660.jpg",
    "OIP-2051233341.jpg",
]


theeshhold = 0.55

while True:

    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for template_path in templates:

        img_template = cv2.imread(template_path, 0)
        if img_template is None:
            print(template_path)
            continue

        h, w = img_template.shape

        if h > frame_gray.shape[0] or w > frame_gray.shape[1]:
            continue

        res = cv2.matchTemplate(frame_gray, img_template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= theeshhold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imshow("park", frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
