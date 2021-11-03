# Python API
FastAPI 示例
 
## 依赖
### 离线安装依赖包
在fastapi-client和fastapi-server目录下执行  
```bash
    # 下载pip包
    $ docker run --rm --name pip_download -v $(pwd):/app -w /app python:3.8.9 pip3 download -d libs -r requirements.txt
    # 缓存编译依赖包
    $ docker run --rm --name pip_build -v $(pwd):/app -v $(pwd)/cache:/root/.cache -w /app python:3.8.9 pip3 install -r requirements.txt
    # 测试离线包
    $ docker run --rm --name pip_install -v $(pwd):/app -w /app python:3.8.9 pip3 install --no-index --find-links=libs -r requirements.txt
```

## 运行

### 运行单个程序
    编译镜像
    $ docker build -t pyapi .
    后台运行
    $ docker run -dp 8000:8000 pyapi
    前台运行
    $ docker run --rm -it -p 8000:8000 pyapi

### 启动所有程序
    $ docker-compose up