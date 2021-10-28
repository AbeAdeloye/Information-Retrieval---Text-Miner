import sys
import math
import numpy,re

#opens and read file
def read_file(file_name):
    file = open(file_name,"r")
    return file.read()

#calculate cosine similarity of two vectors
def cosine_similarity(tfidf,doc_id_1,doc_id_2):
    x = []
    y = []
    tfidf = tfidf.split("\n")[1:]
    for line in tfidf:
        line = re.sub(r"\s+", " ",line).strip().split(" ")
        if len(line) > 1:
            x.append(float(line[int(doc_id_1[1])]))
            y.append(float(line[int(doc_id_2[1])]))
    
    x = numpy.array(x)
    y = numpy.array(y)
    x_dot_y = numpy.dot(x,y)
    
    mag_x   = numpy.linalg.norm(x)
    mag_y   = numpy.linalg.norm(y)
    
    z=mag_x*mag_y
    if z != 0:
        return x_dot_y / (mag_x*mag_y)
    elif z==0:
        return (0.0)



if __name__ == '__main__':
    if len(sys.argv) >= 4:
        input_file = sys.argv[1]
        doc_id_1   = sys.argv[2]
        doc_id_2   = sys.argv[3]
        
        tfidf = read_file(input_file)
        print(round(cosine_similarity(tfidf,doc_id_1,doc_id_2),3))
        
    
