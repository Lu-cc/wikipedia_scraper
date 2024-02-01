# Wikipedia Scraper

The Wikipedia Scraper is a Python script designed to retrieve information about world leaders from Wikipedia pages using web scraping techniques. It utilizes the BeautifulSoup library to parse HTML content and extract relevant data from Wikipedia articles.

## Features

- **Country Leaders Retrieval**: The script allows users to retrieve information about world leaders from various countries.
- **Leader Information Extraction**: It extracts information such as the leader's name, birth date, death date, and the first paragraph from their Wikipedia page.
- **JSON Output**: The extracted leader information, along with the first paragraph, is stored in a JSON file for further analysis or usage.

## Installation

1. Clone the repository to your local machine:
```git clone https://github.com/Lu-cc/wikipedia_scraper.git```

2. Navigate to the project directory:
```cd your_repository```

3. Install dependencies with the help of the requirements file
```pip install -r requirements.txt```

## Usage

1. Run the program using `main.py`:
```python main.py```

2. Follow the on-screen instructions to retrieve information about country leaders and store it in a JSON file.

## Dependencies

- [Requests](https://pypi.org/project/requests/): HTTP library for making requests.
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/): Python library for pulling data out of HTML and XML files.

## Fetching First Paragraph

The first paragraph from each leader's Wikipedia page is fetched and stored during the `get_leaders` method. This paragraph is then included in the leader data as `"first_paragraph"`. By doing this, the `to_json_file` method can directly use the first paragraph without making additional requests to Wikipedia.
