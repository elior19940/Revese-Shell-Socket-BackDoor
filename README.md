# Revese Shell, Socket BackDoor



I've developed a simple backdoor whitch have the cabability to run commands on the victim's side.
This program is complitly encrypted using:

1.The client side generate a random symmetric key which will be used to communicate with the server using AES 128 bit encryption.
To send the key to the server in cipher text, I've used RSA encryption 

2.the server side received the key from the client and decrypts the key with his private RSA key and he will create a session that complitly encrypted side to side as I've mentioned using AES encryption.
The server will send command to the client and the client'll send the output to the server.


You can use WireShark to ensure that all the session is complitly encypted.


The program doesn't get blocked or detected by any AV\EDR!
