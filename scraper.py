import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_flipkart(search_term, num_pages):

    Product_name = []
    Prices = []
    Description = []
    Reviews = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    search_term = search_term.replace(" ", "+")

    for page in range(1, num_pages + 1):

        url = f"https://www.flipkart.com/search?q={search_term}&page={page}"

        try:
            r = requests.get(url, headers=headers, timeout=10)

            soup = BeautifulSoup(r.text, "html.parser")

            box = soup.find("div", class_="QSCKDh dLgFEE")

            if not box:
                continue

            names = box.find_all("div", class_="RG5Slk")
            prices = box.find_all("div", class_="hZ3P6w DeU9vF")
            desc = box.find_all("ul", class_="HwRTzP")
            reviews = box.find_all("div", class_="MKiFS6")

            for item in names:
                Product_name.append(item.text)

            for item in prices:
                Prices.append(item.text)

            for item in desc:
                Description.append(item.text)

            for item in reviews:
                Reviews.append(item.text)

        except Exception:
            pass

    max_len = max(
        len(Product_name),
        len(Prices),
        len(Description),
        len(Reviews),
        1
    )

    Product_name.extend(["N/A"] * (max_len - len(Product_name)))
    Prices.extend(["N/A"] * (max_len - len(Prices)))
    Description.extend(["N/A"] * (max_len - len(Description)))
    Reviews.extend(["N/A"] * (max_len - len(Reviews)))

    df = pd.DataFrame({
        "Product Name": Product_name,
        "Price": Prices,
        "Description": Description,
        "Reviews": Reviews
    })

    return df