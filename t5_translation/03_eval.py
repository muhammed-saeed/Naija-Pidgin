import logging
import sacrebleu
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = T5Args()
model_args.max_length = 512
model_args.length_penalty = 1
model_args.num_beams = 10

model_output_dir = "/home/CE/musaeed/t5_translation/output_dir/checkpoint-4996-epoch-1"
model = T5Model("mt5", model_output_dir, args=model_args)

eval_df = pd.read_csv("/home/CE/musaeed/Naija-Pidgin/t5_translation/data/tsv/eval.tsv", sep="\t").astype(str)

pcm_truth = [eval_df.loc[eval_df["prefix"] == "translate english to pcm"]["target_text"].tolist()]
to_pcm = eval_df.loc[eval_df["prefix"] == "translate english to pcm"]["input_text"].tolist()

english_truth = [eval_df.loc[eval_df["prefix"] == "translate pcm to english"]["target_text"].tolist()]
to_english = eval_df.loc[eval_df["prefix"] == "translate pcm to english"]["input_text"].tolist()

# Predict
pcm_preds = model.predict(to_pcm)

en_pcm_bleu = sacrebleu.corpus_bleu(pcm_preds, pcm_truth)
print("--------------------------")
print("English to Pidgin: ", en_pcm_bleu.score)

english_preds = model.predict(to_english)

pcm_en_bleu = sacrebleu.corpus_bleu(english_preds, english_truth)
print("Pidgin to English: ", pcm_en_bleu.score)
