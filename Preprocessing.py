from bs4 import BeautifulSoup
from Math_tools import Math_tools

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
        stopwords_raw = file.readlines()
        file.close()

        stopwords_list = []

        for word in stopwords_raw: stopwords_list.append(word.replace("\n",""))

        tokenized_text_no_stopwords = []

        for i in range(len(tokenized_text)):

            if (Math_tools.is_string_number_hollistic(tokenized_text[i])):

                continue

            if (tokenized_text[i] not in stopwords_list):

                tokenized_text_no_stopwords.append(tokenized_text[i])

        return tokenized_text_no_stopwords
    
    
    def remove_punctuation_marks(tokenized_text, punctuation_marks_file):

        file = open(punctuation_marks_file,"r", encoding="UTF-8")
        punctuation_marks_raw = file.readlines()
        file.close()

        punctuation_marks_list = []
        for item in punctuation_marks_raw: punctuation_marks_list.append(item.replace("\n",""))


        tokenized_text_no_punctuation = []

        for i in range(len(tokenized_text)):

            if (tokenized_text[i] not in punctuation_marks_list):

                tokenized_text_no_punctuation.append(tokenized_text[i])

        return tokenized_text_no_punctuation

