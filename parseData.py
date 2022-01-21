import re
import requests
from flask import Flask, json
api = Flask(__name__)

@api.route('/getTimeStories', methods=['GET'])

def getTimeStories():
      # Making a GET request
  r = requests.get('https://time.com')
  document = r.content.decode().replace("\n", "")

  section = re.search('<section class="homepage-module latest".+?(?:(</section>))', document).group()
  articles = re.findall('<a href=.+?(?:<\/a>)', section)

  data = []
  for article in articles:
      r = re.search("href=(.+?(?=>))>(.+(?=<))", article)
      data.append({"title": r.group(2), "link": f'https://time.com/{r.group(1)}'})

  print(data)
  return json.dumps(data)

if __name__ == '__main__':
  api.run()