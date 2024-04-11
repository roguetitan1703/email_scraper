import subprocess
import json
from Utils import Utils
import sys
import os


      
def run_crawler(url, depth, uri, emails_file):
    command = [
        sys.executable,  # Path to the Python interpreter
        "-m",            # Run module as a script
        "scraper",       # Module name
        url,             # URL argument
        str(depth),      # Depth argument
        uri,             # URI argument
        emails_file      # Emails file argument
    ]
    result = subprocess.run(command, check=True)

def run_multiple_crawlers_from_txt(url_file="urls.txt"):
    Utils.create_dir_if_not_exists("feed")
    Utils.create_dir_if_not_exists("emails")
    
    urls = Utils.read_urls_from_txt(url_file)
    mapping = {}
    for num,url in enumerate(urls):
        # url = urls[0]
        # num = 0
        mapping[url] = f"{num}"
        print(url, num, f"feed{num}", f"emails{num}.txt")
        run_crawler(url, 1, f"feed/{num}.json", f"emails/{num}.txt")
        
        
def run_multiple_crawlers_from_excel(excel_file="emails.xlsx"):
    Utils.create_dir_if_not_exists("feed")
    Utils.create_dir_if_not_exists("emails")
    
    urls_mapping = Utils.read_urls_from_excel(excel_file)
    for url, location in urls_mapping.items():
        location = f"{location[0]}" + f"{location[1]}"
        print(url, location, f"feed/{location}.json", f"emails/{location}.txt")
        run_crawler(url, 1, f"feed/{location}.json", f"emails/{location}.txt")
        

  
    
if __name__ == "__main__":
    # run_multiple_crawlers_from_txt('urls.txt')
    run_multiple_crawlers_from_excel('emails.xlsx')