import requests
import os
import json

os.environ["CONSUMER_KEY"] = "6iUuJwWiXCWDkJHwmuLN8XND7"
os.environ["CONSUMER_SECRET"] = "cBYPjOKxnlKJSr89OZnzEhtfQrtmxK6mqCFIryNgTZc8bqlRgP"

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
os.environ["BEARER_TOKEN"] = "AAAAAAAAAAAAAAAAAAAAAGLZowEAAAAA4U9OG6LtdP5XBafq7LYrjX5bzuY%3DuycH2q6cN1i7qMbTWbdlrDrPutI2eZ8W0AaHYkFVQyu9cEaGjH%3DiKuyvSsg4FPQr6RsmbfCVF4jBMYmtQe0jSIXlZn0Cxl2n1aNXf"
bearer_token = os.environ.get("BEARER_TOKEN")

ciandt_user_id = 59202292

def create_url():
    # Replace with user ID below
    user_id = 2244994945
    return "https://api.twitter.com/1.1/statuses/show.json?id={}".format(ciandt_user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}, "
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()