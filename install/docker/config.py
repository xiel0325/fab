

import imp
import json
import os
import sys

from dateutil import tz

from flask_appbuilder.security.manager import AUTH_REMOTE_USER, AUTH_DB
from myapp.stats_logger import DummyStatsLogger


# Realtime stats logger, a StatsD implementation exists
STATS_LOGGER = DummyStatsLogger()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if "MYAPP_HOME" in os.environ:
    DATA_DIR = os.environ["MYAPP_HOME"]
else:
    DATA_DIR = os.path.join(os.path.expanduser("~"), ".myapp")

APP_THEME = "readable.css"

FAB_UPDATE_PERMS=True
FAB_STATIC_FOLDER = BASE_DIR + "/static/appbuilder/"

# ---------------------------------------------------------
# Myapp specific config
# ---------------------------------------------------------
# PACKAGE_DIR = os.path.join(BASE_DIR, "static", "assets")
# PACKAGE_FILE = os.path.join(PACKAGE_DIR, "package.json")
# with open(PACKAGE_FILE) as package_file:
#     VERSION_STRING = json.load(package_file)["version"]

MYAPP_WORKERS = 2  # deprecated
MYAPP_CELERY_WORKERS = 32  # deprecated

MYAPP_WEBSERVER_ADDRESS = "0.0.0.0"
MYAPP_WEBSERVER_PORT = 80

# This is an important setting, and should be lower than your
# [load balancer / proxy / envoy / kong / ...] timeout settings.
# You should also make sure to configure your WSGI server
# (gunicorn, nginx, apache, ...) timeout setting to be <= to this setting
MYAPP_WEBSERVER_TIMEOUT = 300


# Your App secret key
# 设置才能正常使用session
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"  # noqa

# The SQLAlchemy connection string.
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DATA_DIR, "myapp.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_SERVICE','mysql+pymysql://root:admin@127.0.0.1:3306/myapp?charset=utf8')  # default must set None

CSV_EXPORT = {"encoding": "utf_8_sig"}
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False

# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = ["myapp.views.core.log"]

# Whether to run the web server in debug mode or not
DEBUG = os.environ.get("FLASK_ENV") == "development"
FLASK_USE_RELOAD = True

# Myapp allows server-side python stacktraces to be surfaced to the
# user when this feature is on. This may has security implications
# and it's more secure to turn it off in production settings.
SHOW_STACKTRACE = True

# Extract and use X-Forwarded-For/X-Forwarded-Proto headers?
ENABLE_PROXY_FIX = False

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "Myapp"

# Uncomment to setup an App icon
APP_ICON = "/static/assets/images/myapp-logo@2x.png"
APP_ICON_WIDTH = 126

# Uncomment to specify where clicking the logo would take the user
# e.g. setting it to '/welcome' would take the user to '/myapp/welcome'
LOGO_TARGET_PATH = None


# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# AUTH_TYPE = AUTH_REMOTE_USER
# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = False

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Gamma"

# RECAPTCHA_PUBLIC_KEY = 'GOOGLE PUBLIC KEY FOR RECAPTCHA'
# RECAPTCHA_PRIVATE_KEY = 'GOOGLE PRIVATE KEY FOR RECAPTCHA'

OAUTH_PROVIDERS=[]

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://open.login.yahoo.com/' },
#    { 'name': 'Flickr', 'url': 'https://www.flickr.com/<username>' },


# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "myapp/translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "zh": {"flag": "cn", "name": "Chinese"},
}

# ---------------------------------------------------
# Feature flags
# ---------------------------------------------------
# Feature flags that are set by default go here. Their values can be
# For example, DEFAULT_FEATURE_FLAGS = { 'FOO': True, 'BAR': False } here
# and FEATURE_FLAGS = { 'BAR': True, 'BAZ': True } in myapp_config.py
# will result in combined feature flags of { 'FOO': True, 'BAR': True, 'BAZ': True }
DEFAULT_FEATURE_FLAGS = {
    # Experimental feature introducing a client (browser) cache
    "CLIENT_CACHE": False,
    "ENABLE_EXPLORE_JSON_CSRF_PROTECTION": False,
}

# A function that receives a dict of all feature flags
# (DEFAULT_FEATURE_FLAGS merged with FEATURE_FLAGS)
# can alter it, and returns a similar dict. Note the dict of feature
# flags passed to the function is a deepcopy of the dict in the config,
# and can therefore be mutated without side-effect
#
# GET_FEATURE_FLAGS_FUNC can be used to implement progressive rollouts,
# role-based features, or a full on A/B testing framework.
#
# from flask import g, request
# def GET_FEATURE_FLAGS_FUNC(feature_flags_dict):
#     feature_flags_dict['some_feature'] = g.user and g.user.id == 5
#     return feature_flags_dict
GET_FEATURE_FLAGS_FUNC = None

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = BASE_DIR + "/static/file/uploads/"
DOWNLOAD_FOLDER = BASE_DIR + "/static/file/download/"
DOWNLOAD_URL = "/static/file/download/"
# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = BASE_DIR + "/static/file/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/file/uploads/"

# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24  # cache默认超时是24小时，一天才过期
CACHE_CONFIG = {"CACHE_TYPE": "null"}    # 不使用缓存
TABLE_NAMES_CACHE_CONFIG = {"CACHE_TYPE": "null"}   # 不使用缓存

# CORS Options
ENABLE_CORS = True
CORS_OPTIONS = {"supports_credentials":True}

# Chrome allows up to 6 open connections per domain at a time. When there are more
# than 6 slices in dashboard, a lot of time fetch requests are queued up and wait for
# next available socket. PR #5039 is trying to allow domain sharding for Myapp,
# and this feature will be enabled by configuration only (by default Myapp
# doesn't allow cross-domain request).
MYAPP_WEBSERVER_DOMAINS = None

# ---------------------------------------------------
# Time grain configurations
# ---------------------------------------------------
# List of time grains to disable in the application (see list of builtin
# time grains in myapp/db_engine_specs.builtin_time_grains).
# For example: to disable 1 second time grain:
# TIME_GRAIN_BLACKLIST = ['PT1S']
TIME_GRAIN_BLACKLIST = []

# Additional time grains to be supported using similar definitions as in
# myapp/db_engine_specs.builtin_time_grains.
# For example: To add a new 2 second time grain:
# TIME_GRAIN_ADDONS = {'PT2S': '2 second'}
TIME_GRAIN_ADDONS = {}

# Implementation of additional time grains per engine.
# For example: To implement 2 second time grain on clickhouse engine:
# TIME_GRAIN_ADDON_FUNCTIONS = {
#     'clickhouse': {
#         'PT2S': 'toDateTime(intDiv(toUInt32(toDateTime({col})), 2)*2)'
#     }
# }
TIME_GRAIN_ADDON_FUNCTIONS = {}

# Console Log Settings
ADDITIONAL_MODULE_DS_MAP = {}
ADDITIONAL_MIDDLEWARE = []

LOG_FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
LOG_LEVEL = "DEBUG"

# ---------------------------------------------------
# Enable Time Rotate Log Handler
# ---------------------------------------------------
# LOG_LEVEL = DEBUG, INFO, WARNING, ERROR, CRITICAL

ENABLE_TIME_ROTATE = False
TIME_ROTATE_LOG_LEVEL = "DEBUG"
FILENAME = os.path.join(DATA_DIR, "myapp.log")
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 30

# Custom logger for auditing queries. This can be used to send ran queries to a
# structured immutable store for auditing purposes. The function is called for
# every query ran, in both SQL Lab and charts/dashboards.
# def QUERY_LOGGER(
#     database,
#     query,
#     schema=None,
#     user=None,
#     client=None,
#     security_manager=None,
# ):
#     pass

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.environ.get("MAPBOX_API_KEY", "")

# If defined, shows this text in an alert-warning box in the navbar
# one example use case may be "STAGING" to make it clear that this is
# not the production version of the site.
WARNING_MSG = None

from celery.schedules import crontab
from werkzeug.contrib.cache import RedisCache

# 查询结果的缓存
RESULTS_BACKEND = RedisCache(
    host='redis', port=6379, key_prefix='myapp_results')


class CeleryConfig(object):
    BROKER_URL = 'redis://redis:6379/0'
    CELERY_IMPORTS = (
        'myapp.tasks',
    )

    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERYD_LOG_LEVEL = 'DEBUG'
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 120,
            'soft_time_limit': 150,
            'ignore_result': True,
        },
    }
    CELERYBEAT_SCHEDULE = {
        'email_reports.schedule_hourly': {
            'task': 'email_reports.schedule_hourly',
            'schedule': crontab(minute=1, hour='*'),
        },
    }


CELERY_CONFIG = CeleryConfig

# Set celery config to None to disable all the above configuration
# CELERY_CONFIG = None

# Additional static HTTP headers to be served by your Myapp server. Note
# Flask-Talisman aplies the relevant security HTTP headers.
HTTP_HEADERS = {
    "Access-Control-Allow-Origin":"*",
    "Access-Control-Allow-Methods":"*",
    "Access-Control-Allow-Headers":"*",
}


# A dictionary of items that gets merged into the Jinja context for
# SQL Lab. The existing context gets updated with this dictionary,
# meaning values for existing keys get overwritten by the content of this
# dictionary.
JINJA_CONTEXT_ADDONS = {}

# Roles that are controlled by the API / Myapp and should not be changes
# by humans.
ROBOT_PERMISSION_ROLES = ["Gamma", "Admin"]

