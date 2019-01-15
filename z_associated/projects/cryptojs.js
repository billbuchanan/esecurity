// Node.js example Run with:
// node crypto.js

message ="Hello"
password="qwerty"

var SHA256 = require("crypto-js/sha256");
var MD5 = require("crypto-js/md5");
var SHA3 = require("crypto-js/sha3");

var AES = require("crypto-js/aes");

var CryptoJS = require("crypto-js");

console.log("\n--- Hashes");
console.log("MD5: ",MD5(message).toString());
console.log("SHA-256: ",SHA256(message).toString());
console.log("SHA-3: ",SHA3(message).toString());

console.log("\n--- AES");
var ciphertext = AES.encrypt(message, password);
 
var bytes  = AES.decrypt(ciphertext.toString(), password);
var plaintext = bytes.toString(CryptoJS.enc.Utf8);
 
console.log("Cipher: ",ciphertext.toString());
console.log("Plaintext: ",plaintext);

console.log("\n--- HMAC-SHA1");
console.log("HMAC: ",CryptoJS.HmacSHA1(message, password).toString());