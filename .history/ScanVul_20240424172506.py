from vulners import Vulners
import subprocess

api_key_Mysql_apache = "BVM7XHOM569FOS926JD3G78BHVTSJTSM6N6EZM3AWLYW3NVH5ZIM6SYO0DX67RIL"
api_token_wpscan = 'bzGYb0wY5MIwW05sbtXbZDWqVxUtn4xV12gGgQmMUGg'

def search_vulnerabilities(service_name, service_version,api_key):
    vulners_api = Vulners(api_key)
    # Search for vulnerabilities related to the service name and version
    vulnerabilities = vulners_api.softwareVulnerabilities(service_name, service_version)
    return vulnerabilities

def display_vulnerabilities_MySQL_Apache(vulnerabilities):
    if vulnerabilities:
        print("Vulnerabilities found:")
        for cve_id, vulnerability_list in vulnerabilities.items():
            for vulnerability in vulnerability_list:
                print("- CVE ID:", cve_id)
                print("  Description:", vulnerability.get('description'))
                print("  CVSS Score:", vulnerability.get('cvss', {}).get('score'))
                print()  # Add a blank line for readability
    else:
        print("No vulnerabilities found.")



def run_wpscan_plugins(site_url, api_token):
    try:
        command = ["wpscan", "--url", site_url, "-e", "vp", "--plugins-detection", "mixed"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        stdout, _ = process.communicate()

        if process.returncode != 0:
            print(f"WPScan failed with error code {process.returncode}")
        else:
            output_file = "/Users/mohammadhosein/Documents/FSTT/outputs/output.txt"
            with open(output_file, "w") as file:
                file.write(stdout.decode())
            print("Output saved to:", output_file)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the execution of the command
        print("Error:", e)
    
def wpscan_version(site_url, api_token):
    try:
        # Construct the WPScan command without specifying the WordPress version
        command = ['wpscan', '--url', site_url, '--enumerate', 'vp', '--no-update', '--api-token', api_token]

        # Execute the WPScan command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Print the WPScan output
        output_file = "/Users/mohammadhosein/Documents/FSTT/outputs/output.txt"
        with open(output_file, "w") as file:
            file.write(stdout.decode())
            print("Output saved to:", output_file)
        

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during WPScan execution
        print(f"An error occurred: {e}")

def identify_vulnerabilities(services, site_url):
    # Identify vulnerabilities in the specified environment
    print("Identifying vulnerabilities...")
    # Check for vulnerabilities in the services
    for service in services:
        service_name = service.get('name')
        service_version = service.get('version')
        if(service_name == "MySQL" or service_name == "Apache"):
            vulnerabilities = search_vulnerabilities(service_name, service_version,api_key_Mysql_apache)
            display_vulnerabilities_MySQL_Apache(vulnerabilities)
        elif(service_name == "WordPress"):
            run_wpscan_plugins(site_url,api_token_wpscan)
            wpscan_version(site_url,api_token_wpscan)
        

