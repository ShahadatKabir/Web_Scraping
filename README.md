# 🎬 Rotten Tomatoes Movie Scraper

This project is a **Python-based web scraper** that collects movie information from **Rotten Tomatoes** using their public `cnapi` endpoint. It dynamically handles **pagination**, extracts movie scores, and saves the results into a **CSV file** for further analysis.

---

## 📁 Project Structure

```
├── movie_scraper.py          # Main Python script
├── movies_at_home-netflix.csv # Output CSV file (example)
├── README.md                 # Project documentation
```

---

## 🚀 Features

* Scrapes movies by **category** and **streaming platform**
* Dynamically handles **pagination** (multiple pages)
* Extracts:

  * Movie title
  * Critics score & sentiment
  * Audience score & sentiment
* Saves all collected data into a **single CSV file**
* Prevents infinite loops during pagination

---

## 🛠️ Requirements

Make sure you have Python **3.8+** installed.

Install required libraries:

```bash
pip install pandas requests
```

---

## ▶️ How to Run

1. Clone or download this repository
2. Navigate to the project directory
3. Run the scraper:

```bash
python movie_scraper.py
```

Example function call inside the script:

```python
movie_scraper('movies_at_home', 'netflix')
```

---

## 📊 Output CSV File

The script generates a CSV file named using the format:

```
<category>-<platform>.csv
```

Example:

```
movies_at_home-netflix.csv
```

### CSV Columns

| Column Name        | Description                      |
| ------------------ | -------------------------------- |
| title              | Movie title                      |
| critic_score       | Critics score percentage         |
| critic_sentiment   | Critics sentiment (Fresh/Rotten) |
| audience_score     | Audience score percentage        |
| audience_sentiment | Audience sentiment               |

---

## 🧠 Pagination Logic

The scraper automatically:

* Detects the **next page cursor**
* Stops when:

  * No new movies are returned
  * The pagination cursor does not change

This ensures:

* No duplicate data
* No infinite loops

---

## ⚠️ Notes

* This project is for **educational purposes only**
* Avoid running the scraper too frequently to prevent IP blocking
* Website structure may change over time

---

## 📌 Future Improvements

* Add page limits
* Add request delays
* Improve error handling
* Support multiple platforms at once

---

## 👤 Author

Developed as a learning project for **Python, APIs, and data scraping**.

---

Happy scraping! 🚀
