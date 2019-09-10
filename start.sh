#!/bin/bash
echo "Стартуем"
CURRENT_UID=$(id -u):$(id -g) TEST=$1 docker-compose up --build pytest
CURRENT_UID=$(id -u):$(id -g) docker-compose up -d allure
echo "Генерируем отчёт"
sleep 3
curl --max-time 10 \
     --retry 5 \
     --retry-delay 0 \
     --retry-max-time 60 -X GET "http://127.0.0.1:5050/generate-report" -H  "accept: */*"
rm -rf tests/__pycache__
