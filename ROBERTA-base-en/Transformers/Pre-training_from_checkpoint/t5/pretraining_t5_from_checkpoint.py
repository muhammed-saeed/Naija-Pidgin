#export CUDA_VISIBLE_DEVICES=7, NVIDIA_VISIBLE_DEVICES=7 ,CUDA_VISIBLE_DEVICES=0
#CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=6,7
from transformers import RobertaTokenizer, RobertaForMaskedLM
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

mono_path = "/home/CE/musaeed/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt"
# tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
# model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= mono_path,
    block_size=4,
)
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False, mlm_probability=0.15
)
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="/home/CE/musaeed/ROBERTA-base-en/Transformers/pre_training_tf5_from_checkpoint/t5-more-pre-trained_100_epoch",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_device_train_batch_size=32,
    save_steps=500,
    save_total_limit=2,
    seed=1,
    report_to="wandb",
    run_name="T5 more pre-training using Transfomers on PCM Data 100 epoch second training time" 
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)
trainer.train()

trainer.save_model("/home/CE/musaeed/ROBERTA-base-en/Transformers/pre_training_tf5_from_checkpoint/t5_more_pretraining_trainer_saved")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="/home/CE/musaeed/ROBERTA-base-en/Transformers/pre_training_tf5_from_checkpoint/t5-more_pretraining_trainer_saved",
    tokenizer="roberta-base"
)
fill_mask("Send these <mask> back!")
