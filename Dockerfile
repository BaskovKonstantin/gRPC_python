FROM python:3.9

WORKDIR /app

# Установка зависимостей
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Копирование файлов проекта в образ
COPY example.proto .
COPY server.py .

# Компиляция .proto файла и установка генерированного кода
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto

EXPOSE 50051

CMD [ "python", "server.py" ]