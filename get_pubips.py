#this program focuses on introducing JSON and getting familiar with 
#exception handling and the service used in this code is used to get
#IPv4 IP address which can be achieved by a single line terminal 
#command which is: curl https://ipinfo.io/ip

import requests

def get_public_ip():
    try:
        # ipify is a free reliable service, is used to get IP addresses in JSON format
        #JSON(JavaScript Object Notation) is used to transmit data between a server and a web app or between different part of the program.
        #It consists of key-value pairs and supports structured data
        #A lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
        response = requests.get("https://api64.ipify.org?format=json")

        #check if the request was successful(status code 200)
        if response.status_code == 200:
            #exracting and returning IP address
            data = response.json()
            public_ip = data["ip"]
            return public_ip
        #handling error if the HTTP req does not return the 200 status code
        else:
            print("Error: Unable to retrieve public IP address.")
            return None
    #a catch-all exception block to catch any exceptions such as network error, DNS resolution problems or if the URL is unreachable or invalid URLs or the content is not in valid json
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
#Main block ensures that the following code is executed only when the script is run as the main program and not when imported as a module   
if __name__ == "__main__":
    #function 'get_public_ip' is called and stored in the 'public_ip' variable
    public_ip = get_public_ip()
    if public_ip:
        print(f"Your public IP address is: {public_ip}")