import cv2
import sys

'''
#Reading and displaying images
img = cv2.imread("./docs/images/Tokyo_Pink.png")##Reads the image
cv2.imshow("Tokyo", img)##Displays the image in a window
'''

'''
#Reading and displaying Videos
#x = "./docs/Videos/My_girl.mp4"#video path
#x = 0 ##For webcam input1st webcam 1 for 2nd and so on

vdo = cv2.VideoCapture(x)

try:
    while True:
        isTrue, frame = vdo.read()##Reads the video frame by frame
        cv2.imshow("Video", frame)#(name,vdo)##Displays the video frames in a window
        cv2.waitKey(5)##Waits for 5 milliseconds before moving to the next frame

except Exception as e:
    print(f"Error: {e}")

finally:
    vdo.release()##Releases the video capture object
'''









####TO stop the program execution and close the window when a key is pressed####

while True:
    k=cv2.waitKey(0)##Waits for another key press
    if k == 27:##If the 'Esc' key is pressed
        break
    else:
        print(f"press ESC to exit.")
cv2.destroyAllWindows()##Closes all OpenCV windows
sys.exit()##Exits the program
