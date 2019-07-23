from bs4 import BeautifulSoup
from glob import glob
from tqdm import tqdm

for h in tqdm(glob('raw/*.html')):
    try:
        with open(h, 'r') as f:
            doc = BeautifulSoup(f.read(), 'html5lib')

            # remove external things
            [x.extract() for x in doc.find_all('link')]

            # remove wastefully embedded css
            style = doc.find('style')
            css = doc.new_tag('link')
            css['rel'] = 'stylesheet'
            css['href'] = 'nim.css'
            style.replace_with(css)

            # kill scripts, especially google analytics
            [x.extract() for x in doc.find_all('script')]

            # remove built-in search bar; your zim reader already has one
            [x.extract() for x in doc.find_all('div', id='searchInputDiv')]
            [x.extract() for x in doc.find_all('div', class_='search-groupby')]

            # remove links to edit the docs
            [x.extract() for x in doc.find_all('a', class_='link-seesrc')]

            # remove empty definitions
            [x.extract() for x in doc.find_all('dd') if x.get_text("", strip=True) == '']

            with open(h[4:], 'w') as f:
                f.write(doc.prettify())
    except:
        print("Bombed out on {}".format(h))
        raise
