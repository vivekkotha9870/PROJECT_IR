# ExtendedTestSpider

## Overview
The `ExtendedTestSpider` is a Scrapy spider designed to crawl Stack Overflow and save HTML pages. It allows users to specify the start URL, maximum number of pages to crawl, and maximum depth of links to follow.

## Setup

1. Navigate to the project directory:
   ```bash
   cd stockoverflow
   ```
2. Install dependencies using pip:
   ```bash
   pip install scrapy
   ```

## Usage
1. Run the spider with default settings:
   ```bash
   scrapy crawl extended_test
   ```
   This will start crawling Stack Overflow and save HTML pages to the `saved_pages` folder.

2. Customize the spider settings (optional):
   - To specify a different start URL:
     ```bash
     scrapy crawl extended_test -a start_url='your-start-url'
     ```
   - To change the maximum number of pages to crawl:
     ```bash
     scrapy crawl extended_test -a max_pages=10
     ```
   - To adjust the maximum depth of links to follow:
     ```bash
     scrapy crawl extended_test -a max_depth=2
     ```

## Folder Structure
- `saved_pages/`: Folder to save the HTML files crawled by the spider.

## Notes
- The spider is configured to restrict the crawl to the Stack Overflow domain (`stackoverflow.com`).
- Adjust the `DEPTH_LIMIT` setting in the spider's `custom_settings` dictionary to change the depth limit for link following.

