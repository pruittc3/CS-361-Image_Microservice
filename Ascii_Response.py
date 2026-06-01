import time

# Wait for the microservice to finish
# generating the ASCII banner

time.sleep(3)

# Read response file
with open("ascii_response.txt", "r") as file:
    response_data = file.readlines()

# Display response
for line in response_data:
    print(line.strip())