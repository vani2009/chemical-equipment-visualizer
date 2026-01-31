import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from api import login, get_latest_summary
from charts import create_summary_chart


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()

        self.title = QLabel("Summary Dashboard")
        self.layout.addWidget(self.title)

        self.refresh_btn = QPushButton("Refresh Summary")
        self.refresh_btn.clicked.connect(self.load_summary)
        self.layout.addWidget(self.refresh_btn)

        self.canvas = None
        self.setLayout(self.layout)

        # 🔐 LOGIN FIRST (REQUIRED)
        try:
            login("vani", "Vanipulkit")  
        except Exception as e:
            QMessageBox.critical(self, "Login Failed", str(e))
            sys.exit(1)

        # Load data after successful login
        self.load_summary()

    def load_summary(self):
        try:
            summary = get_latest_summary()
            fig = create_summary_chart(summary)

            if self.canvas:
                self.layout.removeWidget(self.canvas)
                self.canvas.setParent(None)

            self.canvas = FigureCanvas(fig)
            self.layout.addWidget(self.canvas)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
