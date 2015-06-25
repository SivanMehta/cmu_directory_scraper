from mechanize import Browser
from BeautifulSoup import BeautifulSoup

def make_request(letter):
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
        first = info[0].contents[1].contents
        last = info[1].contents[1].contents
        andrew = info[2].contents[1].contents
        affiliation = info[3].contents
        department = info[4].contents

        print first, last, andrew, affiliation, department
        print "==================="

def main():
    make_request("a")

if __name__ == "__main__":
    main()