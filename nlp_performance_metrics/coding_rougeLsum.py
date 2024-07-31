import nltk
import six
# from rouge import tokenizers
from nltk.stem import porter

"""
DefaultTokenizer : which tokenized on whitespaces
use_stemmer = whether Porter stemmer should be used to strip word suffixes to improve matching

tokenize:
tokenize input text into list of tokens
A text blob to tokenize
stemmer: optional if yes then Porternstemmer
all text lower cased
replacing any non alpha num character with space

"""

def get_rougeLsum():
    return 0


# does not support multiline text
def get_sents(text):
    # split_summaries = whether to add new lines between sentences for rougeLsum
    if split_summaries:
        ## when you are not sure that your text is seperated by newlines 
        sents = nltk.sent_tokenize(text)
    else:
        # when you are sure that your text is seperated by newline for each new sentence
        sents =six.ensure_str(text).split("\n")
        
    # sents is list of sentences from the texts    
    return sents      

from rouge_score import rouge_scorer

if __name__ == "__main__":
    ## We do not do pre comput target tokens and prediction tokens 
    # so target tokens and prediction tokesn = None
    # split_summaries = True
    prediction = "Transformers Transformers are fast plus efficient. They have changed trajectory of data science"
    reference = "HuggingFace Transformers are fast efficient plus awesome. They truley have changed Data science trajectory"
    # result = nltk.sent_tokenize(prediction)
    # print(f"Sentence tokenized result ---> {len(result)}")

    # result_1 = six.ensure_str(prediction).split("\n")
    # print(f"Sentence six result ---> {result_1}")
    scorer = rouge_scorer.RougeScorer(rouge_types= [ 'rougeLsum'],split_summaries=True)

    results = scorer.score(target= reference, prediction= prediction)


