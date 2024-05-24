from genericpath import exists
from itertools import count
import os
from string import punctuation
import math
from typing import Mapping
import numpy as np
from functools import partial
from scipy import sparse
import pickle
import preprocessing
from tqdm import tqdm

current_directory = os.getcwd()
path = current_directory
os.chdir(path)

def booleanSearch(Dict, query):
    
    i = 0
    result = []
    
    if len(query) == 1:
        if query[0] in Dict.keys():
            result = set(Dict[query[0]])
    else:
        for word in query:
            if word == "and":
                if query[i-1] in Dict.keys() and query[i+1] in Dict.keys():
                    result = list(set(Dict[query[i-1]]) & set(Dict[query[i+1]]))           
                else:          
                    return print("Termo(s) não encontrado(s)!")
            i+=1
     
    x = 1        
    for file in sorted(os.listdir()):
        if x in result:
             print(file)
        x+=1
    
#função que realiza a busca vetorial
def vetorialSearch(document, Dict, tf_idf, query):
    queryVector = []
    wordFrequency = {}
    
    
    for word in query:
  
        if(word not in wordFrequency):
            wordFrequency[word] = 1
        else:
            wordFrequency[word] += 1
            
    for term in Dict:
        if term in wordFrequency:
            tf_idf_query = (1 + np.log10(wordFrequency[term])) * np.log10((len(document) / len(Dict[word])))
            tf_idf_query = np.around(tf_idf_query, 2)
            queryVector.append(tf_idf_query)
            
    result = []
    
    normQuery = [queryVector[i] for i in range(len(queryVector))]
    normQuery = np.sum(normQuery, dtype = np.float32)
    
    
    for doc in tf_idf.keys():
        normDoc = [i**2 for i in tf_idf[doc]]
        normDoc = np.sum(normDoc, dtype = np.float32)
        
        norm = math.sqrt(normDoc) * math.sqrt(normQuery)
        result.append(np.dot(tf_idf[doc], queryVector) / norm) 
        
    aux = 1
    print("Rankeamento dos documentos baseado na busca:")
    for i in range(len(result)):
       # if result[i] > 0.7:    
        print("Doc",aux,": " ,np.unique(np.around(result[i], 2)))    
        aux +=1

def main():
    
    doc_load = open("Documents.pkl", "rb")
    doc_load = pickle.load(doc_load)
    Documents = doc_load
    
    dict_load = open("Dict.pkl", "rb")
    dict_load = pickle.load(dict_load)
    Dict = dict(dict_load)
    
    tf_idf_load = open("Tf_idf.pkl", "rb")
    tf_idf_load = pickle.load(tf_idf_load)
    tf_idf = dict(tf_idf_load)
    
    print("Escolha em qual modelo deseja realizar a busca")
    print("1- Modelo Booleano\n2- Modelo Vetorial")
    model = input()
    model = int(model)
    
    if model == 1:
        print("Insira o termo que deseja procurar\nOBS: para pesquisas com mais de um termo utilize o operando 'and' entre os termos desejados\nEx: 'universidade and curso'")
        term = input()
        term = preprocessing.tokenize(term)
        term = preprocessing.filter(term)
        booleanSearch(Dict, term)
    elif model == 2:
        print("Insira o termo que deseja procurar:\n")
        term = input()
        term = preprocessing.tokenize(term)
        term = preprocessing.filter(term)
        vetorialSearch(Documents, Dict, tf_idf, term)
    


if __name__ == "__main__":
    main()
