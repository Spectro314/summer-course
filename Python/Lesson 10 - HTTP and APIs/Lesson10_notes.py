# import requests
# base = "http://localhost:5000"

# requests.get(base)

# requests.get(base).content

# response = requests.get(f"{base}/teapot")
# print(response.status_code)
# print(response.content)
# print(response.headers)

# response = requests.get(f"{base}/api")

# for test in response.content[:10]:
#     print(test) # these are bytes!!!

# print()
# print()

# print()
# for key, val in response.json().items(): # convert to json first (if it's valid json)
#     print(key, ' - ', val) # this is a dictionary!
    
# response = requests.post(f"{base}/requestType")
# print(response.text)

# response = requests.get(f"{base}/requestType")
# print(response.text)

# # post, put, patch, delete, options, etc

# response = requests.get(f"{base}?hello=world") # this is common with get requests
# print(response.text)

# # this is common with post requests, also works with get requests
# response = requests.post(f"{base}", params={"hello": "world"})
# print(response.text)

# # for more info, this is pretty good https://www.echoapi.com/blog/url-vs-body-parameters-in-apis-key-differences-and-how-to-avoid-common-mistakes/    


# import base64

# image_path = 'image.png'
# with open(image_path, 'rb') as file:
#     image_data = file.read()
# b64_bytes = base64.b64encode(image_data)

# headers = {
#     'Content-Type': 'image/png'
# }
# response = requests.post(f"{base}/image", data=b64_bytes, headers=headers)
# print(response.content)


import http
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")
print(response.status_code)
print(response.reason)

content_type = response.headers.get("Content-Type", "<missing>")
elapsed_ms = response.elapsed.total_seconds() * 1000
elapsed_ms = int(elapsed_ms)

print(f"Content-Type: {content_type}")
print(f"Elapsed: {elapsed_ms} ms")

try:
    data = response.json()
    print(f"userId: {data['userId']}")
    print(f"id: {data['id']}")
    print(f"title: {data['title']}")
except ValueError:
    print("Response body was not valid JSON")
    
params = {"postId": 1}
response = requests.get(f"{BASE_URL}/comments", params=params)
comments = response.json()

print(f"Comments returned: {len(comments)}")
if comments:
    print(f"First email: {comments[0]['email']}")
    
def fetch(url: str):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        print(f"Success: {url} -> {response.status_code}")
        return response
    except requests.exceptions.Timeout:
        print(f"Timeout: request to {url} took too long")
    except requests.exceptions.HTTPError as err:
        status = err.response.status_code if err.response is not None else "unknown"
        print(f"HTTP error ({status}) for {url}")
    except requests.exceptions.RequestException as err:
        print(f"Request failed for {url}: {err}")


fetch(f"{BASE_URL}/posts/1")
fetch(f"{BASE_URL}/not-a-real-route")