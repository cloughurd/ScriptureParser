from field_extractor import extract_verse
import json
import pandas as pd

def get_word(volume_name, word):
    volume = json.load(open(volume_name + '_wf.json', 'r'))
    return volume.get(word, 0)

def extend_df(df, word):
    volumes = ['ot','nt','bm','dc','pgp']
    for_df = []
    for v in volumes:
        word_dict = {}
        word_dict['word'] = word
        count = get_word(v, word)
        word_dict['occurrences'] = count
        word_dict['volume'] = v
        total_words = extract_verse(v, 'meta', 'word_count')
        total_verses = extract_verse(v, 'meta', 'verse_count')
        word_dict['times_per_verse'] = count / total_verses
        word_dict['times_per_word'] = count / total_words
        for_df.append(word_dict)
    return df.append(pd.DataFrame(for_df))