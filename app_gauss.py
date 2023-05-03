'''
Matrix calculator based on gauss method
'''
import numpy
from gauss import gauss
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow

class MainDialog(QMainWindow):
    '''
    main
    '''
    def __init__(self):
        '''
        Создает макет и спрашивает про размер
        '''
        super().__init__()
        self.size = 4

        self.setWindowTitle("Gauss calculator")

        self.layout_main = QGridLayout()

        Welcome = QLabel("Choose size: ")
        font = Welcome.font()
        font.setPointSize(15)
        Welcome.setFont(font)
        self.layout_main.addWidget(Welcome, 0,0)

        self.size_cell = QLineEdit(f"{self.size}")
        self.size_cell.setFixedSize(40,30)
        self.size_cell.editingFinished.connect(self.size_set)
        self.layout_main.addWidget(self.size_cell, 0, 1)

        widget = QWidget()
        widget.setLayout(self.layout_main)
        self.setCentralWidget(widget)

    def size_set(self):
        '''
        После выбора размера создает все остальное
        '''
        self.size = int(self.size_cell.displayText())

        for i in reversed(range(self.layout_main.count())): #очищение всего макета после выбора размера
            self.layout_main.itemAt(i).widget().setParent(None)

        layout_coef = QGridLayout()
        layout_coef.setContentsMargins(0,0,30,0)
        layout_b = QGridLayout()
        answer_butt = QPushButton("Calculate")

        layout_answer = QGridLayout()
        self.coefs_cells = []

        for i in range(self.size):
            string_of_coefs_cells = []
            for j in range(self.size):
                string_of_coefs_cells.append(QLineEdit("0"))
                string_of_coefs_cells[j].setFixedSize(50,40)
                layout_coef.addWidget(string_of_coefs_cells[j], i, j)
            self.coefs_cells.append(string_of_coefs_cells)

        self.layout_main.addLayout(layout_coef, 1, 0)

        self.b_cells = []
        for i in range(self.size):
            self.b_cells.append(QLineEdit("0"))
            self.b_cells[i].setFixedSize(50,40)
            layout_b.addWidget(self.b_cells[i], i, 0)

        self.layout_main.addLayout(layout_b, 1, 1)

        answer_butt.setFixedSize(100, 50)
        self.layout_main.addWidget(answer_butt, 2, 0)

        self.determinant = QLabel("det = ")
        font = self.determinant.font()
        font.setPointSize(15)
        self.determinant.setFont(font)
        self.layout_main.addWidget(self.determinant, 3,0)

        self.answer_cells = []
        for i in range(self.size):
            self.answer_cells.append(QLabel(f"x{i+1} ="))
            layout_answer.addWidget(self.answer_cells[i], 0, i)

        self.layout_main.addLayout(layout_answer, 4, 0)

        answer_butt.clicked.connect(self.calculate_solution)

        reminder = QLabel("Use  ' . '  instead of  ' , '  ")
        font = reminder.font()
        font.setPointSize(15)
        reminder.setFont(font)
        self.layout_main.addWidget(reminder, 0, 0)

    def coef_change(self):
        '''
        Читает ячейки коэффициентов
        '''
        self.coefs = []
        for i in range(self.size):
            string_of_coefs = []
            for j in range(self.size):
                string_of_coefs.append(float(self.coefs_cells[i][j].displayText()))
            self.coefs.append(string_of_coefs)
#        print(self.coefs)

    def b_change(self):
        '''
        Читает ячейки правого столбика
        '''
        self.b = []
        for i in range(self.size):
            self.b.append(float(self.b_cells[i].displayText()))
#        print(self.b)

    def calculate_solution(self):
        '''
        Выводит решение и определитель
        '''
        self.coef_change()
        self.b_change()
        a = numpy.array(self.coefs)
        b = numpy.array(self.b)
        det = round(numpy.linalg.det(a),5)
        self.determinant.setText(f"det = {det}")
        if det == 0:
            self.determinant.setStyleSheet("background-color: Red ")
        else:
            self.determinant.setStyleSheet("background-color:  ")
            self.solution = gauss(a, b)
#            print(self.solution)
            for i in range(self.size):
                self.answer_cells[i].setText(f"x{i+1} = {numpy.format_float_positional(self.solution[i])}")

app = QApplication([])
w = MainDialog()
w.show()

app.exec()
