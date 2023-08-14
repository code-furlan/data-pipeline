import tweepy

# API keyws that yous saved earlier
api_key = "6iUuJwWiXCWDkJHwmuLN8XND7"
api_secrets = "cBYPjOKxnlKJSr89OZnzEhtfQrtmxK6mqCFIryNgTZc8bqlRgP"
access_token = "1682922403968565248-60ZlvwVoramMKXMnOOqrWEf0h7J1iV"
access_secret = "p634HMvbp0d9njt0AmIEj3QDd3wMl0qU9Nd7sv0wtSNzM"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

user = api.get_user() # Store user as a variable
 
# Get user Twitter statistics
print(f"user.followers_count: {user.followers_count}")
print(f"user.listed_count: {user.listed_count}")
print(f"user.statuses_count: {user.statuses_count}")