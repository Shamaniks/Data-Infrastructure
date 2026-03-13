# Polyglot Persistence Platform

This repository demonstrates a scalable data infrastructure. It features a MySQL core with a Flask RESTful API, fully containerized and protected by a Role-Based Access Control (RBAC) system.

## Architecture Concept
This is the first step in building a multi-database environment (**Polyglot Persistence**). The goal is to show how different storage engines (MySQL, Redis, MongoDB, ClickHouse) can coexist to handle specific data workloads.

### Current Stack:
*   **Database**: MySQL 8.0 (3NF, RBAC)
*   **API**: Python 3.10 + Flask
*   **Auth**: JWT (JSON Web Tokens)
*   **Testing**: Pytest (Integrated into the CI/CD container flow)
*   **Orchestration**: Docker Compose V2

## Project Structure
The project is split into the database layer and the application layer:
.
├── backend/               # Flask Application
│   ├── app.py             # Entry point
│   ├── auth.py            # JWT & RBAC logic
│   ├── database.py        # MySQL connection manager
│   ├── routes.py          # API Endpoints
│   └── test.py            # Integration tests (Pytest)
├── init-scripts/          # Database initialization (00_init to 04_data)
└── docker-compose.yml     # Infrastructure manifest

## Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shamaniks/Data-Infrastructure
    cd Data-Infrastructure
    ```

2.  **Launch the infrastructure:**
    ```bash
    # This will run migrations, execute Pytest scenarios, and start the API
    docker compose up --build
    # For older docker versions
    docker-comspose up --build
    ```
3.  **Verify the API**
    1. Health Check `GET http://localhost:5000/api/health`
    2. Auth `POST http://localhost:5000/api/login <JSON: login/password>`

4.  **Access the Database:**
    Connect via any SQL client (DBeaver, DataGrip) on `localhost:3306` using:
    *   **User:** `root`
    *   **Password:** `root_password` (defined in docker-compose.yml)

## Roadmap
- [x] **Phase 1:** Core Relational Architecture (MySQL)
- [ ] **Phase 2:** RESTful API implementation (Python/Flask)
- [ ] **Phase 3:** Document-oriented Storage (MongoDB)
- [ ] **Phase 4:** Caching layer integration (Redis)
- [ ] **Phase 5:** Analytical data processing (ClickHouse)

