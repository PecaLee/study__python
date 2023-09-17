from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "https://naver.com"
    )

perfect_URLs = []
web_dicts = {}

#For Loop
for site in websites:
    # print(f"https://{site}")
    # if not site.startswith("https://"):
    #     print("fix it")
    if site.startswith("https://"):
        perfect_URLs.append(site)
    else:
        perfect_URLs.append(f"https://{site}")

for site in perfect_URLs:
    response = get(site)
    if response.status_code == 200:
        web_dicts[site] = "OK"
        print(f"{site} is OK.")
    else:
        web_dicts[site] = "Fail"
        print(f"{site} isn't OK.")

print(web_dicts)