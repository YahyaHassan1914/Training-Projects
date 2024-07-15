import requests
import time
from concurrent.futures import ThreadPoolExecutor

class SiteConnectivityChecker:
    def __init__(self, sites, timeout=5):
        """
        Initialize the SiteConnectivityChecker with a list of sites and a timeout value.
        Ensures all URLs have a valid scheme (http or https).
        """
        self.sites = [self.ensure_scheme(site) for site in sites]
        self.timeout = timeout
        self.results = {}

    def ensure_scheme(self, url):
        """
        Ensure the URL starts with 'http://' or 'https://'. If not, prepend 'http://'.
        """
        if not url.startswith(('http://', 'https://')):
            return 'http://' + url
        return url

    def check_site(self, site):
        """
        Check the connectivity status of a single site.
        Records the response time and status code.
        """
        try:
            start_time = time.time()
            response = requests.get(site, timeout=self.timeout)
            response_time = time.time() - start_time
            status_code = response.status_code
            if 200 <= status_code < 400:
                status = "Online"
            else:
                status = "Error"
            self.results[site] = {
                "status": status,
                "status_code": status_code,
                "response_time": response_time
            }
        except requests.exceptions.RequestException as e:
            self.results[site] = {
                "status": "Offline",
                "error": str(e),
                "response_time": None
            }

    def run_checks(self):
        """
        Run connectivity checks for all sites concurrently.
        """
        with ThreadPoolExecutor() as executor:
            executor.map(self.check_site, self.sites)

    def display_results(self):
        """
        Display the results of the connectivity checks.
        """
        for site, result in self.results.items():
            print(f"Site: {site}")
            print(f"  Status: {result['status']}")
            if 'status_code' in result:
                print(f"  Status Code: {result['status_code']}")
            if 'response_time' in result and result['response_time'] is not None:
                print(f"  Response Time: {result['response_time']:.2f} seconds")
            if 'error' in result:
                print(f"  Error: {result['error']}")
            print("-" * 40)

def main():
    """
    Main function to execute the Site Connectivity Checker.
    Prompts the user to enter websites, runs the checks, and displays the results.
    """
    print("Welcome to the Advanced Site Connectivity Checker!")
    print("This tool allows you to check the connectivity status of multiple websites.")
    print("Please enter the websites you want to check, separated by commas.")
    print("Enter 'q' to quit the program.")
    
    while True:
        # Get user input for websites
        sites_input = input("\nWebsites: ").strip()
        if sites_input.lower() == 'q':
            break

        sites = [site.strip() for site in sites_input.split(",")]
        
        # Create a SiteConnectivityChecker instance
        checker = SiteConnectivityChecker(sites)
        
        # Run connectivity checks and display results
        print("\nChecking site connectivity...\n")
        checker.run_checks()
        checker.display_results()

if __name__ == "__main__":
    main()