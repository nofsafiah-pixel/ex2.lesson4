from pathlib import Path
import numpy as np
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

        
        self.Temperature = [] 
        self.Revenue = []
        self.selected_file = ''

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
            self.select_file= file_path
            self.make_graphe_out_of_file(file_path)

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def plot_temporary_graph(self):
        self.figure.clear()
        axes = self.figure.add_subplot(111)

        if self.Temperature and self.Revenue:
            axes.scatter(self.Temperature, self.Revenue, s=1)
            axes.spines["top"].set_visible(False)
            axes.spines["right"].set_visible(False)
            axes.set_title("Ice Cream Revenue vs. Temperature")
            axes.set_xlabel("Temperature")
            axes.set_ylabel("Revenue")
            m, b = np.polyfit(self.Temperature, self.Revenue, 1)
            x_vals = np.array(self.Temperature)
            y_vals = m * x_vals + b
            axes.text(0.05,0.95,f"y = {m:.2f}x + {b:.2f}",transform=axes.transAxes,verticalalignment="top",)

            axes.plot(x_vals, y_vals, color="red", label="Trendline")
            
        else:
            axes.plot([1, 2, 3, 4], [1, 3, 2, 4])
        
        self.canvas.draw()
   

        

    def make_graphe_out_of_file(self, file_path):
        self.Temperature = []
        self.Revenue = []
            
        if not file_path:
            return

        with open(file_path, 'r') as f:
            next(f)  
            for line in f:
                Temperature, Revenue = line.strip().split(',')
                self.Temperature.append(float(Temperature.strip()))
                self.Revenue.append(float(Revenue.strip()))
        self.plot_temporary_graph()
        
   


if __name__ == "__main__":
    app = QApplication()
    window = CreamWindow()
    window.show()
    app.exec()