# Polyglot Persistence Platform

This repository demonstrates a scalable data infrastructure. It features a MySQL core with a Flask RESTful API, fully containerized and protected by a Role-Based Access Control (RBAC) system.

## Architecture Concept
This is the first step in building a multi-database environment (**Polyglot Persistence**). The goal is to show how different storage engines (MySQL, Redis, MongoDB, ClickHouse) can coexist to handle specific data workloads.

### Current Stack:
  * **Databases**:
    * MySQL 8.0 (3NF schema + full RBAC)
    * Redis 7.x (persistence enabled, password protected)
  * **API Layer**: Python 3.10 + Flask RESTful service (JWT auth, role-based endpoints)
  * **Security**: RBAC enforced at DB, API and Redis levels
  * **Testing**: Pytest suite covering MySQL, Redis and API integration
  * **Orchestration**: Docker Compose V2 (`docker compose up --build`)

## Project Structure
The project is split into the database layer and the application layer:
```
.
├── backend/                  # Flask Application
│   ├── connectors/           # Databases connectors dir   
│   ├── redis_engine/         # Databases connectors dir   
│   │   ├── auth.py           # Redis token storing manager
│   │   └── cart.py           # Client shop cart manager
│   ├── routes/               # API endpoints dir
│   ├── tests/                
│   │   ├── auth_test.py      # Authing and table permissions
│   │   ├── cart_test.py      # Cart using full cycle
│   │   └── conftest.py       # Connections to DB and setting the app config
│   ├── app.py
│   ├── auth.py               # JWT + RBAC
│   └── base_routes.py        # Old API endpoint (gotta fix that soon)
├── init-scripts/             # MySQL initialization
├── redis/                    # Redis config & persistence volume
├── docker-compose.yml        # Full stack manifest (MySQL + Redis + API)
└── README.md                 # You reading that right now
```

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
    3. Test `docker compose run --rm tests`

4.  **Access the Database:**
    Connect via any SQL client (DBeaver, DataGrip) on `localhost:3306` using:
    *   **User:** `root`
    *   **Password:** `root_password` (defined in docker-compose.yml)

## Roadmap
- [x] **Phase 1:** Core Relational Architecture (MySQL)
- [x] **Phase 2:** RESTful API implementation (Python/Flask)
- [ ] **Phase 3:** Document-oriented Storage (MongoDB)
- [x] **Phase 4:** Caching layer integration (Redis)
- [ ] **Phase 5:** Analytical data processing (ClickHouse)

