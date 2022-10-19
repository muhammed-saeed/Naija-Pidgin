import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3,2"
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

train_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/train.tsv", sep="\t").astype(str)
eval_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/eval.tsv", sep="\t").astype(str)

train_df["prefix"] = ""
eval_df["prefix"] = ""
model_args = T5Args()
model_args.max_seq_length = 96
model_args.train_batch_size = 20
model_args.eval_batch_size = 20
model_args.num_train_epochs = 1
model_args.evaluate_during_training = True
model_args.evaluate_during_training_steps = 30000
model_args.use_multiprocessing = False
model_args.fp16 = False
model_args.save_steps = -1
model_args.save_eval_checkpoints = False
model_args.no_cache = True
model_args.reprocess_input_data = True
model_args.overwrite_output_dir = True
model_args.preprocess_inputs = False
model_args.num_return_sequences = 1
model_args.n_gpu = 2
model_args.output_dir = "/home/CE/musaeed/t5_translation/output_dir"

model_args.wandb_project = "MT5 PCM-English Translation"
model_output_dir = "/home/CE/musaeed/t5_translation/firt_epoch"

model = T5Model("mt5", model_output_dir, args=model_args, cuda_devices=[3,2])

model.train_model(train_df, eval_data=eval_df)