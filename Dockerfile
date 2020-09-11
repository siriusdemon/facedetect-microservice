# 将官方 Python 运行时用作父镜像
FROM ubuntu:18.04
ENV LANG C.UTF-8

# 更换apt国内源（阿里源）
COPY ./files/sources.list /var/local/
COPY ./files/centerface /var/local/

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \ 
    && mv /var/local/sources.list /etc/apt/ \ 
    && apt-get -y clean \
    && apt-get -y update \
    # python 36
    # && apt-get -y install software-properties-common \
    && apt-get -y update  \
    && apt-get -y install python3.6 \
    && apt-get -y install python3-pip \
    # python dependences
    # && echo "nameserver 8.8.8.8" >> /etc/resolv.conf
    && apt-get -y install libsm6 libxrender-dev libxext-dev \
    && pip3 install -i https://pypi.douban.com/simple opencv-python==4.2.0.32 \
    && pip3 install -i https://pypi.douban.com/simple matplotlib flask
# ENTRYPOINT []

WORKDIR /var/local
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]