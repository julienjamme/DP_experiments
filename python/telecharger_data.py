from urllib.request import urlretrieve

data_files = ("capital_bike_share.csv", "user_visits.csv")

url_r = (
    "https://raw.githubusercontent.com/Hands-on-Differential-Privacy-Book/"
    "hands-on-differential-privacy/refs/heads/main/data/"
)

for f in data_files:
    url = url_r + f
    filename = "data/" + f
    urlretrieve(url, filename)
