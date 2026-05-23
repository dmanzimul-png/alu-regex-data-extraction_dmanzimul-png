# Regex Data Extraction & Secure Validation

## Project Description

This project is a Python program that uses Regular Expressions (Regex) to extract useful information from messy text data.

The program reads raw text from a file and finds:

- Email addresses
- Phone numbers
- URLs
- Credit card numbers

It also checks for invalid input and hides sensitive credit card information for security purposes.

This project helped me understand how regex can be used in real-world situations such as validating data, cleaning text, and handling unsafe input.

---

## Features

- Extracts valid email addresses
- Validates ALU email domains
- Extracts phone numbers
- Extracts URLs
- Extracts credit card numbers
- Masks sensitive card information
- Saves results into a JSON file
- Handles realistic messy text input

---

## Technologies Used

- Python 3
- Regex (`re` module)
- JSON

---

## Project Structure

```text
alu-regex-data-extraction_dmanzimul-png/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-link>
```

### 2. Move into the project folder

```bash
cd alu-regex-data-extraction_dmanzimul-png
```

### 3. Run the program

```bash
python3 src/main.py
```

---

## Regex Patterns Used

### Email Extraction

```python
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

### Phone Numbers

```python
\+?\d{10,15}
```

### URLs

```python
https?://[^\s]+
```

### Credit Card Numbers

```python
\d{4}-\d{4}-\d{4}-\d{4}
```

---

## ALU Email Validation

The project validates these ALU email domains:

- @alueducation.com
- @alumni.alueducation.com
- @si.alueducation.com

---

## Security Considerations

This project demonstrates simple security practices by:

- ignoring malformed email addresses
- validating extracted data
- hiding most digits of credit card numbers
- avoiding unnecessary exposure of sensitive information

Only the last 4 digits of a credit card are displayed in the output.

---

## Example Output

```json
{
    "emails": [
        "d.manzimul@alueducation.com"
    ],
    "phone_numbers": [
        "+250798686752"
    ],
    "urls": [
        "https://www.google.com"
    ],
    "credit_cards": [
        "****-****-****-9999"
    ]
}
```

---

## Author

Developed by Manzi Mulinda Divin Elvis
