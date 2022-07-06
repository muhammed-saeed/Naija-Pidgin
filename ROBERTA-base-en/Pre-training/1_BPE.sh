# script_1 multiprocessing_bpe_encoder for (train, dev, test) datasets
train_data=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.train.raw
test_data=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.test.raw
val_data=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.val.raw
train_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.train.bpe
test_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.test.bpe
val_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.val.bpe
roberta_merges=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/tokenization_pcm_files/merges.txt
roberta_vocab_json=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/tokenization_pcm_files/vocab.json


python -m examples.roberta.multiprocessing_bpe_encoder  --encoder-json $roberta_vocab_json  --vocab-bpe $roberta_merges   --inputs $train_data  --outputs $train_bpe --keep-empty         --workers 60;

python -m examples.roberta.multiprocessing_bpe_encoder  --encoder-json $roberta_vocab_json  --vocab-bpe $roberta_merges   --inputs $test_data  --outputs $test_bpe --keep-empty         --workers 60;

python -m examples.roberta.multiprocessing_bpe_encoder  --encoder-json $roberta_vocab_json  --vocab-bpe $roberta_merges   --inputs $val_data  --outputs $val_bpe --keep-empty         --workers 60;
