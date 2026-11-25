# Hello CI/CD Project

A sample application for Jenkins CI/CD pipeline integration, automated testing, and build artifact packaging.

## Features
- Automated unit testing with Python `unittest`
- Automated packaging and artifact archiving
- Jenkins Pipeline (`Jenkinsfile`) & Freestyle job support
- GitHub Webhook integration (`/github-webhook/`)

## Local Run
```bash
python app.py
python -m unittest test_app.py
```

## Build
```bash
bash build.sh
```

<!-- Webhook Trigger Test -->
