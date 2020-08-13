import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest


def text_summarizer(raw_docx):
    raw_text = raw_docx
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency
# word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Calculate Sentence Score and Ranking
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Find N Largest
    summary_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summary_sentences ]
    summary = ' '.join(final_sentences)
    return [raw_docx, len(raw_docx), summary, len(summary)]

# Reading Time
def reading_time(docs):
    nlp = spacy.load('en_core_web_sm')
    total_words_tokens =  [ token.text for token in nlp(docs)]
    estimatedtime  = len(total_words_tokens)/200
    time = round(estimatedtime)
    if time==0:
        time=1
    return '{} mins'.format(time)