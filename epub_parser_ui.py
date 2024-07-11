# Form implementation generated from reading ui file 'epub-parser.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 608)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.scrollChapters = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollChapters.setWidgetResizable(True)
        self.scrollChapters.setObjectName("scrollChapters")
        self.scrollChaptersContents = QtWidgets.QWidget()
        self.scrollChaptersContents.setGeometry(QtCore.QRect(0, 0, 154, 558))
        self.scrollChaptersContents.setObjectName("scrollChaptersContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollChaptersContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollChapters.setWidget(self.scrollChaptersContents)
        self.verticalLayout.addWidget(self.scrollChapters)
        self.verticalLayout.setStretch(2, 4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.chapterTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.chapterTitle.setText("")
        self.chapterTitle.setObjectName("chapterTitle")
        self.verticalLayout_3.addWidget(self.chapterTitle)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 312, 510))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chapterTextLabel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.chapterTextLabel.setText("")
        self.chapterTextLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.chapterTextLabel.setWordWrap(True)
        self.chapterTextLabel.setObjectName("chapterTextLabel")
        self.verticalLayout_7.addWidget(self.chapterTextLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.moveChapterButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.moveChapterButton.setObjectName("moveChapterButton")
        self.verticalLayout_3.addWidget(self.moveChapterButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.bookTitle = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookTitle.sizePolicy().hasHeightForWidth())
        self.bookTitle.setSizePolicy(sizePolicy)
        self.bookTitle.setObjectName("bookTitle")
        self.verticalLayout_2.addWidget(self.bookTitle)
        self.bookCreator = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookCreator.sizePolicy().hasHeightForWidth())
        self.bookCreator.setSizePolicy(sizePolicy)
        self.bookCreator.setObjectName("bookCreator")
        self.verticalLayout_2.addWidget(self.bookCreator)
        self.bookLanguage = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookLanguage.sizePolicy().hasHeightForWidth())
        self.bookLanguage.setSizePolicy(sizePolicy)
        self.bookLanguage.setObjectName("bookLanguage")
        self.verticalLayout_2.addWidget(self.bookLanguage)
        self.bookCover = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookCover.sizePolicy().hasHeightForWidth())
        self.bookCover.setSizePolicy(sizePolicy)
        self.bookCover.setMaximumSize(QtCore.QSize(80, 120))
        self.bookCover.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bookCover.setText("")
        self.bookCover.setPixmap(QtGui.QPixmap(":/no-image/F:/PersonalStuff/Screenshots/Dexter/0a5cfe22b33051829d731e6b126f4262.jpg"))
        self.bookCover.setScaledContents(True)
        self.bookCover.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bookCover.setObjectName("bookCover")
        self.verticalLayout_2.addWidget(self.bookCover)
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.bookSelectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookSelectButton.sizePolicy().hasHeightForWidth())
        self.bookSelectButton.setSizePolicy(sizePolicy)
        self.bookSelectButton.setObjectName("bookSelectButton")
        self.verticalLayout_2.addWidget(self.bookSelectButton)
        self.exportJsonButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exportJsonButton.setObjectName("exportJsonButton")
        self.verticalLayout_2.addWidget(self.exportJsonButton)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.scrollExcludeChapters = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollExcludeChapters.setWidgetResizable(True)
        self.scrollExcludeChapters.setObjectName("scrollExcludeChapters")
        self.scrollExcludedChaptersContents = QtWidgets.QWidget()
        self.scrollExcludedChaptersContents.setGeometry(QtCore.QRect(0, 0, 154, 396))
        self.scrollExcludedChaptersContents.setObjectName("scrollExcludedChaptersContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollExcludedChaptersContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollExcludeChapters.setWidget(self.scrollExcludedChaptersContents)
        self.verticalLayout_2.addWidget(self.scrollExcludeChapters)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Epub parser"))
        self.label.setText(_translate("MainWindow", "Available Chapters"))
        self.label_3.setText(_translate("MainWindow", "Chapter Info"))
        self.moveChapterButton.setText(_translate("MainWindow", "Remove/Restore"))
        self.label_4.setText(_translate("MainWindow", "Book Info"))
        self.bookTitle.setText(_translate("MainWindow", "Title: "))
        self.bookCreator.setText(_translate("MainWindow", "Author:"))
        self.bookLanguage.setText(_translate("MainWindow", "Language:"))
        self.bookSelectButton.setText(_translate("MainWindow", "Select Book"))
        self.exportJsonButton.setText(_translate("MainWindow", "Export Json"))
        self.label_2.setText(_translate("MainWindow", "Excluded From Export"))
