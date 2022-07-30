import sentencepiece as spm

en_tokenizer = spm.SentencePieceProcessor(model_file="/home/CE/musaeed/ironside_2/ironside/bpe_dict_path/en__vocab_4000.model")
# pcm_tokenizer = spm.SentencePieceProcessor(model_file="/home/CE/musaeed/ironside/bpe_dict_path/pcm__vocab_4000.model")

pcm_mono_token="/home/CE/musaeed/train.en"
pcm_mono_bpe_token="/home/CE/musaeed/ironside_2/ironside/Machine_Translation/back_translation/en_back_tranlsation_data_bpe.txt"
with open(pcm_mono_token, "r", encoding="utf-8") as rf, open(pcm_mono_bpe_token, "w", encoding="utf-8") as wf:
    output_lines = []
    for line in rf.readlines():
        wf.write(' '.join(en_tokenizer.encode(line, out_type=str)))
        # output_lines.append(tokenizer.encode(input = line, out_type = str))
        wf.write("\n")

    # wf.writelines(str(output_lines))