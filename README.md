# 🧮 Health Calculator Microservice

[![CI/CD](https://github.com/Rahman-git7/health-calculator-service-rs/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Rahman-git7/health-calculator-service-rs/actions/workflows/ci-cd.yml)
![GitHub language count](https://img.shields.io/github/languages/top/Rahman-git7/health-calculator-service-rs)
![Docker](https://img.shields.io/badge/docker-containerized-blue) ![Azure](https://img.shields.io/badge/Deployed%20on-Azure-blue)


A simple Flask-based microservice to calculate:

- **BMI** (Body Mass Index)
- **BMR** (Basal Metabolic Rate)

☁️ Deployed via Docker on **Azure App Service**  
⚙️ Automated with **GitHub Actions** and **Azure Container Registry (ACR)**

---

## 🌐 Live Demo

**Base URL:**  

[UI App](https://health-calculator-app-rs-ddcfa6fka3grc9du.francecentral-01.azurewebsites.net)


`https://health-calculator-app-rs-ddcfa6fka3grc9du.francecentral-01.azurewebsites.net`

---

## 📌 API Endpoints

### 🔹 `POST /bmi`

**Request:**

```json
{
  "height": 1.75,
  "weight": 70
}
```
Test with curl : 
```bash
curl -X POST https://health-calculator-app-rs-ddcfa6fka3grc9du.francecentral-01.azurewebsites.net/bmi \
  -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70}'
```

### 🔹 `POST /bmr`


**Request:**

```json
{
  "height": 1.75,
  "weight": 70
}
```

Test with curl : 

```bash

curl -X POST https://health-calculator-app-rs-ddcfa6fka3grc9du.francecentral-01.azurewebsites.net/bmi \
  -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70}'
```

### 🛠️ Local Development

* `make init`      # Install dependencies
* `make run`       # Run app locally (http://localhost:5000)
* `make test`      # Run unit tests
* `make build`     # Build Docker image

### 🔄 GitHub Actions CI/CD

This project uses GitHub Actions to automate:

* 🔍 Installing dependencies and running tests
* 🐳 Building the Docker image
* ☁️ Pushing the image to Azure Container Registry (ACR)
* 🚀 Deploying the image to Azure App Service

**The workflow is defined in**: `.github/workflows/ci-cd.yml`

Secrets used:

- `AZURE_WEBAPP_PUBLISH_PROFILE` : for App Service deployment
- (optional) `AZURE_CREDENTIALS` – if pushing directly to ACR from CI



### 🚀 Tech Stack

* Python + Flask
* Docker
* GitHub Actions
* Azure Container Registry (ACR)
* Azure App Service (Linux)