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

    """
    nlp = spacy.load('es_core_news_md')

    for i in range(len(tokenized_text)):

        minidoc = nlp(tokenized_text[i])
        tokens = [str(token) for token in minidoc]
        tokenized_text[i] = ' '.join(tokens)
    """

print(tokenized_text)