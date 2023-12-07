from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000, 1000)
        self.fact = QtWidgets.QTextEdit(Form)
        self.fact.setGeometry(QtCore.QRect(750, 300, 400, 500))  # 已选事实框
        self.fact.setStyleSheet("font: 12pt \"方正颜宋简体\";")
        self.fact.setObjectName("fact")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(700, 70, 700, 100))  # 动物识别系统
        self.label.setStyleSheet("font: 36pt \"字酷堂清楷体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(750, 230, 200, 50))  # 已选事实
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1400, 230, 200, 50))  # 推理过程
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
        self.procedure = QtWidgets.QTextEdit(Form)
        self.procedure.setGeometry(QtCore.QRect(1400, 300, 400, 500))  # 推理结果框
        self.procedure.setStyleSheet("font: 12pt \"方正颜宋简体\";")
        self.procedure.setObjectName("procedure")
        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setGeometry(QtCore.QRect(1180, 500, 180, 50))  # 正向推理
        self.startBtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.startBtn.setObjectName("startBtn")
        self.BackBtn = QtWidgets.QPushButton(Form)
        self.BackBtn.setGeometry(QtCore.QRect(1180, 600, 180, 50))  # 反向推理
        self.BackBtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.BackBtn.setObjectName("BackBtn")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 850, 200, 50))  # 添加规则
        self.pushButton.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 230, 200, 50))  # 选择事实
        self.label_6.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_6.setObjectName("label_6")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(200, 300, 400, 500))  # 选择事实框
        self.listView.setStyleSheet("font: 10pt \"方正颜宋简体\";")
        self.listView.setObjectName("listView")
        self.update = QtWidgets.QPushButton(Form)
        self.update.setGeometry(QtCore.QRect(600, 850, 300, 50))  # 删除/修改规则
        self.update.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.update.setObjectName("update")

        self.retranslateUi(Form)
        self.startBtn.clicked.connect(Form.ForwardReasoning)
        self.BackBtn.clicked.connect(Form.BackwardReasoning)
        self.pushButton.clicked.connect(Form.add)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "动物识别系统"))
        self.label_2.setText(_translate("Form", "已选事实"))
        self.label_3.setText(_translate("Form", "推理过程"))
        self.startBtn.setText(_translate("Form", "正向推理"))
        self.BackBtn.setText(_translate("Form", "反向推理"))
        self.pushButton.setText(_translate("Form", "添加规则"))
        self.label_6.setText(_translate("Form", "选择事实"))
        self.update.setText(_translate("Form", "删除/修改规则"))
