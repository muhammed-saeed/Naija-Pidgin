TOTAL_NUM_UPDATES=7812  # 10 epochs through IMDB for bsz 32
WARMUP_UPDATES=469      # 6 percent of the number of updates
LR=1e-05                # Peak LR for polynomial LR scheduler.
HEAD_NAME="pcm_head"     # Custom name for the classification head.
NUM_CLASSES=3         # Number of classes for the classification task.
MAX_SENTENCES=8         # Batch size.
ROBERTA_PATH="/home/CE/musaeed/pcm_roberta/data-bin/multirun/2022-06-12/13-27-34/0/checkpoints/checkpoint_best.pt"
# ROBERTA_PATH = "/content/checkpoint_best.pt"

# CUDA_VISIBLE_DEVICES=0 
fairseq-train /home/CE/musaeed/pcm_roberta/pcm-bin/ \
    --restore-file $ROBERTA_PATH \
    --max-positions 512 \
    --batch-size $MAX_SENTENCES \
    --max-tokens 4400 \
    --task sentence_prediction \
    --reset-optimizer --reset-dataloader --reset-meters \
    --required-batch-size-multiple 1 \
    --init-token 0 --separator-token 2 \
    --arch roberta \
    --criterion sentence_prediction \
    --classification-head-name $HEAD_NAME \
    --num-classes $NUM_CLASSES \
    --dropout 0.1 --attention-dropout 0.1 \
    --weight-decay 0.1 --optimizer adam --adam-betas "(0.9, 0.98)" --adam-eps 1e-06 \
    --clip-norm 0.0 \
    --lr-scheduler polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates $WARMUP_UPDATES \
    --fp16 --fp16-init-scale 4 --threshold-loss-scale 1 --fp16-scale-window 128 \
    --max-epoch 10 \
    --best-checkpoint-metric accuracy --maximize-best-checkpoint-metric \
    --shorten-method "truncate" \
    --find-unused-parameters \
    --update-freq 4 \
    --log-format=json --log-interval=10 2>&1 |  tee "/home/CE/musaeed/pcm_fine_tuning_log.log"  