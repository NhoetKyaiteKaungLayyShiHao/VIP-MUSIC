FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN git clone https://github.com/Zenaku2050s/ZenakuXMusic/root/smdd
RUN rm -rf /root/smdd/.git
WORKDIR /root/smdd
RUN npm install || yarn install
EXPOSE 8080
CMD bash start
