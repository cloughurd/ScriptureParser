import json

def extract_book(volume_name, book_name):
    volume = json.load(open(volume_name + '.json', 'r'))
    book = volume[book_name]
    return book

def extract_verse(volume_name, book_name, verse):
    volume = json.load(open(volume_name + '.json', 'r'))
    book = volume[book_name]
    return book[verse]