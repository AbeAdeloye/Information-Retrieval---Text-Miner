from pre_process import pre_process
from inverted_index import generate_inverted_index
from tfidf import generate_tfidf
import sys , numpy


def read_file(file_name):
    file = open(file_name,"r")
    return file.read()

def convert_to_str(inv_index):
    dump = ""
    for word in inv_index:
        dump += word + " "
        doc_count = inv_index[word]
        for count in doc_count:
            dump += count + "," +str(doc_count[count]) + "\t"
        dump += "\n"
    return dump

if __name__ == '__main__':
    stop_word_file = "stopword.txt"
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        query      = sys.argv[2]
        
        # process corpus

        document   = read_file(input_file)
        document   = document + "\nDquery " + query
        stop_words = read_file(stop_word_file).split(",")
        documents  = pre_process(document,stop_words)
        document   = "\n".join(documents)
        
        inv_index           = generate_inverted_index(document)
        inv_index           = convert_to_str(inv_index)

        tf_idf  , docs_id   = generate_tfidf(inv_index)

        tfidf_doc   = {}
        tfidf_query = []

        for word in tf_idf:
            for doc_id in docs_id:
                if doc_id == "Dquery":
                    tfidf_query.append(tf_idf[word][doc_id])
                else:
                    if doc_id not in tfidf_doc:
                        tfidf_doc[doc_id] = []
                    tfidf_doc[doc_id].append(tf_idf[word][doc_id])
        
        cosine_sim = {}

        for doc_id in tfidf_doc:

            x = numpy.array(tfidf_doc[doc_id])
            y = numpy.array(tfidf_query)
            x_dot_y = numpy.dot(x,y)
            
            mag_x   = numpy.linalg.norm(x)
            mag_y   = numpy.linalg.norm(y)

            z=mag_x*mag_y
            if z != 0:
                cosine_sim[doc_id] = x_dot_y / (mag_x*mag_y)
            elif z==0:
                cosine_sim[doc_id] = 0.0

        cosine_sim = sorted(cosine_sim.items(), key=lambda x: x[1],reverse=True)
        for doc_id , score in cosine_sim:
            print(doc_id ,round(score,3) )