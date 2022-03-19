docs = """
🙂 thank you
**nodejs**
```
// npm i axios
const axios = require("axios")
const url = "https://translatorapi-production.up.railway.app/"
// data must looks like
const data = {
  text: "thank you",
  lang: "es"
}
axios.post(url, data).then((data) => {
  console.log(data) 
  // or
  console.log(data.data)
})
```
**python**
```
# pip install requests
import requests
url = "https://translatorapi-production.up.railway.app/"
data = {
  "text": "thank you",
  "lang": "es"
}
response = requests.post(url, data).text
print (response)
```
⚠️ note - we are working on this api for supporting other languages
"""
deep_links = {
  "enc-own_chat": "Please Move To Another Chat",
  "enc-off_api": docs,
}
