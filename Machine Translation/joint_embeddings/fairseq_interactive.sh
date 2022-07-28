CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 fairseq-interactive \
"/home/CE/musaeed/ironside/JW300_with_bible_joined_embeddings/bpe_vocab_bpe_pcm-en.tokenized.pcm-en" \
--input="/home/CE/musaeed/ironside_roberta/ROBERTA-base-en/Mono_lingual_data/pcm_entire_mono.txt" \
--path "/home/CE/musaeed/ironside/joint_vocab_checkpoints/validation/config_validation_joint_data_bpe_pcm_en_6_l_4_h_256_embedd_64_b_1024_ffnn_checkpoints/checkpoint_last.pt" \
--buffer-size 1024 --beam 5 --batch-size 128 \
--skip-invalid-size-inputs-valid-test >>/home/CE/musaeed/back_translation_pcm_en.txt