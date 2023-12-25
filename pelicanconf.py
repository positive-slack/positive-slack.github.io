# Base configuration
AUTHOR = 'esynr3z'
SITENAME = 'positive slack'
SITESUBTITLE = 'Digital design and verification.'
SITEURL = 'http://localhost:8000'
OUTPUT_PATH = 'docs/'
PATH = "content"
STATIC_PATHS = ['assets']

# Date and locale
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'Europe/Moscow'
LOCALE = 'en_US'
DEFAULT_LANG = 'en'

# Author
AUTHOR_META = {
  "esynr3z": {
    "name": "esynr3z",
    "image": "assets/avatar.gif",
    "github": "esynr3z",
    "website": "https://t.me/esynr3z",
    "bio": "ASIC verification engineer. Former RTL design engineer. Secretly love embedded systems and smell of flux."
  }
}

# Articles
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
ARTICLE_URL = 'articles/{slug}/'

# Categories
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Random'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'

# Pages
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_URL = 'archive/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'archive/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

# Tags
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Authors
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# Appearance
DEFAULT_PAGINATION = False
THEME = 'attila'
MENUITEMS = (
    ('Home', '/'),
    ('Tags', f'/{TAGS_URL}'),
    ('Categories', f'/{CATEGORIES_URL}'),
    ('Archives', f'/{ARCHIVES_URL}'),
)

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        # Needed for code syntax highlighting
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # This is for enabling the TOC generation
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
