from Preprocessing import Preprocessing
import nltk


if __name__ == "__main__":

    # Extract text from file
    raw_text = Preprocessing.extract_text_from_file("e990519_mod.htm", "UTF-8")    

    # Preprocessing
    # Clean text from HTML tags
    no_html_text = Preprocessing.clean_text_from_html_tags(raw_text)

    # Tokenize
    #nltk.download('punkt_tab')
    tokenized_text = nltk.word_tokenize(no_html_text)

    # Lower case
    for i in range(len(tokenized_text)): tokenized_text[i] = tokenized_text[i].lower()    

    # Clean text from stopwords
    tokenized_text = Preprocessing.remove_stopwords(tokenized_text,"stopwords_es.txt")

    # Obtain vocabulary
    vocabulary = set(tokenized_text)


    print(tokenized_text)

    
