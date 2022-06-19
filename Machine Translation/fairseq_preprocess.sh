SOURCE_LANGUAGE=pcm
TARGET_LANGUAGE=en
TRAIN_PREF="/home/VD/cychang/ironside_nmt/JW300 with bible/train/train"
VALID_PREF="/home/VD/cychang/ironside_nmt/JW300 with bible/val/val"
TEST_PREF="/home/VD/cychang/ironside_nmt/JW300 with bible/test/test"
PCM_EN_DEST_DIR="/home/VD/cychang/ironside_nmt/JW300 with bible/pcm_en.tokenized.pcm-en"
EN_PCM_DEST_DIR="/home/VD/cychang/ironside_nmt/JW300 with bible/en_pcm.tokenized.en-pcm"
SRC_THRES=0
TGT_THRES=0

fairseq-preprocess \
    --source-lang $SOURCE_LANGUAGE \ 
    --target-lang $TARGET_LANGUAGE \
    --trainpref  $TRAIN_PREF\
    --validpref $VALID_PREF \ 
    --testpref $TEST_PREF \ 
    --destdir  $PCM_EN_DEST_DIR\ 
    --thresholdsrc $SRC_THRES \ 
    --thresholdtgt $TGT_THRES
