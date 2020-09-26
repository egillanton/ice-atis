import pathlib
from itertools import chain
import sys
import re
import string

train_data_name = "atis.train.w-intent.iob"
test_data_name = "atis.test.w-intent.iob"

train_file = pathlib.Path(train_data_name)
test_file = pathlib.Path(test_data_name)


def remove_number_strings(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    list = [re.sub(pattern, '', i) for i in list]
    return list


def remove_empty_strings(list):
    while '' in list:
        list.remove('')


def remove_puctuations(list):
    list = [re.sub('[%s]' % re.escape(string.punctuation), '', s)
            for s in list]
    return list


if not train_file.exists() or not test_file.exists():
    raise FileNotFoundError

train_data = []

with train_file.open(encoding="utf8") as file:
    for line in file:
        tokens, labels_intent = line.split('\t')
        labels = " ".join(labels_intent.split(" ")[:-1])
        intent = labels_intent.split(" ")[-1]
        train_data.append(
            {"tokens": tokens.strip(), "labels": labels.strip(), "intent": intent.strip()})

test_data = []

with test_file.open(encoding="utf8") as file:
    for line in file:
        tokens, labels_intent = line.split('\t')
        labels = " ".join(labels_intent.split(" ")[:-1])
        intent = labels_intent.split(" ")[-1]
        test_data.append(
            {"tokens": tokens.strip(), "labels": labels.strip(), "intent": intent.strip()})


tokens_train = [sample["tokens"] for sample in train_data]
tokens_train = [sample.split(" ") for sample in tokens_train]
tokens_train = list(chain.from_iterable(tokens_train))
tokens_train = [sample.strip() for sample in tokens_train]
# tokens_train = list(filter(lambda x: x != "BOS" and x != "EOS", tokens))
# tokens_train = [sample.lower().replace("\u200b", "") for sample in tokens]
# tokens_train = remove_number_strings(tokens)
tokens_train = remove_puctuations(tokens_train)
remove_empty_strings(tokens_train)
vocab_train = sorted(list(set(tokens_train)))

tokens_test = [sample["tokens"] for sample in test_data]
tokens_test = [sample.split(" ") for sample in tokens_test]
tokens_test = list(chain.from_iterable(tokens_test))
tokens_test = [sample.strip() for sample in tokens_test]
# tokens_test = list(filter(lambda x: x != "BOS" and x != "EOS", tokens))
# tokens_test = [sample.lower().replace("\u200b", "") for sample in tokens]
# tokens_test = remove_number_strings(tokens)
tokens_test = remove_puctuations(tokens_test)
remove_empty_strings(tokens_test)
vocab_test = sorted(list(set(tokens_test)))


# original_stdout = sys.stdout

# with open('vocab.txt', 'w', encoding="utf8") as f:
#     sys.stdout = f  # Change the standard output to the file we created.
#     for v in vocab:
#         print(v)
#     sys.stdout = original_stdout

# print(tokens)
# print(vocab)
# N = len(tokens)
V_train = len(vocab_train)
V_test = len(vocab_test)

unseen_words_in_test = list(set(vocab_test).difference(set(vocab_train)))
diff_size = len(unseen_words_in_test)
print("ATIS")
print(f"Vocabsize for train_data: {V_train}")
print(f"Vocabsize for test_data: {V_test}")
print(f"Nr. of unseen words in test set: {diff_size}")
print("")

# for w in unseen_words_in_test:
#     print(w)
