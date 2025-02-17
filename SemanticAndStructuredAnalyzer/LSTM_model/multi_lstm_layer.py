import tensorflow as tf
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Concatenate,Dense,Dropout
from tensorflow.keras.initializers import Constant
# from basic_text_processing_layer import BasicTextProcessingLayer
# from input_divider_layer import InputDividerLayer
from SemanticAndStructuredAnalyzer.LSTM_model.basic_text_processing_layer import BasicTextProcessingLayer
from SemanticAndStructuredAnalyzer.LSTM_model.input_divider_layer import InputDividerLayer

# basic_text_processing_layer_config={
    
# "lstm_layer_config":
# [
#     {
#         "units":,
#         "activation":,
#         "return_sequences":,
#         "bidirection":True/False
#     },

# ],

# "dense_layer_config":
# [
#     {
#         "units":,
#         "activation":,
#         "kernel_initializer":
#     }
# ]

# }

class MultiLSTMLayer(Layer):
    def __init__(self,basic_text_processing_layer_config,embedding_matrix,num_models,vocab_size,embedding_output_dim,**kwargs):
        super().__init__(**kwargs)
        self.basic_text_processing_layer_config=basic_text_processing_layer_config
        self.embedding_matrix=embedding_matrix
        self.num_models=num_models
        self.vocab_size=vocab_size
        self.embedding_output_dim=embedding_output_dim
        
        # Initializing Embedding Layer:
        self.embedding_layer=Embedding(
            input_dim=self.vocab_size,
            output_dim=self.embedding_output_dim,
            embeddings_initializer=Constant(self.embedding_matrix),
            trainable=True  
        )
        
        # Initializing Multi Lstm models:
        self.multi_lstm_models=[]
        for _ in range(self.num_models):
            self.multi_lstm_models.append(
                BasicTextProcessingLayer(
                    lstm_layer_config=self.basic_text_processing_layer_config["lstm_layer_config"],
                    dense_layer_config=self.basic_text_processing_layer_config["dense_layer_config"]
                )
            )
        
        
        # Initializing final layers:
        output_dim_after_multi_lstm_layers=self.num_models*self.basic_text_processing_layer_config["dense_layer_config"][-1]["units"]
        
        self.final_layers=[
            Dense(units=2* output_dim_after_multi_lstm_layers,activation="relu",kernel_initializer="he_uniform"),
            Dense(units=int(0.5* output_dim_after_multi_lstm_layers),activation="relu",kernel_initializer="he_uniform"),
            Dropout(0.3),
            Dense(units=16,activation="relu",kernel_initializer="he_uniform"),
            Dense(units=4,activation="relu",kernel_initializer="he_uniform"),
            Dense(units=1,activation="sigmoid",kernel_initializer="glorot_uniform")
        ]
        
        
    def call(self,inputs):
        x=self.embedding_layer(inputs)
        model_inputs=InputDividerLayer(num_models=self.num_models)(x)
        
        model_outputs=[]
        ind=0
        while ind<self.num_models:
            model=self.multi_lstm_models[ind]
            inp=model_inputs[ind]
            out=model(inp)
            model_outputs.append(out)
            ind+=1
            
        final_out=Concatenate(axis=-1)(model_outputs)
        
        ind=0
        while ind<len(self.final_layers):
            layer=self.final_layers[ind]
            final_out=layer(final_out)
            ind+=1
            
        return final_out
        
    def compute_output_shape(self,input_shape):
        return (input_shape[0],1)
        
    def get_config(self):
        config=super().get_config()
        config.update(
            {
                "basic_text_processing_layer_config":self.basic_text_processing_layer_config,
                "embedding_matrix":self.embedding_matrix,
                "num_models":self.num_models,
                "vocab_size":self.vocab_size,
                "embedding_output_dim":self.embedding_output_dim
            }
        )
        return config





        

