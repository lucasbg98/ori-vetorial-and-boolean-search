# ori-vetorial-and-boolean-search
O algoritmo tem como objetivo, a partir de uma coleção de documentos realizar uma busca de uma determinada query através do modelo vetorial ou do modelo booleano. Desta forma, o objetivo é modularizar um sistema que é capaz de efetuar:
- A retirada de stopwords/pontuações
- A tokenização dos documentos
- A criação de um índice invertido
- A busca booleana através do índice invertido.
- O Cálculo de IDF/TF
- A busca vetorial com vetores normalizados
- O produto cartesiano para cada vetor de busca.
- O ranqueamento dos termos pesquisados

### Funcionamento
O sistema possui uma coleção de documementos armazenados que são préviamente processados, onde há a remoção de stopwords, pontuações e a tokenização dos documentos, para que possam ser utilizados como fonte de busca de uma determinada consulta. O sistema recebe uma query que é digitada pelo usuário, onde ele também escolhe por qual dos modelos ele deseja realizar a busca (Modelo Booleano ou Vetorial), onde no modelo vetorial temos um rankeamento dos 5 documentos mais relevantes par a consulta realizada, enquanto no modelo booleano temos a integração do operador lógico "AND", que nos permite realizar consultas de multiplos termos e retornar os documentos que satisfazem a consulta requisitada

### Bibliotecas utilizadas:
- **Numpy:** Trata-se de um pacote para o python que trabalha com arrays e matrizes multidimencionais. É uma biblioteca completa que possui uma grande quantidade de funções matemáticas para efetuar operações dentro de um array
- **Pickle:** Responsável pelo armazenamento do índice invertido, coleção de documentos já pré-processada e do índice TF-IDF em documentos binarios do tipo ".pkl" o que serve de auxilio para a economia de tempo de execução, pois não existe a necessidade de processar esses dados multiplas vezes
- **Tqdm:** Nos fornece uma visualização melhor sobre o progresso no processamento dos documentos e índices, tornando a visualização mais fácil e compreensível
- **Partial:** Da biblioteca functools, que é utilizado para alteração do metodo open com o encoding "UTF-8" pois para a leitura do arquivo original foi utilizado o encoding "latin-1"

## Funções criadas:
Neste trabalho temos três arquivos .py diferentes, onde cada um executa uma função diferente dentro do sistema como um todo, nessa seção será explicado as funções contidas dentro de cada um desses arquivos e quais suas funcionalidades:
- **script.py:** Arquivo responsável pela criação dos documentos que serão utilizados como base para as consultas realizadas, ele utiliza como fonte para criação desses documentos o arquivo de texto "corpus.txt".
  - Esse arquivo possui apenas uma função que é a responsável por analiar todas as linhas do arquivos "corpus.txt" e separa-las em vários documentos ".txt" onde os nomes desses documentos são dados pela seção "NOME" contida no arquivo base e o conteúdo de cada um desses novos documentos são dados pela seção "RESU" de cada respectivo "NOME", como há a existência de palavras em ingles e alguns termos em latin, foi utilizado a codificação "latin-1" para leitura desse documento original.
- **preprocessing.py** - Arquivo responsável por todas as operações de pré-processamento dos documentos de criação do índice invertido e do índice tf-idf.
  - Observação: os Arquivos já pré processados se encontram salvos dentro da pasta "Texts" dentro dos arquivos do sistema.
    
  **Metódos:**
  - **readDoc():** Método responsável pela leitura de um documento com a codificação "latin-1" usando biblioteca 'partial', recebe como parâmetro algum documento qualquer, realiza a leitura do mesmo e o retorna para a variável que o chamou.
  - **tokenize():** Método responsável pela tokenização dos documentos e da query.
  - **removeStopwords():** Método responsável pela remoção de stopwords dos documentos e da query.
  - **removePunctuation():** Método responsável pela remoção de pontuações dos documentos e da query.
  - **filter():** Método que realiza a conversão dos termos nos documentos e/ou query para minúsculo e faz utilziaçãod os metodos **removeStopwords()** e **removePunctuation()**.
  - **tf-term():** Método que realiza o cálculo do TF.
  - **df-term():** Método que realiza o cálculo do DF.
  - **mat-tf-idf():** Método onde ocorre a criação do índice tf-idf, onde é realizada a criação de um dicionário onde as chaves são os "docids" e dentro de cada chave temos o vetor tf-idf de cada termo contido naquele documento.
  - **makeDictionary():** Método onde ocorre a criação do índice invertido através da criação de um dicionário onde as chaves são cada termoe xistente dentro de todas a coleção de documentos e dentro de cada chave temos o "docid" dos documentos onde aquele termo aparece.
  - **readCollection():** Método que faz a leitura de toda a coleção de documentos e realiza o pré-processamento da mesma através da utilização dos métodos **tokenize()** e **filter()**, para que essa coleção possa ser utilizada no processamento de outros índices.
- **vetorial-and-boolean-search.py** Arquivo que realiza os algoritmos de busca vetorial e booleana com o uso dos índices criados previamente
  - **booleanSearch():** Método que realiza a busca booleana através do índice invertido e a consulta desejada pelo usuário, retornando os valores que atendem aos requisitos daquela consulta.
  - **vetorialSearch():** Método que realiza a busca vetorial através do índice tf-idf realizando o produto cartesiano do vetor de busca e do vetor de documentos, realizando também a normalização através da reggra de similaridade do cosseno e por fim realiza o rankeamento desses documentos e retorna ao usuário os 5 documentos que foram melhores rankeados para a consulta.
  
