import time
import matplotlib.pyplot as plt

while True:

    try:
        # Read request file
        with open("graph_request.txt", "r") as file:
            lines = file.readlines()

        # Store request parameters
        request_data = {}

        for line in lines:
            key, value = line.strip().split("=")
            request_data[key] = value

        # Extract graph data
        graph_type = request_data["graph_type"]
        title = request_data["title"]
        labels = request_data["labels"].split(",")
        values = list(map(int, request_data["values"].split(",")))
        x_label = request_data["x_label"]
        y_label = request_data["y_label"]
        output_filename = request_data["output_filename"]

        # Generate graph
        plt.figure()

        if graph_type == "bar":
            plt.bar(labels, values)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # Save graph image
        plt.savefig(output_filename)

        plt.close()

        # Write response file
        with open("graph_response.txt", "w") as response:
            response.write("status=success\n")
            response.write("message=Graph generated successfully\n")
            response.write(f"image_path={output_filename}\n")

        print("Graph generated successfully.")

        # Pause before checking again
        time.sleep(3)

    except Exception as error:

        with open("graph_response.txt", "w") as response:
            response.write("status=error\n")
            response.write(f"message={str(error)}\n")

        time.sleep(3)