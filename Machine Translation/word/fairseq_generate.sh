 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="/home/VD/cychang/ironside_nmt/en_pcm_checkpoints/checkpoint_last.pt" 

fairseq-generate "/home/VD/cychang/ironside_nmt/JW300 with bible/en_pcm.tokenized.en-pcm" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "/home/VD/cychang/ironside_nmt/en_pcm_550_256_test_results_l.txt"