import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.result_line = QLineEdit()
        self.layout.addWidget(self.result_line)

        self.create_buttons()
        self.layout.addLayout(self.grid)

    def create_buttons(self):
        self.grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, t=text: self.on_button_clicked(t))
            self.grid.addWidget(button, row, col)

    def on_button_clicked(self, button_text):
        current_text = self.result_line.text()

        if button_text == 'C':
            self.result_line.clear()
        elif button_text == '=':
            try:
                result = str(eval(current_text))
                self.result_line.setText(result)
            except Exception as e:
                self.result_line.setText("Ошибка")
        else:
            self.result_line.setText(current_text + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())