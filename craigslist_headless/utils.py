from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
from .browser import CraigslistBrowser

ALL_SITES_URL = 'http://www.craigslist.org/about/sites'
SITE_URL = 'http://%s.craigslist.org'
USER_AGENT = 'Mozilla/5.0'

def bs(content):
    return BeautifulSoup(content, 'html.parser')


def isiterable(var):
    try:
        return iter(var) and True
    except TypeError:
        return False


def requests_get(browser, *args, **kwargs):
    """
    Retries if a RequestException is raised (could be a connection error or
    a timeout).
    """
    logger = kwargs.pop('logger', None)
    wait = kwargs.pop('wait', False)
    # Set default User-Agent header if not defined.
    # kwargs.setdefault('headers', {}).setdefault('User-Agent', USER_AGENT)
    print(kwargs)
    if kwargs:
        query_string = urlencode(kwargs["params"])
        print(query_string)
        url = args[0] + "?" + query_string
    else:
        url = args[0]
    try:
        browser.visit(url)
        page_source = browser.show_source(wait)
        # if "unrecoverableError" in str(page_source):
        #     logger.warning("We have been found out?")
            # quit_browser()
            # raise Exception("We've been had!")
        return page_source
    except RequestException as exc:
        if logger:
            logger.warning('Request failed (%s). Retrying ...', exc)
        browser.visit(url)
        return browser.show_source(wait)


def get_all_sites():
    response = requests.get(ALL_SITES_URL)
    response.raise_for_status()  # Something failed?
    soup = BeautifulSoup(response.content, 'html.parser')
    sites = set()

    for box in soup.findAll('div', {'class': 'box'}):
        for a in box.findAll('a'):
            # Remove protocol and get subdomain
            site = a.attrs['href'].rsplit('//', 1)[1].split('.')[0]
            sites.add(site)

    return sites


def get_all_areas(site):
    response = requests.get(SITE_URL % site)
    response.raise_for_status()  # Something failed?
    soup = BeautifulSoup(response.content, 'html.parser')
    raw = soup.select('ul.sublinks li a')
    sites = set(a.attrs['href'].rsplit('/')[1] for a in raw)
    return sites


def get_list_filters(url):
    browser = CraigslistBrowser()
    list_filters = {}
    page_source = requests_get(browser, url)
    soup = bs(page_source)
    for list_filter in soup.find_all('div', class_='search-attribute'):
        filter_key = list_filter.attrs['data-attr']
        filter_labels = list_filter.find_all('label')
        options = {opt.text.strip(): opt.find('input').get('value')
                   for opt in filter_labels}
        list_filters[filter_key] = {'url_key': filter_key, 'value': options}
    browser.quit()
    return list_filters
