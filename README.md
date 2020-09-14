# facedetect-microservice


人脸检测微服务。模型基于开源的 CenterFace 构建， WebAPI 使用 flask。在预装 Docker 环境的条件下，build 一次就可以到处运行。

镜像大小为 

```bash
$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
v12                 latest              d7f8a497c34a        36 minutes ago      729MB
```


### 使用方法

1、安装 Docker 环境

```bash
$ docker version
Client: Docker Engine - Community
 Version:           19.03.12
 API version:       1.40
 Go version:        go1.13.10
 Git commit:        48a66213fe
 Built:             Mon Jun 22 15:45:36 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.12
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.10
  Git commit:       48a66213fe
  Built:            Mon Jun 22 15:44:07 2020
  OS/Arch:          linux/amd64
  Experimental:     false
```

2、进入本项目目录下，创建镜像，镜像名估且叫 myimage

```bash
docker build -t myimage .
```

3、启动容器

```bash
docker run -p 5000:5000 myimage &
```
把宿主机的 5000 端口 映射到容器内部的 5000 端口。


4、测试容器

进入`files/centerface`，有一个`test.py`文件，供测试，需要安装`requests`

```bash
python test.py
# <Response [200]>
# {'result': [[[430.74, 57.97, 508.11, 147.98, 0.93], [452.08, 97.65, 482.94, 88.14, 475.44, 110.83, 466.38, 127.49, 493.09, 119.71]], [[179.58, 55.11, 248.31, 151.37, 0.91], [217.7, 93.27, 242.76, 95.81, 237.31, 112.59, 212.67, 127.32, 233.23, 129.81]], [[585.62, 38.75, 640.0, 137.49, 0.87], [595.39, 72.17, 615.8, 75.73, 596.25, 92.18, 593.25, 109.34, 610.49, 111.65]]]}
```

至此，人脸检测微服务完成！

### 参考链接

+ centerface: https://github.com/Star-Clouds/CenterFace
+ docker: https://vuepress.mirror.docker-practice.com