CONFIG_PATH_ENV_VAR = "MYAPP_CONFIG_PATH"

# If a callable is specified, it will be called at app startup while passing
# a reference to the Flask app. This can be used to alter the Flask app
# in whatever way.
# example: FLASK_APP_MUTATOR = lambda x: x.before_request = f
FLASK_APP_MUTATOR = None

# Set this to false if you don't want users to be able to request/grant
ENABLE_ACCESS_REQUEST = True

# smtp server configuration
EMAIL_NOTIFICATIONS = False  # all the emails are sent using dryrun
SMTP_HOST = "localhost"
SMTP_STARTTLS = True
SMTP_SSL = False
SMTP_USER = ""
SMTP_PORT = 25
SMTP_PASSWORD = ""
SMTP_MAIL_FROM = ""

if not CACHE_DEFAULT_TIMEOUT:
    CACHE_DEFAULT_TIMEOUT = CACHE_CONFIG.get("CACHE_DEFAULT_TIMEOUT")

# Whether to bump the logging level to ERROR on the flask_appbuilder package
# Set to False if/when debugging FAB related issues like
# permission management
SILENCE_FAB = True

# The link to a page containing common errors and their resolutions
# It will be appended at the bottom of sql_lab errors.
TROUBLESHOOTING_LINK = ""

# CSRF token timeout, set to None for a token that never expires
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 7

# This link should lead to a page with instructions on how to gain access to a
PERMISSION_INSTRUCTIONS_LINK = ""

# Integrate external Blueprints to the app by passing them to your
# configuration. These blueprints will get integrated in the app
BLUEPRINTS = []

# Provide a callable that receives a tracking_url and returns another
# URL. This is used to translate internal Hadoop job tracker URL
# into a proxied one
TRACKING_URL_TRANSFORMER = lambda x: x  # noqa: E731

# Allow for javascript controls components
# this enables programmers to customize certain charts (like the
# geospatial ones) by inputing javascript in controls. This exposes
# an XSS security vulnerability
ENABLE_JAVASCRIPT_CONTROLS = False


# A callable that allows altering the database conneciton URL and params
# on the fly, at runtime. This allows for things like impersonation or
# arbitrary logic. For instance you can wire different users to
# use different connection parameters, or pass their email address as the
# username. The function receives the connection uri object, connection
# params, the username, and returns the mutated uri and params objects.
# Example:
#   def DB_CONNECTION_MUTATOR(uri, params, username, security_manager, source):
#       user = security_manager.find_user(username=username)
#       if user and user.email:
#           uri.username = user.email
#       return uri, params
#
# Note that the returned uri and params are passed directly to sqlalchemy's
# as such `create_engine(url, **params)`
DB_CONNECTION_MUTATOR = None

# When not using gunicorn, (nginx for instance), you may want to disable
# using flask-compress
ENABLE_FLASK_COMPRESS = True

# Enable / disable scheduled email reports
ENABLE_SCHEDULED_EMAIL_REPORTS = True

# If enabled, certail features are run in debug mode
# Current list:
# * Emails are sent using dry-run mode (logging only)
SCHEDULED_EMAIL_DEBUG_MODE = True

# 任务的最小执行间隔min
PIPELINE_TASK_CRON_RESOLUTION = 15

# Email report configuration
# From address in emails
EMAIL_REPORT_FROM_ADDRESS = "reports@myapp.org"

# Send bcc of all reports to this address. Set to None to disable.
# This is useful for maintaining an audit trail of all email deliveries.


# User credentials to use for generating reports
# This user should have permissions to browse all the dashboards and
# slices.
# TODO: In the future, login as the owner of the item to generate reports
EMAIL_REPORTS_USER = "admin"
EMAIL_REPORTS_SUBJECT_PREFIX = "[Report] "

# The webdriver to use for generating reports. Use one of the following
# firefox
#   Requires: geckodriver and firefox installations
#   Limitations: can be buggy at times
# chrome:
#   Requires: headless chrome
#   Limitations: unable to generate screenshots of elements
EMAIL_REPORTS_WEBDRIVER = "chrome"

# Any config options to be passed as-is to the webdriver
WEBDRIVER_CONFIGURATION = {}

# The base URL to query for accessing the user interface

# Send user to a link where they can report bugs
BUG_REPORT_URL = None
# Send user to a link where they can read more about Myapp
DOCUMENTATION_URL = None

# Do you want Talisman enabled?
TALISMAN_ENABLED = False
# If you want Talisman, how do you want it configured??
TALISMAN_CONFIG = {
    "content_security_policy": None,
    "force_https": True,
    "force_https_permanent": False,
}


