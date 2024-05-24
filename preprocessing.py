from genericpath import exists
import os
from string import punctuation
from functools import partial
import pickle
from tqdm import tqdm
import numpy as np

current_directory = os.getcwd()
path = current_directory +"/Trab1/Texts/"
os.chdir(path)

#funcao que le o documento recebido
def readDoc (file):
    open_latin = partial(open, encoding='latin-1')
    
    with open_latin(file) as outputfile:
        text = outputfile.read()
        return text

#funcao para tokenizar o documento
def tokenize(file):
    return file.split()

#funcao que remove stopwords do documento
def remove_stopwords(document):
    tokens_filtered= [word for word in document if not word in stopwords ]
    return tokens_filtered

#funcao que remove pontuacao do documento
def remove_punctuation(document):
    output = []
    
    for word in document:
        for letter in word:
            if letter in punctuation:
                word = word.replace(letter,"")   
        output.append(word)
    return output

#funcao filtro que realiza a remocao das stopwords e pontuacoes do documento e ja o retorna todo em letra minuscula
def filter(document):
    
    output = []
    
    for word in document:
        output.append(word.lower())
      
    filter = remove_punctuation(output)
    filter = remove_stopwords(filter)
    
    return filter

def tf_term(term, docid, Dict):
    if docid in Dict[term]:
        return 1 + np.log10(np.bincount(Dict[term])[docid])
    else:
        return 0
    
def df_term(term,Dict):
    return  len(np.unique(Dict[term]))

def mat_tf_idf(document, Dict):
    dict_tfidf = {}
    
    i = 1
    for doc in tqdm(document, desc="Processing tf-idf..."):
        j = 0
        for word in doc:
            tf = tf_term(word, i, Dict)
            idf = np.log10(len(document)/df_term(word, Dict))
            if i in dict_tfidf:
                if i not in dict_tfidf[i]:
                    dict_tfidf[i].append(np.around(tf*idf,2))
            else:
                dict_tfidf.setdefault(i, [])
                dict_tfidf[i].append(np.around(tf*idf, 2))
            
            j+=1
        i += 1    

    return dict_tfidf

#funcao que cria o dicionario e organiza os indices invertidos dentro do mesmo
def makeDictionary(document):
    
    Dict = {}
    
    #separo todas as palavras de todos os documentos em um vetor 
    i = 1 
    for doc in tqdm(document, desc="Processing Dictionary..."):
        for word in doc:
            if word in Dict:
                if i not in Dict[word]:
                    Dict[word].append(i)
            else:
                Dict.setdefault(word, [])
                Dict[word].append(i)
        i+=1       
             
    return(Dict)

#funcao que le diversos documentos de um determinado diretorio e ja as tokeniza totalmente (removendo stopwords, pontuacoes e deixando em letra minuscula)
def readCollection():
    i = 1
    docs = []
    
    for file in tqdm(sorted(os.listdir()), desc="Processing Documents..."):
        if file.endswith('.txt'):
            file_path =f"{path}{file}"
            output = readDoc(file_path)
            output = tokenize(output)
            output = filter(output)                    
        docs.append(output) 
        i+=1
    return docs

stopwords = readDoc(current_directory + "/Filters/stopwords_ptbr.txt")
stopwords = tokenize(stopwords)

punctuation = readDoc(current_directory +"/Filters/punctuation.txt")

def main():
    Documents = readCollection()
    
    Dict = makeDictionary(Documents)
    
    tf_idf = mat_tf_idf(Documents, Dict)

    document_save = open("Documents.pkl", "wb")
    pickle.dump(Documents, document_save)

    dict_save = open("Dict.pkl", "wb")
    pickle.dump(Dict, dict_save)
    
    tf_idf_save = open("Tf_idf.pkl", "wb")
    pickle.dump(tf_idf, tf_idf_save)

    print("done")

if __name__ == "__main__":
    main()
