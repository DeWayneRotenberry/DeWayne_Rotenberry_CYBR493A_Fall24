"""
Web scrapping in Python
This is an example of scrapping a web page in Python using requests and lxml

"""
import requests
from lxml import html
import DBConnector
import os


def get_web_tree(link):
    """
    This method gets a web page from the specified url, and returns a tree of all elements in the page
    :param link: The webpage to access and process
    :return: The tree element created from the page
    """
    # Welcome message
    # print('Obtaining the page: ', str(link))
    # get the page
    page = requests.get(link)
    # get the elements from the page
    page_tree = html.fromstring(page.content)
    # return the tree of the web page
    return page_tree


# In[51]:


url = 'https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0'

# In[52]:


main_tree = get_web_tree(url)
print(main_tree.xpath)

# In[53]:


bugInfo = main_tree.xpath('//*[@class= "buglisting-row"]')

# In[66]:


print("Bug Number: Status: Heat: Title:")

for bug in bugInfo:
    bugImportance = bug.xpath(".//div['buglisting-col1']//text()")
    print(bugImportance[9].strip(), bugImportance[3].strip(), bugImportance[18].strip(), bugImportance[11].strip())




my_db = DBConnector.MyDB()

sqlCommand = 'CREATE TABLE IF NOT EXISTS Activity10_DeWayne_Rotenberry (Bug_Number int, Bug_Status varchar, Bug_Heat int, Bug_Title varchar);'

my_db.query(sqlCommand, '')





my_db = DBConnector.MyDB()

sqlCommand = """
    INSERT INTO Activity10_DeWayne_Rotenberry (Bug_Number, Bug_Status, Bug_Heat, Bug_Title)
    VALUES (%s, %s, %s, %s)
    """
my_db.query(sqlCommand, '')
# In[ ]:




