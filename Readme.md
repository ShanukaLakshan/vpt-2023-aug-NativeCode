# Book Search App

A simple web application to search for books using the OpenLibrary API.

## Table of Contents

- [Description](#description)
- [Technical Stack](#technical-stack)
- [Folder Structure](#folder-structure)
- [Local Setup](#local-setup)
- [Adapting Flask for Vercel](#adapting-flask-for-vercel)
- [Deployment to Vercel](#deployment-to-vercel)
- [Future Enhancements](#future-enhancements)

## Description

Search books by keywords, view results, and delve into detailed book data.

## Technical Stack

- Backend: Flask (Python)
- Frontend: Basic HTML/CSS with JavaScript (jQuery)
- API: OpenLibrary

## Folder Structure

```plaintext
book_search_app/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── vercel.json
│
├── requirements.txt
│
└── .gitignore
```

## Local Setup

1. Clone the repository:

```bash
git clone [REPO_URL]

cd book_search_app


pip install -r requirements.txt

FLASK_APP=book_search_app/app.py FLASK_ENV=development flask run


Open http://127.0.0.1:5000/ in your browser.

Adapting Flask for Vercel
The application is adapted to run as a serverless function on Vercel. The Flask app is housed within the api directory and is configured to respond to Vercel's expected handler function.


```
