# Find Your Book

**Find Your Book** is a tool that uses semantic search to help users discover books based on a description or a general topic. The repository leverages embeddings and vector storage to create a highly responsive search engine for book recommendations, ideal for avid readers looking for specific themes or genres.

## Features

- **Semantic Search**: Retrieves books based on meaning rather than exact keywords.
- **Book Database**: Utilizes the Goodreads book descriptions dataset.
- **Customizable Embeddings**: Built with `HuggingFace` sentence transformers to provide meaningful search results.
- **Scalable Storage**: Utilizes ChromaDB for efficient storage and search across book embeddings.

## Installation

To install the required libraries, run:

```bash
!pip install sentence-transformers langchain langchain-community chromadb datasets
