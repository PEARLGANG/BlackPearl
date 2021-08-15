FROM drmechanic/blackpearl:1.0
RUN pip3 install --upgrade pip setuptools==57.4.0 && exit 0
RUN pip3 install --upgrade pip && exit 0
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache && exit 0
ENV PYTHONUNBUFFERED=1
RUN git clone https://github.com/PEARLGANG/BlackPearl /root/pearl

RUN mkdir /root/pearl/bin/
WORKDIR /root/pearl/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt && exit 0
CMD ["bash","start.sh"]
