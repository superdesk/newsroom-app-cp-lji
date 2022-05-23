import pathlib
from flask_babel import lazy_gettext

from newsroom.web.default_settings import (
    CELERY_BEAT_SCHEDULE as CELERY_BEAT_SCHEDULE_DEFAULT,
    CORE_APPS as DEFAULT_CORE_APPS,
    BLUEPRINTS as DEFAULT_BLUEPRINTS,
)


SERVER_PATH = pathlib.Path(__file__).resolve().parent
CLIENT_PATH = SERVER_PATH.parent.joinpath("client")

SITE_NAME = 'News Centre'
SHOW_USER_REGISTER = True
COPYRIGHT_HOLDER = 'LJI-IJL'
COPYRIGHT_NOTICE = ''
USAGE_TERMS = ''

PRIVACY_POLICY = PRIVACY_POLICY_EN = '/privacy'
TERMS_AND_CONDITIONS = TERMS_AND_CONDITIONS_EN = '/terms'
CONTACT_ADDRESS = 'https://www.thecanadianpress.com/contact/'
CONTACT_ADDRESS_EN = 'https://www.thecanadianpress.com/contact/'

WIRE_AGGS = {
    'language': {'terms': {'field': 'language', 'size': 50}},
    'service': {'terms': {'field': 'service.name', 'size': 50}},
    'subject': {'terms': {'field': 'subject.name', 'size': 20}},
}

WIRE_GROUPS = [
    {
        "field": "language",
        "label": lazy_gettext("Language"),
    },
]


BLUEPRINTS = [
    blueprint
    for blueprint in DEFAULT_BLUEPRINTS
    if blueprint not in [
        "newsroom.agenda",
        "newsroom.design",
        "newsroom.monitoring",
        "newsroom.news_api.api_tokens"
    ]
]

CORE_APPS = [
    app
    for app in DEFAULT_CORE_APPS
    if app not in [
        "newsroom.agenda",
        "newsroom.monitoring",
        "newsroom.news_api",
        "newsroom.news_api.api_tokens",
        "newsroom.news_api.api_audit",
    ]
]

COVERAGE_TYPES = {
    'text': {'name': 'Text', 'icon': 'text'},
    'photo': {'name': 'Photo', 'icon': 'photo'},
    'picture': {'name': 'Picture', 'icon': 'photo'},
    'audio': {'name': 'Audio', 'icon': 'audio'},
    'video': {'name': 'Video', 'icon': 'video'},
    'explainer': {'name': 'Explainer', 'icon': 'explainer'},
    'infographics': {'name': 'Infographics', 'icon': 'infographics'},
    'graphic': {'name': 'Graphic', 'icon': 'infographics'},
    'live_video': {'name': 'Live Video', 'icon': 'live-video'},
    'live_blog': {'name': 'Live Blog', 'icon': 'live-blog'},
    'video_explainer': {'name': 'Video Explainer', 'icon': 'explainer'}
}

DISPLAY_ABSTRACT = False

CLIENT_LOCALE_FORMATS = {
    "en": {  # defaults
        "TIME_FORMAT": "HH:mm",
        "DATE_FORMAT": "MMM DD, YYYY",
        "COVERAGE_DATE_TIME_FORMAT": "HH:mm DD/MM",
        "COVERAGE_DATE_FORMAT": "DD/MM",
    },
    "fr_CA": {
        "DATE_FORMAT": "DD MMM YYYY",
    }
}

LANGUAGES = ['en', 'fr_CA']
DEFAULT_LANGUAGE = 'en'

# Client configuration
CLIENT_CONFIG = {
    'default_language': DEFAULT_LANGUAGE,
    'locale_formats': CLIENT_LOCALE_FORMATS,
    'coverage_types': COVERAGE_TYPES,
    'display_abstract': DISPLAY_ABSTRACT,
    'display_all_versions_toggle': False,
    'hide_company_topics_feature': True,
    'list_animations': True,  # Enables or disables the animations for list item select boxes,
    'display_news_only': False,  # Displays news only switch in wire
    'item_actions': {
        'share': False,
    },
    'topic_actions': {
        'share': False,
    },
    'filter_panel_defaults': {
        'tab': {'wire': 'filters'},
        'open': {'wire': True},
    },
}

WATERMARK_IMAGE = None

CELERY_BEAT_SCHEDULE = {key: val for key, val in CELERY_BEAT_SCHEDULE_DEFAULT.items()
                        if key == 'newsroom.company_expiry'}

ENABLE_WATCH_LISTS = False

ACCOUNT_CREATED_EMAIL_SUBJECT = 'LJI News Centre account created/Accès au Centre de nouvelles de l’IJL'
