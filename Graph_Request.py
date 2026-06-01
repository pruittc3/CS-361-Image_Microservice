import time

with open("graph_request.txt", "w") as file:

    file.write("graph_type=bar\n")
    file.write("title=Monthly Expenses\n")
    file.write("labels=Rent,Food,Gas,Utilities\n")
    file.write("values=1200,400,150,250\n")
    file.write("x_label=Expense Category\n")
    file.write("y_label=Amount in Dollars\n")
    file.write("output_filename=monthly_expenses.png\n")

print("Request sent to graph generation microservice.")

time.sleep(3)

with open("graph_response.txt", "r") as file:
    response = file.read()

print("Response from microservice:")

print(response)