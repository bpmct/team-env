# coder-project-template

An example template for building a custom [Coder](https://coder.com/docs) workspace around a project. This includes:

* Coder workspace template - `.coder/coder.yaml`
* Custom image for Coder - `.coder/img`
* GitHub Actions CI for building the custom image - `.github/workflows/build-image.yaml`
* Sample "app code" in `src/`

## Set up

1. Use this template to [create your own repository](https://github.com/bpmct/coder-project-template/generate)
1. Add [secrets](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) to the repository with your [Docker Hub](https://hub.docker.com/) account details:

        DOCKERHUB_USERNAME (your username for Docker Hub)
        DOCKERHUB_TOKEN (your password or token)

1. Rename `username/projectname` in [.coder/coder.yaml](https://github.com/bpmct/coder-project-template/blob/main/.coder/coder.yaml#L5) and `projectname` in [.github.workflows/build-image.yaml](https://github.com/bpmct/coder-project-template/blob/main/.github/workflows/build-image.yaml#L32). Username should be the same as your DOCKERHUB_USERNAME you set above.

1. Push to `main` (to build the image).

1. Add the image into Coder. (repository: your value for `username/projectname` tag: `latest`)

1. If you haven't already, enable Workspace Templates under Manage -> Admin -> Templates

1. You're done! 🎉 Create a new workspace from this template in the Ui, or create an [embeddable button/link](https://coder.com/docs/admin/templates) for others to clone.

    - The "project repository" can also be this repository if you want the workspace to be defined in the same place. I often do this.

---

To modify the image or workspace definition, simply push to `main` . GitHub actions will re-build the image and Coder will notify developers when an update is available for their workspace.

Check out this video for an overview on how this works: https://youtu.be/BrZhBJtjkYk?t=104
