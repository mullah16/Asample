from pprint import pprint as pp

def group_words_by_count(wc):
    group_by = dict()

    for word, count in wc.iteritems():
        if count not in group_by:
            group_by[count] = list()

        group_by[count].append(word)

    return group_by

def get_word_count(txt_file):
    word_count =dict()

    for line in open(txt_file):
        print line
        for word in line.rstrip().split():
            word_count[word] = word_count.get(word,0)+1

    return word_count

wc = get_word_count("data")
grp_by = group_words_by_count(wc)
pp(grp_by)