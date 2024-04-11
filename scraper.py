import argparse
import requests
from bs4 import BeautifulSoup
import re
import scrapy
from scrapy.crawler import CrawlerProcess
import json

EMAIL_REGEX = r'[^.]([a-zA-Z0-9._%+-]+[^.])@([a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*\.[a-zA-Z]{2,})'

class Utils:
    
    @staticmethod
    def read_urls_from_txt(file_path):
        """Reads URLs from a text file, removes newline characters, and returns them as a list."""
        try:
            with open(file_path, "r") as file:
                urls = [line.strip("\n") for line in file.readlines()]  # Remove "\n" from each line
            return urls
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    @staticmethod
    def filter_emails_from_json(file_path):
        """
        Reads all the emails from the json file and deletes mutltiple
        and empty arrays making a text file for the emails of the json file
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                emails = []
                for emails_dict in data:
                    emails.extend(emails_dict["emails"])
                    
                emails = list(set(emails))  # Remove duplicates
                
                return emails
            
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []
                    
    @staticmethod
    def write_emails_to_txt(file_path, emails):
        """Writes the emails to a text file, separated by newlines."""
        try:
            with open(file_path, "w") as file:
                file.writelines(email + "\n" for email in emails)
        except Exception as e:
            print(f"An error occurred while writing the file: {e}")
            return False
        return True
    
    def urls_from_excel():
        pass     


class EmailSpider(scrapy.Spider):
    name = "email_scraper"
    start_urls = []

    def parse(self, response):
        emails = self.extract_emails(response.text)
        yield {"emails": emails}

        next_page_links = response.css("a::attr(href)").getall()
        for link in next_page_links:
            if link.startswith("/"):
                link = response.urljoin(link)
            yield response.follow(link, callback=self.parse)

    def extract_emails(self, text):
        email_regex = EMAIL_REGEX
        emails = re.findall(email_regex, text)
        for idx, email in enumerate(emails):
            emails[idx] = email[0] + '@' + email[1]
        return emails


def crawl_emails_from_url(url, depth, uri, emails_file):
    custom_settings = {
        "DEPTH_LIMIT": depth,
        "FEEDS": {
            f"{uri}": {
                "format": "json",
            },
        },
        "LOG_FILE": f"{uri.split('.')[0]}.log",  # Configure log file path
    }

    process = CrawlerProcess(settings=custom_settings)
    process.crawl(EmailSpider, start_urls=[url])
    process.start()
    
    process.join()

    crawled_emails = Utils.filter_emails_from_json(uri)
    Utils.write_emails_to_txt(emails_file, crawled_emails)


def run_from_terminal():
    parser = argparse.ArgumentParser(description="Email Crawler")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("depth", type=int, help="Crawling depth")
    parser.add_argument("uri", help="URI for feed output")
    parser.add_argument("emails_file", help="Output file for emails")

    args = parser.parse_args()
    print(f"args url : {args.url}")
    print(f"args depth : {args.depth}")
    print(f"args uri : {args.uri}")
    print(f"args emails_file : {args.emails_file}")
    
    crawl_emails_from_url(args.url, args.depth, args.uri, args.emails_file)


def run_from_script():
    crawl_emails_from_url("https://www.cmu.edu/tepper/faculty-and-research/faculty-by-area/economics.html", 2, "feed/245.json", "emails/245.txt")


if __name__ == "__main__":
    run_from_script()
    # run_from_terminal()