FROM ubuntu

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update

RUN apt install -y python3 python3-pip git wget ffmpeg libsndfile-dev

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3-latest-Linux-x86_64.sh &&\
    chmod +x Miniconda3-latest-Linux-x86_64.sh &&\
    bash Miniconda3-latest-Linux-x86_64.sh -b

RUN conda install -c conda-forge gxx  

RUN mkdir /scripts

COPY ./scripts/ /scripts/

RUN pip install subaligner

WORKDIR /scripts

ENTRYPOINT ["python", "/extract_subtitle.py"]
