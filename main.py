import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow


def main() -> None:
    # Initialize a QApplication
    app = QApplication(sys.argv)
    # Initialize a MinaWindow
    MainWindow = QMainWindow()
    # Instantiate the main ui
    main_ui = Ui_App()
    # Run the main window
    main_ui.setupUi(MainWindow)
    # Show the main window
    MainWindow.show()
    # Exit the App when the main window closes
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
