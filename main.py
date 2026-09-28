from ultralytics import YOLO
import cv2
import os

# Load YOLO model
model = YOLO("yolo11n.pt")

# Choose input
# 0 = webcam
# "sample/test.jpg" = image
# "sample/video.mp4" = video
SOURCE = "sample/bicycle.jpg"


def detect_image(source):
    results = model(source)

    for result in results:
        annotated_frame = result.plot()

        cv2.imshow("YOLO Object Detection", annotated_frame)

        # Save output
        output_path = "output.jpg"
        cv2.imwrite(output_path, annotated_frame)

        print("\nDetection Results:")
        print("-" * 40)

        if result.boxes is not None:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]

                print(
                    f"Object: {class_name:<15} "
                    f"Confidence: {confidence:.2f}"
                )

        print("-" * 40)
        print(f"Output saved as: {output_path}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam started.")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to read frame.")
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        cv2.imshow(
            "YOLO Real-Time Object Detection",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def detect_video(source):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        cv2.imshow(
            "YOLO Video Object Detection",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# -------------------------------
# Main Program
# -------------------------------

if SOURCE == 0:
    detect_webcam()

elif SOURCE.lower().endswith(
    (".jpg", ".jpeg", ".png", ".bmp")
):
    detect_image(SOURCE)

elif SOURCE.lower().endswith(
    (".mp4", ".avi", ".mov", ".mkv")
):
    detect_video(SOURCE)

else:
    print("Invalid source.")