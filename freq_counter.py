import json
import sys
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def sort_by(x):
    return x[1]

def run(vol_name):
    file = vol_name + '.json'
    volume = json.load(open(file, 'r'))
    word_frequencies = {}
    trans_table = str.maketrans("", "", string.punctuation)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    num_good_words = 0
    godly_titles = ['god','lord','jesus','christ','father']
    godly_adjectives = {}
    for book_name, book in volume.items():
        if book_name == 'meta':
            continue
        for _, chapter in book.items():
            for _, verse in chapter.items():
                word_list = verse.lower().translate(trans_table).split()
                for idx, word in enumerate(word_list):
                    if word not in stop_words:
                        stem = stemmer.stem(word)
                        if stem in godly_titles and idx > 0:
                            adj = stemmer.stem(word_list[idx - 1])
                            if adj not in stop_words and adj not in godly_titles:
                                prev_count = godly_adjectives.get(adj, 0)
                                godly_adjectives[adj] = prev_count + 1
                        num_good_words += 1
                        prev = word_frequencies.get(stem, 0)
                        word_frequencies[stem] = prev + 1
    tuples_list = []
    for word, count in word_frequencies.items():
        tuples_list.append((word, count))
    # print(sorted(tuples_list, key=sort_by, reverse=True)[:50])
    print('Total number of words: {}'.format(volume['meta']['word_count']))
    print('Total number of verses: {}'.format(volume['meta']['verse_count']))
    print('Number of words after filter: {}'.format(num_good_words))
    gospel_terms = ['baptism','gift','faith','repent','holy','spirit','ghost','endure','covenant','ordinance','christ','jesus','lord','god','forgive','grace']
    for term in gospel_terms:
        print('{} appears {} times'.format(term, word_frequencies.get(stemmer.stem(term), 0)))
    adj_list = []
    for word, count in godly_adjectives.items():
        adj_list.append((word, count))
    print(sorted(adj_list, key=sort_by, reverse=True)[:25])
    json.dump(word_frequencies, open(vol_name + '_wf.json', 'w'))


if __name__ == '__main__':
    try:
        vol_name = sys.argv[1]
    except IndexError:
        vol_name = 'bm'
    run(vol_name)