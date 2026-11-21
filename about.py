from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt
from pathlib import Path
import webbrowser

class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Nof")
        self.setFixedSize(480, 520)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #111827, stop:1 #312e81
                );
                color: #f8fafc;
                font-family: "Segoe UI";
            }
            QLabel.card {
                background-color: rgba(255, 255, 255, 25);
                border: 1px solid rgba(255, 255, 255, 40);
                border-radius: 18px;
            }
            QLabel.title {
                color: #ffffff;
                font-size: 28px;
                font-weight: 700;
                border: none;
                background: transparent;
            }
            QLabel.subtitle {
                color: #c7d2fe;
                font-size: 14px;
                border: none;
                background: transparent;
            }
            QPushButton {
                border: none;
                border-radius: 12px;
                padding: 10px;
                font-size: 13px;
                font-weight: 700;
            }
            QPushButton:hover {
                border: 2px solid rgba(255, 255, 255, 180);
            }
            QPushButton:pressed {
                padding-top: 12px;
                padding-bottom: 8px;
            }
        """)

        self.profile_card = QLabel(self)
        self.profile_card.setGeometry(28, 28, 424, 464)
        self.profile_card.setProperty("class", "card")

        self.my_name = QLabel("Nof Safiae", self)
        self.my_name.setGeometry(58, 58, 360, 40)
        self.my_name.setAlignment(Qt.AlignCenter)
        self.my_name.setProperty("class", "title")

        self.my_email = QLabel("nofsafiah@gmail.com", self)
        self.my_email.setGeometry(58, 100, 360, 28)
        self.my_email.setAlignment(Qt.AlignCenter)
        self.my_email.setProperty("class", "subtitle")

        self.image_manu = QLabel(self)
        self.image_manu.setGeometry(165, 150, 150, 150)
        self.image_manu.setAlignment(Qt.AlignCenter)
        self.image_manu.setStyleSheet("""
            background-color: rgba(255, 255, 255, 18);
            border: 2px solid rgba(255, 255, 255, 70);
            border-radius: 75px;
        """)
        self.image_manu.setVisible(False)

        self.btn_football = QPushButton("My football team", self)
        self.btn_football.setGeometry(58, 320, 364, 44)
        self.btn_football.setStyleSheet("""
            background-color: #dc2626;
            color: white;
        """)
        self.btn_football.clicked.connect(self.open_manu)

        self.btn_linkedin = QPushButton("LinkedIn", self)
        self.btn_linkedin.setGeometry(58, 378, 172, 44)
        self.btn_linkedin.setStyleSheet("""
            background-color: #2563eb;
            color: white;
        """)
        self.btn_linkedin.clicked.connect(self.open_linkedin)

        self.btn_github = QPushButton("GitHub", self)
        self.btn_github.setGeometry(250, 378, 172, 44)
        self.btn_github.setStyleSheet("""
            background-color: #111827;
            color: white;
        """)
        self.btn_github.clicked.connect(self.open_github)

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/nof-safiae/")

    def open_github(self):
        webbrowser.open("https://github.com/nofsafiah-pixel")

    def open_manu(self):
        image_path = Path(__file__).with_name("ManchesterUnited.webp")
        source = QPixmap(str(image_path)).scaled(
            150, 150,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation,
        )

        size = 150
        circular = QPixmap(size, size)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        clip_path = QPainterPath()
        clip_path.addEllipse(0, 0, size, size)
        painter.setClipPath(clip_path)
        painter.drawPixmap(
            (size - source.width()) // 2,
            (size - source.height()) // 2,
            source,
        )
        painter.end()

        self.image_manu.setPixmap(circular)
        self.image_manu.show()

if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()