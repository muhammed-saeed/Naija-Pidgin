# train_bpe
train_input_file=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_train.input0
test_input_file=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_test.input0
dev_input_file=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_dev.input0
vocab_json=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/config_files/vocab.json
merges_text=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/config_files/merges.txt

train_bpe_out=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/bpe_output/train.input0.bpe
test_bpe_out=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/bpe_output/test.input0.bpe
dev_bpe_out=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/bpe_output/dev.input0.bpe

src_dict=/home/CE/musaeed/ironside_nmt/ironside_roberta/pcm_roberta_fairseq/data-bin/pcm/dict.txt
preprocess_text_dest_dir=/home/CE/musaeed/ironside_nmt/ironside_roberta/pcm_roberta_fairseq/data-bin/pcm-bin/input0

train_label_path=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_train.label
dev_label_path=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/sentiment/sentiment_analysis_data/pidgin/pcm_dev.label
preprocess_label_dest_dir=/home/CE/musaeed/ironside_nmt/ironside_roberta/pcm_roberta_fairseq/data-bin/pcm-bin/label

python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json $vocab_json \
    --vocab-bpe $merges_text  \
    --inputs $train_input_file   \
    --outputs $train_bpe_out \
    --workers 60  \
    --keep-empty

#dev_bpe
python -m examples.roberta.multiprocessing_bpe_encoder \
    --encoder-json $vocab_json \
    --vocab-bpe $merges_text \
    --inputs $dev_input_file \
    --outputs $dev_bpe_out \
    --workers 60   \
    --keep-empty

#train_bpe + dev_bpe --> input0
fairseq-preprocess     --only-source   \
--trainpref $train_bpe_out  \
--validpref $dev_bpe_out \
--destdir $preprocess_text_dest_dir    \
--workers 60   \
--srcdict $src_dict

#label
fairseq-preprocess     --only-source  \
--trainpref $train_label_path  \
--validpref $dev_label_path   \
--destdir $preprocess_label_dest_dir \
--workers 60
