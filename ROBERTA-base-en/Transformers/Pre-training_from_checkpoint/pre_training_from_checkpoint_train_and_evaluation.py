
from transformers import RobertaTokenizer, RobertaForMaskedLM
#don't know why using evaluaiton in the more pretraining results in worse results
model_folder = "/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Transformers/Pre-training_from_checkpoint/pretraining_from_scratch_train_eval/"
mono_path = "/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

# dataset = LineByLineTextDataset(
#     tokenizer=tokenizer,
#     file_path= mono_path,
#     block_size=64,
# )
from transformers import DataCollatorForLanguageModeling


from transformers import LineByLineTextDataset
train_data_path = "/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pre_training/train_pcm.txt"
eval_data_path = "/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pre_training/eval_pcm.txt"
train_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= train_data_path,
    block_size=64,
)

eval_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= eval_data_path,
    block_size=64,
)

from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import DataCollatorForLanguageModeling

# Define the Data Collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)


import torch
from transformers import Trainer, TrainingArguments
# Define the training arguments

TRAIN_EPOCHS= 100
VALID_BATCH_SIZE = 8
TRAIN_BATCH_SIZE = 8
WEIGHT_DECAY = 0.0
LEARNING_RATE = 1e-3
training_args = TrainingArguments(
    output_dir=model_folder,
    overwrite_output_dir=True,
    evaluation_strategy = 'epoch',
    num_train_epochs=TRAIN_EPOCHS,
    learning_rate=LEARNING_RATE,
    weight_decay=WEIGHT_DECAY ,
    per_device_train_batch_size=TRAIN_BATCH_SIZE ,
    save_steps=8192,
    eval_steps=4096,
    # per_device_eval_batch_size=VALID_BATCH_SIZE ,
    report_to="wandb",
    run_name="RoBERTa  pre-training from checkpoint with train/eval using Transfomers on PCM Data",
    save_total_limit=1
)
# Create the trainer for our model
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    #prediction_loss_only=True,
    
)
# Train the model
trainer.train()

from transformers import pipeline
# Create a Fill mask pipeline
fill_mask = pipeline(
    "fill-mask",
    model=model_folder,
    tokenizer=tokenizer_folder
)
# Test some examples
# knit midi dress with vneckline
# =>
fill_mask("midi <mask> with vneckline.")
# The test text: Round neck sweater with long sleeves
fill_mask("Round neck sweater with <mask> sleeves.")


