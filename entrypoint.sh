#!/bin/bash
set -e

# Starte EPG-Generator
python3 /app/api/epg.py &

# Starte API
python3 /app/api/app.py &

# Starte nginx
nginx -g 'daemon off;'
