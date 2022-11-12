import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "2"
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

train_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/train.tsv", sep="\t").astype(str)
eval_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/eval.tsv", sep="\t").astype(str)

# train_df["prefix"] = ""
# eval_df["prefix"] = ""
model_args = T5Args()
model_args.max_seq_length = 128
model_args.train_batch_size = 16
model_args.eval_batch_size = 16
model_args.num_train_epochs = 20
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
model_args.n_gpu = 2
model_args.num_return_sequences = 1
model_args.output_dir = "/home/CE/musaeed/t5_translation/t5_en_pcm_pretrained_for_translation"

model_args.wandb_project = "T5-EN_BASE PCM-English Translation"
model_dir = "/home/CE/musaeed/t5_translation/output_dir_backup_7_epoch/checkpoint-49960-epoch-8"
english_dir = "/home/CE/musaeed/t5_translation/t5_english_base_translation/checkpoint-75162-epoch-2"
english_t5_pretrained_on_pcm = "/home/CE/musaeed/t5_pretrained_pcm/pre_training_tf5_from_checkpoint"
# model = T5Model("mt5", "google/mt5-base", args=model_args, cuda_devices=[3,2])
# model = T5Model("mt5", "google/mt5-base", args=model_args, cuda_devices=[2])
# model = T5Model("mt5", model_dir, args=model_args, cuda_devices=[2])

model = T5Model("t5", english_t5_pretrained_on_pcm, args=model_args, cuda_devices=[3])

model.train_model(train_df, eval_data=eval_df)