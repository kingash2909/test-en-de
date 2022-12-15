from flask import Flask, jsonify, request  
from simplecrypt import encrypt, decrypt
import hashlib  
import binascii
import os

app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello"

@app.route('/homed/<string:num>', methods = ['GET']) 
def de(num): 
    message = num
    byte_str = bytes.fromhex(message)
    original = decrypt('AIM', byte_str)
    final_msg = original.decode("utf-8") 
    print(final_msg)
    return jsonify({'data': final_msg}) 

@app.route('/homee/<string:num>', methods = ['GET']) 
def en(num): 
    message = num
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    print("hex -  "+hex_string)
    return jsonify({'data': hex_string}) 

if __name__ =='__main__':  
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port, debug = True)  
