import json
from datetime import datetime
from pprint import pprint
from statistics import mean

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, f1_score
from transformers.data.metrics.squad_metrics import compute_exact, compute_f1

from simpletransformers.t5 import T5Model
# import os
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def f1(truths, preds):
    return mean([compute_f1(truth, pred) for truth, pred in zip(truths, preds)])


def exact(truths, preds):
    return mean([compute_exact(truth, pred) for truth, pred in zip(truths, preds)])




model_args = {
    "overwrite_output_dir": True,
    "max_seq_length": 256,
    "eval_batch_size": 16,
    "use_multiprocessing": False,
    "num_beams": None,
    "do_sample": True,
    "max_length": 128,
    "top_k": 1,
    "top_p": 0.95,
    "num_return_sequences": 2,
}

# Load the trained model
model_path="/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/t5_model_train/checkpoint-16500"
# model_path = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/t5_model_train"
best_more_pretrained_model_path = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/more_t5_model_train_11_epochs/checkpoint-15000"
more_pretrained_model_path = "/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/mt5_large/checkpoint-4000"
model = T5Model("mt5",more_pretrained_model_path, args=model_args)

# Load the evaluation data
df = pd.read_csv("/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/test.tsv", sep="\t").astype(str)

# Prepare the data for testing
to_predict = [
    prefix + ": " + str(input_text)
    for prefix, input_text in zip(df["prefix"].tolist(), df["input_text"].tolist())
]
truth = df["target_text"].tolist()
tasks = df["prefix"].tolist()

# Get the model predictions
preds = model.predict(to_predict)

# Saving the predictions if needed
with open(f"/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/predictions/predictions_{datetime.now()}.txt", "w") as f:
    for i, text in enumerate(df["input_text"].tolist()):
        f.write(str(text) + "\n\n")

        f.write("Truth:\n")
        f.write(truth[i] + "\n\n")

        f.write("Prediction:\n")
        for pred in preds[i]:
            f.write(str(pred) + "\n")
        f.write(
            "________________________________________________________________________________\n"
        )

# Taking only the first prediction
preds = [pred[0] for pred in preds]
df["predicted"] = preds

# Evaluating the tasks separately
output_dict = {
    
    "multilabel classification": {
        "truth": [],
        "preds": [],
    }
}

results_dict = {}

for task, truth_value, pred in zip(tasks, truth, preds):
    output_dict[task]["truth"].append(truth_value)
    output_dict[task]["preds"].append(pred)

print("-----------------------------------")
weighted="weighted"
macro="macro"
print("Results: ")
for task, outputs in output_dict.items():
    if task == "multilabel classification":
        try:
            task_truth = output_dict[task]["truth"]
            task_preds = output_dict[task]["preds"]
            results_dict[task] = {
                "F1 Score weighted": f1_score(task_truth, task_preds, average='weighted'),
                "F1 Score macro": f1_score(task_truth, task_preds, average='macro'),
                "Exact matches": exact(task_truth, task_preds),
            }
            print(f"Scores for {task}:")
            print(f"F1 score weighted: {f1_score(task_truth, task_preds, average=weighted)}")
            print(f"F1 score macro: {f1_score(task_truth, task_preds, average=macro)}")
            print(f"Exact matches: {exact(task_truth, task_preds)}")
            print()
        except:
            pass

    
with open(f"/home/CE/musaeed/ROBERTA-base-en/Transformers/Classification_from_hub/t5/mutli_label_pcm/results/result_{datetime.now()}.json", "w") as f:
    json.dump(results_dict, f)