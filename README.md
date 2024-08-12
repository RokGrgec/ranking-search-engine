# Ranking Search Engine Application

This is a simple FastAPI application that provides an API for searcing simple and complex frazes in the 20 Newsgroups documents and ability to extend those documents by providing additional ones.

## Features

- **POST /search_word/{word}**: Returns a dictionary with found word and the sentances that it was found in with the appropriate score
- **POST /add_document/**: Adds additional document to the list

## Local Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RokGrgec/ranking-search-engine.git
    cd ranking-search-engine
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

## Running the Application

To run the application locally, use the following command:

```bash
uvicorn main:app --reload
```

- The application will be accessible at http://127.0.0.1:8000/

## Standalone app instalation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/RokGrgec/ranking-search-engine.git
    cd ranking-search-engine
    ```

2. **Insall docker** (if docker is not already present on host machine):
    - Official docs: https://docs.docker.com/engine/install/ubuntu/

3. **Deploy stack**:
    ```bash
    bash ./deploy_app.sh
    ```

4. **Clean stack**
    ```bash
    bash ./clean_app.sh
    ```# ranking-search-engine
