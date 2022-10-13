import torch
from transformers import BartModel, BartConfig
from transformers import BartTokenizer, BartForSequenceClassification
import pandas as pd
# Initializing a BART facebook/bart-large style 


from sklearn import metrics

def mapping_function(predicted_label, mapping):
    for index, label in enumerate(predicted_label):
        if label == "positive":
            predicted_label[index] = mapping["positive"]
        elif label == "negative":
            predicted_label[index] = mapping["negative"]
        else :
            predicted_label[index] = mapping["neutral"]




configuration = BartConfig()
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base", input_ids=(64,12))
# Initializing a model from the facebook/bart-large style configuration
model = BartForSequenceClassification.from_pretrained("facebook/bart-base", id2label={
    "0": "Negative",
    "1": "Neutral",
    "2": "Positive"
  },label2id={
    "Negative": "0",
    "Neutral": "1",
    "Positive": "2"
  })


# print(f"the bart model is{model.config}")


inputs = tokenizer("I love this girl ", return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
print(predicted_class_id)
print(model.config.id2label[str(predicted_class_id)])
print(model.config.id2label)


pcm_test_dataset = "/home/CE/musaeed/ROBERTA-base-en/pidgin/pcm_test.csv"

test_df = pd.read_csv(pcm_test_dataset)
test_df.dropna(inplace=True)

test_text = test_df['text'].tolist()
test_label = test_df['label'].tolist()

predicted_label = []


with torch.no_grad():
    
    for line in test_text:
        inputs = tokenizer(line, return_tensors="pt")

        logits = model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        # print()

        predicted_label.append(model.config.id2label[str(predicted_class_id)])

# print(f"the predicted_labels are {predicted_label}")

mapping = {"positive":2, "neutral":1, "negative":0 }

mapping_function(predicted_label, mapping)
mapping_function(test_label, mapping)

accuracy = metrics.accuracy_score(test_label, predicted_label)
f1_score_macro = metrics.f1_score(test_label, predicted_label, average='macro')
f1_score_weighted = metrics.f1_score(test_label, predicted_label, average='weighted')

print(f"the model accuracy is {accuracy}")
print(f"the model  f1_macro is  is {f1_score_macro}")
print(f"the model f1_weighted  is {f1_score_weighted}")


