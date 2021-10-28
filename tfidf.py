import sys
import math

#open file and read it
def read_file(file_name):
    file = open(file_name,"r")
    return file.read()

#generates tf idf 
#tf-idf = (freq of that term in a doc /max freq of doc) * ( log base 10(total doc/number of documents that contain that term ))

def generate_tfidf(document):
    doc_id = []
    maxfreq={}
    inverted_index = {}
    documents = document.split("\n")
    for document in documents:
        line = document.split(" ")
        if len(line) == 2:
            inverted_index[line[0]] = {}
            for count in line[1].split("\t"):
                count = count.split(",")     
                if len(count) == 2:
                    doc_id.append(count[0])
                    inverted_index[line[0]][count[0]] = int(count[1])
                    if count[0]  in  maxfreq:
                        if int(count[1]) > maxfreq[count[0]]:
                            maxfreq[count[0]]=int(count[1])
                    elif count[0] not in maxfreq:
                        maxfreq[count[0]] = int(count[1])


    docs_id = sorted(set(doc_id))

    if "Dquery" in docs_id:
        length=len(docs_id)-1
    else:
        length=len(docs_id)

    for word in inverted_index:
        
        if "Dquery" in inverted_index[word].keys():
            doc_freq = len(inverted_index[word].keys())-1
        else:
            doc_freq = len(inverted_index[word].keys())
        for doc_id in docs_id:
            if doc_id not in inverted_index[word]:
                inverted_index[word][doc_id] = 0
        
        for doc_id in inverted_index[word]:
            tf  = (inverted_index[word][doc_id]) / maxfreq[doc_id]
            idf = math.log10(length/doc_freq)
            tfidf = round(tf*idf,3)
            inverted_index[word][doc_id] = tfidf
    
    return inverted_index , docs_id

#writes output to file
def write_file(file_name,docs_id,tfidf):
    file = open(file_name,"w")
    file.write("".format().ljust(15))
    for doc_id in docs_id:
        file.write("{0}".format(doc_id).ljust(7))
    file.write("\n")
    for word in tfidf:
        file.write("{0}".format(word.ljust(15)))
        for doc_id in docs_id:
            file.write("{0}".format(str(tfidf[word][doc_id]).ljust(7)))
        file.write("\n")




if __name__ == '__main__':
    if len(sys.argv) >= 3:
        input_file      = sys.argv[1]
        output_file     = sys.argv[2]
        
        inverted_index = read_file(input_file)
        tfidf , docs_id = generate_tfidf(inverted_index)
        write_file(output_file,docs_id,tfidf)
        
    