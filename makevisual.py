from field_extractor import extract_verse
from volume_access import get_word
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use('Agg')

visualizations_folder = 'static/visuals/'

def make_visualization(term: str, per_verse=True):
    term = term.lower()
    term = term.split()[0]
    term = term.strip()
    filename = term + '-{}.jpg'
    title = '{term} (by {measurement})'
    if per_verse:
        title = title.format(measurement='Verses', term=term.title())
        filename = filename.format('v')
    else:
        title = title.format(measurement='Words', term=term.title())
        filename = filename.format('w')

    if os.path.exists(visualizations_folder + filename):
        print('{} already exists, returning'.format(filename))
        return filename

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
    plt.xlabel('Book of Scripture')
    plt.ylabel('Percent %')
    plt.savefig(visualizations_folder + filename)
    plt.close()
    print('{} created, returning'.format(filename))
    return filename
