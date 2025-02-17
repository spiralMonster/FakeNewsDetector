def GetModelConfig():
    basic_text_processing_layer_config = {
        "lstm_layer_config": [
            {
                "units": 8,
                "activation": "relu",
                "return_sequences": True,
                "bidirection": True
            },
            {
                "units": 32,
                "activation": "relu",
                "return_sequences": True,
                "bidirection": False
            },
            {
                "units": 64,
                "activation": "relu",
                "return_sequences": False,
                "bidirection": False
            }

        ],
        "dense_layer_config": [
            {
                "units": 128,
                "activation": "relu",
                "kernel_initializer": "he_uniform"
            },
            {
                "units": 256,
                "activation": "relu",
                "kernel_initializer": "he_uniform"
            }

        ]
    }
    return basic_text_processing_layer_config
