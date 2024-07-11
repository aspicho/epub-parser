from html.parser import HTMLParser
import json
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

class EpubParser:
    def __init__(self, path: str):
        self.title: str = None
        self.author: str = None
        self.language: str = None
        self.cover = None
        self.chapters: dict = {}
        self.excluded_chapters: dict = {}
        self.book: epub.EpubBook
        self.file_names: dict = {}
        self.path = path
        self.parse()

    def parse(self):
        self.book = epub.read_epub(self.path)
        self.title = self.book.get_metadata('DC', 'title')[0][0]
        self.author = self.book.get_metadata('DC', 'creator')[0][0]
        self.language = self.book.get_metadata('DC', 'language')[0][0]
        self.cover = None

        for item in self.book.get_items_of_type(ebooklib.ITEM_IMAGE):
            if not item:
                continue
            if 'cover' in item.file_name:
                self.cover = item

        for c in self.book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            file_name = c.get_name()
            if '/' in file_name:
                file_name = file_name.split('/')[-1]

            self.chapters[file_name] = self.chapter_to_str(c)
            self.file_names_from_href(c)

        self.reneme_chapters_by_file_names()

    def chapter_to_str(self, chapter):
        soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
        text = [para.get_text() for para in soup.find_all('p')]
        return ' '.join(text)
    
    def file_names_from_href(self, chapter):
        soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
        hrefs = soup.find_all('a')
        if not hrefs:
            return None
        
        if not hrefs[0].get('href'):
            return None
        
        for i in range(len(hrefs)):
            try:
                file_name = hrefs[i].get('href').split('#')[0]
                if '.html' not in file_name:
                    continue
                self.file_names[file_name] = hrefs[i].text
            except Exception:
                continue

    def reneme_chapters_by_file_names(self):
        for file in self.file_names.keys():
            new_name = self.file_names[file]
            self.chapters[new_name] = self.chapters[file]
            del self.chapters[file]

    def export_to_json(self, save_path: str):
        with open(save_path, 'w') as f:
            f.write(json.dumps(self.chapters))
    
    def exclude_chapter(self, chapter):
        if chapter not in self.chapters:
            return
        self.excluded_chapters[chapter] = self.chapters[chapter]
        del self.chapters[chapter]
    
    def include_chapter(self, chapter):
        if chapter not in self.excluded_chapters:
            return
        self.chapters[chapter] = self.excluded_chapters[chapter]
        del self.excluded_chapters[chapter]
    
    def rename_chapter(self, oldname, newname):
        if oldname == newname:
            return

        if (oldname in self.excluded_chapters 
            and newname not in self.excluded_chapters):
            self.excluded_chapters[newname] = self.excluded_chapters[oldname]
            del self.excluded_chapters[oldname]

        if (oldname in self.chapters and newname not in self.chapters):
            self.chapters[newname] = self.chapters[oldname]
            del self.chapters[oldname]




if __name__ == '__main__':
    parser = EpubParser('test.epub')
    print(parser.author)
    print(parser.language)
    print(parser.title)
    print(parser.file_names)
    with open('cover.png', 'wb') as f:
        f.write(parser.cover.get_content())


