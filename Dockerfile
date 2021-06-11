FROM python:3.6 
MAINTAINER Fei
WORKDIR /demo
COPY demo_code.py /demo/demo_code.py
COPY compile_intermediate.sh /demo/compile_intermediate.sh
ENTRYPOINT ["sh","/demo/compile_intermediate.sh"]
