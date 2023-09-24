import sys, requests

if len(sys.argv) > 2:
    ty = sys.argv[1]
    category = sys.argv[2]
elif len(sys.argv) > 1:
    ty = "sfw"
    category = sys.argv[1]
else:
    ty = "sfw"
    category = "neko"

response = requests.get(f"https://api.waifu.pics/{ty}/{category}")
body = response.json()

print(body['url'])