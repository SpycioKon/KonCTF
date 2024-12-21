FROM python:3.10-slim

ENV USER=user

# Cài đặt OpenSSH server và các gói cần thiết
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt các yêu cầu từ requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Tạo thư mục làm việc và sao chép ứng dụng vào /app
WORKDIR /app

RUN chmod 666 /etc/passwd && \
    chmod 755 /app

# Sao chép ứng dụng và thay đổi quyền sở hữu cho user
COPY --chown=$USER:$USER . /app

RUN useradd --no-log-init --create-home --shell /bin/bash $USER && \
    chown -R $USER:$USER /app

# Cấu hình SSH
RUN mkdir /var/run/sshd
RUN echo 'root:THIS3r34@#sgfh%%@#%Tg' | chpasswd 
USER $USER

EXPOSE 5000 22

# CMD khởi chạy cả SSH và ứng dụng Flask
CMD service ssh start && python main.py
