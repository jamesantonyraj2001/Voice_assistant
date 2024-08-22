import cv2
import numpy as np

def apply_thermal_vision_live():
    # Open a connection to the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply a colormap to simulate thermal vision
        thermal_frame = cv2.applyColorMap(grayscale_frame, cv2.COLORMAP_HOT)

        # Display the original and thermal frames
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Thermal Vision", thermal_frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Apply thermal vision effect to live video
    apply_thermal_vision_live()
