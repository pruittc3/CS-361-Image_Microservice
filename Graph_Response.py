import time

# Wait for the microservice to finish generating the graph

time.sleep(3)

with open("graph_response.txt", "r") as file:
    response_data = file.readlines()


for line in response_data:
    print(line.strip())