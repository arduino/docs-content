FROM node:20-bullseye-slim

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    fontconfig \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libgcc1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    lsb-release \
    xdg-utils \
    chromium \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/scripts/datasheet-rendering

COPY . .

RUN mkdir -p /usr/share/fonts/truetype/custom && \
    cp ./styles/fonts/*.ttf /usr/share/fonts/truetype/custom/ 2>/dev/null || true && \
    fc-cache -f -v

ENV PUPPETEER_SKIP_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
ENV CI=true

RUN npm install

ENTRYPOINT ["npx", "datasheet-renderer", "config.json"]