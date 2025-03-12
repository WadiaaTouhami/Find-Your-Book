# Find Your Book - A Book Recommendation System

## Overview
Find Your Book is a FastAPI-based book recommendation system that leverages sentence embeddings and a vector database (ChromaDB) to suggest books based on user queries.

## Features
- Uses `sentence-transformers/all-MiniLM-L6-v2` for embedding generation.
- Stores and retrieves book embeddings using ChromaDB.
- Provides an interactive web interface using FastAPI and Jinja2 templates.
- Allows users to specify the number of recommendations (between 1 and 10).
- Responsive UI with an intuitive design.

## Dataset Description
This project utilizes the **Goodreads Book Descriptions** dataset, which contains over **one million** book records, including **titles and descriptions**. The dataset was sourced from the **Hugging Face Datasets** library and serves as the foundation for the semantic search functionality of this application.

### Data Processing Workflow
1. **Data Loading**: The dataset is imported and preprocessed.
2. **Quality Verification**: Ensuring there are no missing values in book descriptions.
3. **Embedding Creation**: Each book description is converted into a numerical representation using the **sentence-transformers/all-MiniLM-L6-v2** model.
4. **Vector Storage**: Embeddings are stored in **ChromaDB**, with batch processing (e.g., chunks of 10,000 books) to optimize memory usage.

By leveraging these embeddings, the project enables **efficient and accurate semantic search**, allowing users to find books based on content similarity rather than just keyword matching.


## Project Structure
```
/
├── app/
│   ├── static/
│   │   └── style.css          # CSS styling for the web interface
│   ├── templates/
│   │   ├── index.html         # Main search page
│   │   └── recommendations.html  # Results page for displaying recommendations
│   └── main.py                # FastAPI application logic
├── chroma_books_data/         # ChromaDB vector database (download separately)
├── create_vectorDB.ipynb      # Notebook for creating the vector database
├── test_vectorDB.ipynb        # Notebook for testing the vector database
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## System Requirements

- Python 3.9 or higher
- 8GB RAM (minimum)
- 20GB free disk space

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/WadiaaTouhami/Find-Your-Book.git
cd Find-Your-Book
```

### 2. Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Download or create the vector database
You can either:
- **Download the pre-built vector database** from [chroma_books_data](https://drive.google.com/drive/folders/1-2l29QrB3uABGft0ofro4wGE9Qh8R4DG?usp=sharing) and place it in the project root.
- **Generate it yourself** by running:
```sh
jupyter notebook create_vectorsDB.ipynb
```

## Running the Application
```sh
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Then, open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.


## API Endpoints
### `GET /`
Serves the homepage.

### `POST /recommendations`
#### Request Form Data:
- `query` (string): A textual description of the book(s) you're looking for.
- `k` (integer): Number of recommendations (default: 3, range: 1-10).

#### Response:
An HTML page displaying the recommended books.

## Technologies Used
- **FastAPI** - Backend framework
- **Hugging Face Sentence Transformers** - Embedding generation
- **ChromaDB** - Vector storage and retrieval
- **Jinja2** - HTML templating
- **CSS** - Frontend styling

## Contributing
Feel free to fork this repository and submit pull requests. Any improvements, bug fixes, or new features are welcome!

## License
MIT License. See `LICENSE` for details.
