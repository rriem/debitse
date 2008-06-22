# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre.ui'
#
# Created: Sun Oct 29 12:13:44 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,640,480).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setMinimumSize(QtCore.QSize(64,64))
        MainWindow.setMaximumSize(QtCore.QSize(640,480))
        MainWindow.setWindowIcon(QtGui.QIcon(":/icones/Images/SE.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20,30,310,401))
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(40,30,218,151))
        self.widget.setObjectName("widget")

        self.gridlayout = QtGui.QGridLayout(self.widget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.poids = QtGui.QLineEdit(self.widget)
        self.poids.setObjectName("poids")
        self.gridlayout.addWidget(self.poids,3,1,1,1)

        self.posologie = QtGui.QLineEdit(self.widget)
        self.posologie.setObjectName("posologie")
        self.gridlayout.addWidget(self.posologie,4,1,1,1)

        self.concentration = QtGui.QLineEdit(self.widget)
        self.concentration.setObjectName("concentration")
        self.gridlayout.addWidget(self.concentration,2,1,1,1)

        self.debit = QtGui.QLineEdit(self.widget)
        self.debit.setObjectName("debit")
        self.gridlayout.addWidget(self.debit,5,1,1,1)

        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,5,0,1,1)

        self.label = QtGui.QLabel(self.widget)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,2,0,1,1)

        self.volume = QtGui.QLineEdit(self.widget)
        self.volume.setObjectName("volume")
        self.gridlayout.addWidget(self.volume,1,1,1,1)

        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,3,0,1,1)

        self.quantite = QtGui.QLineEdit(self.widget)
        self.quantite.setObjectName("quantite")
        self.gridlayout.addWidget(self.quantite,0,1,1,1)

        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,4,0,1,1)

        self.message = QtGui.QTextBrowser(self.frame)
        self.message.setGeometry(QtCore.QRect(10,200,291,191))

        font = QtGui.QFont(self.message.font())
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.message.setFont(font)
        self.message.setFocusPolicy(QtCore.Qt.NoFocus)
        self.message.setAcceptRichText(False)
        self.message.setObjectName("message")

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(440,30,131,401))
        self.frame_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.raz = QtGui.QPushButton(self.frame_2)
        self.raz.setGeometry(QtCore.QRect(10,160,109,32))
        self.raz.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.raz.setObjectName("raz")

        self.apropos = QtGui.QPushButton(self.frame_2)
        self.apropos.setGeometry(QtCore.QRect(10,10,109,32))
        self.apropos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.apropos.setObjectName("apropos")

        self.calcul = QtGui.QPushButton(self.frame_2)
        self.calcul.setGeometry(QtCore.QRect(10,120,109,32))
        self.calcul.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.calcul.setObjectName("calcul")

        self.quitter = QtGui.QPushButton(self.frame_2)
        self.quitter.setGeometry(QtCore.QRect(10,330,109,32))
        self.quitter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.quitter.setObjectName("quitter")

        self.imprimer = QtGui.QPushButton(self.frame_2)
        self.imprimer.setGeometry(QtCore.QRect(10,290,109,32))
        self.imprimer.setObjectName("imprimer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,640,19))
        self.menubar.setObjectName("menubar")

        self.menu_Fichier = QtGui.QMenu(self.menubar)
        self.menu_Fichier.setObjectName("menu_Fichier")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,461,640,19))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")

        self.actionImprimer = QtGui.QAction(MainWindow)
        self.actionImprimer.setObjectName("actionImprimer")

        self.actionA_Propos = QtGui.QAction(MainWindow)
        self.actionA_Propos.setObjectName("actionA_Propos")
        self.menu_Fichier.addAction(self.actionA_Propos)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionImprimer)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.label_6.setBuddy(self.debit)
        self.label.setBuddy(self.quantite)
        self.label_2.setBuddy(self.volume)
        self.label_3.setBuddy(self.concentration)
        self.label_4.setBuddy(self.poids)
        self.label_5.setBuddy(self.posologie)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quitter,QtCore.SIGNAL("clicked()"),MainWindow.close)
        QtCore.QObject.connect(self.quantite,QtCore.SIGNAL("returnPressed()"),self.volume.setFocus)
        QtCore.QObject.connect(self.volume,QtCore.SIGNAL("returnPressed()"),self.poids.setFocus)
        QtCore.QObject.connect(self.poids,QtCore.SIGNAL("returnPressed()"),self.posologie.setFocus)
        QtCore.QObject.connect(self.concentration,QtCore.SIGNAL("returnPressed()"),self.poids.setFocus)
        QtCore.QObject.connect(self.debit,QtCore.SIGNAL("returnPressed()"),self.calcul.animateClick)
        QtCore.QObject.connect(self.posologie,QtCore.SIGNAL("returnPressed()"),self.debit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.quantite,self.volume)
        MainWindow.setTabOrder(self.volume,self.concentration)
        MainWindow.setTabOrder(self.concentration,self.poids)
        MainWindow.setTabOrder(self.poids,self.posologie)
        MainWindow.setTabOrder(self.posologie,self.debit)
        MainWindow.setTabOrder(self.debit,self.calcul)
        MainWindow.setTabOrder(self.calcul,self.raz)
        MainWindow.setTabOrder(self.raz,self.apropos)
        MainWindow.setTabOrder(self.apropos,self.quitter)
        MainWindow.setTabOrder(self.quitter,self.label_4)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Seringue électrique", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "&Débit en ml/h : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Q&uantité en mg :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "&Volume en ml : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "C&oncentration en µg/ml : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "P&oids en kg : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Po&sologie en µg/kg/min : ", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setDocumentTitle(QtGui.QApplication.translate("MainWindow", "Resultats", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setHtml(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Resultats</title></head><body style=\" white-space: pre-wrap; font-family:Arial; font-size:12pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:Lucida Grande;\"><span style=\" font-size:10pt;\">Entrez les informations dont vous disposez et pressez  </span><span style=\" font-size:10pt; font-weight:600;\">Calculer</span><span style=\" font-size:10pt;\"> !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.raz.setText(QtGui.QApplication.translate("MainWindow", "&Effacer", None, QtGui.QApplication.UnicodeUTF8))
        self.apropos.setText(QtGui.QApplication.translate("MainWindow", "&A propos", None, QtGui.QApplication.UnicodeUTF8))
        self.calcul.setText(QtGui.QApplication.translate("MainWindow", "&Calculer", None, QtGui.QApplication.UnicodeUTF8))
        self.quitter.setText(QtGui.QApplication.translate("MainWindow", "&Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.imprimer.setText(QtGui.QApplication.translate("MainWindow", "Im&primer", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Fichier.setTitle(QtGui.QApplication.translate("MainWindow", "&Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(QtGui.QApplication.translate("MainWindow", "&Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImprimer.setText(QtGui.QApplication.translate("MainWindow", "Im&primer ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImprimer.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_Propos.setText(QtGui.QApplication.translate("MainWindow", "&A Propos ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_Propos.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
