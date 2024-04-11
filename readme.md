# 📋 Email Scraper

## 📝 Description

This Python script crawls websites to extract email addresses. It provides functionalities for processing URLs from text files, crawling emails with depth control, and saving extracted emails to separate files. 

## 🌟 Features

* Extracts emails from websites using Beautiful Soup and regular expressions.
* Handles pagination by following next-page links.
* Writes extracted emails to text files.
* Supports processing URLs from text files.
* Offers depth control for limited crawling.

## 💻 Technologies Used

* Python 3
* Requests library for making HTTP requests
* BeautifulSoup for HTML parsing
* Regular expressions for email extraction
* Scrapy framework for efficient web scraping (wrapper.py)
* openpyxl library for reading and manipulating Excel files (wrapper.py)

## 🛠️ Setup Instructions

1. Install required libraries using `pip install -r requirements.txt`.
2. Ensure you have Python 3 and `pip` installed on your system.

## 🚀 Usage

**Running from Script (Simple Example):**

```bash
python scraper.py https://www.example.com/ 2 feed/1.json emails/1.txt
```

This command crawls the provided URL (`https://www.example.com/`) with a depth of 2, saves extracted emails to `emails/1.txt`, and generates a temporary JSON feed file (`feed/1.json`).

**Running from Terminal (Advanced):**

Use `python scraper.py -h` to view available command-line arguments for more granular control over scraping.

* `url`: The URL to crawl.
* `depth`: Crawling depth (number of pages to follow).
* `uri`: URI for the Scrapy feed output (JSON format).
* `emails_file`: Output file path for storing extracted emails.

## Processing URLs from Text Files:

1. Place URLs, one per line, in a text file (e.g., `urls.txt`).
2. Run the script with `python wrapper.py run_multiple_crawlers_from_txt urls.txt`. This crawls URLs from `urls.txt` and saves emails to separate files based on their corresponding line numbers in the text file.

## Processing URLs from Excel Files (wrapper.py):

1. Create an Excel file (`emails.xlsx`) with one column containing department URLs.
2. Run the script with `python wrapper.py run_multiple_crawlers_from_excel emails.xlsx`. This reads URLs and their corresponding cell locations from the Excel file, crawls emails, and saves them to designated files based on cell locations.

## Combined Takeaways and Challenges

* **Learning Scrapy framework:** This project provided an opportunity to learn and use Scrapy for efficient web scraping, improving scalability and handling complex websites.
* **Balancing Efficiency and Accuracy:** While depth control limits unnecessary crawling, it might miss emails on deeper pages. Finding the optimal depth balance remains a challenge for comprehensive extraction.
* **Handling Dynamic Content:** Websites with dynamically loaded content using JavaScript might require additional libraries or techniques to scrape emails effectively.

## License

This project is distributed under the MIT License. See the LICENSE file for details.
