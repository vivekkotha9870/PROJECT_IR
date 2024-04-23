import scrapy
import os

class ExtendedTestSpider(scrapy.Spider):
    name = "extended_test"
    allowed_domains = ['stackoverflow.com']  # Restrict the crawl to Stack Overflow
    save_folder = 'saved_pages'  # Folder to save the HTML files

    def __init__(self, start_url='https://stackoverflow.com', max_pages=6, max_depth=1, *args, **kwargs):
        super(ExtendedTestSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.max_pages = int(max_pages)
        self.crawled_count = 0
        self.max_depth = int(max_depth)

        # Ensure the folder for saving HTML files exists
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    custom_settings = {
        'DEPTH_LIMIT': 1  # Adjust depth as needed
    }

    def parse(self, response):
        # Check if the maximum number of pages has been reached
        if self.crawled_count >= self.max_pages:
            return

        # Increment the count of crawled pages
        self.crawled_count += 1

        # Save the current page
        filename = response.url.split("/")[-1]
        filename = filename + '.html' if filename else "index.html"
        file_path = os.path.join(self.save_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {file_path}')

        # Extract and follow links only if the count is less than max pages
        if self.crawled_count < self.max_pages:
            links = response.css('a::attr(href)').getall()
            for link in links:
                link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse)
