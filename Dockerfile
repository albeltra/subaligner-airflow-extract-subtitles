FROM ubuntu

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update

RUN apt install -y python3 python3-pip git wget ffmpeg libsndfile-dev

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -O Miniconda3-latest-Linux-x86_64.sh &&\
    chmod +x Miniconda3-latest-Linux-x86_64.sh &&\
    bash Miniconda3-latest-Linux-x86_64.sh -b

RUN conda install -c conda-forge gxx

RUN pip install subaligner

RUN mkdir /scripts

COPY ./scripts/ /scripts/

WORKDIR /scripts

ENTRYPOINT ["python", "extract_subtitle.py"]
