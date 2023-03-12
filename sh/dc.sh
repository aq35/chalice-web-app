#!/bin/bash
#!chmod +x dc.sh
#!./dc.sh 
echo "DockerComposeを操作したい"
echo "1 全てのコンテナ起動する"
echo "2 全てのコンテナビルドする(キャッシュクリア)"
read -p "(1,2)を選択してください。: " choice

case $choice in
  1)
    docker-compose up
    ;;
  2)
    docker-compose build --no-cache
    ;;
  *)
    echo "Invalid choice"
    ;;
esac