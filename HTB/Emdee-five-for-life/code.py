import requests
import hashlib
import re

def find_string(text):
    begin = text.find("<h3 align='center'>")+19
    end = text.find("</h3>")
    md5_string = text[begin:end].encode('utf-8')
    return md5_string

def md5_hash(text):
    hash_string = hashlib.md5(text).hexdigest()
    return hash_string

def post_request(url, session, hash_string):
    new_req = session.post(url, data={"hash":hash_string})
    print(new_req.text)

url = input("URL: ")
print("Connect to " + url)

session = requests.session()
respond = session.get(url)

if (respond.status_code == 200):
    md5_string = find_string(respond.text)
    hash_string = md5_hash(md5_string)
    print("MD5 hash: " + hash_string)
    post_request(url, session, hash_string) 

else :
    print("Error!")
