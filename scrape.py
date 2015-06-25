from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from pprint import pprint
import string, sys

def clean(text):
    for char in string.whitespace + string.punctuation:
        text = text.replace(char, "")

    return text

def make_request(letter, people):
    browser = Browser()
    browser.open("https://directory.andrew.cmu.edu/")

    browser.select_form(nr=0)

    browser.form['search[generic_search_terms]'] = letter
    browser.submit()
    with open("response.html", "w") as f:
        f.write(browser.response().read())
        f.close()

    page = open("response.html", "r").read()
    soup = BeautifulSoup(page)

    table = soup.findAll('tr')
    for row in table[1:]:
        info = row.findAll('td')
        data = {}

        data["first"] = clean(info[0].contents[1].contents[0])
        data["last"] = clean(info[1].contents[1].contents[0])
        data["affiliation"] = clean(info[3].contents[0])
        data["department"] = clean(info[4].contents[0])

        andrew = info[2].contents[1].contents[0]
        people[andrew] = data

def main():
    people = {}
    for char in string.ascii_lowercase:
        make_request(char, people)

    #     sys.stdout.flush()
    #     sys.stdout.write("\rfinished %s... " % char)

    # print "done!"

    pprint(people)

if __name__ == "__main__":
    main()