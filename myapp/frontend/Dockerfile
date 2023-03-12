# ベースイメージの指定
FROM node:14-alpine

# コンテナ内で作業するディレクトリの指定
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY package*.json ./
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションをビルド
RUN npm run build

# ポートの指定
EXPOSE 3000

# アプリケーションの起動
CMD ["npm", "run", "dev"]