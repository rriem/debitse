#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# programme principal pour la version 0.5 - en cours de test

import sys

#import sip #nécessaire pour la création d'une application par py2.exe avec le fichier setup actuel
from PyQt4 import QtCore, QtGui

import mainWindow  # l'interface graphique issue de QtDesigner
import calcExpress  # le dialogue de calcul express issu de QtDesigner

__version__ = "0.5.0"


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

        #action préférences
        QtCore.QObject.connect( self.fenetre.actionPreferences,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action imprimer
        QtCore.QObject.connect( self.fenetre.actionPrint,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #Actions d'édition
        #action annuler
        QtCore.QObject.connect( self.fenetre.actionUndo,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action couper
        QtCore.QObject.connect( self.fenetre.actionCut,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action copier
        QtCore.QObject.connect( self.fenetre.actionCopy,QtCore.SIGNAL("triggered()"),self.nonImplemented)
        #action coller
        QtCore.QObject.connect( self.fenetre.actionPaste,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action données patient
        QtCore.QObject.connect( self.fenetre.actionPatient_Data,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action données médicaments
        QtCore.QObject.connect( self.fenetre.actionDrug_Data,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action calcul
        QtCore.QObject.connect( self.fenetre.actionCalc,QtCore.SIGNAL("triggered()"),self.nonImplemented)

        #action calcul express
        QtCore.QObject.connect( self.fenetre.actionExpress_Calc,QtCore.SIGNAL("triggered()"),self.calcExpress)

        #action calcul table
        QtCore.QObject.connect( self.fenetre.actionTable,QtCore.SIGNAL("triggered()"),self.nonImplemented)

    ##################



    #fonction pour quitter
    def quit(self):
        #pour la version de développement, et pour accélérer la sortie, on cour circuite le dialogue
        #ret = QtGui.QMessageBox.question(self, self.tr("Débit SE developpement"), self.tr("Voulez vous vraiment quitter Débit SE ?"),QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel )
        ret = QtGui.QMessageBox.Ok
        if ret == QtGui.QMessageBox.Ok:
            self.close()
        return

    # fonction à propos
    def about (self):
        titre = app.applicationName()
        mes = titre.append (" \n")
        mes.append(app.applicationVersion() )
        mes.append (" \n")
        mes.append(app.organizationName() )
        #QtGui.QMessageBox.about(self,self.tr("Débit SE developpement"),self.tr("Débit SE en cours de développement"))
        QtGui.QMessageBox.about(self, titre, mes)

    #  fonction de calcul express
    def calcExpress (self) :
        dia = calc_express (parent = self)
        dia.exec_()


    #Message pour fonction non encore implémentée
    def nonImplemented (self):
        QtGui.QMessageBox.information(self,self.tr("Débit SE developpement"),self.tr("fonction non implantée"))


##################
# Classe pour le calcul express
class calc_express (QtGui.QDialog):
    def __init__(self, parent = None):
        super(calc_express,self).__init__(parent)
        self.dia = calcExpress.Ui_Dialog ()
        self.dia.setupUi(self)
        QtCore.QObject.connect(self.dia.pushButton,QtCore.SIGNAL("clicked()"), self.calc) # attention les noms (fonction et bouton) changeront)

    def calc (self):
        # récupération du contenu des différents champs
        #concentration
        c= self.dia.lineEdit_Conc.text()
        con=c.toDouble()
        #poids
        p = self.dia.lineEdit_Weight.text()
        poi = p.toDouble()
        #posologie
        po = self.dia.lineEdit_Poso.text()
        poso = po.toDouble()
        #vérification que les valeurs sont correctes et calcul
        if con[1] & poi [1] & poso[1]:
            d = (poso[0] * poi[0] * 60) / con[0]
            self.dia.lineEdit_Flow.setText(loc.toString(round(d, 1)))

        else:
            QtGui.QMessageBox.warning(self, app.applicationName(), self.tr("Attention ! Données erronées"))  #self.tr("Débit SE developpement")


####################

#programme principal
app=QtGui.QApplication(sys.argv)

__VERSION__  = "0.5.0 test"

#essai de splash screen
import time
pix = QtGui.QPixmap("icons/splashscreen.png")
splash = QtGui.QSplashScreen(pix)
splash.show()

app.processEvents()

time.sleep(1.)


app.setOrganizationName("RR et Cie")
app.setOrganizationDomain("r-riem.fr")
app.setApplicationName("Débit SE développement")
app.setApplicationVersion(__VERSION__)

window=fenetre()
window.show()

#pour tenir compte de la localisation
loc = QtCore.QLocale()

splash.finish(window)

sys.exit(app.exec_())
