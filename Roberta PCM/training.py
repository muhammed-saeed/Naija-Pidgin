#/home/CE/musaeed/RoBERTa/config.json
import os
from transformers import RobertaForMaskedLM, RobertaConfig
token_dir = '/home/CE/musaeed/RoBERTa'

config = RobertaConfig.from_pretrained("/home/CE/musaeed/RoBERTa/config.json")
model = RobertaForMaskedLM(config=config)
print(model)

##########################
#/home/CE/musaeed/pcm_mono.txt

####################################
from transformers import LineByLineTextDataset

from transformers import RobertaTokenizer
tokenizer = RobertaTokenizer.from_pretrained(token_dir, max_length=512)

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="/home/CE/musaeed/pcm_mono.txt",
    block_size=128,
)
#The program will now load the dataset line by line for batch training with block_
#size=128 limiting the length of an ex

###########################333

####

from transformers import DataCollatorForLanguageModeling
#to pre-pare the dataset into batches to be passed to the run_mlm
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)


######################################
num_epochs_ = 5
train_output_path =     "/home/CE/musaeed/RoBERTa/" + str(num_epochs_)
try:
    os.mkdir('/home/CE/musaeed/RoBERTa')
except OSError as error:
    print(error) 
#############################


from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir=train_output_path,
    overwrite_output_dir=True,
    num_train_epochs=num_epochs_,
    per_device_train_batch_size=64,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)


#########################################3
trainer.train()