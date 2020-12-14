from flask import Flask, jsonify, request  
from simplecrypt import encrypt, decrypt
import hashlib  
import binascii

app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello"

if __name__ =='__main__':  
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port, debug = True)  
