# SmartShelfX Inventory Monitor — Lab ISE 2

## 1. Project Overview

SmartShelfX Inventory Monitor is a simple web application developed using Python and Flask. It displays inventory stock levels and identifies items whose stock falls below the minimum threshold.

This project demonstrates the DevOps lifecycle using Git, GitHub, Docker, and Jenkins as part of the ML DevOps Laboratory ISE 2 assignment.

## 2. Objectives

- Develop a web application using Python and Flask.
- Use Git for source code version control.
- Use GitHub to host the project repository.
- Containerize the application using Docker.
- Use Jenkins to automate build and testing tasks in a CI/CD pipeline.
- Verify the application using a health-check endpoint.

## 3. Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Version Control:** Git
- **Source Code Hosting:** GitHub
- **Containerization:** Docker
- **CI/CD Automation:** Jenkins
- **Operating System:** Windows

## 4. Project Structure

```text
Lab-ISE2-CICD/
├── app.py
├── README.md
├── .gitignore
├── requirements.txt
├── Dockerfile
└── Jenkinsfile
```

The `requirements.txt`, `Dockerfile`, and `Jenkinsfile` will be added as the project setup progresses.

## 5. Application Features

- Displays an inventory dashboard.
- Shows item names, available stock, and minimum stock levels.
- Identifies items with low stock.
- Provides a health-check endpoint at `/health`.
- Returns a JSON response indicating the application's health status.

## 6. Prerequisites

Install the following tools before running the project:

- Python
- Git
- Docker Desktop
- Java JDK
- Jenkins

## 7. Installation and Execution

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Lab-ISE2-CICD
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### Step 2: Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

Open the following URLs in a browser:

- Dashboard: http://127.0.0.1:5000
- Health check: http://127.0.0.1:5000/health

## 8. Git Version Control

Initialize the repository and commit the source code:

```bash
git init
git add .
git commit -m "Initial commit: Flask inventory monitoring app"
```

After creating a GitHub repository, connect and push the code:

```bash
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## 9. Docker and Jenkins

Docker will be used to package the Flask application into a container. Jenkins will be configured to automate the build and testing stages of the CI/CD pipeline.

The Docker configuration and Jenkins pipeline will be documented after they have been implemented and verified.

## 10. Expected Outcome

The project demonstrates how a small Flask web application can be version-controlled, hosted on GitHub, containerized with Docker, and integrated with Jenkins for CI/CD automation.

## 11. Author

**Student Name:** Shweta Patil  
**Department:** CSE (Artificial Intelligence and Machine Learning)  
**Academic Year:** 2026–27  
**Course:** ML DevOps Laboratory  
**Assessment:** Lab ISE 2 — CI/CD Pipeline and Monitoring Tools
