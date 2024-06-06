# Caesar Cipher Client and Server

## Overview
The **Caesar Cipher Client and Server** project demonstrates basic networking concepts, including sockets, IP, localhost, and multithreading. This project features a server that can handle multiple clients simultaneously using multithreading. Each client can input a rotation number for the Caesar cipher, send a sentence to the server, and receive the ciphered text. Additionally, the project demonstrates decryption by connecting two clients where one encrypts a message and the other decrypts it using the inverse rotation.

## Features
- **Multithreaded Server**: Handles multiple clients at the same time.
- **Client-Server Communication**: Clients can send messages to the server and receive responses.
- **Caesar Cipher**: Simple encryption and decryption using rotation.
- **Networking Basics**: Demonstrates usage of sockets, IP addresses, and localhost.

## Demonstration Video
In the demonstration video, two clients connect to the server. One client uses a rotation number to encrypt a message, and the second client decrypts the message using the inverse rotation (26 - n).



### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Caeer-Cipher-Client-and-Server.git
    cd caesar-cipher-client-server
    ```

2. Install any necessary dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

### Running the Server
1. Navigate to the server directory:
    ```sh
    cd server
    ```

2. Run the server script:
    ```sh
    python3 <CaesarServer.py> <port>
    ```

### Running the Client
1. Open a new terminal and navigate to the client directory:
    ```sh
    cd client
    ```

2. Run the client script:
    ```sh
    python3 <CaesarClient.py> <hostname> <port>
    ```

3. Input the rotation number and the sentence to be encrypted when prompted.

### Example Usage
1. Start the server:
    ```sh
    python3 CaesarServer.py 2222
    ```

2. Start the first client and input the rotation number and sentence:
    ```sh
    python3 CaesarClient.py 127.0.0.5 2222
    ```

    ```
    Enter rotation number: 5
    Enter a sentence: Hello World
    ```

3. The server responds with the ciphered text:
    ```
    Server Response: Mjqqt Btwqi
    ```

4. Start the second client and use the inverse rotation to decrypt:
    ```sh
    python3 CaesarClient.py 127.0.0.5 2222
    ```

    ```
    Enter rotation number: 21
    Enter a sentence: Mjqqt Btwqi
    ```

5. The server responds with the decrypted text:
    ```
    Server Response: Hello World
    ```




## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or feedback, please contact [davidkim184@gmail.com](mailto:davidkim184@gmail.com).
