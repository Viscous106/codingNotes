import cv2
import sys

img = cv2.imread("./docs/images/Tokyo_Pink.png")##Reads the image
cv2.imshow("Tokyo", img)##Displays the image in a window






k = cv2.waitKey(0)##Waits for a key press to close the window
while True:
    k=cv2.waitKey(0)##Waits for another key press
    if k == 27:##If the 'Esc' key is pressed
        break
    else:
        print(f"press ESC to exit.")

cv2.destroyAllWindows()##Closes all OpenCV windows
sys.exit()##Exits the program
