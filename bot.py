#importing files/libraries
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Define the URL of the website you want to scrape
url_to_scrape = "https://brainlox.com/courses/category/technical"

@app.route('/')
def scrape_data():
    # Send an HTTP GET request to the URL
    response = requests.get(url_to_scrape)

    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Create empty lists to store the scraped data
        titles = []
        descriptions = []
        urls = []

        # Find and extract data from the HTML
        for link in soup.find_all('a'):
            title = link.text
            url = link.get('href')
            description = link.get('title')

            # Add data to the respective lists
            titles.append(title)
            urls.append(url)
            descriptions.append(description)

        # Render the data in an HTML template
        return render_template('results.html', titles=titles, descriptions=descriptions, urls=urls)
    else:
        return "Failed to retrieve the website content."

if __name__ == '__main__':
    app.run(debug=True)
