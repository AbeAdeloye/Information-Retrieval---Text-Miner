## System Requirements: 
<p>Windows with Python 3.9.2 installed.
<p>Coding Language and version:
 Python 3.9.2
<p>List of files in the application: 
<li>porter_stemmer.py	
<li>pre_process.py
<li>inverted_index.py
<li>tfidf.py
<li>cosine_sim.py
<li>ir_system.py
<li>input.txt          		(sample input file for checking)
<li>stopword.txt		(small file of stop words created manually )
 

## Instructions to Run Program
### 1. PREPROCESSING:
python .\pre_process.py .\input.txt .\pre_processed.txt .\stopword.txt

Expected file format:

<b>input.txt</b>

D1 This is a sample document, it has less document then the first one.
D2 This is a name of second sample document. This one has more sentences than a sample document first.
D3 The name of the sample document is spaced by a TAB character! all docs are on a single line

<b>pre_processed.txt</b>

D1	sampl document less document first
D2	name second sampl document more sentenc than sampl document first
D3	name sampl document space tab charact doc singl line




### 2. INVERTED INDEX:
python .\inverted_index.py .\pre_processed.txt .\inverted_indexed.txt

Expected file format:

<b>pre_processed.txt </b>

D1	sampl document less document first
D2	name second sampl document more sentenc than sampl document first
D3	name sampl document space tab charact doc singl line

<b>inverted_indexed.txt </b>

sampl D1,1	D2,2	D3,1	
document D1,2	D2,2	D3,1	
less D1,1	
first D1,1	D2,1	
name D2,1	D3,1	
second D2,1	
more D2,1	
sentenc D2,1	
than D2,1	
space D3,1	
tab D3,1	
charact D3,1	
doc D3,1	
singl D3,1	
line D3,1	assign	D3,1
challeng	D4,1	D6,1
barrier	D5,1





### 3. TF-IDF:
python .\tfidf.py .\inverted_indexed.txt .\tfidf.txt

Expected file format:

<b>inverted_indexed.txt </b>

sampl D1,1	D2,2	D3,1	
document D1,2	D2,2	D3,1	
less D1,1	
first D1,1	D2,1	
name D2,1	D3,1	
second D2,1	
more D2,1	
sentenc D2,1	
than D2,1	
space D3,1	
tab D3,1	
charact D3,1	
doc D3,1	
singl D3,1	
line D3,1	

<b>tfidf.txt </b>

               D1     D2     D3     
sampl          0.0    0.0    0.0    
document       0.0    0.0    0.0    
less           0.239  0.0    0.0    
first          0.088  0.088  0.0    
name           0.0    0.088  0.176  
second         0.0    0.239  0.0    
more           0.0    0.239  0.0    
sentenc        0.0    0.239  0.0    
than           0.0    0.239  0.0    
space          0.0    0.0    0.477  
tab            0.0    0.0    0.477  
charact        0.0    0.0    0.477  
doc            0.0    0.0    0.477  
singl          0.0    0.0    0.477  
line           0.0    0.0    0.477  




### 4. COSINE:
python .\cosine_sim.py .\tfidf.txt D1 D2

Expected file format:

<b> tfidf.txt </b>

               D1     D2     D3     
sampl          0.0    0.0    0.0    
document       0.0    0.0    0.0    
less           0.239  0.0    0.0    
first          0.088  0.088  0.0    
name           0.0    0.088  0.176  
second         0.0    0.239  0.0    
more           0.0    0.239  0.0    
sentenc        0.0    0.239  0.0    
than           0.0    0.239  0.0    
space          0.0    0.0    0.477  
tab            0.0    0.0    0.477  
charact        0.0    0.0    0.477  
doc            0.0    0.0    0.477  
singl          0.0    0.0    0.477  
line           0.0    0.0    0.477  

Output on cmd:
0.062




### 5. IR SYSTEM:
python .\ir_system.py .\input.txt "first"

Expected input file format:

<b>input.txt </b>

D1 This is a sample document, it has less document then the first one.
D2 This is a name of second sample document. This one has more sentences than a sample document first.
D3 The name of the sample document is spaced by a TAB character! all docs are on a single line

<b>Output on cmd: </b>

D1 0.346
D2 0.178
D3 0.0
