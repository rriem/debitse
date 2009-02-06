#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# programme principal pour la version 0.5 - en cours de test

import sys
import sip #n�cessaire pour la cr�ation d'une application par py2.exe avec le fichier setup actuel
from PyQt4 import QtCore, QtGui

import mainWindow # l'interface graphique issue de QtDesigner



class fenetre(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #QtGui.QMainWindow.__init__(self, parent)
        super(fenetre,self).__init__(parent)
        self.fenetre = mainWindow.Ui_DebitSE ()
        self.fenetre.setupUi(self)

        ###########
        #connection des actions
        #action quitter
        QtCore.QObject.connect(self.fenetre.actionQuit,QtCore.SIGNAL("triggered()"),self.quit)

        #action a propos
        QtCore.QObject.connect( self.fenetre.actionAbout_Debit_SE,QtCore.SIGNAL("triggered()"),self.about)

        #action pr�f�rences
        QtCore.QObject.connect( self.fenetre.actionPreferences,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action imprimer
        QtCore.QObject.connect( self.fenetre.actionPrint,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #Actions d'�dition
        #action annuler
        QtCore.QObject.connect( self.fenetre.actionUndo,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action couper
        QtCore.QObject.connect( self.fenetre.actionCut,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action copier
        QtCore.QObject.connect( self.fenetre.actionCopy,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action coller
        QtCore.QObject.connect( self.fenetre.actionPaste,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action donn�es patient
        QtCore.QObject.connect( self.fenetre.actionPatient_Data,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action donn�es m�dicaments
        QtCore.QObject.connect( self.fenetre.actionDrug_Data,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action calcul
        QtCore.QObject.connect( self.fenetre.actionCalc,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action calcul express
        QtCore.QObject.connect( self.fenetre.actionExpress_Calc,QtCore.SIGNAL("triggered()"),self.nonImplemented)


    ##################
    #fonction pour quitter
    def quit(self):
        self.close()

    def about (self):
        QtGui.QMessageBox.about(self,self.tr("D�bit SE developpement"),"D�bit SE en cours de d�veloppement")


    #Message pour fonction non encore impl�ment�e
    def nonImplemented (self):
        QtGui.QMessageBox.information(self,self.tr("D�bit SE developpement"),"fonction non implant�e")




#programme principal
app=QtGui.QApplication(sys.argv)
window=fenetre()
window.show()
sys.exit(app.exec_())
