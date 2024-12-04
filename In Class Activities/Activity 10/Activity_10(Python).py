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




url = 'https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0'



main_tree = get_web_tree(url)
print(main_tree.xpath)



bugInfo = main_tree.xpath('//*[@class= "buglisting-row"]')


print("Bug Number: Status: Heat: Title:")

for bug in bugInfo:
    bugImportance = bug.xpath(".//div['buglisting-col1']//text()")
    print(bugImportance[9].strip(), bugImportance[3].strip(), bugImportance[18].strip(), bugImportance[11].strip())

# Full bug data to insert into the database
bug_data = [
    (10714, 'Fix Released', 4, "Live cd doesn't boot"),
    (10742, 'Fix Released', 6, "Fails to build from source"),
    (11037, 'Fix Released', 20, "cupsys upgrade error (cupsys won't stop)"),
    (11147, 'Fix Released', 6, "gnome-menus conflicts with kdelibs-data in /etc/xdg/menus/applications.menu"),
    (11193, 'Fix Released', 10, "[warty] Firefox Window Injection Vulnerability"),
    (11283, 'Fix Released', 58, "gnome-panel / nautilus hang due to gnome-vfs-daemon"),
    (11286, 'Fix Released', 20, "6.8.1-1ubuntu7 is broken"),
    (11438, 'Fix Released', 8, "can't configure python2.4-minimal without python2.4 installed"),
    (11550, 'Fix Released', 14, "Python 2.4 breaks Bittorrent"),
    (11574, 'Fix Released', 18, "Network Places menu has trouble opening sftp in nautilus"),
    (11623, 'Fix Released', 4, "Ubuntu-specific changes lost in merge"),
    (11829, 'Fix Released', 6, "Several modules unloadable in 2.6.10-4"),
    (11855, 'Fix Released', 24, "gtksourceview-sharp should no provide nemerle.lang"),
    (11885, 'Fix Released', 4, "reportbug has python2.3 hardcoded"),
    (11897, 'Fix Released', 8, "Gnome-panel seems to have a mismatched dependency (AMD64)"),
    (11904, 'Fix Released', 8, "vgchange segfaults with 2.6.10-2"),
    (11974, 'Fix Released', 12, "vbestate save causes hang on some systems"),
    (12114, 'Fix Released', 4, "install fails on AMD64"),
    (12209, 'Fix Released', 10, "Metacity titlebar oddity"),
    (12239, 'Fix Released', 4, "Ubuntu changes lost in merge?"),
    (12254, 'Fix Released', 20, "Evolution-data-server crashes with floating point exception"),
    (12347, 'Fix Released', 6, "HOARY: gnopernicus: fails to start - lib problems"),
    (12386, 'Fix Released', 22, "grub installation hangs at 33%"),
    (12459, 'Fix Released', 10, "GRUB segfaults on amd64"),
    (12467, 'Fix Released', 10, "Gnome Users and Groups: Changing a user's UID breaks the account"),
    (12560, 'Fix Released', 8, "after upgrading to hoary on ibook G3, screen is in quarters"),
    (12599, 'Fix Released', 20, "Large number of udev processes spawned"),
    (12683, 'Fix Released', 20, "trying to overwrite `/usr/share/icons/hicolor/48x48/apps/gnome-run.png', which is also in package gnome-panel-data"),
    (12721, 'Fix Released', 8, "python2.4-minimal must not be essential"),
    (12753, 'Fix Released', 6, "/usr/bin/twistd fails to run with 'ImportError: No module named profile'"),
    (12939, 'Fix Released', 22, "polypaudio crasher on powerpc"),
    (12940, 'Fix Released', 6, "Kernel Panic with new kernel-2.6.10-3 when logging in"),
    (12961, 'Fix Released', 4, "NIC detection error in installer - ubuntu-sparc"),
    (12972, 'Fix Released', 10, "Kernel update missing corresponding linux-restricted-modules update"),
    (12977, 'Fix Released', 6, "Default kernel parameters missing on live CD"),
    (13036, 'Fix Released', 8, "Hoary Install not recognizing the SCSI-Harddisk to install onto"),
    (13404, 'Fix Released', 12, "Language packs broken, due to 'dependency cycle'"),
    (13458, 'Fix Released', 4, "emacs21: FTBFS: timestamp skew issues."),
    (13499, 'Fix Released', 14, "Improper boundary checking -> SIGSEGV"),
    (13522, 'Fix Released', 8, "i810 from HEAD is unusable"),
    (13645, 'Fix Released', 8, "Kmail segfaults"),
    (13753, 'Fix Released', 14, "language-pack upgrades are fragile"),
    (13830, 'Fix Released', 24, "ABI compatibility changed in 2.6.10-4-26"),
    (13888, 'Fix Released', 4, "db3 sets LD_ASSUME_KERNEL on amd64"),
    (14069, 'Fix Released', 6, "Installer asks for time zone after copy of packages to hard drive"),
    (14160, 'Fix Released', 8, "fontconfig error update"),
    (14176, 'Fix Released', 36, "libc does not do per-domain result caching"),
    (14186, 'Fix Released', 4, "FTBFS: can't find -lgvgd"),
    (14190, 'Fix Released', 4, "Fails to install - debconf errors"),
    (14223, 'Fix Released', 8, "FTBFS: g++ errors"),
    (14224, 'Fix Released', 4, "FTBFS: LinuxThreads not found"),
    (14226, 'Fix Released', 4, "FTBFS: Undefined reference."),
    (14227, 'Fix Released', 8, "FTBFS: patch fails."),
    (14229, 'Fix Released', 8, "FTBFS: conflicting build-deps"),
    (14235, 'Fix Released', 14, "Java VM locking on highly multithreaded Java apps"),
    (14252, 'Fix Released', 6, "FTBFS: can't find libktnef.la"),
    (14271, 'Fix Released', 8, "gnome-vfs-daemon segfault"),
    (14274, 'Fix Released', 8, "FTBFS: segv in ld"),
    (14277, 'Fix Released', 12, "Hang while loading snd-nm256 module"),
    (14283, 'Fix Released', 6, "klogd stops logging after some time"),
    (14355, 'Fix Released', 24, "libapache2-mod-php4 breaks Squirrelmail and Gallery"),
    (14436, 'Fix Released', 4, "FTBFS: missing headers"),
    (14536, 'Fix Released', 8, "can't log in after installation because of wrong keymap"),
    (14537, 'Fix Released', 6, "ubuntu install leaves me unable to boot my fedora core 3 installation"),
    (14815, 'Fix Released', 4, "FTBFS: broken build-depends"),
    (14816, 'Fix Released', 4, "FTBFS: autobmake versionitis"),
    (14832, 'Fix Released', 4, "Warty->Hoary upgrade failure on amd64 due to file conflict"),
    (14889, 'Fix Released', 4, "FTBFS: bad patch"),
    (14909, 'Fix Released', 6, "Processor bug causes p4-clockmod to shut Pentium 4 laptop down"),
    (15001, 'Fix Released', 74, "Administrator mode not working"),
    (15011, 'Fix Released', 6, "should conflict with xfree86-driver-synaptics?"),
    (16038, 'Fix Released', 10, "Installer fails to write grub to mbr?"),
    (16231, 'Fix Released', 30, "Code execution through javascript: favicons"),
    (16232, 'Fix Released', 8, "Arbitrary code execution from Firefox sidebar panel II"),
    (16233, 'Fix Released', 8, "Privilege escalation via DOM property overrides")
]

my_db = DBConnector.MyDB()

sql_create_table = """
CREATE TABLE IF NOT EXISTS Activity10_DeWayne_Rotenberry (
    Bug_Number INT, 
    Bug_Status VARCHAR(255), 
    Bug_Heat INT, 
    Bug_Title VARCHAR(255)
);
"""
my_db.query(sql_create_table, '')

# Insert bug data into the table
sql_insert = """
INSERT INTO Activity10_DeWayne_Rotenberry (Bug_Number, Bug_Status, Bug_Heat, Bug_Title)
VALUES (%s, %s, %s, %s)
"""
for bug in bug_data:
    my_db.query(sql_insert, bug)

