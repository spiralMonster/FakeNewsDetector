import numpy as np

def GetEmbeddingMatrix(embedding_path:str,word_index:dict):
    embed_dict = {}
    vocab_length=len(word_index)

    embedding_matrix = np.zeros((vocab_length + 1, 100))
    with open(embedding_path, 'r', encoding='utf-8') as file:
        for line in file:
            vector = line.split()
            word = vector[0]
            embed = np.asarray(vector[1:])
            embed_dict[word] = embed

    for word, index in word_index.items():
        if word in embed_dict.keys():
            embedding_matrix[index] = embed_dict[word]

    print("Embedding Matrix Created.....")
    return embedding_matrix
