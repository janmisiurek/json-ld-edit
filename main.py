import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QLabel, QWidget, QSizePolicy
from graph_editor import load_jsonld, save_jsonld, edit_jsonld
from graph_visualizer import draw_graph

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Knowledge Graph App')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        # JSON-LD Text Edit
        self.jsonld_edit = QTextEdit(self)
        vbox.addWidget(self.jsonld_edit)

        # Load Button
        self.load_button = QPushButton('Load JSON-LD', self)
        self.load_button.clicked.connect(self.load_jsonld)
        vbox.addWidget(self.load_button)

        # Save Button
        self.save_button = QPushButton('Save JSON-LD', self)
        self.save_button.clicked.connect(self.save_jsonld)
        vbox.addWidget(self.save_button)

        # Edit Button
        self.edit_button = QPushButton('Edit JSON-LD', self)
        self.edit_button.clicked.connect(self.edit_jsonld)
        vbox.addWidget(self.edit_button)

        # Draw Graph Button
        self.draw_button = QPushButton('Draw Graph', self)
        self.draw_button.clicked.connect(self.draw_graph)
        vbox.addWidget(self.draw_button)

        # Extract Information Button
        self.extract_button = QPushButton('Extract Information', self)
        self.extract_button.clicked.connect(self.extract_information_ui)
        vbox.addWidget(self.extract_button)

        central_widget.setLayout(vbox)

    # ... (other methods here)

    def extract_information_ui(self):
        jsonld_data = self.jsonld_edit.toPlainText()
        # You need to define schema_dict here or get it from the user
        # For example, you could use a simple hardcoded schema_dict:
        schema_dict = {
            "Person": {
                "path": ["@graph", "Person"],
                "attributes": ["name", "email"]
            }
        }
        extracted_data = extract_information(jsonld_data, schema_dict)
        # Display extracted_data as needed, e.g., in a QLabel, QMessageBox,
        # or other widget, or even in the jsonld_edit widget
        # Here, we will convert extracted_data to a string and display it in a QMessageBox
        from PyQt5.QtWidgets import QMessageBox

        extracted_data_str = str(extracted_data)
        msg = QMessageBox()
        msg.setWindowTitle('Extracted Information')
        msg.setText(extracted_data_str)
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


