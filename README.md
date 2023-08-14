# YouTube Search API Documentation

Welcome to the documentation for the YouTube Search API – a powerful tool built using Python, Flask, and a combination of libraries that lets you seamlessly search for YouTube videos and retrieve raw search data. Whether you're a developer building applications or a curious user exploring video content, this API simplifies the process of accessing YouTube's vast collection.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Landing Page](#landing-page)
  - [Search Endpoint](#search-endpoint)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The YouTube Search API is designed to make searching for YouTube videos easy and accessible. It employs the power of Flask, the simplicity of requests, the parsing capabilities of BeautifulSoup, and the flexibility of json5 to offer a seamless experience. With this API, you can explore YouTube video content programmatically and integrate it into your projects.

## Getting Started

### Prerequisites

Before you can use the YouTube Search API, you need to ensure you have the following prerequisites:

- Python 3.11 installed on your system.
- Basic understanding of using the command line or terminal.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/LuisRamosOfficial/Youtube-Searcher-API.git
   cd youtube-search-api
   ```

2. Install the required libraries using pip:

   ```bash
   pip install flask requests beautifulsoup4 json5
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

You should now have the YouTube Search API up and running on your local machine.

## Usage

### Landing Page

Navigate to `http://localhost:4040/` in your web browser to access the landing page of the API. This page provides you with an interactive interface to test the API. You can enter search queries and see the search results without needing to make direct API calls.

### Search Endpoint

To programmatically retrieve raw search data, you can use the `/search` endpoint. Send a GET request to `http://localhost:4040/search?q=YOUR_SEARCH_TERM` where `YOUR_SEARCH_TERM` is the term you want to search for on YouTube. This endpoint returns the raw search data in JSON format.

For example, to search for videos about "cute cats", you would use the following URL:

```http
GET http://localhost:4040/search?q=cute%20cats
```

This request would provide you with detailed information about videos related to cute cats.

## Dependencies

The YouTube Search API relies on the following libraries:

- **Flask**: A micro web framework that simplifies building web applications in Python.
- **requests**: A library for making HTTP requests.
- **BeautifulSoup**: A library for parsing HTML and XML documents.
- **json5**: A library for parsing and encoding JSON-like data.

These libraries work together to create a smooth experience for searching YouTube videos and retrieving data.

## Contributing

Contributions to the YouTube Search API are welcome! If you encounter any issues or have suggestions for improvements, feel free to open issues and submit pull requests on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

