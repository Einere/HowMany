# program name : HowMany
# description : extract most popular words and draw chart
# write date : 2018.11.29
# writer : 2013726058 Choi HyungJun

# coding: utf-8

from collections import Counter as Counter
import sys
import os
import copy
import random
import locale
import pandas as pd

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTextBrowser
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


# enable korean at chart
plt.rcParams['axes.unicode_minus'] = False
f_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)


class Form(QtWidgets.QDialog):
    # declare class variables
    filePath = ''
    fileName = ''
    fileContents = ''
    paragraph = []
    sentence = []
    words = []
    blackList = ['a', 'the', 'to', 'of', 'that', 'in', 'and', 'with', 'at', 'for', 'on', 'off', '--', 'top', 'out',
                 'their', 'his', 'by', 'another', 'ahead', 'over', 'without', 'but', 'into', 'this', '(', ')']
    counts = {}
    keys = []
    values = []
    df = pd.DataFrame()

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("form.ui", self)
        self.myInit()
        self.ui.show()

    # connect widget with event handler
    def myInit(self):
        self.btn_openFile.clicked.connect(self.openFile)
        self.btn_analyze.clicked.connect(self.analyze)
        self.btn_chart.clicked.connect(self.drawChart)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout(self)
        leftLayout.addWidget(self.canvas)
        self.chartWidget.setLayout(leftLayout)

    # reset data
    def myReset(self):
        self.filePath = ''
        self.fileName = ''
        self.fileContents = ''
        self.paragraph = []
        self.sentence = []
        self.words = []
        self.counts = {}
        self.keys = []
        self.values = []
        self.df = pd.DataFrame()
        self.tb_input.clear()
        self.tb_output.clear()
        if self.fig.get_axes():
            self.ax.clear()
            self.canvas.draw()

    # get file encoding
    # noinspection PyTypeChecker
    def getEncoding(self, myPath):
        with open(myPath, mode='rb') as f:
            data = f.read(3)

        if data[:2] in ('\xff\xfe', '\xfe\xff'):
            return 'utf-16'
        if data == u''.encode('utf-8-sig'):
            return 'utf-8-sig'

        # presumably "ANSI"
        return locale.getpreferredencoding()

    # open file event handler
    @pyqtSlot()
    def openFile(self):
        # get opened file data
        fileTuple = QFileDialog.getOpenFileName(self, filter="Text files (*.txt)", initialFilter="Text files (*.txt)")

        # if user chose file
        if not fileTuple[0] == '':
            self.myReset()
            self.filePath = fileTuple[0]
            tmpStr = self.filePath
            self.fileName = tmpStr.split('/')[-1]
            self.lb_filePath.setText(self.filePath)
            self.readFile()

    # read file event handler
    @pyqtSlot()
    def readFile(self):
        # get file encoding
        myEncoding = self.getEncoding(self.filePath)

        if myEncoding == 'utf-8-sig':
            self.fileContents = open(self.filePath, "r", encoding='utf-8-sig').read()
        elif myEncoding == 'cp949':
            # need to handling
            self.fileContents = open(self.filePath, "r", encoding='cp949').read()

        self.tb_input.setText(self.fileContents)

    # tokenize read contents to paragraph, sentences, words
    @pyqtSlot()
    def tokenize(self):
        # disassemble read contents
        self.paragraph = self.fileContents.split('\n')

        # remove space in paragraph
        while '' in self.paragraph:
            self.paragraph.remove('')

        # print output text browser
        self.tb_output.setText("-------------------- tokenized paragraph --------------------")

        for e in self.paragraph:
            self.tb_output.append(e)

        self.tb_output.append("\n\n")

        # tokenize paragraph to sentence with removing space
        for e in self.paragraph:
            tmp = e.split('.')

            while '' in tmp:
                tmp.remove('')

            self.sentence += tmp

        # print output text browser
        self.tb_output.append("-------------------- tokenized sentences --------------------")

        for e in self.sentence:
            self.tb_output.append(e)

        self.tb_output.append("\n\n")

        # tokenize sentence to words with removing ' ', ',', '"', '''...
        tmp = []
        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        tmp5 = []
        for e in self.sentence:
            tmp += e.split(' ')

        for e in tmp:
            tmp1 += e.split(',')

        for e in tmp1:
            tmp2 += e.split('\'')

        for e in tmp2:
            tmp3 += e.split('"')

        for e in tmp3:
            tmp4 += e.split('‘')

        for e in tmp4:
            tmp5 += e.split('’')

        while '' in tmp5:
            tmp5.remove('')
        while ',' in tmp5:
            tmp5.remove(',')

        self.words += tmp5

        # print output text browser
        self.tb_output.append("-------------------- tokenized words --------------------")

        for e in self.words:
            self.tb_output.append(e)

        self.tb_output.append("\n\n")

    # analyze event handler
    def analyze(self):
        # if user didn't chose file, no operation
        if self.fileName == '':
            return

        # tokenize
        self.tokenize()

        # counting most frequent words
        self.counts = Counter(self.words)

        # get most frequent words
        keys = self.counts.keys()

        # remove preposition, unnecessary words, make data frame, keys, values
        tmp = copy.deepcopy(self.counts)
        for e in keys:
            if e.lower() in self.blackList:
                tmp.pop(e)

        self.counts = tmp
        self.df = pd.DataFrame.from_dict(self.counts, 'index', int, ['count'])

        for e in self.counts:
            self.keys.append(e)
            self.values.append(self.counts[e])

        # get two most frequent words
        self.tb_output.append("-------------------- most common tow words --------------------")

        most = self.counts.most_common(2)
        for e in most:
            self.tb_output.append(e[0] + ", " + str(e[1]))

        self.tb_output.append("\n\n")

        # print sentence include most frequent words
        self.tb_output.append("-------------------- 3 sentence summary --------------------")

        if most[0][1] < 4:
            most = self.counts.most_common(1)
            for e in self.sentence:
                if most[0][0] in e:
                    self.tb_output.append(e)
        else:
            for e in self.sentence:
                if most[0][0] in e and most[1][0] in e:
                    self.tb_output.append(e)

        self.tb_output.append("\n\n")

    # draw pie chart to canvas
    def drawChart(self):
        if not self.df.empty:
            self.ax = self.fig.add_subplot(111)
            self.ax.pie(x=self.values[0:10], labels=self.keys[0:10], autopct='%1.1f%%', startangle=90)
            self.ax.axis('equal')
            self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
