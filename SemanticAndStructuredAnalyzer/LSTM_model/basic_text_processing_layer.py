import tensorflow as tf
from tensorflow.keras.layers import Layer,Dense,LSTM,Bidirectional
from typing import List

# lstm_layer_config=[
#     {
#         "units":,
#         "activation":,
#         "return_sequences":,
#         "bidirection":True/False
#     },

# ]


# dense_layer_config=[
#     {
#         "units":,
#         "activation":,
#         "kernel_initializer":
#     }
# ]

class BasicTextProcessingLayer(Layer):
    def __init__(self,lstm_layer_config:List,dense_layer_config:List,**kwargs):
        super().__init__(**kwargs)
        self.lstm_layer_config=lstm_layer_config
        self.dense_layer_config=dense_layer_config

        #Initializing LSTM Layers:
        self.lstm_layers=[]
        for config in self.lstm_layer_config:
            if config['bidirection']:
                self.lstm_layers.append(
                    Bidirectional(
                        LSTM(
                            units=config["units"],
                            activation=config["activation"],
                            return_sequences=config["return_sequences"]
                        )
                    )
                )
            
            else:
                self.lstm_layers.append(
                    LSTM(
                            units=config["units"],
                            activation=config["activation"],
                            return_sequences=config["return_sequences"]
                    )
                )
                
                
        #Initializing Dense Layers:
        self.dense_layers=[]
        for config in self.dense_layer_config:
            self.dense_layers.append(
                Dense(
                    units=config["units"],
                    activation=config["activation"],
                    kernel_initializer=config["kernel_initializer"]
                )
            )
            
         
    def call(self,x):
        ind=0
        while ind<len(self.lstm_layers):
            lstm_layer=self.lstm_layers[ind]
            x=lstm_layer(x)
            ind+=1
            
        ind=0
        while ind<len(self.dense_layers):
            dense_layer=self.dense_layers[ind]
            x=dense_layer(x)
            ind+=1

        return x
        
    def compute_output_shape(self,input_shape):
        return (input_shape[0],self.dense_layer_config[-1]["units"])
        
    def get_config(self):
        config=super().get_config()
        config.update(
            {
                "lstm_layer_config":self.lstm_layer_config,
                "dense_layer_config":self.dense_layer_config
            }
        )
        return config
        
            
        

                