import os
os.environ["CUDA_VISIBLE_DEVICES"]="2"
from datetime import datetime
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs

# from utils import load_data, clean_unnecessary_spaces


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.ERROR)

train_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/train.tsv", sep="\t").astype(str)
eval_df = pd.read_csv("/home/CE/musaeed/t5_translation/data/tsv/eval.tsv", sep="\t").astype(str)


model_args = Seq2SeqArgs()
model_args.do_sample = True
model_args.eval_batch_size = 8
model_args.evaluate_during_training = True
model_args.evaluate_during_training_steps = 2500
model_args.evaluate_during_training_verbose = True
model_args.fp16 = False
model_args.learning_rate = 5e-5
model_args.max_length = 128
model_args.max_seq_length = 128
model_args.num_beams = None
model_args.num_return_sequences = 3
model_args.num_train_epochs = 2
model_args.overwrite_output_dir = True
model_args.reprocess_input_data = True
model_args.save_eval_checkpoints = False
model_args.save_steps = -1
model_args.top_k = 50
model_args.top_p = 0.95
model_args.train_batch_size = 2
model_args.use_multiprocessing = False
model_args.output_dir = "/home/CE/musaeed/mbart/output_dir"
model_args.wandb_project = "Multi-lingual Translation with mBART"


model = Seq2SeqModel(
    encoder_decoder_type="mbart",
    encoder_decoder_name="facebook/mbart-large-50",
    args=model_args,
    cuda_devices=[2],
    use_cuda=True
)

model.train_model(train_df, eval_data=eval_df)

to_predict = [
    prefix + ": " + str(input_text)
    for prefix, input_text in zip(eval_df["prefix"].tolist(), eval_df["input_text"].tolist())
]
truth = eval_df["target_text"].tolist()

preds = model.predict(to_predict)

# Saving the predictions if needed
os.makedirs("predictions", exist_ok=True)

with open(f"predictions/predictions_{datetime.now()}.txt", "w") as f:
    for i, text in enumerate(eval_df["input_text"].tolist()):
        f.write(str(text) + "\n\n")

        f.write("Truth:\n")
        f.write(truth[i] + "\n\n")

        f.write("Prediction:\n")
        for pred in preds[i]:
            f.write(str(pred) + "\n")
        f.write(
            "________________________________________________________________________________\n"
        )