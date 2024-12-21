import cv2
import os
import time

def save_images(output_folder, capture_duration=10):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    fps = 30
    interval = 1 / fps  

    print("Press 'q' to quit early.")
    start_time = time.time()
    frame_count = 0

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > capture_duration:
            print("Capture duration completed.")
            break

        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        time.sleep(interval)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("User interrupted the capture.")
            break

    cap.release()
    cv2.destroyAllWindows()

    print(f"Saved {frame_count} images in '{output_folder}'.")

output_folder = "D:/ML project/American Sign Language/dataset/train/A"
capture_duration = 10

save_images(output_folder, capture_duration)