import tensorflow as tf
from tensorflow.keras.layers import Layer,Dense,LSTM,Bidirection

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
    def __init__(lstm_layer_config,dense_layer_config,**kwargs):
        super().__init__(**kwargs)
        self.lstm_layer_config=lstm_layer_config
        self.dense_layer_config=dense_layer_config

        #Initializing LSTM Layers:
        self.lstm_layers=[]
        for config in self.lstm_layer_config:
            if config['bidirection']:
                self.lstm_layers.append(
                    Bidirection(
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
        for lstm_layer in self.lstm_layers:
            x=lstm_layer(x)
            
        for dense_layer in self.dense_layers:
            x=dense_layer(x)

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
        
            
        

                