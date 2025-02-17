import qrcode
import cv2
try:
    from PIL import Image
except ImportError:
    print("Pillow (PIL) library is not installed. Please install it using 'pip install Pillow'")
    exit()

# Function to generate a QR code
def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

# Function to scan a QR code from an image
def scan_qr_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not open or find the image at '{image_path}'")
        return

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)

    if bbox is not None and len(bbox) > 0:
        for i in range(len(bbox)):
            bbox = bbox.astype(int)  # Convert to integer coordinates safely
            cv2.line(image, tuple(map(int, bbox[i][0])), tuple(map(int, bbox[(i + 1) % len(bbox)][0])), color=(255, 0, 0), thickness=2)

        cv2.imshow("QR Code", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if data:
        print(f"QR Code data: {data}")
    else:
        print("QR Code not detected or image is invalid.")

# Function to scan a QR code from a webcam
def scan_qr_webcam():
    cap = cv2.VideoCapture(0)  # Open the default camera
    detector = cv2.QRCodeDetector()

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam.")
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        # Check if bbox is valid and not empty
        if bbox is not None and len(bbox) > 0:
            bbox = bbox.astype(int)  # Convert to integer coordinates safely
            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(0, 255, 0), thickness=2)

        if data:
            print(f"QR Code data: {data}")
            break  # Exit the loop once a QR code is detected

        cv2.imshow("QR Code Scanner", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    choices = {
        "1": "Generate QR Code",
        "2": "Scan QR Code from Image",
        "3": "Scan QR Code from Webcam"
    }

    print("Options:")
    for key, value in choices.items():
        print(f"{key}: {value}")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter the data for QR Code: ")
        filename = input("Enter the filename to save QR Code (with .png extension): ")
        generate_qr(data, filename)

    elif choice == "2":
        image_path = input("Enter the image path to scan QR Code: ")
        scan_qr_image(image_path)

    elif choice == "3":
        scan_qr_webcam()
        
    else:
        print("Invalid choice!")