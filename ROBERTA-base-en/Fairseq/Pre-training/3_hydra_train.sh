
config_dir=/home/CE/musaeed/fairseq/examples/roberta/config/pretraining
# task_data=/home/VD/cychang/ironside_nmt/pcm_roberta_fairseq/data-bin/pcm
task_data=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data-bin/pcm
wandb="ROBERTa Scratch Same config as English Version on PCM data only"
fairseq-hydra-train -m --config-dir $config_dir --config-name base task.data=$task_data   >> "/home/CE/musaeed/roberta_en_continue_pretraining_pcm_roberta_log.txt"


#modify the base.yaml dataset: batchsize = 8 and make skip_invalid_validatoian_test true and then train the model
