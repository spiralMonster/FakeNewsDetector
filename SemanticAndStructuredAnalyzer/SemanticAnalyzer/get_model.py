import tensorflow as tf
import json
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from SemanticAndStructuredAnalyzer.LSTM_model.multi_lstm_layer import MultiLSTMLayer
from get_embedding_matrix import GetEmbeddingMatrix
from get_model_config import GetModelConfig

def GetModel(model_weights_path:str,embedding_path:str,word_index_path:str):

    with open(word_index_path,"r") as file:
        word_index=json.load(file)

    word_index=dict(word_index)
    vocab_length=len(word_index)
    embedding_matrix=GetEmbeddingMatrix(embedding_path,word_index)
    basic_text_processing_layer_config=GetModelConfig()



    inp = Input(shape=(300,), dtype=tf.int32)
    x = MultiLSTMLayer(
        basic_text_processing_layer_config=basic_text_processing_layer_config,
        embedding_matrix=embedding_matrix,
        num_models=6,
        vocab_size=vocab_length + 1,
        embedding_output_dim=100
    )(inp)

    model=Model(inputs=inp,outputs=x)

    model.load_weights(model_weights_path)
    print("Model Created...")
    return model