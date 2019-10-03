import json
import sys

# ot_books = [
#     'Genesis', 'Exodus','Leviticus','Numbers','Deuteronomy',
#     'Joshua','Judges','Ruth','1 Samuel','2 Samuel',
#     '1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra',
#     'Nehemiah','Esther','Job','Psalms','Proverbs',
#     'Ecclesiastes','Song of Solomon','Isaiah','Jeremiah','Lamentations',
#     'Ezekiel','Daniel','Hosea','Joel','Amos',
#     'Obadiah','Jonah','Micah','Nahum','Habakkuk',
#     'Zephaniah','Haggai','Zechariah','Malachi'
# ]
# nt_books = [
#     'Matthew','Mark','Luke','John','Acts',
#     'Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians',
#     'Philippians','Colossians','1 Thessalonians','2 Thessalonians','1 Timothy',
#     '2 Timothy','Titus','Philemon','Hebrews','James',
#     '1 Peter','2 Peter','1 John','2 John','3 John',
#     'Jude','Revelations'
# ]
# bom_books = []

def run(vol_name):
    volume = {}
    volume_verse_count = 0
    volume_word_count = 0
    # vol_name_list = []
    with open('lds-scriptures.json') as f:
        line_num = 0
        for line in f:
            line_num += 1
            try:
                line = line.replace('\\"', '\"')
                verse = json.loads(line)
                # if verse['volume_lds_url'] not in vol_name_list:
                #     vol_name_list.append(verse['volume_lds_url'])
                if verse['volume_lds_url'] == vol_name or verse['volume_title'] == vol_name:
                    volume_verse_count += 1
                    book_name = verse['book_title']
                    if book_name not in volume:
                        volume[book_name] = {}
                    book = volume[book_name]
                    chapter_number = verse['chapter_number']
                    if chapter_number not in book:
                        book[chapter_number] = {}
                    chapter = book[chapter_number]
                    verse_number = verse['verse_number']
                    text = verse['scripture_text']
                    chapter[verse_number] = text
                    volume_word_count += len(text.split())
            except json.decoder.JSONDecodeError as e:
                print('Error on line {}'.format(line_num))
                print(line)
                print(e)
    meta = {
        'word_count': volume_word_count,
        'verse_count': volume_verse_count
    }
    volume['meta'] = meta
    json.dump(volume, open(vol_name + '.json', 'w'))


if __name__ == '__main__':
    try:
        vol_name = sys.argv[1]
    except IndexError:
        vol_name = 'bm'
    run(vol_name)