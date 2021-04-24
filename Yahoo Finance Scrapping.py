from requests_html import HTMLSession,HTML

stocks = ["%5EIXIC","%5EGSPC","%5ERUT","GC%3DF","BTC-CAD"]

session = HTMLSession()
print("starting...")
for stock in stocks:
    try:
        r = session.get("https://finance.yahoo.com/quote/"+stock+"?p="+stock)
    except:
        print("an error occured while trying to load "+stock.replace("%5E",""))
        print("--------------------------------------")

    name = r.html.xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/h1")
    price = r.html.xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]")
    activity = r.html.xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[2]")

    print(name[0].text)
    print(price[0].text)
    print(activity[0].text)
    print("--------------------------------------")