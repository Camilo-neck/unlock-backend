FROM python:3.12.1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

# ENV MONGO_URI="mongodb://host.docker.internal:27017/"
ENV SUPABASE_URL="https://vkduiueevhxmjujorjry.supabase.co"
ENV SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrZHVpdWVldmh4bWp1am9yanJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM5MzUwMDgsImV4cCI6MjAzOTUxMTAwOH0.3ff9Gz8FDGLvEk6kq0q85Rky9VWl4OcPDx2nrQA7Olo"
ENV SUPABASE_DB_PASSWORD="4i6u4IqnfwnHquww"
ENV SUPABASE_SERVICE_ROLE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZrZHVpdWVldmh4bWp1am9yanJ5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMzkzNTAwOCwiZXhwIjoyMDM5NTExMDA4fQ.Y84ZtWal1IMv0cCZwGokjFTT1QJ9tWyPDRv8SRXLLWg"

# CMD /bin/sleep 180 && python3 ./app/main.py
CMD ["python", "main.py"]