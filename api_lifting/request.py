import requests

url = "https://app.goflightlabs.com/advanced-real-time-flights"

# Example Casablanca Airport
params = {
  'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiYzA1YWI5ODRiM2ZjMzg1NTVjNjgzZjEzMzRhYjA2NzU4OTk4ZGE2MGQ0OGM0OTIzNzIxMmVjNzAxOTM5ZGQ5OGQ0OGJhZjA0ZjQ2YTRhOWIiLCJpYXQiOjE2NzAyMjg3ODQsIm5iZiI6MTY3MDIyODc4NCwiZXhwIjoxNzAxNzY0Nzg0LCJzdWIiOiIxOTEwOCIsInNjb3BlcyI6W119.XYSGIskzdtgoVnX7rIEaquOrrvzrECJMu42_R4LkKVUXEqXmlQy2RqSvXpcsGz1OkUkR8hWZYfklwlZ4mg_Fxg',
  'arrIata': 'CMN'
}

api_result = requests.get(url, params)

api_response = api_result.json()

print(api_response)



