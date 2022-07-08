from transformers import RobertaTokenizer, RobertaForMaskedLM


mono_path = "/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForMaskedLM.from_pretrained('roberta-base')



isExist = os.path.exists(model_folder)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(model_folder)
  print("The new directory is created!")


isExist = os.path.exists(tokenizer_folder)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(tokenizer_folder)
  print("The new directory is created!")









from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= mono_path,
    block_size=64,
)
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./roberta-more-pre-trained",
    overwrite_output_dir=True,
    num_train_epochs=25,
    per_device_train_batch_size=64,
    save_steps=500,
    save_total_limit=2,
    seed=1,
    report_to="wandb",
    run_name="RoBERTa more pre-training using Transfomers on PCM Data"
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)
trainer.train()

trainer.save_model("/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Transformers/Pre-training_from_checkpoint/roberta-retrained")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="/home/VD/cychang/ironside_roberta/ROBERTA-base-en/Transformers/Pre-training_from_checkpoint/roberta-retrained",
    tokenizer="roberta-base"
)
fill_mask("Send these <mask> back!")