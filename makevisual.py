from field_extractor import extract_verse
from volume_access import get_word
import matplotlib.pyplot as plt

def make_visualization(term: str, per_verse=True):
    term = term.lower()
    title = 'Percent of {measurement} that Mention {term} by Volume'
    if per_verse:
        title = title.format(measurement='Verses', term=term.title())
    else:
        title = title.format(measurement='Words', term=term.title())

    volumes = {'ot':'OT',
               'nt':'NT',
               'bm':'BoM',
               'dc':'D&C',
               'pgp':'PGP'}
    info = []
    for v in volumes.keys():
        if per_verse:
            total = extract_verse(v, 'meta', 'verse_count')
        else:
            total = extract_verse(v, 'meta', 'word_count')
        term_count = get_word(v, term)

        info.append((volumes[v], term_count / total * 100))

    x = [i for i in range(len(volumes))]
    h = [i[1] for i in info]
    tick_label = [i[0] for i in info]
    plt.bar(x=x, height=h, tick_label=tick_label)
    plt.title(title)
    plt.xlabel('Volume')
    plt.ylabel('Percent %')
    plt.savefig(title + '.jpg')
