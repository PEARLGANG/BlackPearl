FROM drmechanic/blackpearl:1.0

RUN git clone https://github.com/PEARLGANG/BlackPearl /root/pearl

RUN mkdir /root/pearl/bin/
WORKDIR /root/pearl/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["bash","start.sh"]
