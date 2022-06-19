DROPOUT=0.3
ATTENTION_DROPOUT=0.0
ACTIVATION_DROPOUT=0.3
EMBEDDING_SIZE=420
ENC_FFNN=2048
ENCODER_LAYERS=5
ENCODER_ATTENTION_HEADS=6
DECODER_LAYERS=5
DECODER_ATTENTION_HEADS=6
DEC_FFNN=2048
EPOCH=550
BATCH_SIZE=64
ENCODER_LAYER_DROPOUT= 0.0
DECODER_LAYER_DROPOUT=0.1
SOURCE_LANGUAGE=pcm
TARGET_LANGUAGE=en
LABEL_SMOOTHING=0.4
SAVE_DIR="/home/VD/cychang/ironside_nmt/420_embed_checkpoints/"
LABEL_CROSS_ENTROPY="label_smoothed_cross_entropy"
WARMUP_UPDATES=4000
lEARNING_POLICY = inverse_sqrt

fairseq-train "/home/VD/cychang/ironside_nmt/JW300 with bible/pcm_en.tokenized.pcm-en" \
    --arch transformer \
    --dropout $DROPOUT \
    --attention-dropout $ATTENTION_DROPOUT \ 
    --encoder-embed-dim   $EMBEDDING_SIZE\
    --encoder-ffn-embed-dim $ENC_FFNN  \
    --encoder-layers $ENCODER_LAYERS  \
    --encoder-attention-heads $ENCODER_ATTENTION_HEADS \
    --encoder-learned-pos  \
    --decoder-embed-dim $EMBEDDING_SIZE \
    --decoder-ffn-embed-dim $DEC_FFNN  \
    --decoder-layers $DECODER_LAYERS \
    --decoder-attention-heads $DECODER_ATTENTION_HEADS \
    --decoder-learned-pos   \
    --max-epoch $EPOCH  \
    --optimizer adam \
    --lr 5e-4 \
    --batch-size $BATCH_SIZE \
    --seed 1  \
    --encoder-layerdrop $ENCODER_LAYER_DROPOUT \
    --decoder-layerdrop $DECODER_LAYER_DROPOUT \
    --criterion $LABEL_CROSS_ENTROPY \ 
    --warmup-updates $WARMUP_UPDATES \
    --source-lang $SOURCE_LANGUAGE \ 
    --label-smoothing $LABEL_SMOOTHING \
    --lr-scheduler $lEARNING_POLICY \ 
    --save-dir $SAVE_DIR \
    
    --find-unused-parameters  \
    --target-lang $TARGET_LANGUAGE \
    --activation-dropout $ACTIVATION_DROPOUT  \
    --ddp-backend=no_c10d \
    
    --log-format=json --log-interval=10 2>&1 \
    --no-epoch-checkpoints   |  tee  "/home/VD/cychang/pcm_en_5_2048_550_64_420_embed_arch_training_log.log"