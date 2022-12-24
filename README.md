# Reverse Shell Socket Backdoor

This program is a simple backdoor that allows you to run commands on the victim's side. It is completely encrypted using AES 128-bit encryption for the communication between the client and server.

### How it works
- The client generates a random symmetric key, which is used to communicate with the server. The key is encrypted using RSA encryption and sent to the server.
- The server receives the encrypted key and decrypts it using its private RSA key. A session is then established between the client and server, using AES encryption for complete end-to-end encryption.
- The server can send commands to the client, which will execute them and send the output back to the server.

### Running the program
To successfully run the program, you need to install the required dependencies by running the following command:

##### pip install -r requirements.txt
You can use a tool like WireShark to verify that the session is completely encrypted.

### Detection and evasion
This program is designed to not be detected or blocked by any antivirus or endpoint detection and response (EDR) software. However, it is always a good idea to use caution when deploying and using such tools.
