FROM nvcr.io/nvidia/cuda:11.4.2-cudnn8-runtime-ubuntu20.04

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \
 && DEBIAN_FRONTEND=noninteractive apt-get -qqy install \
        python3-pip \
        ffmpeg \
        git \
        less \
        nano \
        libsm6 \
        libxext6 \
        libxrender-dev \
        curl &&\
     rm -rf /var/lib/apt/lists/*


RUN curl -o ~/miniconda.sh -O  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda config --set always_yes yes --set changeps1 no && conda update -q conda 
RUN conda install pytorch torchvision cudatoolkit=10.1 -c pytorch


# Install face-alignment package
COPY . /workspace/
WORKDIR /workspace
RUN chmod -R a+w /workspace
RUN git clone https://github.com/1adrianb/face-alignment
RUN pip install -r requirements.txt