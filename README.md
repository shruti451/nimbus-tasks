# NimbusTasks ☁️

> A cloud-native task management application built to learn modern DevOps practices from the ground up.

## 📖 About

NimbusTasks is a personal learning project that evolves through multiple versions.

Instead of creating separate projects for every technology, this application will gradually incorporate modern DevOps tools and cloud practices while keeping the same core application.

The objective is to understand how real-world applications evolve over time.

---

## 🚀 Current Version

### Version 1 (Completed)

- Python Flask application
- Harry Potter inspired UI
- Create, Read, Update & Delete (CRUD)
- Git Version Control
- GitHub Repository

### Next

- Docker
- Docker Compose
- MySQL
- Redis
- Jenkins
- Kubernetes
- GCP
---

Version 1 ✅ Flask CRUD Application

Version 2 🐳 Docker

Version 3 🐳 Docker Compose

Version 4 🗄️ MySQL & Redis

Version 5 🔄 Jenkins CI/CD

Version 6 ☸️ Kubernetes

Version 7 ☁️ Google Cloud Platform Deployment

Version 8 ☁️ AWS Migration

---

## 🏗️ Current Architecture

Internet
   ↓
Google Cloud VM
   ↓
Docker Compose
   ↓
┌───────────────┐
│ Flask         │
│ Application   │
└───────┬───────┘
        │
   ┌────┴─────┐
   ↓          ↓
 MySQL      Redis
   │          │
Persistent   Cache
 Storage

---

### Redis Caching

Redis is used as a caching layer alongside MySQL.

- Implemented a cache-aside strategy for task retrieval.
- Flask checks Redis for cached tasks before querying MySQL.
- On a cache miss, tasks are retrieved from MySQL and stored in Redis.
- Cache is invalidated when tasks are created, deleted, or updated.
- MySQL remains the persistent source of truth.
- Redis runs as a separate container managed by Docker Compose.

## 📚 Technologies

- Python
- Flask
- MySQL
- Redis
- Docker
- Docker Compose
- Linux
- Git
- GitHub
- Google Cloud Platform

---

## ✨ Features

- Add quests
- Complete/Undo quests
- Delete quests
- Harry Potter inspired interface

---

## 📸 Screenshots

### Home Page

<img src="images/home.png" width="900">

### Quest Board

<img src="images/quest-board.png" width="900">

## 📌 Status

🚧 Currently under development.
