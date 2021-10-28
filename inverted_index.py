from nltk.tokenize import word_tokenize
import sys

#open and reads a file
def read_file(file_name):
    file = open(file_name,"r")
    return file.read();

#writes to output file
def write_file(file_name,document):
    file = open(file_name,"w")
    for word in document:
        file.write(word + " ")
        for count in document[word]:
            file.write(count + "," + str(document[word][count]) + "\t")
        file.write("\n")

#tokenize the words
def sentence_to_words(document):
    documents = document.split("\n")
    return [word_tokenize(doc) for doc in documents]

#generates inverted index
def generate_inverted_index(document):
    documents =sentence_to_words(document)
    vocab = {}
    for document in documents:
        if len(document) > 0:
            doc_no   = document[0]
            document = document[1:]
            for word in document:
                if word in vocab:
                    if doc_no in vocab[word]:
                        vocab[word][doc_no] += 1
                    else:
                        vocab[word][doc_no] = 1
                else:
                    vocab[word] = {doc_no:1}
    return vocab

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        input_file      = sys.argv[1]
        output_file     = sys.argv[2]
        
        document = read_file(input_file)
        document = generate_inverted_index(document)
        write_file(output_file,document)
        
    