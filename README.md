# team-env

An example Coder workspace with a lot of powerful features.

![Coder dashboard preview](preview.png)

## Applications

- Remote desktop from web browser (VNC + noVNC)
    - Insomnia 
- Podman (container management GUI)
- code-server (specific version)
- JupyterLab (via dev URL)

## Custom image

- Extends Coder's [VNC](https://github.com/cdr/enterprise-images/tree/main/images/vnc) image to include remote desktop support
- Custom image that installs applications, dev tools, and dependencies

## Workspace template

- See template in [.coder/coder.yaml](.coder/coder.yaml)