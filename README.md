# Polyglot Persistence Platform — Phase 1: Relational Core (MySQL)

This repository demonstrates a scalable data infrastructure. It starts with a robust **MySQL** architecture, designed for transactional integrity, and is containerized for instant deployment.

## Architecture Concept
This is the first step in building a multi-database environment (**Polyglot Persistence**). The goal is to show how different storage engines (MySQL, Redis, MongoDB, ClickHouse) can coexist to handle specific data workloads.

### Current Stack:
*   **Database:** MySQL 8.0
*   **Orchestration:** Docker Compose
*   **Design Patterns:** 3NF (Third Normal Form), RBAC (Role-Based Access Control)

## Project Structure
The initialization logic is decoupled into sequential SQL scripts located in `/init-scripts`. Docker executes them in alphabetical order:

1.  `00_init.sql` — Database creation and environment settings.
2.  `01_schema.sql` — Data Definition Language (DDL): Tables and relations.
3.  `02_indexes.sql` — Performance optimization and constraints.
4.  `03_roles.sql` — Security layer: User roles and privilege grants.
5.  `04_data.sql` — DML: Initial seed data for demonstration.

## Quick Start

1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd <project-folder>
    ```

2.  **Launch the infrastructure:**
    ```bash
    docker-compose up -d
    ```

3.  **Access the Database:**
    Connect via any SQL client (DBeaver, DataGrip) on `localhost:3306` using:
    *   **User:** `root`
    *   **Password:** `root_password` (defined in docker-compose.yml)

## Roadmap
- [x] **Phase 1:** Core Relational Architecture (MySQL)
- [ ] **Phase 2:** RESTful API implementation (Python/Flask)
- [ ] **Phase 3:** Document-oriented Storage (MongoDB)
- [ ] **Phase 4:** Caching layer integration (Redis)
- [ ] **Phase 5:** Analytical data processing (ClickHouse)

