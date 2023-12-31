from datetime import datetime

# Site information
AUTHOR = 'esynr3z'
SITENAME = 'positive slack blog'
SITETITLE = SITENAME
SITESUBTITLE = 'digital design, verification and collaterals'
SITEDESCRIPTION = SITESUBTITLE
SITEURL = 'http://localhost:8000'
SITELOGO = '/assets/logo.jpg'

# Paths and metadata
RELATIVE_URLS = True
OUTPUT_PATH = 'docs/'
PATH = "content"
STATIC_PATHS = ['assets']
EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/css/myblog.css': {'path': 'assets/css/myblog.css'},
}

# Date and locale
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'Europe/Moscow'
LOCALE = 'en_US'
DEFAULT_LANG = 'en'
OG_LOCALE = LOCALE

# Articles
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}/index.html'
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
DISPLAY_PAGES_ON_MENU = False

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

# Appearance
THEME = 'flex'
BROWSER_COLOR = '#369DBE'
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
USE_LESS = False
CUSTOM_CSS = 'assets/css/myblog.css'

# Page structure
DEFAULT_PAGINATION = 10
MAIN_MENU = True
HOME_HIDE_TAGS = False
MENUITEMS = (
    ('Tags', f'/{TAGS_URL}'),
    ('Categories', f'/{CATEGORIES_URL}'),
    ('Archives', f'/{ARCHIVES_URL}'),
)
SOCIAL = (
    ("question", "/pages/about/"),
    ("github", "https://github.com/esynr3z"),
    ("telegram", "https://t.me/positiveslack"),
    ("comment", "https://github.com/positive-slack/positive-slack.github.io/discussions/categories/feedback"),
    ("rss", "/feeds/all.atom.xml"),
)
LINKS = ()
LINKS_IN_NEW_TAB = 'external'

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
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
  'pelican.plugins.neighbors',
  'pelican.plugins.related_posts',
  'pelican.plugins.series',
  'post_stats',
]

# Related posts
RELATED_POSTS_MAX = 3

# Comments
GISCUS_ENABLED = True
GISCUS_REPO = "positive-slack/positive-slack.github.io"
GISCUS_REPO_ID = "R_kgDOK9PAQQ"
GISCUS_CATEGORY = "Posts"
GISCUS_CATEGORY_ID = "DIC_kwDOK9PAQc4CcALQ"
GISCUS_MAPPING = "title"
GISCUS_REACTIONS_ENABLED = "1"

# License
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}
COPYRIGHT_YEAR = datetime.now().year

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
