import requests
import socket
import re
def detect_mysql(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Look for common MySQL error messages in the response content
            if 'SQL syntax' in response.text or 'MySQL' in response.text:
                print("MySQL may be in use (SQL syntax error detected)")
            # Check if the website uses PHP which often integrates with MySQL
            elif '.php' in response.text:
                print("PHP found, MySQL may be in use")
            # You can add more specific checks if necessary
            else:
                print("No clear indication of MySQL usage")
        else:
            print("Failed to access website. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error accessing website:", e)
        
def extract_mysql_version(response_text):
    # Regular expression pattern to match MySQL version numbers
    pattern = r'\b\d+\.\d+\.\d+\b'  # Matches version numbers like 5.7.33
    matches = re.findall(pattern, response_text)
    if matches:
        return matches[0]  # Return the first match
    return None
# Function to perform web scraping
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is accessible.")
            # Add your scraping logic here
        else:
            print("Failed to access website. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error accessing website:", e)

def identify_services(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            headers = response.headers
            server_header = headers.get('Server', '')
            print("Server header:", server_header)
            if 'SQL syntax' in response.text:
                print("MySQL may be in use (SQL syntax error detected)")
            # Check if the website uses PHP which often integrates with MySQL
            elif '.php' in response.text:
                print("PHP found, MySQL may be in use")
            # You can add more specific checks if necessary
            else:
                print("No clear indication of MySQL usage")
            # Check for MySQL version
            version = extract_mysql_version(response.text)
            if version:
                print("MySQL version:", version)
            else:
                print("MySQL version not found")
            
            if 'Apache' in server_header or 'apache' in server_header or 'httpd' in server_header:
                print("Apache server detected")
                version = re.search(r'Apache/(\d+\.\d+\.\d+)', server_header)
                if version:
                    print("Apache version:", version.group(1))
                else:
                    print("Unable to determine Apache version")
            if 'WordPress' in response.text:
                print("WordPress detected")
                version = re.search(r'WordPress (\d+\.\d+\.\d+)', response.text)
                if version:
                    print("WordPress version:", version.group(1))
                else:
                    print("Unable to determine WordPress version")
            # You can add additional checks for other services
        else:
            print("Failed to access website. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error accessing website:", e)

def D
website_url = "http://localhost/sitevul/"


# Scrape website
scrape_website(website_url)



# Identify services
identify_services(website_url)



        
        

