FROM drmechanic/blackpearl:latest

RUN mkdir /pearl && chmod 777 /pearl
ENV PATH="/pearl/bin:$PATH"
WORKDIR /pearl

RUN git clone https://github.com/PEARLGANG/BlackPearl -b master /pearl

#transfer

RUN curl -sL https://git.io/file-transfer | sh

#
# Finalization
#
CMD ["python3","-m","pearl"]
