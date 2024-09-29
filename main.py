from Preprocessing import Preprocessing
import nltk
import spacy


if __name__ == "__main__":

    # Extract text from file
    raw_text = Preprocessing.extract_text_from_file("e990519_mod.htm", "UTF-8")

    # Preprocessing
    # Clean text from HTML tags
    no_html_text = Preprocessing.clean_text_from_html_tags(raw_text)

    # Tokenize
    tokenized_text = nltk.word_tokenize(no_html_text)


    # Lower case
    for i in range(len(tokenized_text)): tokenized_text[i] = tokenized_text[i].lower()    

    # Clean text from stopwords
    tokenized_text_no_stopwords = Preprocessing.remove_stopwords(tokenized_text,"stopwords_es.txt")

    # Clean text from punctuation marks
    tokenized_text_no_stopwords_no_punctuation = Preprocessing.remove_punctuation_marks(tokenized_text_no_stopwords,"punctuation_marks_es.txt")

    # Obtain vocabulary
    vocabulary = set(tokenized_text_no_stopwords_no_punctuation)

    # Import NLP model es_core_news_md
    text_to_lemmatize = " ".join(str(word) for word in tokenized_text_no_stopwords_no_punctuation)

    nlp = spacy.load('es_core_news_md')
    spacy_document = nlp(text_to_lemmatize)

    # POS tagging
    tokenized_text_pos_tagged = []

    for token in spacy_document:

        tokenized_text_pos_tagged.append([token,token.pos_])

    # Lemmatization
    lemmatized_tokens = []

    for token in spacy_document:

        lemmatized_tokens.append([token.lemma_])\

    lemmatized_text = ""

    for item in lemmatized_tokens:

        lemmatized_text = lemmatized_text + " " + item[0]
    
    
    print(lemmatized_text)

    
