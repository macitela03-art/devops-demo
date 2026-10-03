# DevOps Demo: Flask app with a CI/CD pipeline

A small Flask web app that shows an automated CI pipeline and a Docker container.

## Files
| File | Purpose |
|---|---|
| app.py | The web app (home page and /health) |
| test_app.py | Automated tests (pytest) |
| requirements.txt | Dependencies |
| Dockerfile | Packages the app as a container image |
| .github/workflows/ci.yml | GitHub Actions pipeline |
| azure-pipelines.yml | Azure DevOps pipeline (alternative) |

## Run locally
    pip install -r requirements.txt
    pytest -v
    python app.py            # open http://localhost:5000

## Run with Docker
    docker build -t devops-demo .
    docker run -p 5000:5000 devops-demo     # open http://localhost:5000

## What the pipeline does
1. Triggers on every commit to main
2. Installs the dependencies
3. Runs the tests
4. Builds the Docker image
