def tokenize(line):
    return line.strip().split()


def build_vocab(tokenized_lines):
    vocab = {}
    index = 1  

    for tokens in tokenized_lines:
        for token in tokens:
            if token not in vocab:
                vocab[token] = index
                index += 1

    return vocab


def encode_lines(tokenized_lines, vocab):
    encoded = []
    for tokens in tokenized_lines:
        encoded.append([vocab[token] for token in tokens])
    return encoded


def pad_sequences(encoded_lines, pad_value=0):
    max_len = max(len(seq) for seq in encoded_lines)

    padded = []
    for seq in encoded_lines:
        padded_seq = seq + [pad_value] * (max_len - len(seq))
        padded.append(padded_seq)

    return padded, max_len


def process_file(filename):
    with open(filename, "r") as f:
        lines = f.read()
    
    # split on full stop
    raw_lines = [part.strip() for part in lines.split('.') if part.strip()]

    tokenized_lines = [tokenize(line) for line in raw_lines]


    # new number for each uniique word
    vocab = build_vocab(tokenized_lines)

    # use that vocab to map the file
    encoded_lines = encode_lines(tokenized_lines, vocab)

    padded_lines, max_len = pad_sequences(encoded_lines)

    return vocab, encoded_lines, padded_lines, max_len


if __name__ == "__main__":
    filename = "input.txt"

    vocab, encoded, padded, max_len = process_file(filename)

    print("Vocabulary:", vocab)


    print("\nEncoded Lines:")
    for line in encoded:
        print(line)

    print("\nPadded Lines (length = {}):".format(max_len))
    for line in padded:
        print(line)