import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
          yn=input("Did you mean %s instead? Enter Y for YES and N for NO:"%get_close_matches(w, data.keys())[0])
          if yn== "Y":
              return data[get_close_matches(w,data.keys())[0]]
          elif yn== "N":
              return "The world does not exist.Please check it."
          else:
              return "We did not understand your entry"

    else:
        return "The world does not exist"


word= input("Enter words:")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
