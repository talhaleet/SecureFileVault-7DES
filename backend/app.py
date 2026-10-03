"""FastAPI backend for DES 7-round file encryption/decryption."""
import os
import urllib.parse
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from des import encrypt_bytes, decrypt_bytes, validate_and_parse_key

load_dotenv()

app = FastAPI(title="DES-7 File Encrypt/Decrypt", version="1.0.0")

# Load allowed origins from .env (comma-separated)
raw_origins = os.getenv("FRONTEND_URL", "http://localhost:5500")
allowed_origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Original-Filename", "X-File-Size"],
)

ENCRYPTED_MARKER = b"DES7ENC:"  # 8-byte magic header to identify encrypted files


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "algorithm": "DES-7-rounds", "version": "1.0.0"}


@app.post("/encrypt")
async def encrypt_file(
    file: UploadFile = File(...),
    key: str = Form(...),
):
    """
    Encrypt an uploaded file using 7-round DES.
    Returns the encrypted file with a .des7 extension.
    """
    # Validate the key
    try:
        parsed_key = validate_and_parse_key(key.strip())
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid key: {e}")

    # Read file bytes
    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # Encrypt
    try:
        encrypted = encrypt_bytes(file_bytes, parsed_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Encryption failed: {e}")

    # Build output: magic marker + original filename length (2 bytes) + original filename + ciphertext
    original_name = (file.filename or "file").encode("utf-8")
    name_len = len(original_name).to_bytes(2, "big")
    payload = ENCRYPTED_MARKER + name_len + original_name + encrypted

    # Output filename
    out_name = (file.filename or "file") + ".des7"
    encoded_name = urllib.parse.quote(out_name)

    return Response(
        content=payload,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename*=UTF-8''{encoded_name}",
            "X-Original-Filename": encoded_name,
            "X-File-Size": str(len(payload)),
        },
    )


@app.post("/decrypt")
async def decrypt_file(
    file: UploadFile = File(...),
    key: str = Form(...),
):
    """
    Decrypt an uploaded .des7 file using 7-round DES.
    Returns the original decrypted file.
    """
    # Validate the key
    try:
        parsed_key = validate_and_parse_key(key.strip())
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid key: {e}")

    # Read file bytes
    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # Verify magic header
    marker_len = len(ENCRYPTED_MARKER)
    if not file_bytes.startswith(ENCRYPTED_MARKER):
        raise HTTPException(
            status_code=400,
            detail="File does not appear to be a valid DES-7 encrypted file. Please upload a .des7 file.",
        )

    # Parse: marker + 2-byte name length + original name + ciphertext
    offset = marker_len
    name_len = int.from_bytes(file_bytes[offset: offset + 2], "big")
    offset += 2
    original_name = file_bytes[offset: offset + name_len].decode("utf-8", errors="replace")
    offset += name_len
    ciphertext = file_bytes[offset:]

    if not ciphertext:
        raise HTTPException(status_code=400, detail="Encrypted payload is empty.")

    # Decrypt
    try:
        plaintext = decrypt_bytes(ciphertext, parsed_key)
    except (ValueError, Exception) as e:
        raise HTTPException(
            status_code=400,
            detail=f"Decryption failed. Wrong key or corrupted file. ({e})",
        )

    encoded_name = urllib.parse.quote(original_name)

    return Response(
        content=plaintext,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename*=UTF-8''{encoded_name}",
            "X-Original-Filename": encoded_name,
            "X-File-Size": str(len(plaintext)),
        },
    )
