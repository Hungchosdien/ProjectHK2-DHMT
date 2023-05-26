import cv2
import pytesseract
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog

def recognize_text(image_path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Đọc hình ảnh đầu vào
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Nhận dạng văn bản trên hình ảnh
    data = pytesseract.image_to_string(img, lang="vie")

    return data

def save_result_to_file(test4, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(test4)

class OCRWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng OCR")
        self.setGeometry(100, 100, 600, 300)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 500, 100)


        self.button = QPushButton("Chọn ảnh", self)
        self.button.setGeometry(200, 200, 100, 30)
        self.button.clicked.connect(self.select_image)

    def select_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileNames(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg)")
        if image_path:
            text = recognize_text(image_path[0])  # Chỉ lấy đường dẫn đầu tiên
            self.label.setText(text)
            output_file = "SCAN.txt"
            save_result_to_file(text, output_file)

if __name__ == "__main__":
    app = QApplication([])
    window = OCRWindow()
    window.show()
    app.exec_()
