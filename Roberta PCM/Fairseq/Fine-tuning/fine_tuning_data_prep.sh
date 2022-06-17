# train_bpe
python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json "/home/CE/musaeed/pcm_roberta/RoBERTa/vocab.json" \
    --vocab-bpe "/home/CE/musaeed/pcm_roberta/RoBERTa/merges.txt"  \
    --inputs "/home/CE/musaeed/pcm_roberta/pcm_senti/train.input0"   \
    --outputs "/home/CE/musaeed/pcm_roberta/pcm_senti/train.input0.bpe" \
    --workers 60  \
    --keep-empty

#dev_bpe
python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json "/home/CE/musaeed/pcm_roberta/RoBERTa/vocab.json" \
    --vocab-bpe "/home/CE/musaeed/pcm_roberta/RoBERTa/merges.txt" \
    --inputs "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.input0" \
    --outputs "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.input0.bpe" \
    --workers 60   \
    --keep-empty

#train_bpe + dev_bpe --> input0
fairseq-preprocess     --only-source   \
--trainpref "/home/CE/musaeed/pcm_roberta/pcm_senti/train.input0.bpe"  \
--validpref "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.input0.bpe" \
--destdir "/home/CE/musaeed/pcm_roberta/pcm-bin/input0"    \
--workers 60   \
--srcdict /home/CE/musaeed/pcm_roberta/data-bin/pcm/dict.txt

#label
fairseq-preprocess     --only-source  \
--trainpref "/home/CE/musaeed/pcm_roberta/pcm_senti/train.label"  \
--validpref "/home/CE/musaeed/pcm_roberta/pcm_senti/dev.label"   \
--destdir "/home/CE/musaeed/pcm_roberta/pcm-bin/label" \
--workers 60

