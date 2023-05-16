from PyQt5 import uic
from checker import *
import webbrowser
from PyQt5.QtWidgets import *
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

Form, Window = uic.loadUiType(resource_path('checker.ui'))

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedWidth(400) # ставит фиксированную ширину 400
        self.setFixedHeight(320) # ставит фиксированную высоту 320

# main
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click_helpme():
    print("Открыта ссылка по нажатию кнопки How to use?...")
    webbrowser.open_new_tab("https://drive.google.com/file/d/1LYrRzIkmOC_OrtzCJzUyLOwfmmSJaThE/view?usp=share_link")
    # тут кароче понятно, вставляем гиперссылку и усе

# здесь жмякаем по "How to use?"
form.helpme.clicked.connect(on_click_helpme)

result = 3
def on_click_result():
    print("\nЗапущена проверка...")

    # zdes X
    X = float(form.x_box.value())
    print("X =", X)
    #X = float(form.x_box
    #print("X =", X)

    # zdes Y
    Y = float(form.y_box.value())
    print("Y =", Y)

    underground = 3
    # zdes чекаем подземку (доделать)
    if form.underground.isChecked():
        underground = 1
        print("s podzemkoi")
        c = 5325.181015  # * na Z
    else:
        underground = 0
        print("bez undera")
        c = 0  # * na Z

    # здесь делаем развилку на подземку и NON-подземку:
    a = 2992.911117  # * na X
    b = 14174.264968  # * na Y
    d = 32788.72792

    # пробую здесь сделать нормально
    step1 = float(a*X + b*Y + c*underground + d)
    step2 = float(step1 % 32768)
    step3 = float(step2 % 100)

    if step3 < 50.0:
        result = 1
        print("result =", result)
        print('Обнаружен улучшенный стек!')
        form.result_label.setText("Обнаружен улучшенный стек!")

    else:
        result = 0
        print("result =", result)
        print('Нет улучшенного стека...')
        form.result_label.setText("Нет улучшенного стека...")

# здесь жмякаем по "Проверить"
form.check_button.clicked.connect(on_click_result)


app.exec_()
