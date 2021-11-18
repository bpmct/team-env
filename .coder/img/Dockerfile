FROM codercom/enterprise-vnc:ubuntu

USER root

# Move the VNC configure script
RUN mv /coder/configure /coder/configure-vnc

# Copy /coder/ folder (configure and applications)
COPY ["./coder", "/coder"]

# Give Coder user permissions to applications folder
RUN chown -R coder /coder/apps

# Install Insomnia
RUN wget -O wget -O /tmp/insomnia.deb https://github.com/Kong/insomnia/releases/download/core%402021.5.3/Insomnia.Core-2021.5.3.deb && \
    dpkg -i /tmp/insomnia.deb && \
    rm /tmp/insomnia.deb

# Install code-server
ARG VERSION=3.12.0
ARG ARCH=amd64
RUN curl -L "https://github.com/cdr/code-server/releases/download/v$VERSION/code-server_${VERSION}_$ARCH.deb" -o \
    "/tmp/code-server_${VERSION}_$ARCH.deb" && \
    dpkg -i "/tmp/code-server_${VERSION}_$ARCH.deb" && \
    rm "/tmp/code-server_${VERSION}_$ARCH.deb"

# Install xdotool (for desktop apps)
RUN sudo apt-get install -y xdotool

# Install JupyterLab
RUN pip3 install jupyter-core==4.7.1 && \
    pip3 install jupyterlab

# Install WebStorm
# Install webstorm.
RUN mkdir -p /opt/webstorm
RUN curl -L "https://download.jetbrains.com/product?code=WS&latest&distribution=linux" | tar -C /opt/webstorm --strip-components 1 -xzvf -

# Add a binary to the PATH that points to the webstorm startup script.
RUN ln -s /opt/webstorm/bin/webstorm.sh /usr/bin/webstorm

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nodejs

# Install Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y yarn

USER coder
