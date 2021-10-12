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
    dpkg -i "/tmp/code-server_${VERSION}_$ARCH.deb"
    rm "/tmp/code-server_${VERSION}_$ARCH.deb"

USER coder
