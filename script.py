from functools import partial
import os.path

current_directory = os.getcwd()
path = current_directory +"/Texts/"
os.chdir(path)

def main():
    open_latin = partial(open, encoding='latin-1')
    
    with open_latin(current_directory+"/corpus.txt") as corpus:
        for line in corpus:
            if "NOME  -" in line:
                docName = [word for word in line.split() if word != "NOME" and word != "-"]
                docs = os.path.join(path, ' '.join(docName)+".txt")
                files = open_latin(docs, "w")
            if "RESU  -" in line:
                docResu = [word for word in line.split() if word != "RESU" and word != "-"]
                files.write(' '.join(docResu))
                
                
if __name__ == "__main__":
    main()

# open_latin = partial(open, encoding='latin-1')