from collections import Counter
def main1():
    with open('oppenheimer.txt','r') as file:
        content = file.read()
        word_arr = content.strip().split()
        word_dic = Counter(word_arr)
    
    key_idx = {}
    idx_dic = {}
    for idx,key in enumerate(word_dic.keys()):
        key_idx[idx] = key
        idx_dic[idx] = word_dic[key]
        key = idx
        idx += 1
    print(idx_dic)

def main2():
    with open('./inputs/oppenheimer.txt','r') as file:
        content = file.read()
        line_arr = content.strip().splitlines()
        max_len = max([len(l) for l in line_arr])
        for idx,line in enumerate(line_arr):
            if len(line) != max_len:
                line_arr[idx] = line_arr[idx].center(max_len,' ')
    status = all((len(l) == max_len for l in line_arr))
    print(line_arr)
    print(f"is Correct: {status}")

if __name__ == "__main__":
    main2()