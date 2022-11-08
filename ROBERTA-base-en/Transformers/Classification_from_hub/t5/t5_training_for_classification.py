# import os
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"

# os.environ["CUDA_VISIBLE_DEVICES"] = "2"
import pandas as pd

from simpletransformers.t5 import T5Model
import torch
# torch.cuda.set_device("2")


train_df = pd.read_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/train.tsv", sep="\t").astype(str)
eval_df = pd.read_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/eval.tsv", sep="\t").astype(str)
LEARNING_RATE = 1e-2

model_args = {
    "max_seq_length": 128,
    "train_batch_size": 4,
    "eval_batch_size": 4,
    "num_train_epochs": 11,
    "evaluate_during_training": True,
    "evaluate_during_training_steps": 15000,
    "evaluate_during_training_verbose": True,
    "use_multiprocessing": False,
    "fp16": False,
    "save_steps":1000,
    "save_total_limit":2,
    "save_eval_checkpoints": False,
    "save_model_every_epoch": False,
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "output_dir":"/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/mt5_large/",
    "wandb_project": "mT5-large  Multi-Label",
}
t5_pcm_plus_path = "/home/CE/musaeed/ROBERTA-base-en/Transformers/pre_training_tf5_from_checkpoint"
model = T5Model("t5", "t5-large", args=model_args, cuda_devices=[6])
model = T5Model("mt5", "google/mt5-large", args=model_args, cuda_devices=[1,0])
# model = T5Model("t5", t5_pcm_plus_path, args=model_args, cuda_devices=[3,2])


model.train_model(train_df, eval_data=eval_df)