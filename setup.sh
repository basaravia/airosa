mkdir -p ~/.streamlit/

echo "[general]
email = "info@sunplenatech.com"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml