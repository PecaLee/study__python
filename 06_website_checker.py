websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "https://naver.com"
    )

perfect_URLs = []

#For Loop
for site in websites:
    # print(f"https://{site}")
    # if not site.startswith("https://"):
    #     print("fix it")
    if site.startswith("https://"):
        perfect_URLs.append(site)
    else:
        perfect_URLs.append(f"https://{site}")

print(perfect_URLs)
