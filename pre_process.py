from nltk.tokenize import word_tokenize
from porter_stemmer import PorterStemmer
import sys , string

ps = PorterStemmer()

#opens a file and read it 
def read_file(file_name):
    file = open(file_name,"r")
    return file.read()

#removes punctuations from the document
def remove_punctuation(document):
    return document.translate(str.maketrans('', '', string.punctuation))

#removes digits from document
def remove_digits(document):
    return document.translate(str.maketrans('', '', string.digits))

#tokenize the words
def sentence_to_words(document):
    documents = document.split("\n")
    return [word_tokenize(doc) for doc in documents]

#preprocess the docs
def pre_process(document,stop_words):
    document  = remove_punctuation(document)
    documents = sentence_to_words(document)
    processed_doc = []
    for document in documents:
        if len(document) > 0:
            doc_no   = document[0]
            document = [word.lower() for word in document if word.lower() not in stop_words ]
            document = [ps.stem(word,0,len(word)-1) for word in document[1:]] # stemming 
            document = " ".join(document)  # list to str
            document = remove_digits(document)  
            document = doc_no + "\t" + document
            processed_doc.append(document)
    return processed_doc

#write output to file
def write_file(file_name,documents):
    file = open(file_name,"w")
    for document in documents:
        file.write(document + "\n")


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        input_file      = sys.argv[1]
        output_file     = sys.argv[2]
        stop_words_file = sys.argv[3]
        
        document   = read_file(input_file)
        stop_words = read_file(stop_words_file).split(",")
        document   = pre_process(document,stop_words) 
        write_file(output_file,document)
        
    