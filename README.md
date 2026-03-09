# ML Inference API

A scalable machine learning inference API built with FastAPI and Docker. 
This project demonstrates how to serve ML models in production, with caching, containerization, and async-ready endpoints.

## Features
- REST API with FastAPI
- Model loading and prediction using Scikit-learn
- Redis caching for repeated requests
- Containerized with Docker and Docker Compose
- Swagger UI documentation at `/docs`

## Architecture
Client → FastAPI → ML Model → Redis Cache

## Run
1. Build and run Docker: docker-compose up --build
2. API available at `http://localhost:8000`
3. Swagger docs: `http://localhost:8000/docs`