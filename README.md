# PIA Network - Crypto Miner Project

A simulated crypto mining web application with Telegram bot integration, referral system, leaderboard, tasks, and wallet functionality.

---

## Features

- Simulated mining every 12 hours via web UI and Telegram bot
- User authentication via Telegram and Google OAuth
- Referral system with rewards
- Task-based reward system
- Leaderboard to track top miners
- Wallet to track and manage PIA token balance
- Dark and light mode UI toggle
- Admin panel for managing users and tasks
- Dockerized backend and frontend for easy deployment

---

## Tech Stack

- **Backend:** FastAPI, PostgreSQL, Redis, SQLAlchemy, Pydantic
- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Bot:** Python Telegram Bot API
- **Deployment:** Docker, Docker Compose, Hostinger (optional)

---

## Project Structure


---

## Getting Started

### Prerequisites

- Docker and Docker Compose installed ([Install Docker](https://docs.docker.com/get-docker/))
- Node.js and npm/yarn (for frontend development)
- Python 3.10+ (for backend local development)

### Environment Setup

Create `.env` files in both `backend/` and `frontend/` directories with appropriate variables.

Example `.env` for backend:

