import cv2
import os
from ultralytics import YOLO

# Load a custom trained model
model = YOLO('D:/Progetto/Progetto finale Sysag/train43/weights/best.pt')

# Path to the folder containing images
image_folder = 'C:/Users/gmrut/Desktop/Imgs'

# Iterate over images in the folder
for image_filename in os.listdir(image_folder):
    if image_filename.endswith(('.jpg', '.png', '.jpeg')):
        image_path = os.path.join(image_folder, image_filename)

        # Run inference on the image
        results = model([image_path])

        # Load the image
        img = cv2.imread(image_path)

        # Process results list
        for result in results:
            for value, box in zip(result.boxes.cls, result.boxes.xywh):
                x, y, width, height = box.tolist()

                if value.item() == 1.:
                    # Start blur
                    blur_x = int(x - width / 2)
                    blur_y = int(y - height / 2)
                    blur_width = int(width)
                    blur_height = int(height)

                    roi = img[blur_y:blur_y + blur_height, blur_x:blur_x + blur_width]
                    blur_image = cv2.GaussianBlur(roi, (51, 51), 0)

                    img[blur_y:blur_y + blur_height, blur_x:blur_x + blur_width] = blur_image
                else:
                    # Draw bounding box
                    top_left = (int(x - width / 2), int(y - height / 2))
                    bottom_right = (int(x + width / 2), int(y + height / 2))
                    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        # Save the modified image
        output_image_path = os.path.join('output_folder', f'processed_{image_filename}')
        cv2.imwrite(output_image_path, img)