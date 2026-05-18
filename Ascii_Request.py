import time

# Send request to microservice
with open("ascii_request.txt", "w") as file:
    file.write("header_text=Lab Ordering System\n")
    file.write("style=standard\n")

print("Request sent to ASCII banner microservice.")

# Wait for the microservice to process the request
time.sleep(3)

# Read the response
with open("ascii_response.txt", "r") as file:
    response = file.read()

print("Response from microservice:")
print(response)