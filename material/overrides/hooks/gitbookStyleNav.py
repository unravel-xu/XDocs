import os
import re

from glob import iglob
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from urllib.parse import urlencode, urlparse

def on_page_content(context: dict, page: Page, config: MkDocsConfig, nav: Navigation):


