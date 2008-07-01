#!/usr/bin/env python
#-*- coding: iso-8859-15 -*-
import sip #nécessaire pour la création d'une application par py2.exe avec le fichier setup actuel
import sys
from PyQt4 import QtCore, QtGui
from fenetre import Ui_MainWindow
import ressources

#Création de la classe représentant l'interface
class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.interface=Ui_MainWindow()
        self.interface.setupUi(self)
        #lien entre le bouton calcul et la fonction de calcul
        QtCore.QObject.connect( self.interface.calcul,QtCore.SIGNAL("clicked()"),self.calcul)
        #lien entre le bouton effacer et la fonction
        QtCore.QObject.connect( self.interface.raz,QtCore.SIGNAL("clicked()"),self.raz)
        #lien entre le bouton a propos et la fonction
        QtCore.QObject.connect( self.interface.apropos,QtCore.SIGNAL("clicked()"),self.apropos)
        #lien entre le bouton impression et la fonction
        QtCore.QObject.connect( self.interface.imprimer,QtCore.SIGNAL("clicked()"),self.impression)
        
        #définition du lien entre actionImprimer (menu) et l'action prévue (affichage pour l'instant d'un message)
        QtCore.QObject.connect(self.interface.actionImprimer,QtCore.SIGNAL("triggered()"),self.impression)
        
        #définition du lien entre actionQuiter et l'action quitter
        QtCore.QObject.connect(self.interface.actionQuitter,QtCore.SIGNAL("triggered()"),self.quit)
        
        #définition du lien entre actionA_propos (menu) et l'action prévue 
        QtCore.QObject.connect(self.interface.actionA_Propos,QtCore.SIGNAL("triggered()"),self.apropos)
       
    def calcul(self):
        ## Récupération du code de la version 0.3.1
                
        #fonction pour tester et récupérer les valeurs entrées dans les champs
        #en tenant compte d'une virgule éventuelle
        #retourne 1 si le champs est numérique, 0 si le champs n'est pas numérique,
        #         la valeur du champs
        #         1 si le champs est à calculer (champs vide ou non numérique), 0 si le champs est numérique 
        def estok (champs):
            #c = str(champs.text())
            c = champs.text()
            c = str(c.toUtf8())
            #traitement des champs vides: retourne champs non numérique, valeur 0, et champs à calculer
            if c == "":
                return 0, 0., 1
                
            #else:
                #acalculer = 0
            if ',' in c:
                    c=('.'.join(c.split(',')))
            try:
                z = float(c)
                ok = 1
                acalculer = 0
            except:
                z=0.
                ok = 0
                acalculer = 1
                champs.clear()
            return ok, z, acalculer

        
        ##
        #version 0.4.1
        
        #1) récupération des variables, détermination de leur statut OK ou non et du statut à calculer
        #tr_ indique que c'est une variable de travail
        tr_quantite = estok(self.interface.quantite)
        tr_volume = estok(self.interface.volume)
        tr_concentration = estok(self.interface.concentration)
        tr_poids = estok(self.interface.poids)
        tr_posologie = estok(self.interface.posologie)
        tr_debit = estok(self.interface.debit)
        
        #2) traitement de la concentration
        if (tr_quantite[0] and tr_volume[0])or tr_concentration[0]:
            if tr_quantite[0]and tr_volume[0]:
                concentration = tr_quantite [1]*1000/tr_volume[1]
                if tr_concentration[0]:
                    if round(concentration,1) != tr_concentration[1]:
                        self.interface.message.setHtml(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-family:Arial; font-size:12pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:Lucida Grande;\"><span style=\" font-size:10pt;\">Attention ! Il y a discordance entre les donn&eacute;es saisies !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                        return
            if tr_concentration[0]:
                concentration = tr_concentration[1]
            self.interface.concentration.clear ()
            self.interface.concentration.setText(",".join(str(round(concentration,1)).split("."))) # on insère dans le champs la valeur calculée
            tr_concentration = estok(self.interface.concentration)

        #3 calcul des autres paramètres
        #calcul de la concentration à partir des autres paramètres
        if tr_concentration[2] and ((tr_quantite[0] and tr_volume[0]) or (tr_poids[0] and tr_debit[0] and tr_posologie[0])):
            concentration = (tr_posologie[1] * tr_poids[1] * 60) / tr_debit[1]
            m = "<b>Concentration: </b>" + (",".join(str(round(concentration,1)).split("."))) + " &micro;g/ml"
        
        #calcul du débit
        elif tr_debit[2] and  (tr_concentration[0] and tr_poids[0] and tr_posologie[0]):            
            debit = (tr_posologie[1] * tr_poids[1] * 60) / tr_concentration[1]
            m = "<b>D&eacute;bit: </b>" + (",".join(str(round(debit,1)).split("."))) + " ml/h"

        #calcul du poids
        elif tr_poids[2] and (tr_concentration[0] and tr_debit[0] and tr_posologie[0]):
            poids = (tr_concentration[1] * tr_debit[1]) / (tr_posologie[1] * 60)
            m = "<b>Poids: </b>" + (",".join(str(round(poids,2)).split("."))) + " kg"
            
        #calcul de la posologie
        elif tr_posologie[2] and (tr_concentration[0] and tr_debit[0] and tr_poids[0]):
            posologie = (tr_concentration[1] * tr_debit[1]) / (tr_poids[1] * 60)
            m = "<b>Posologie: </b>" + (",".join(str(round(posologie,2)).split("."))) + " &micro;g/kg/min"
        else:
            m = "<b>Attention !</b> les donn&eacute;es sont insuffisantes pour d&eacute;terminer les param&egrave;tres"
            self.interface.message.setHtml(QtGui.QApplication.translate("MainWindow", m , None, QtGui.QApplication.UnicodeUTF8))     
            return
        
        self.interface.message.setHtml(QtGui.QApplication.translate("MainWindow", m , None, QtGui.QApplication.UnicodeUTF8))     
        #insertion des données saisies
        self.interface.message.append("") #Je n'ai pas trouvé d'autres moyens pour sauter une ligne. A revoir
        self.interface.message.append("<u>Donn&eacute;es initiales:</u>")
        if self.interface.quantite.text() != "":
            self.interface.message.append("<b>Quantit&eacute;: </b>" + self.interface.quantite.text()+ " mg")
        if self.interface.volume.text() != "":
            self.interface.message.append("<b>Volume: </b>" + self.interface.volume.text()+ " ml")
        if self.interface.concentration.text() != "":
            self.interface.message.append("<b>Concentration: </b>" + self.interface.concentration.text()+ " &micro;g/ml")
        if self.interface.poids.text() != "":
            self.interface.message.append("<b>Poids: </b>" + self.interface.poids.text()+ " Kg")
        if self.interface.posologie.text() != "":
            self.interface.message.append("<b>Posologie: </b>" + self.interface.posologie.text()+ " &micro;g/kg/min")
        if self.interface.debit.text() != "":
            self.interface.message.append("<b>D&eacute;bit: </b>" + self.interface.debit.text()+ " ml/h")
        return
    
    def apropos(self):
        ##Fenètre / Dialogue A propos
        m=QtCore.QString(self.tr("""Ce programme calcule le débit à  afficher sur une seringue électrique pour assurer une dose en µg/kg/min
        
21 octobre 2006 Romuald Riem

Ce programme ne comporte aucune garantie.  Il ne peut remplacer l'avis d'un professionnel qualifié
"""))
        
        QtGui.QMessageBox.about(self,self.tr("Débit SE"),m)
        
    #fonction d'impression
    #pour l'instant,n'imprime qu'une seule ligne de résultats
    def impression(self):
        document = self.interface.message.document()            
        imprimante = QtGui.QPrinter()
        
        dialogue = QtGui.QPrintDialog(imprimante,self)
        
        if dialogue.exec_() != QtGui.QDialog.Accepted:
            return
        document.print_(imprimante)
        self.statusBar().showMessage(self.tr("Pret"),2000)

        
    #fonction pour quitter
    def quit(self):
        self.close()
        
    #fonction de remise à zéro des champs
    def raz(self):
        self.interface.quantite.clear ()
        self.interface.quantite.setFocus ()
        self.interface.volume.clear ()
        self.interface.concentration.clear ()
        self.interface.poids.clear ()
        self.interface.posologie.clear ()
        self.interface.debit.clear ()
        self.interface.message.setHtml(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-family:Arial; font-size:12pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:Lucida Grande;\"><span style=\" font-size:10pt;\">Entrez les informations dont vous disposez et pressez  </span><span style=\" font-size:10pt; font-weight:600;\">Calculer</span><span style=\" font-size:10pt;\"> !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


    

#programme principal
app=QtGui.QApplication(sys.argv)
window=MyWindow()
window.show()
sys.exit(app.exec_())

