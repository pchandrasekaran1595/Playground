import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from Ant import Ant

def app():
    args_1 = "--width"
    args_2 = "--height"
    args_3 = "--speed"
    args_4 = "--animate"

    w, h = 640, 360
    speed = 100
    animate = False

    if args_1 in sys.argv:
        w = int(sys.argv[sys.argv.index(args_1) + 1])
    if args_2 in sys.argv:
        h = int(sys.argv[sys.argv.index(args_2) + 1])
    if args_3 in sys.argv:
        speed = int(sys.argv[sys.argv.index(args_3) + 1])
    if args_4 in sys.argv:
        animate = True
    
    frame = (np.ones((h, w)) * 255).astype("uint8")
    A = Ant(int(w/2), int(h/2), w, h)

    if animate:
        while True:
            for _ in range(speed):
                frame = A.update(frame, animate)
            cv2.imshow("Feed", frame)
            if cv2.waitKey(1) == ord("q"):
                break
    else:
        frame = A.update(frame)

        plt.figure("Langton's Ant after 11000 Steps")
        plt.imshow(frame, cmap="gray")
        plt.axis("off")
        plt.show()

    cv2.destroyAllWindows()
