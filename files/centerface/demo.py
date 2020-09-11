import cv2
import matplotlib.pyplot as plt

import centerface



def draw():
    im = cv2.imread(input)
    det, lms = centerface.detect(im)[0]
    cv2.rectangle(im, (int(det[0]), int(det[1])), (int(det[2]), int(det[3])), (0, 255, 0), thickness=2)
    for i in range(0, len(lms), 2):
        x = lms[i]
        y = lms[i+1]
        cv2.circle(im, (x, y), 2, (255, 0, 0), thickness=2)
    cv2.imshow("demo", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def align():
    input = 'my.png'
    res = centerface.align(input)
    cv2.imshow("demo", res[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    align()