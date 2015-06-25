from mechanize import Browser
from BeautifulSoup import BeautifulSoup

def make_request(letter):
    br = Browser()
    br.open("https://directory.andrew.cmu.edu/")

    br.select_form(nr=0)

    br.form['search[generic_search_terms]'] = letter
    br.submit()
    with open(".reponse.html", "w") as f:
        f.write(br.response().read())

def main():
    make_request("a")

if __name__ == "__main__":
    main()