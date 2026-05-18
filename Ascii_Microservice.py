import time
import pyfiglet

while True:

    try:
        # Read request file
        with open("ascii_request.txt", "r") as file:
            lines = file.readlines()

        # Store request parameters
        request_data = {}

        for line in lines:
            key, value = line.strip().split("=")
            request_data[key] = value

        # Extract request data
        header_text = request_data["header_text"]
        style = request_data.get("style", "standard")

        # Generate ASCII banner
        ascii_banner = pyfiglet.figlet_format(header_text, font=style)

        # Write banner to response file
        with open("ascii_response.txt", "w") as response:
            response.write("status=success\n")
            response.write("message=ASCII banner generated successfully\n\n")
            response.write(ascii_banner)

        print("ASCII banner generated successfully.")

        # Pause before checking again
        time.sleep(3)

    except Exception as error:

        with open("ascii_response.txt", "w") as response:
            response.write("status=error\n")
            response.write(f"message={str(error)}\n")

        time.sleep(3)
