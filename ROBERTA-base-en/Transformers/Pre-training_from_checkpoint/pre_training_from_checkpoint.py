from transformers import RobertaTokenizer, RobertaForMaskedLM


mono_path = "/tmp/tweeteval/datasets/hate/train_text.txt"
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForMaskedLM.from_pretrained('roberta-base')

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path= mono_path,
    block_size=64,
)
#block_size if large value then the model will simply crash
from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./roberta-more-pre-trained",
    overwrite_output_dir=True,
    num_train_epochs=25,
    per_device_train_batch_size=48,
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

trainer.save_model("./roberta-retrained")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="./roberta-retrained",
    tokenizer="roberta-base"
)
fill_mask("Send these <mask> back!")