train_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.train.bpe
test_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.test.bpe
valid_bpe=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data/pcm.val.bpe
destdir=/home/CE/musaeed/ironside_nmt/ROBERTA-base-en/data-bin/pcm
src_dict=/home/CE/musaeed/fairseq_checker/roberta.base/dict.txt
fairseq-preprocess    --only-source      --trainpref $train_bpe --validpref $valid_bpe --testpref $test_bpe --destdir $destdir --workers 60
