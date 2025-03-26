FROM nvidia/cuda:12.3.1-runtime-ubuntu22.04

RUN apt update && apt install -y \
    python3 python3-pip ffmpeg nginx curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
