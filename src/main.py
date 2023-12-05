import sys
from PyQt5 import QtWidgets, QtGui
from System import Ui_Form
from ADDGUI import Ui_Dialog
from UPDATEGUI import Ui_Dialog2
from PyQt5.QtCore import QStringListModel


class MainGUI(QtWidgets.QWidget, Ui_Form):

    def __init__(self):  # 初始化
        super(MainGUI, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        slm = QStringListModel()
        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        slm.setStringList(self.__s__)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.select)

    def __read_file__(self):  # 读取规则
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines.split('/'))
        with open("Q.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

    def start(self):  # 开始推理
        str = self.fact.toPlainText().split('\n')
        self.__DB__ = str
        self.__read_file__()
        self.procedure.setText("识别开始：\n")
        self.procedure.append('正向推理:\n')
        self.inference()
        self.procedure.append('\n识别结束')
        self.result.setText(self.__result__)

    def is_include_in_DB(self, p):  # 判断是否存在这个条件p
        for i in p:
            if i not in self.__DB__:
                return False
        return True

    def inference(self):  # 推理识别
        self.__result__ = '无法识别'
        for i, p in enumerate(self.__P__):
            if self.is_include_in_DB(p):
                self.__DB__.append(self.__Q__[i])  # 对应下标即对应结果，输入即可
                self.__result__ = self.__Q__[i]
                self.procedure.append('%s -> %s' % (p, self.__Q__[i]))

    def add(self):
        pass

    def select(self, qModelIndex):
        self.fact.append(self.__s__[qModelIndex.row()])


class AddGUI(QtWidgets.QDialog, Ui_Dialog):  # 添加规则交互
    def __init__(self):
        super(AddGUI, self).__init__()
        self.setupUi(self)

    def accept(self):  # 添加规则对话框中确定按钮的点击事件处理函数
        DB = self.textEdit.toPlainText().split('\n')
        P = []
        Q = []
        for d in DB:
            d = d.split('>')
            P.append(d[0])
            Q.append(d[1])
        self.write(P, Q)
        self.close()

    def write(self, P, Q):
        with open("Q.txt", 'a+', encoding='utf-8') as f_q, open("P.txt", 'a+', encoding='utf-8') as f_p:
            f_q.seek(0)  # 将文件指针移动到文件开头
            f_p.seek(0)  # 将文件指针移动到文件开头

            for q, p in zip(Q, P):  # 同时遍历Q和P
                found_q = False
                found_p = False

                for line_q, line_p in zip(f_q, f_p):  # 同时遍历Q.txt和P.txt的对应行
                    if q in line_q:
                        found_q = True
                    if p in line_p:
                        found_p = True

                    if found_q and found_p:  # 如果找到相同内容，则不进行写入
                        break

                if not found_q or not found_p:  # 如果两个列表中的元素有一个不同
                    f_q.write("\n" + q)  # 进行写入操作
                    f_p.write("\n" + p)


class UpdateGui(QtWidgets.QDialog, Ui_Dialog2):  # 更新规则交互
    def __init__(self):
        super(UpdateGui, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def accept(self):  # 更新规则对话框中确定按钮的点击事件处理函数
        self.__P__ = self.slm1.stringList()
        self.__Q__ = self.slm2.stringList()
        self.update_files(self.__P__, self.__Q__)
        self.close()

    def delete(self):
        select = self.PList.currentIndex().row()
        self.__P__.pop(select)
        self.__Q__.pop(select)
        self.slm1.setStringList(self.__P__)
        self.slm2.setStringList(self.__Q__)
        self.update_files(self.__P__, self.__Q__)
        self.update_display(self.__P__, self.__Q__)

    def update_files(self, P, Q):
        with open("Q.txt", 'w', encoding='utf-8') as f_q, open("P.txt", 'w', encoding='utf-8') as f_p:
            for i, q in enumerate(Q):
                f_q.write(q)
                if i != len(Q) - 1:
                    f_q.write("\n")
            for i, p in enumerate(P):
                f_p.write(p)
                if i != len(P) - 1:
                    f_p.write("\n")

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            self.__P__ = f.read().splitlines()
        with open("Q.txt", 'r', encoding='utf-8') as f:
            self.__Q__ = f.read().splitlines()

    def update_display(self, P, Q):
        slm1 = QStringListModel()
        slm1.setStringList(P)
        self.PList.setModel(slm1)
        slm2 = QStringListModel()
        slm2.setStringList(Q)
        self.listView_2.setModel(slm2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainGUI = MainGUI()
    child1 = AddGUI()
    btn = mainGUI.pushButton
    btn.clicked.connect(child1.show)
    child2 = UpdateGui()
    btn2 = mainGUI.update
    btn2.clicked.connect(child2.show)
    mainGUI.show()
    sys.exit(app.exec())
