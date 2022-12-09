import csv
import time

import requests

from config import key

stocks = ["PFE", "JNJ","WBA","CVS", "MRK"]
for stock in stocks :
    #construct a query URL for each day of data and saving into a ictionary 
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data = requests.get(url)
    jdata =  data.json()
    results = jdata["results"]
    stockdata=[]
    # looping through each day of data and saving into a list 
    for day in results:
        print(day)
        closing_p = day["c"]
        closing_t = day ["t"]
        print(closing_p)
        print(closing_t)
        # convert to human readable time
        x = time.strftime('%Y-%m-%d', time.localtime(closing_t/1000))
        print(x)
        row = {"date":x, "price": closing_p}
        stockdata.append(row)
    with open(f"{stock}.csv", "w") as outfile:
        writer=csv.DictWriter(outfile, fieldnames=["date", "price"])
        writer.writeheader()
        writer.writerows(stockdata)













