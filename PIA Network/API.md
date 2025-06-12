# PIA Network API Documentation

This document outlines the REST API endpoints for the PIA Network crypto miner backend.

---

## Authentication

### POST /auth/telegram-login
Authenticate or register user via Telegram token.

- **Request Body:**
  ```json
  {
    "token": "telegram_auth_token"
  }


