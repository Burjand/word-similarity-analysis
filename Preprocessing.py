from bs4 import BeautifulSoup
import nltk

class Preprocessing():

    def extract_text_from_file(file_path, encoding):

        file = open(file_path,"r", encoding=encoding)
        raw_file = file.readlines()
        file.close()

        raw_text = ""

        for line in raw_file:

            raw_text = raw_text + " " + line

        return raw_text
    

    def clean_text_from_html_tags(raw_text):

        soup = BeautifulSoup(raw_text)
        
        return soup.get_text()
    

    def remove_stopwords(tokenized_text, stopwords_file):

        file = open(stopwords_file,"r", encoding="UTF-8")
        stopwords = file.readlines()
        file.close()

        for word in tokenized_text:

            if (word)