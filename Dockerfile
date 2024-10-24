FROM docker.arvancloud.ir/ultralytics/ultralytics:latest
LABEL authors="Safaei"

WORKDIR /app

RUN sed -i 's/archive.ubuntu.com/ubuntu.shatel.ir/g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

COPY . .

RUN pip install --no-cache-dir --index-url https://nexus.aiengines.ir/repository/pypi/simple -r requirements.txt

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
