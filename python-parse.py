import requests
import json

def parse_markdown_table(markdown):
    # Split the markdown content into lines
    lines = markdown.split("\n")

    # Extract the header columns
    headers = [h.strip() for h in lines[1].split("|") if h.strip()]
    
    # Process the table rows
    data = []
    for line in lines[3:]:
        if line.strip() == "" or line.strip().startswith("|---"):
            continue
        row = [r.strip() for r in line.split("|") if r.strip()]
        if len(row) == len(headers):
            row_dict = {headers[i]: row[i] for i in range(len(headers))}
            data.append(row_dict)

    return data

# URL of the raw markdown file in the GitHub repository
url = "https://raw.githubusercontent.com/GSSoC24/Postman-Challenge/main/add-your-certificate.md"

# Fetch the content from the URL
response = requests.get(url)
markdown_content = response.text

# Parse the markdown table and convert to JSON
parsed_data = parse_markdown_table(markdown_content)
json_data = json.dumps(parsed_data, indent=4)

# Print the JSON data
print(json_data)

# Optionally, write the JSON data to a file
with open("data.json", "w") as json_file:
    json_file.write(json_data)

