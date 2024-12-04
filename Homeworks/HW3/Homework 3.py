import Web_Scraping as wb
import DBConnector as dbc
import requests
from lxml import html



"""
This will be our main screen
"""


def main():
    # Your code goes here.
    main_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=0&start=0"
    links = generate_links(main_link)
    user_input = int(input('Which page would you like to view?'))
    display_bugs_info(links[user_input])



def generate_links(start_link):
    """
        This method generates ALL the links to all pages and stores them in a list (This is activity #10)
        :param start_link: The start link of the bug tracking system.
        :return: The list of all pages to all bugs. Each element in the list will refer to one page
    """
    BUGS = 420638  # Total number of bugs
    BUGS_PER_PAGE = 75  # Bugs displayed per page
    total_pages = (BUGS + BUGS_PER_PAGE - 1) // BUGS_PER_PAGE  # Total pages

    # Generate URLs for each page
    list_of_links = []
    for page in range(total_pages):
        start_value = page * BUGS_PER_PAGE
        page_url = f"{start_link}&memo={BUGS_PER_PAGE}&start={start_value}"
        list_of_links.append(page_url)

    return list_of_links


def display_bugs_info(bugs_page):
    """
        This method displays the bugs info. for a specific page
        Display: Bug Number, Title, Importance, and Heat - in this order for each bug.(This is activities #11 and 12)
        :param bugs_page: The  link to the page
    """
 # Fetch and parse the webpage
    page = requests.get(bugs_page)
    tree = html.fromstring(page.content)

    # Locate the bug rows
    bug_rows = tree.xpath('//div[@class="buglisting-row"]')

    # Display header
    print("Bug Number:   Title:                                        Importance:   Heat:")

    # Extract and display details for each bug
    for row in bug_rows:
        bug_number = row.xpath('.//span[@class="bugnumber"]/text()')[0].strip()
        bug_title = row.xpath('.//a[@class="bugtitle"]/text()')[0].strip()
        bug_importance = row.xpath('.//div[contains(@class, "importance")]/text()')[0].strip()
        bug_heat = row.xpath('.//span[@class="sprite flame"]/text()')[0].strip()
        print(f"{bug_number:<12} {bug_title:<50} {bug_importance:<12} {bug_heat:<5}")

if __name__ == "__main__":
    main()
