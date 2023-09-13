import cv2
from ultralytics import YOLO
import sys


class ImageProcessor:
    #
    def __init__(self, model_path, image_path):
        self.model = YOLO(model_path)
        self.image_path = image_path

    def pklot_busy(self):
        # Run batched inference on a list of images
        results = self.model([self.image_path])

        # Load the image
        img = cv2.imread(self.image_path)

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

        cv2.imwrite("example_with_blur.jpg", img)

    def pklot_free(self):
        # Run batched inference on a list of images
        results = self.model([self.image_path])

        # Load the image
        img = cv2.imread(self.image_path)

        # Process results list
        for result in results:
            for value, box in zip(result.boxes.cls, result.boxes.xywh):
                x, y, width, height = box.tolist()

                if value.item() == 0.:
                    # Draw bounding box
                    top_left = (int(x - width / 2), int(y - height / 2))
                    bottom_right = (int(x + width / 2), int(y + height / 2))
                    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        cv2.imwrite("example_with_blur.jpg", img)

    def pklot_total(self):
        # Run batched inference on a list of images
        results = self.model([self.image_path])

        # Load the image
        img = cv2.imread(self.image_path)

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

        cv2.imwrite("example_with_blur.jpg", img)

    def pklot_count(self):
        # Run batched inference on a list of images
        results = self.model([self.image_path])
        counter = 0
        # Process results list
        for result in results:
            for value, box in zip(result.boxes.cls, result.boxes.xywh):

                if value.item() == 0.:
                    counter = counter + 1

        return counter


if __name__ == "__main__":
    model_path = 'best.pt'
    image_path = sys.path[0] + '/dataset/test/images/2012-09-12_10_05_57_jpg.rf.5f9542ab6498fd436eef35d5ac8f5c04.jpg'

    processor = ImageProcessor(model_path, image_path)
