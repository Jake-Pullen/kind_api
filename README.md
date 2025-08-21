# 🌟 Kind API - Random Compliment Service

A simple REST API that provides random compliments from a YAML file.

---

## 🚀 Features

✅ Returns a random compliment from a YAML file.  
✅ Health check endpoint for monitoring.  
✅ Error handling for missing files or malformed YAML.  
✅ Secure YAML parsing (yaml.safe_load).  
✅ Easy to deploy with Docker(soon) or local development.  

---

## 📦 Dependencies

Uses UV for environment and package version handling: 
[uv link](https://docs.astral.sh/uv/)

`uv sync`

---

### 📁 File Structure

Your project should have these files:

kind-api/
├── kind_response.yaml        # Your YAML file with compliments  
├── main.py                   # Flask API script  
└── README.md                 # This file  

---

## 🔧 Configuration

1. YAML Format (kind_response.yaml)  
Ensure your YAML file follows this structure:

```
compliments:
  - "Your kindness makes others feel seen and valued."
  - "Your creativity inspires me every time I see it."
  # ... (add more compliments)
```

---

## 📡 API Endpoints

### ✅ Get a Random Compliment

Request:

`curl http://localhost:5000/api/v1/compliment`

Response:

```
{
  "api_version": "v1",
  "compliment": "Your kindness makes others feel seen and valued.",
  "status": "success"
}
```

### 📊 Health Check

Request:

`curl http://localhost:5000/api/health`

Response:
```
{
  "status": "ok",
  "message": "Kind API is running",
  "version": "1.0.0"
}
```

---

## 🚀 Deployment Options

### ✅ Local Development

Run the server:

`uv run main.py`

### 🐳 Docker (Coming Soon)

Create a Dockerfile with:

FROM python:3.10-slim  
WORKDIR /app  
COPY . .  
RUN pip install flask pyyaml  
CMD ["python3", "kind_api.py"]  
Build and run:  

docker build -t kind-api .  
docker run -p 5000:5000 kind-api

---

## 🛡️ Security Notes

- Uses yaml.safe_load() to avoid YAML injection risks.
- Proper HTTP status codes for errors (404, 500).
- Environment variables support for flexible deployment.

