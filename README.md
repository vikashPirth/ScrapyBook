# Scrapy Web Scraping with MongoDB

This project demonstrates how to use the **Scrapy** web scraping framework to extract data from websites and store it in **MongoDB**.

## Features
- Scrapes structured data from websites using **Scrapy**.
- Stores scraped data in a **MongoDB** database for further analysis.
- Demonstrates the use of custom item pipelines to process and store data efficiently.

## Requirements
To run this project, you'll need to install the following dependencies:

- Python 3.x
- Scrapy
- MongoDB
- pymongo (MongoDB client for Python)

### Install Dependencies
You can install the required Python libraries using the following command:

```bash
pip install scrapy pymongo
```


# Setting up MongoDB

Install MongoDB on your machine if you haven't already. You can download it from the [official MongoDB website](https://www.mongodb.com/try/download/community).

### Start the MongoDB server locally:
```bash
mongod
```

# Scrapy Web Scraping with MongoDB

Scrapy will connect to the MongoDB instance during the scraping process and store the scraped data.

---

## Project Structure.

- **`books/`**:  Main Scrapy project folder.
  - **`spiders/`**: Folder for Scrapy spiders.
    - **`book.py`**: Scrapy spider for web scraping.
  - **`pipelines.py`**: Pipeline to process and store scraped data.
  - **`settings.py`**: Project settings.
- **`tests/`**: Unit tests for the project.
  - **`test_book.py`**: Tests for the scraping logic.
- **`README.md`**: Project documentation

---

## How to Use

### Clone the repository:
```
git clone https://github.com/your-username/scrapy-mongodb-project.git
```

### Navigate to the project directory:
```
cd scrapy-mongodb-project
```

### Run the Scrapy spider:

```
scrapy crawl book
```

The scraped data will be stored in your MongoDB database.

### Configurations
You can adjust the settings for the MongoDB connection and the target website by modifying the settings.py file in the Scrapy project.

MongoDB settings:

```
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'books'
```

I used this tutorial  [RealPython](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)
