"""
Web scrapping in Python
This is an example of scrapping a web page in Python using requests and lxml

"""
import requests
from lxml import html


def get_web_tree(link):
    """
    This method gets a web page from the specified url, and returns a tree of all elements in the page
    :param link: The webpage to access and process
    :return: The tree element created from the page
    """
    # Welcome message
    #print('Obtaining the page: ', str(link))
    # get the page
    page = requests.get(link)
    # get the elements from the page
    page_tree = html.fromstring(page.content)
    # return the tree of the web page
    return page_tree
