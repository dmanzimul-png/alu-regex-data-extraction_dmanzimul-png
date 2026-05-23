import re
import json

with open("input/raw-text.txt", "r") as file:
    text = file.read()

# Extracting emails
emails_found = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    text
)

# Extracting phone numbers
phone_numbers_found = re.findall(
    r'\+?\d{10,15}',
    text
)

# Extracting URLs
urls_found = re.findall(
    r'https?://[^\s]+',
    text
)

# Extracting credit cards
credit_cards_found = re.findall(
    r'\d{4}-\d{4}-\d{4}-\d{4}',
    text
)

# Masking credit cards
masked_credit_cards = []

for card in credit_cards_found:
    masked = "****-****-****-" + card[-4:]
    masked_credit_cards.append(masked)

print("Emails:")
print(emails_found)

print("\nPhone Numbers:")
print(phone_numbers_found)

print("\nURLs:")
print(urls_found)

print("\nMasked Credit Cards:")
print(masked_credit_cards) 

extracted_data = {
    "emails": emails_found,
    "phone_numbers": phone_numbers_found,
    "urls": urls_found,
    "credit_cards": masked_credit_cards
}
# Saving the results to json file 
with open("output/sample-output.json", "w") as output_file:
    json.dump(extracted_data, output_file, indent=4)

print("\nResults successfully saved to output/sample-output.json")
