import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Layer

class InputDividerLayer(Layer):
    def __init__(self,num_models,**kwargs):
        super().__init__(**kwargs)
        self.num_models=num_models
        
    def call(self,inputs):
        words_per_text=inputs.shape[1]
        factor=words_per_text//self.num_models
        embedding_dim=inputs.shape[2]
        
        x=tf.transpose(
            tf.reshape(inputs,(-1,self.num_models,factor,embedding_dim)),
            perm=[1,0,2,3]
        )
        
        x=tf.cast(x,dtype=tf.float32)
        return x
        
    def compute_output_shape(self,input_shape):
        return (self.num_models,input_shape[0],input_shape[1],input_shape[2])
        
    def get_config(self):
        config=super().get_config()
        config.update(
            {
                "num_models":self.num_models
            }
        )
        return config
            
        