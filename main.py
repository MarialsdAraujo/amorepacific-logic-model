# https://c654c09e-98a7-4ab7-9c26-3cfdecb88dd0-00-136diagctce1k.picard.replit.dev/

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import json  # For saving JSON

# Get website content
res = requests.get('https://c654c09e-98a7-4ab7-9c26-3cfdecb88dd0-00-136diagctce1k.picard.replit.dev/')
res.raise_for_status()  # Check for request errors

# Parse HTML
parseSoup = BeautifulSoup(res.text, 'html.parser')
elements = parseSoup.select('p')  # Select all <p> elements

# Save scraped text to a TXT file
with open('scraped_elements.txt', 'w', encoding='utf-8') as file:  # Open a file in write mode
    for el in elements:  # Iterate over each paragraph element
        file.write(el.get_text().strip() + '\n')  # Write each paragraph text to the file

# Save full HTML to a local file
with open('website.html', 'w', encoding='utf-8') as website:  # Open a file in write mode
    website.write(res.text)  # Write the HTML content to the file

# Extract text from paragraphs into a list
data = [p.get_text().strip() for p in elements]

# Save to a JSON file
with open("scraped_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)  
# .dump() method to write the data to the file  
# Use ensure_ascii=False to handle special characters

print("Scraped data saved to scraped_data.json")