import mechanize

def main():
    br = mechanize.Browser()
    br.open("https://directory.andrew.cmu.edu/")

    br.select_form(nr=0)

    br.form['search[generic_search_terms]'] = "a"
    br.submit()
    print br.response().read()

if __name__ == "__main__":
    main()