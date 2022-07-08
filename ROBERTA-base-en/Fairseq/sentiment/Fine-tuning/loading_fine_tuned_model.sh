from fairseq.models.roberta import RobertaModel
roberta = RobertaModel.from_pretrained(
    'checkpoints',
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path='pcm-bin'
)
roberta.eval()  # disable dropout


label_fn = lambda label: roberta.task.label_dictionary.string(
    [label + roberta.task.label_dictionary.nspecial]
)

tokens = roberta.encode('Best movie this year')
pred = label_fn(roberta.predict('imdb_head', tokens).argmax().item())
assert pred == '1'  # positive

tokens = roberta.encode('Worst movie ever')
pred = label_fn(roberta.predict('imdb_head', tokens).argmax().item())
assert pred == '0'  # negative