from pathlib import Path

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from about import AboutWindow


class SimpleNavigationToolbar(NavigationToolbar2QT):
    toolitems = (
        ("Zoom", "Zoom to rectangle", "zoom_to_rect", "zoom"),
        ("Save", "Save the graph", "filesave", "save_figure"),
    )


class CreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Data")
        self.resize(800, 600)

        stylesheet_path = Path(__file__).with_name("app_cream.qss")
        self.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

        self.file_button = QPushButton("Select file")
        self.file_button.clicked.connect(self.select_file)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.open_about_window)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = SimpleNavigationToolbar(self.canvas, self)
        self.plot_temporary_graph()

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.file_button)
        buttons_layout.addWidget(self.about_button)
        buttons_layout.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.about_window = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file")
        if file_path:
            self.file_button.setText(Path(file_path).name)

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def plot_temporary_graph(self):
        axes = self.figure.add_subplot(111)
        axes.plot([1, 2, 3, 4], [1, 3, 2, 4])
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication()
    window = CreamWindow()
    window.show()
    app.exec()