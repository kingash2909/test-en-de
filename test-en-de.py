from flask import Flask, jsonify, request  
from simplecrypt import encrypt, decrypt
import hashlib  
import binascii

app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello"

if __name__ =='__main__':  
    app.run(debug = True)  