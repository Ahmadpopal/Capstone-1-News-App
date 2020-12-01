import requests

# API KEY
# Yahoo
# key = "14b26be65a0a42c292fae32a756fd7c6"
# Gmail
key = "d6ebb4e56508451dbe4b97c8ce82ccbe"
# BASE URL
BASE_URL = "https://newsapi.org/v2/"


# GENERAL HEADLINES ENDPOINT
headlines_response = requests.get(
    f"{BASE_URL}top-headlines", params={"category": "general", "apiKey": key, "pageSize": 50})

HEADLINES = headlines_response.json()


# GENERAL TECH CRANCH

TECH_CRUNCH_NEWS_response = requests.get(f"{BASE_URL}everything", params={
    "apiKey": key, "domains": "techcrunch.com,thenextweb.com"})

TECH_CRUNCH_data = TECH_CRUNCH_NEWS_response.json()


# OTHER NEWS SOURCES
"https://newsapi.org/v2/sources?language=en&apiKey=14b26be65a0a42c292fae32a756fd7c6"
OTHER_SOURCES_NEWS_response = requests.get(f"{BASE_URL}sources", params={
    "apiKey": key, "language": "en", "apiKey": key})

OTHER_SOURCE_data = OTHER_SOURCES_NEWS_response.json()


# FUNCTION WILL GET NEWS BY REGION
def get_news(country):
    response = requests.get(f"{BASE_URL}top-headlines",
                            params={"apiKey": key, "country": country, "pageSize": 100})
    data = response.json()

    return data


# FUNCTION TO SEARCH FOR ARTICLES
def search_news(query):
    search_query_response = requests.get(
        f"{BASE_URL}everything", params={"apiKey": key, "q": query, "pageSize": 100})
    SEARCH_QUERY_DATA = search_query_response.json()

    return SEARCH_QUERY_DATA


# FUNCTION TO GET NEWS BY CATEGORY

def get_news_by_category(country, cat):
    response = requests.get(f"{BASE_URL}top-headlines", params={"apiKey": key,
                                                                "country": country, "category": cat})
    data = response.json()

    return data
