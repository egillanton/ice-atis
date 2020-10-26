import os
import sys



def remove_digits(list):
    ret = []
    for item in list:
        if not item.isdigit():
            ret.append(item)
    return ret


def main():
    wc = 0

    for filename in sys.argv[1:]:

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split('\t')[0].split(' ')[1:-1]
                words[-1] = "EOS"
                wc += len(words)
                for word in words:
                    if word not in vocab:
                        vocab.add(word)
            print("File: ", filename)
    print("word count: ", wc)
    print("vocab size: ", len(vocab))

    with open("vocab.txt", 'w', encoding='utf-8') as output_file:
        for word in vocab:
            output_file.write(f'{word}\n')


if __name__ == '__main__':
    main()
