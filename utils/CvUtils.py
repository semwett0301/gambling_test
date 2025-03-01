import cv2
from pytesseract import pytesseract


class CvUtils:
    @staticmethod
    def extract_text(img_src) -> str:
        img = cv2.imread(img_src)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        text = pytesseract.image_to_string(thresh)

        return text.lower()
