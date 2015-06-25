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
    # print soup
    table = soup.findAll('td')
    for row in table:
        print row, "\n"
        
def main():
    make_request("a")

if __name__ == "__main__":
    main()