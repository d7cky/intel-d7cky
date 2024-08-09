# Intel d7cky Search

## Description
This project is a Intel d7cky application hat utilizes the `intelxapi` library to search and display data from IntelX. The application features a simple web interface that allows users to enter search queries and view detailed results.

## Directory Structure
/project_folder
/template
/index.html
/static
/searchWorker.js
Dockerfile
main.py
requirements.txt

## Requirements
- Python 3.9+
- Docker
- Git

### Using Docker

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/d7cky/intel-d7cky.git
    cd intel-d7cky
    ```

2. Configure the Dockerfile and docker-compose.yml to build and run the application:
    ```sh
    docker-compose up --build
    ```

3. The application will be available at `http://localhost:8000`.

### Manual Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/d7cky/intel-d7cky.git
    cd intel-d7cky
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Install the `intelx` library:
    ```sh
    pip install "intelx @ git+https://github.com/IntelligenceX/SDK#subdirectory=Python"
    ```

4. Run the application:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

5. The application will be available at `http://localhost:8000`.

## Usage

1. Open `http://localhost:8000` in your web browser.
2. Enter a search query in the search box and click `Search`.
3. The search results will be displayed. You can click `View Details` to see more information about each result.

## Environment Configuration

This application uses the IntelX API key to perform searches. You need to set the `INTELX_API_KEY` environment variable to use your API key.

In Docker Compose, this environment variable is configured in the `docker-compose.yml` file:
```yaml
environment:
  - INTELX_API_KEY=your-intelx-api-key
```

### Contribution

If you want to contribute to this project, please create a pull request or open an issue on GitHub.

### Contact

If you have any questions, please contact us at d3cky.duck@gmail.com.