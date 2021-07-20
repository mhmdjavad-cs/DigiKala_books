from bs4 import BeautifulSoup
from requests import get

def get_books(page_number):
    page = get(f"https://www.digikala.com/search/category-book/?pageno={page_number}&sortby=4")
    MySoup = BeautifulSoup(page.content, "html.parser")
    contents = MySoup.find("ul", class_="c-listing__items js-plp-products-list")

    for book in contents.find_all("a", class_="js-product-url"):
        if book.string != None:
            print(book.string)


n = input("how many pages to display?(or just enter \"pass\" to see the first page results):")

if n == "pass":
    get_books(1)
else:
    get_books(int(n))



