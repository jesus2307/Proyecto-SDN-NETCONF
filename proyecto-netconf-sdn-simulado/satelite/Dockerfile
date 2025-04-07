FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server python3 python3-pip sudo && \
    pip3 install ncclient && \
    mkdir /var/run/sshd && \
    useradd -m admin && echo 'admin:admin' | chpasswd && \
    echo 'admin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 22

CMD ["/start.sh"]