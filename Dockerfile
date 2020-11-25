  
FROM PEARLGANG/BlackPearl:latest

RUN git clone https://github.com/PEARLGANG/BlackPearl /root/pearl

WORKDIR /root/pearl

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","pearl"]
