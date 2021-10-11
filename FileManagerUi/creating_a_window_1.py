# Only needed for access to command line arguments
import sys

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([])
# works too.
from helloApp.ui.MainWindow import MainWindow

app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec_()
# Your application won't reach here until you exit and the event
# loop has stopped.
