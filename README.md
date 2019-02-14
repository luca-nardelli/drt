# DRT: Docker Repository Management Tool

**IMPORTANT: This tool is being actively developed and its interface is not stable at the moment**

This tool helps you to perform common tasks related to building, tagging and pushing docker images.

It requires at least Python 3.5.

As of now, the tool allows you to manage a single git repository that can host multiple docker images (with different tags/variants).

The repo has a fixed structure:
- drt.json
- logs
- images

The images folder contains all the docker images you want to build. In order to name images, the file system hierarchy is exploited.
Inside of the images subfolder, you can have as many folders as you want.
An image root is defined by the presence of a `drt-image.json` file, created by the relevant `drt` command (see below). The name of the folder containing this file will be used as the image name.

In order to define image tags, you can add *variants*. Variants actually hold the Dockerfile that is used to build the image.
Inside an image root the hierarchy of folders is important. Example:

- awesome-image-name
  - drt-image.json
  - 1.0
    - ...
    - Dockerfile
  - 1.1
    - ...
    - Dockerfile
    - minimal
      - ...
      - Dockerfile

With an image root structured this way, if you invoke `drt build` you will get the following images:

- awesome-image-name:1.0
- awesome-image-name:1.1
- awesome-image-name:1.1-minimal

Thanks to .dockerignore files, the build context does not automatically include all the children images when building parent images.

Drt also helps to push images to a common registry. When building images, drt will also prefix the reigstry to their name, so that they can be pushed to different registries (e.g. gitlab, dockerhub, etc...)

## Installation

Clone the repo, then run `python3 setup.py install` (sudo might be required).

## Usage

### Init a repository

```bash
drt init
```

### Add an image

From the `images` subfolder of the repo

```bash
drt add-image <image name>
```

### Add a variant

From inside an image root

```bash
drt add-variant <variant name>
```

### List all the images

```bash
drt ls
```

### Build

```bash
drt build
```

Its behavior depends on where you are in the filesystem:

- If you are inside an image folder (identified by the `drt-image.json` file) it will build that image only;
- If you are inside a variant folder (with a Dockerfile), it will build that variant only
- If you are inside the repo but not in any particular folder, it will build all the images contained in the repo

#### Image tagging

Each image is built with 2 tags. One is defined as above depending on the folder hierarchy inside the image root, another tag is the same one but prefixed with the registry information, so that it's ready for being pushed.

### Push

```bash
drt push
```

Its behavior with respect to which image(s) are pushed is the same as build