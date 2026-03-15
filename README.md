# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      ...tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      ...tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      ...tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

## Deployment (Vercel + Supabase)

### 1) Create a Supabase project

- Go to https://app.supabase.com and create a new project.
- From the **Settings > API** page, copy the `Project URL` and **Service Role** key.
- Create a storage bucket named `post-media` (or update `SUPABASE_BUCKET_NAME` to match).
- Use the provided Postgres connection string as `DATABASE_URL`.

### 2) Configure environment variables

- Copy `.env.example` to `.env` for local development.
- Fill in:
  - `DATABASE_URL` (Supabase Postgres connection string)
  - `SUPABASE_URL` and `SUPABASE_KEY` (Supabase project URL and service role key)
  - `VITE_API_BASE_URL` (backend URL; for local dev: `http://localhost:8000`)
  - `CORS_ALLOWED_ORIGINS` (comma-separated allowed frontend origins, e.g. `http://localhost:5173,https://<your-vercel-domain>.vercel.app`)

### 3) Run locally

```bash
# install deps for frontend (node)
npm install

# install deps for backend (python)
pip install -r requirements.txt

# run backend
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# run frontend
npm run dev
```

### 4) Deploy the frontend to Vercel

1. Connect this Git repo to Vercel.
2. Use the default build command `npm run build` and output directory `dist`.
3. Add the following Environment Variable in the Vercel dashboard:
   - `VITE_API_BASE_URL` → the URL where your backend is hosted (e.g. `https://my-backend.example.com`).

> Note: This repo includes a `vercel.json` file to ensure client-side routes work correctly.

### 5) Backend hosting options

This project includes a FastAPI backend (in `api/`). Vercel does not natively run FastAPI, so you will need to host the backend on a platform that supports Python (e.g. Render, Railway, Fly, or Supabase Edge Functions).

If you host the backend elsewhere, set `VITE_API_BASE_URL` in Vercel to point to it.

### 6) Deploy backend on Render

This repo includes `render.yaml` and `runtime.txt` for Render deployment.

Steps:

1. Push your latest code to GitHub.
2. In Render, create a new Blueprint and connect your repository.
3. Render will detect `render.yaml` and create the `technosk-api` web service.
4. In Render service environment settings, set these values:
  - `DATABASE_URL`
  - `SUPABASE_URL`
  - `SUPABASE_KEY` (service role key)
  - `SECRET_KEY`
  - `CORS_ALLOWED_ORIGINS` (include local + your Vercel URL)
  - `SUPABASE_BUCKET_NAME` (default `post-media`)
5. Deploy and open `/docs` on your Render backend URL to verify API health.

After backend is live, set `VITE_API_BASE_URL` in Vercel to your Render URL.