import re
import nltk

# TODO: Fix pathing of this
try:
    nltk.data.find('stopwords')
    nltk.data.find('wordnet')
    nltk.data.find('averaged_perceptron_tagger')
except LookupError:
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords, \
    wordnet
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

from text_expressions.emoticons_dict import EMOTICONS
from text_expressions.emojis_dict import UNICODE_EMO
from text_expressions.slang import SLANG_LIST, SLANG_DICT


# TODO: Improve docstrings
class TextPreprocessor:
    """Class containing typical functions for text preprocessing.
    Can call preprocessing functions as so desired.
    Args:
        - text(str)
    Ref:
        - https://www.kaggle.com/sudalairajkumar/getting-started-with-text-preprocessing
    """
    def __init__(self, text: str):
        self.text = text
        
    def _make_lowercase(self):
        self.text = self.text.lower()
        
    def _remove_punctuation(self):
        """Note: We do not include '@' or because it is used to reference 
        other twitter accounts
        """
        punctuation_to_remove="\"\!#$%&\'()*+,-./:;<=>?[\\]^_{|}~`"
        self.text = self.text.translate(
            str.maketrans('', '', punctuation_to_remove)
        )
    
    def _remove_stopwords(self):
        nltk_stopwords = set(stopwords.words('english'))
        self.text = " ".join([
            word for word in str(self.text).split() if word not in nltk_stopwords
        ])
        
    def _stem(self):
        """Note: Can also use SnowballStemmer for languages other than English
        """
        stemmer = PorterStemmer()
        self.text = " ".join([stemmer.stem(word) for word in self.text.split()])
        
    def _lemmatize(self):
        """Note: Different Lemmatizing options: N (noun), 
        V (verb), J (adjective) and R (adverb)
        """
        lemmatizer = WordNetLemmatizer()
        wordnet_map = {
            "N":wordnet.NOUN, 
            "V":wordnet.VERB, 
            "J":wordnet.ADJ, 
            "R":wordnet.ADV
        }
        pos_tagged_text = nltk.pos_tag(self.text.split())
        self.text = " ".join([
            lemmatizer.lemmatize(
                word, wordnet_map.get(pos[0], wordnet.NOUN)
            ) for word, pos in pos_tagged_text
        ])
        
    def _remove_emojis(self):
        """Ref: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
        """
        emoji_pattern = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       "]+", flags=re.UNICODE
                                  )
        self.text = emoji_pattern.sub(r'', self.text)
        
    def _convert_emojis_to_words(self):
        for emoji in UNICODE_EMO:
            self.text = re.sub(
                r'('+emoji+')', 
                "_".join(UNICODE_EMO[emoji].replace(",","").replace(":","").split()), 
                self.text
            )
        
    def _remove_emoticons(self):
        emoticon_pattern = re.compile(
            u'(' + u'|'.join(k for k in EMOTICONS) + u')'
        )
        self.text = emoticon_pattern.sub(r'', self.text)
        
    def _convert_emoticons_to_words(self):
        for emoticon in EMOTICONS:
            self.text = re.sub(
                u'('+emoticon+')', 
                "_".join(EMOTICONS[emoticon].replace(",","").split()), 
                self.text
            )
        
    def _remove_urls(self):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self.text = url_pattern.sub(r'', self.text)
        
    def _remove_html_tags(self):
        html_pattern = re.compile('<.*?>')
        self.text = html_pattern.sub(r'', self.text)

    def _remove_slang(self):
        new_text = []
        for w in self.text.split():
            if w.upper() in SLANG_LIST:
                continue
            else:
                new_text.append(w)
            
        self.text = " ".join(new_text)
    
    def _spellcheck(self):
        spellchecker = SpellChecker()
        corrected_text = []
        
        misspelled_words = spellchecker.unknown(self.text.split())
        
        for word in self.text.split():
            if word in misspelled_words:
                corrected_text.append(spellchecker.correction(word))
            else:
                corrected_text.append(word)
                
        self.text = " ".join(corrected_text)
    

def stanford_NER(text):
    """
    Tokenise words then apply stanford NER
    """

    # Tokenise words then apply Stanford NER Tagger

    # from nltk.tag import StanfordNERTagger
    # from nltk.tokenize import word_tokenize

    # st = StanfordNERTagger('/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
    #                        '/usr/share/stanford-ner/stanford-ner.jar',
    #                        encoding='utf-8')

    # tokenized_text = word_tokenize(text)
    # classified_text = st.tag(tokenized_text)

    # print(classified_text)
    return stanford_NER_tagged_Text


def apply_hashtag_preprocessing(hashtag:str) -> str:
    """Simply makes lowercase and removes punctuation from hashtags
    Args:
        - hashtag (str)
    Returns:
        - processed_hashtag (str)
    """
    hashtag_txt = TextPreprocessor(hashtag)

    # Apply preprocessing steps
    hashtag_txt._make_lowercase()
    hashtag_txt._remove_punctuation()
    
    return hashtag_txt.text


def apply_tweet_text_preprocessing(text: str) -> str:
    """Make Text Preprocessor object and apply some basic techniques to preprocess tweet text.
    Args:
        - text(str)
    Returns:
        - preprocessed_text(str)
    Note:
        - We opt for lemmatizing in this use case, just that the example output looks better.
        Would require more samples to be sure.
        - We opt for removing emoticons and emojis than converting to words as we want to have
        a simple model to begin with and conversion may not be so greatly depicted in tweets.
        May be for other use cases
        - Keeping slang as it may contain important nuances.
    """
    
    txt_sample = TextPreprocessor(text)

    # Apply preprocessing steps
    txt_sample._make_lowercase()
    txt_sample._remove_punctuation()
    txt_sample._remove_stopwords()
    txt_sample._lemmatize()
    txt_sample._remove_emojis()
    txt_sample._remove_emoticons()
    txt_sample._remove_urls()
    txt_sample._remove_html_tags()
    txt_sample._spellcheck()
    
    return txt_sample.text