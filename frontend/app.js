/* DES-7 File Encrypt/Decrypt — app.js */

'use strict';

// API_BASE is loaded from config.js

/* -- Utility: format bytes -- */
function formatBytes(bytes) {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

/* -- Tab switching -- */
function switchTab(mode) {
  const isEncrypt = mode === 'encrypt';
  document.getElementById('encryptTab').classList.toggle('active', isEncrypt);
  document.getElementById('decryptTab').classList.toggle('active', !isEncrypt);

  document.getElementById('encrypt-section').hidden = !isEncrypt;
  document.getElementById('decrypt-section').hidden = isEncrypt;
}
window.switchTab = switchTab;

/* -- Validate hex key -- */
function validateKey(key) {
  const clean = key.trim().toUpperCase();
  if (clean.length !== 16) return null;
  if (!/^[0-9A-F]{16}$/.test(clean)) return null;
  return clean;
}

/* -- Download blob -- */
function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}

/* -- Get filename from response -- */
function getFilenameFromResponse(response, fallback) {
  const raw = response.headers.get('Content-Disposition') || '';
  const utf8match = raw.match(/filename\*=UTF-8''(.+)/i);
  if (utf8match) return decodeURIComponent(utf8match[1]);
  const plain = raw.match(/filename="?([^";\n]+)"?/i);
  if (plain) return plain[1].trim();
  return fallback;
}

/* -- ENCRYPT form -- */
let encryptedBlob = null, encryptedName = '';

document.getElementById('encryptForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById('encryptFile');
  const file = fileInput.files[0];
  if (!file) { alert('Please select a file.'); return; }

  const rawKey = document.getElementById('encryptKey').value;
  const key = validateKey(rawKey);
  if (!key) { alert('Key must be exactly 16 hex characters (0-9, A-F).'); return; }

  document.getElementById('encryptResult').hidden = true;
  document.getElementById('encryptError').hidden = true;

  const btn = document.getElementById('encryptSubmit');
  btn.disabled = true;
  btn.textContent = 'Encrypting...';

  try {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('key', key);

    const res = await fetch(`${API_BASE}/encrypt`, {
      method: 'POST',
      body: formData,
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }

    encryptedBlob = await res.blob();
    encryptedName = getFilenameFromResponse(res, file.name + '.des7');

    document.getElementById('encryptResultDetail').textContent =
      encryptedName + ' - ' + formatBytes(encryptedBlob.size);
    document.getElementById('encryptResult').hidden = false;

    downloadBlob(encryptedBlob, encryptedName);

  } catch (err) {
    document.getElementById('encryptErrorDetail').textContent = err.message;
    document.getElementById('encryptError').hidden = false;
  } finally {
    btn.disabled = false;
    btn.textContent = 'Encrypt and Download';
  }
});

document.getElementById('encryptDownloadBtn').addEventListener('click', () => {
  if (encryptedBlob) downloadBlob(encryptedBlob, encryptedName);
});

/* -- DECRYPT form -- */
let decryptedBlob = null, decryptedName = '';

document.getElementById('decryptForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById('decryptFile');
  const file = fileInput.files[0];
  if (!file) { alert('Please select an encrypted .des7 file.'); return; }

  const rawKey = document.getElementById('decryptKey').value;
  const key = validateKey(rawKey);
  if (!key) { alert('Key must be exactly 16 hex characters (0-9, A-F).'); return; }

  document.getElementById('decryptResult').hidden = true;
  document.getElementById('decryptError').hidden = true;

  const btn = document.getElementById('decryptSubmit');
  btn.disabled = true;
  btn.textContent = 'Decrypting...';

  try {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('key', key);

    const res = await fetch(`${API_BASE}/decrypt`, {
      method: 'POST',
      body: formData,
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }

    decryptedBlob = await res.blob();
    decryptedName = getFilenameFromResponse(res, 'decrypted_file');

    document.getElementById('decryptResultDetail').textContent =
      decryptedName + ' - ' + formatBytes(decryptedBlob.size);
    document.getElementById('decryptResult').hidden = false;

    downloadBlob(decryptedBlob, decryptedName);

  } catch (err) {
    document.getElementById('decryptErrorDetail').textContent = err.message;
    document.getElementById('decryptError').hidden = false;
  } finally {
    btn.disabled = false;
    btn.textContent = 'Decrypt and Download';
  }
});

document.getElementById('decryptDownloadBtn').addEventListener('click', () => {
  if (decryptedBlob) downloadBlob(decryptedBlob, decryptedName);
});
