import cv2
import numpy as np
import time






def run_park():

    cv2.setUseOptimized(True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera is not available!")
        return
    prev_time = time.time()
    fps = 0


    template_paths = [
        "./src/images.png",
        "./src/images (1).png",
        "./src/Free_parking_sign_cropped.jpg",
        "./src/Pasted image.png",
        "./src/download.jpeg",
        "./src/download1.jpeg",
        "./src/download2.jpeg",
        "./src/download3.jpeg",
        "./src/download4.jpeg",
        "./src/OIP-2000455660.jpg",
        "./src/OIP-2051233341.jpg",
    ]


    theeshhold = 0.55

    templates = []

    for path in template_paths:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            templates.append(img)

    while True:

        ret, frame = cap.read()
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time    

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for img_template in templates:

            if img_template is None:
                print(img_template)
                continue

            h, w = img_template.shape

            if h > frame_gray.shape[0] or w > frame_gray.shape[1]:
                continue

            res = cv2.matchTemplate(frame_gray, img_template, cv2.TM_CCOEFF_NORMED)

            loc = np.where(res >= theeshhold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                cv2.putText(frame, 'Here is parking!',(225,300),font,1.5,(255,0,0),1)



        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        cv2.imshow("park", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



