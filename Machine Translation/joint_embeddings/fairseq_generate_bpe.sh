 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="/home/VD/cychang/ironside_nmt/bpe_pcm_en_300_32_1024_ffnn_checkpoints/checkpoint_last.pt" 

fairseq-generate "/home/VD/cychang/ironside_nmt/JW300 with bible/pcm_en.tokenized.pcm-en" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "/home/VD/cychang/ironside_nmt/bpe_pcm_en_550_32_300_embed_test_results_l.txt"
