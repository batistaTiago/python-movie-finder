from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 900)
        self.movieTitleLabel = QtWidgets.QLabel(Dialog)
        self.movieTitleLabel.setGeometry(QtCore.QRect(50, 30, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.movieTitleLabel.setFont(font)
        self.movieTitleLabel.setObjectName("movieTitleLabel")
        self.movieYearLabel = QtWidgets.QLabel(Dialog)
        self.movieYearLabel.setGeometry(QtCore.QRect(50, 100, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.movieYearLabel.setFont(font)
        self.movieYearLabel.setObjectName("movieYearLabel")
        self.movieDirectorLabel = QtWidgets.QLabel(Dialog)
        self.movieDirectorLabel.setGeometry(QtCore.QRect(50, 170, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.movieDirectorLabel.setFont(font)
        self.movieDirectorLabel.setObjectName("movieDirectorLabel")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(610, 30, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.imageLabel = QtWidgets.QLabel(Dialog)
        self.imageLabel.setGeometry(QtCore.QRect(30, 380, 371, 501))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.movieGenreLabel = QtWidgets.QLabel(Dialog)
        self.movieGenreLabel.setGeometry(QtCore.QRect(50, 240, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.movieGenreLabel.setFont(font)
        self.movieGenreLabel.setObjectName("movieGenreLabel")

        self.closeButton.clicked.connect(self.closeButtonClick)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.movieTitleLabel.setText(_translate("Dialog", "Titulo"))
        self.movieYearLabel.setText(_translate("Dialog", "Ano"))
        self.movieDirectorLabel.setText(_translate("Dialog", "Diretor"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.movieGenreLabel.setText(_translate("Dialog" , "Genre"))

    #Codigo Próprio
    def closeButtonClick(self):
        print('close clicked')

    def setMovieTitle(self, newTitle):
        self.movieTitleLabel.setText("Título: " + newTitle)

    def setMovieYear(self, newYear):
        self.movieYearLabel.setText("Ano: " + newYear)

    def setMovieDirector(self, newDirector):
        self.movieDirectorLabel.setText("Diretor: " + newDirector)

    def setMoviePoster(self, fileName):
        print('looking for file: ' + fileName)
        pixmap = QPixmap(fileName)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.show()


    def setMovieGenre(self , newGenre):
        self.movieGenreLabel.setText("Gênero: " + newGenre)
