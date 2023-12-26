# Base configuration
AUTHOR = 'esynr3z'
SITENAME = 'positive slack'
SITESUBTITLE = 'Digital design, verification and collaterals'
SITEURL = 'http://localhost:8000'
OUTPUT_PATH = 'docs/'
PATH = "content"
STATIC_PATHS = ['assets']
EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
}


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
ARTICLE_LANG_URL = 'articles/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'articles/{slug}-{lang}/index.html'
DEFAULT_METADATA = {
    'status': 'draft',
}

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
HOME_COLOR = '#369dbe'
MENUITEMS = (
    ('Home', '/'),
    ('Tags', f'/{TAGS_URL}'),
    ('Categories', f'/{CATEGORIES_URL}'),
    ('Archives', f'/{ARCHIVES_URL}'),
)
CSS_OVERRIDE = ['assets/css/myblog.css']
SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = True
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = True

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

# Plugins
PLUGIN_PATHS = [
  'plugins',
]
PLUGINS = [
  'pelican.plugins.sitemap',
  'pelican.plugins.neighbors',
  'pelican.plugins.webassets',
  'post_stats',
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
GISCUS_ENABLED = False
GISCUS_REPO = "positive-slack/positive-slack.github.io"
GISCUS_REPO_ID = "R_kgDOK9PAQQ"
GISCUS_CATEGORY = "Posts"
GISCUS_CATEGORY_ID = "DIC_kwDOK9PAQc4CcALQ"
GISCUS_MAPPING = "title"
GISCUS_STRICT = "1"
GISCUS_REACTIONS_ENABLED = "1"
GISCUS_INPUT_POSITION = "bottom"
GISCUS_THEME = "dark"
GISCUS_LANG = "en"

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
