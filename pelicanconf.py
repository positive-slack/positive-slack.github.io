AUTHOR = 'esynr3z'
SITENAME = 'positive slack'
SITEURL = ""

OUTPUT_PATH = 'docs/'

ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'

PATH = "content"

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'Europe/Moscow'

LOCALE = 'en_US'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

DEFAULT_PAGINATION = False

THEME = 'attila'

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

MENUITEMS = (
    ('Home', '/'),
    ('Tags', '/tags.html'),
    ('Categories', '/categories.html'),
    ('Archives', '/archives.html'),
)
