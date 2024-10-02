import cv2
import numpy as np
import hashlib

def captureentropy():
    cap = cv2.VideoCapture(0)  

    entropysource = []

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            # process video
            grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            entropysource.append(grayframe.tobytes())

            # Display video stream 
            cv2.imshow("Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass

    cap.release()
    cv2.destroyAllWindows()

    return b"".join(entropysource)

def generaterandomnumbers(entropy, num_numbers):
    random_numbers = []
    sha256 = hashlib.sha256(entropy)

    for _ in range(num_numbers):
        random_bytes = sha256.digest()
        sha256.update(sha256.digest())
        random_number = int.from_bytes(random_bytes, byteorder='big')
        random_numbers.append(random_number)

    return random_numbers
#usage
if __name__ == "__main__":
    entropy_data = captureentropy()
    random_numbers = generaterandomnumbers(entropy_data, num_numbers=10)
    print("Generated Random Numbers:", random_numbers)
