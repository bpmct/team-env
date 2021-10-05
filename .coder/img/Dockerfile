FROM codercom/enterprise-vnc:ubuntu

USER root

# Move the VNC configure script
RUN mv /coder/configure /coder/configure-vnc

# Copy /coder/ folder (configure and applications)
COPY ["./coder", "/coder"]

# Give Coder user permissions to applications folder
RUN chown -R coder /coder/apps

USER coder
