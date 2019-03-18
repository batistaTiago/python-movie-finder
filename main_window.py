from PyQt5 import QtCore, QtGui, QtWidgets
import DataFetcher
import movieInfoWindow
import pprint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 131)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label.setObjectName("label")
        self.movieNameTextField = QtWidgets.QLineEdit(self.centralwidget)
        self.movieNameTextField.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.movieNameTextField.setObjectName("movieNameTextField")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.goButton.setObjectName("goButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        # Meu codigo

        self.goButton.clicked.connect(self.goButtonClick)
        self.movieNameTextField.returnPressed.connect(self.movieNameTextFieldEnterPressed)

        #Fim do meu codigo

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome do filme"))
        self.goButton.setText(_translate("MainWindow", "PushButton"))


    def goButtonClick(self):
        self.fetchData()

    def movieNameTextFieldEnterPressed(self):
        self.fetchData()

    def fetchData(self):
        movieData = {}
        if self.movieNameTextField.text() != "":
            movieData = DataFetcher.fetchMovieContent(self.movieNameTextField.text())
        else:
            print('DIGITE ALGUMA COISA!') #  TODO: trocar para janela de warning


        if movieData != {}:

            movieTitle = movieData[0]['Title']
            movieYear = movieData[0]['Year']
            movieDirector = movieData[0]['Director']
            movieGenre = movieData[0]['Genre']

            #Este conjunto cria uma janela e associa a uma interface
            #Cria uma janela (QDialog), e armazena na variavel
            movieDetailsWindow = QtWidgets.QDialog()
            #construtor da classe de interface do designer
            ui = movieInfoWindow.Ui_Dialog()
            #carrega a interface pra dentro da janela criada
            ui.setupUi(movieDetailsWindow)
            #Fim do conjunto


            ui.setMovieTitle(movieTitle)
            ui.setMovieYear(movieYear)
            ui.setMovieDirector(movieDirector)
            ui.setMovieGenre(movieGenre)
            ui.setMoviePoster(movieData[1])

            movieDetailsWindow.exec_()

        else:
            print('O SERVIDOR NÃO RETORNOU DADOS')  #  TODO: trocar para janela de warning


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedWidth(287)
    MainWindow.setFixedHeight(105)
    MainWindow.show()
    sys.exit(app.exec_())
