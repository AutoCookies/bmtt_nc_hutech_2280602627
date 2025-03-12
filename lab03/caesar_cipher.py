import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.caesar import Ui_MainWindow  # Fixed the typo here

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()  # Fixed the typo
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/ceasar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()  # Use toPlainText() here
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print(data)
                self.ui.txt_ciphertext.setPlainText(data["encrypted_message"])  # Use setPlainText() here
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")  # Fixed the error message formatting

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/ceasar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),  # Fixed typo in txt_ciphertext
            "key": self.ui.txt_key.toPlainText()  # Use toPlainText() here
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print(data)
                self.ui.txt_plaintext.setPlainText(data["decrypted_message"])  # Use setPlainText() here
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")  # Fixed the error message formatting

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
