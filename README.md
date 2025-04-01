# Health Calculator Microservice

A simple Flask-based microservice to calculate:

- **BMI** (Body Mass Index)
- **BMR** (Basal Metabolic Rate)

☁️ Deployed via Docker on **Azure App Service**  
⚙️ Automated with **GitHub Actions** and **Azure Container Registry (ACR)**

---

## 🌐 Live Demo

**Base URL:**  
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

`make init`      # Install dependencies
`make run`       # Run app locally (http://localhost:5000)
`make test`      # Run unit tests
`make build`     # Build Docker image

### 🚀 Tech Stack

* Python + Flask
* Docker
* GitHub Actions
* Azure Container Registry (ACR)
* Azure App Service (Linux)