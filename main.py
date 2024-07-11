import os
import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QSizePolicy
from epub_parser_ui import Ui_MainWindow
from epub_parser import EpubParser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.folder: str = None
        self.parser: EpubParser = None

        self.bookSelectButton.clicked.connect(self.select_book)
        self.moveChapterButton.clicked.connect(self.move_selected_chapter)
        self.exportJsonButton.clicked.connect(self.export_json)

    def select_book(self):
        '''Opens epub book selection dialog'''
        self.folder = QFileDialog.getOpenFileName(self, "Select book",
                                                  "", "EPUB (*.epub)")[0]
        print(self.folder)
        if not self.folder:
            return

        self.parser = EpubParser(self.folder)
        self.update_book_info()
        self.populate_chapters()
    
    def update_book_info(self):
        self.bookLanguage.setText(f'Language: {self.parser.language}')
        self.bookTitle.setText(f'Title: {self.parser.title}')
        self.bookCreator.setText(f'Author: {self.parser.author}')

        if self.parser.cover:
            image_bytes = self.parser.cover.get_content()
            self.bookCover.setPixmap(self.image_from_bytes(image_bytes))

    def image_from_bytes(self, image_bytes):
        byte_array = QtCore.QByteArray(image_bytes)
        buffer = QtCore.QBuffer(byte_array)
        buffer.open(QtCore.QIODevice.OpenModeFlag.ReadOnly)
        
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(buffer.data())
        
        return pixmap
    
    def populate_chapters(self):
        for i in reversed(range(self.scrollExcludedChaptersContents.layout().count())):
            self.scrollExcludedChaptersContents.layout().itemAt(i).widget().deleteLater()

        for i in reversed(range(self.scrollChaptersContents.layout().count())):
            self.scrollChaptersContents.layout().itemAt(i).widget().deleteLater()
        
        for chapter in self.parser.chapters.keys():
            chapter_button = QtWidgets.QPushButton(chapter, self)

            lambda_ = self.create_lambda(chapter)
            chapter_button.clicked.connect(lambda_)
            self.scrollChaptersContents.layout().addWidget(chapter_button)
        
        for chapter in self.parser.excluded_chapters.keys():
            chapter_button = QtWidgets.QPushButton(chapter, self)

            lambda_ = self.create_lambda(chapter)
            chapter_button.clicked.connect(lambda_)
            layout = self.scrollExcludedChaptersContents.layout()
            layout.addWidget(chapter_button)
    
    def display_chapter(self, chapter):
        self.chapterTitle.setText(chapter)
        if chapter in self.parser.excluded_chapters.keys():
            self.chapterTextLabel.setText(self.parser.excluded_chapters[chapter])
        else:
            self.chapterTextLabel.setText(self.parser.chapters[chapter])
        print(f'Displaying {chapter}')

    def create_lambda(self, chapter):
        '''Creates lambda function for each button'''
        return lambda: self.display_chapter(chapter)
    
    def move_selected_chapter(self):
        cur_chapter = self.chapterTitle.text()
        if cur_chapter in self.parser.chapters:
            self.parser.exclude_chapter(cur_chapter)
        else:
            self.parser.include_chapter(cur_chapter)
        self.populate_chapters()

    def export_json(self):
        '''Opens json save dialog'''
        self.folder = QFileDialog.getSaveFileName(self, "Select book",
                                                  "", "Json (*.json)")[0]
        print(self.folder)
        if not self.folder:
            return
        self.parser.export_to_json(self.folder)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())