try:
    if CONFIG_PATH_ENV_VAR in os.environ:
        # Explicitly import config module that is not in pythonpath; useful
        # for case where app is being executed via pex.
        print(
            "Loaded your LOCAL configuration at [{}]".format(
                os.environ[CONFIG_PATH_ENV_VAR]
            )
        )
        module = sys.modules[__name__]
        override_conf = imp.load_source(
            "myapp_config", os.environ[CONFIG_PATH_ENV_VAR]
        )
        for key in dir(override_conf):
            if key.isupper():
                setattr(module, key, getattr(override_conf, key))

    else:
        from myapp_config import *  # noqa
        import myapp_config

        print(
            "Loaded your LOCAL configuration at [{}]".format(myapp_config.__file__)
        )
except ImportError:
    pass


def get_env_variable(var_name, default=None):
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = 'The environment variable {} was missing, abort...'.format(var_name)
            raise EnvironmentError(error_msg)


# 数据库连接池的配置
SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_POOL_RECYCLE = 300  # 超时重连， 必须小于数据库的超时终端时间
SQLALCHEMY_MAX_OVERFLOW = 300


# redis的配置
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'admin')   # default must set None
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
WEBDRIVER_BASEURL=os.getenv('WEBDRIVER_BASEURL', 'http://127.0.0.1/')
SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_SERVICE','mysql+pymysql://root:password@127.0.0.1:3306/myapp?charset=utf8')  # default must set None
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@host.docker.internal:3306/myapp?charset=utf8'

from celery.schedules import crontab
from werkzeug.contrib.cache import RedisCache

RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST, port=int(REDIS_PORT), key_prefix='myapp_results',password=REDIS_PASSWORD)

class CeleryConfig(object):
    # 任务队列
    BROKER_URL =  'redis://:%s@%s:%s/0'%(REDIS_PASSWORD,REDIS_HOST,str(REDIS_PORT)) if REDIS_PASSWORD else 'redis://%s:%s/0'%(REDIS_HOST,str(REDIS_PORT))
    # celery_task的定义模块
    CELERY_IMPORTS = (
        'myapp.tasks',
    )
    # 结果存储
    CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/0'%(REDIS_PASSWORD,REDIS_HOST,str(REDIS_PORT)) if REDIS_PASSWORD else 'redis://%s:%s/0'%(REDIS_HOST,str(REDIS_PORT))
    CELERYD_LOG_LEVEL = 'DEBUG'
    # celery worker每次去redis取任务的数量
    CELERYD_PREFETCH_MULTIPLIER = 10
    # 每个worker执行了多少次任务后就会死掉，建议数量大一些
    # CELERYD_MAX_TASKS_PER_CHILD = 200
    # celery任务执行结果的超时时间
    # CELERY_TASK_RESULT_EXPIRES = 1200
    # 单个任务的运行时间限制，否则会被杀死
    # CELERYD_TASK_TIME_LIMIT = 60
    # 任务发送完成是否需要确认，对性能会稍有影响
    CELERY_ACKS_LATE = True
    # celery worker的并发数，默认是服务器的内核数目, 也是命令行 - c参数指定的数目
    # CELERYD_CONCURRENCY = 4
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = False

    # 任务的限制，key是celery_task的name，值是限制配置
    CELERY_ANNOTATIONS = {
        'task.task1': {
            'rate_limit': '1/s',
            'time_limit': 1200,
            'soft_time_limit': 1200,
            'ignore_result': True,
        },
    }


    # 定时任务的配置项，key为celery_task的name，值是调度配置
    CELERYBEAT_SCHEDULE = {
        'task_task1': {
            'task': 'task.task1',
            'schedule': 10.0,
            # 'schedule': crontab(minute='1', hour='*'),
        },
    }


DOCUMENTATION_URL='https://github.com/tencentmusic/fab'  # 帮助文档地址，显示在web导航栏

ROBOT_PERMISSION_ROLES=[]   # 角色黑名单

FAB_API_MAX_PAGE_SIZE=100    # 最大翻页数目，不设置的话就会是20
CACHE_DEFAULT_TIMEOUT = 10*60  # 缓存默认过期时间，10分钟才过期
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis', # 使用 Redis
    'CACHE_REDIS_HOST': REDIS_HOST, # 配置域名
    'CACHE_REDIS_PORT': int(REDIS_PORT), # 配置端口号
    'CACHE_REDIS_URL':'redis://:%s@%s:%s/0'%(REDIS_PASSWORD,REDIS_HOST,str(REDIS_PORT)) if REDIS_PASSWORD else 'redis://%s:%s/0'%(REDIS_HOST,str(REDIS_PORT))   # 0，1为数据库编号（redis有0-16个数据库）
}

CELERY_CONFIG = CeleryConfig

REMEMBER_COOKIE_NAME="remember_token"   # 使用cookie认证用户的方式
AUTH_HEADER_NAME = 'Authorization'
