## AI Finance Coach

### Project Overview
AI Finance Coach is a full-stack application that provides users with an AI-powered finance dashboard and insights. The backend is built with FastAPI and SQLAlchemy, while the frontend uses Next.js 14, Tailwind CSS, and animate.css for a modern, interactive UI.

---

### What We Have Achieved

#### Backend
- FastAPI backend with endpoints for:
  - Categories (CRUD)
  - Transactions (CRUD, auto-categorization)
  - Analytics (category totals)
  - Trends (weekly changes)
  - Forecast (monthly estimate)
  - AI Insights (OpenAI integration)
- PostgreSQL database integration (with SQLAlchemy ORM)
- Automated backend tests (pytest, httpx)
- Duplicate category handling and timestamp serialization fixes

#### Frontend
- Next.js 14 project scaffolded in `/frontend`
- Tailwind CSS and animate.css integrated
- Landing page migrated from static HTML to React/Next.js
- Live dashboard section fetching analytics, trends, and forecast from backend
- Modular code for easy expansion

#### Integration
- Frontend and backend are connected via REST API
- API URL is configurable via `NEXT_PUBLIC_BACKEND_URL` environment variable

---

### What Is Not Yet Achieved
- No authentication or user accounts
- No persistent user sessions or login/logout
- No forms for adding transactions or categories from the frontend
- No deployment (project is running locally)
- No CI/CD pipeline
- No advanced error handling or notifications in the frontend
- No mobile/responsive optimizations beyond basic Tailwind breakpoints
- No Docker or containerization setup

---

### How to Run Locally

#### Backend
1. Install Python dependencies:
	```bash
	cd backend
	pip install -r requirements.txt
	```
2. Set up your `.env` file (see `.env.example` if available).
3. Start the backend:
	```bash
	uvicorn backend.main:app --reload
	```

#### Frontend
1. Install Node.js dependencies:
	```bash
	cd frontend
	pnpm install
	# or npm install
	```
2. Set the backend URL if needed:
	```bash
	export NEXT_PUBLIC_BACKEND_URL="http://localhost:8000"
	# or set in .env.local
	```
3. Start the frontend:
	```bash
	pnpm dev
	# or npm run dev
	```
4. Visit [http://localhost:3000](http://localhost:3000)

---

### Next Steps
- Add authentication and user management
- Add forms for transaction/category creation from the frontend
- Improve error handling and user feedback
- Prepare for deployment (Docker, CI/CD, hosting)
- Expand AI insights and dashboard features

---

### Repository Structure
- `/backend` - FastAPI backend
- `/frontend` - Next.js frontend
- `index.html` - Original static landing page (reference)

---

### Authors
- Project bootstrapped and integrated by wkyarua and Topsy-yy
