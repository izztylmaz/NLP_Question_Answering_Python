from bs4 import BeautifulSoup
from bs4 import Comment


class PreProcessor:
    def __init__(self, raw_data, f_name, f_type):
        self.decoders = {
            "html": self.__html_decode,
            "txt": self.__txt_decode,
            "pdf": self.__pdf_decode
        }

        self.data = self.decoders[f_type](raw_data)
        self.processing_data = self.data if self.data is str else self.data["body"]

        self.paragraphs = list()
        self.sentences = list()
        self.words = dict()

        # print("<meta charset=\"utf-8\">" in str(raw_data))
        # print(str(raw_data)[str(raw_data).find("charset"):])
        # print(type(str(raw_data)))
        # print(str(raw_data))

    def __del__(self):
        pass

    def __html_decode(self, raw_data):
        def tag_visible(element):
            if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                return False
            if isinstance(element, Comment):
                return False
            return True

        def text_from_html(body):
            soup = BeautifulSoup(body, 'html.parser')
            texts = soup.findAll(text=True)
            visible_texts = filter(tag_visible, texts)
            return " ".join(t.strip() for t in visible_texts)

        raw_data = raw_data.decode("utf-8")
        # print(text_from_html(raw_data[raw_data.find("<body"):raw_data.find("</body>") + 7]))
        return {
            "info": raw_data[:raw_data.find("<head")],
            "head": raw_data[raw_data.find("<head"):raw_data.find("</head>") + 7],
            # "body": raw_data[raw_data.find("<body"):raw_data.find("</body>") + 7],
            "body": text_from_html(raw_data[raw_data.find("<body"):raw_data.find("</body>") + 7]),
            "footer": raw_data[raw_data.find("<footer"):raw_data.find("</footer>") + 9]
        }

    def __txt_decode(self, raw_data):
        return raw_data

    def __pdf_decode(self, raw_data):
        return raw_data

    def __split_into_sentences(self):
        return list(filter(lambda x: x != '', self.data.split('\n\n')))

    def split_into_paragraphs(self):
        return list(filter(lambda x: x != '', self.processing_data.split('\n\n')))
