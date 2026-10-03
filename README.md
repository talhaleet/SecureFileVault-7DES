# DES-7 File Encrypt / Decrypt

A web application for encrypting and decrypting files using a 7-round DES algorithm.

<img src="/assets/image.png" alt="DES-7">

## Project Structure

```
Encrypt-Decrypt/
├── backend/
│   ├── app.py              # FastAPI server (encrypt/decrypt endpoints)
│   ├── des.py              # DES algorithm implementation (7 rounds)
│   ├── main.py             # CLI version
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables (CORS origins)
├── frontend/
│   ├── index.html          # Main page
│   ├── style.css           # Styles
│   └── app.js              # Frontend logic
├── start_server.bat        # Quick-start script for backend
└── README.md
```

## Setup

### Backend

1. Install Python dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Configure `.env` file in `backend/` folder:

   ```
   FRONTEND_URL=http://localhost:5500,https://your-app-name.vercel.app
   ```

   Replace `https://your-app-name.vercel.app` with your actual Vercel deployment URL.

3. Start the server:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

   Or use the provided `start_server.bat` from the root folder.

### Frontend

1. Update `API_BASE` in `frontend/app.js` with your deployed backend URL:

   ```js
   const API_BASE = 'https://your-backend-url.onrender.com';
   ```

   For local development, keep it as `http://localhost:8000`.

2. Open `index.html` in a browser or deploy the `frontend/` folder to Vercel.

## Deployment

### Frontend (Vercel)

1. Push the `frontend/` folder to a GitHub repository.
2. Import the repository in Vercel.
3. Set the root directory to `frontend`.
4. Deploy.

### Backend (Render / Railway / any hosting)

1. Push the `backend/` folder to a GitHub repository.
2. Import in your hosting platform.
3. Set the start command: `uvicorn app:app --host 0.0.0.0 --port 8000`
4. Add the environment variable `FRONTEND_URL` with your Vercel URL.

### Connecting Frontend and Backend

- In `backend/.env`, set `FRONTEND_URL` to include your Vercel domain.
- In `frontend/app.js`, set `API_BASE` to your deployed backend URL.

## How It Works

1. Select a file and enter a 16-character hexadecimal key.
2. Click **Encrypt and Download** to encrypt the file. A `.des7` file is downloaded.
3. To decrypt, switch to the Decrypt tab, upload the `.des7` file, enter the same key, and click **Decrypt and Download**.

## Algorithms

- 7-round DES (Data Encryption Standard) with ECB mode
- PKCS#7 padding for block alignment
- 64-bit key (provided as 16 hex characters)
