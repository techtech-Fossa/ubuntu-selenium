FROM ubuntu:22.04

SHELL ["/bin/bash", "-l", "-c"]
RUN apt-get -y update && apt-get install -y sudo

RUN sudo apt-get -y update --fix-missing
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y python3-pip

RUN sudo apt install -y locales-all
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN echo "root:root" | chpasswd

# 各環境変数を設定
ENV USER user1

# 一般ユーザーアカウントを追加
RUN useradd -m ${USER} -s /bin/bash
RUN usermod -d /home/${USER} ${USER}
# 一般ユーザーにsudo権限を付与
RUN gpasswd -a ${USER} sudo
# 一般ユーザーのパスワード設定
RUN echo "${USER}:${USER}" | chpasswd

COPY ./sample/ /home/${USER}/sample/

CMD ["/bin/bash"]

