import json

def extract(number):
  img_url = "https://themetakongz.com/kongz/images/" + number + ".png"
  
  with open('ranking.json', 'r') as f:
    data = json.load(f)
  
  return data[int(number)][0], data[int(number)][1], img_url