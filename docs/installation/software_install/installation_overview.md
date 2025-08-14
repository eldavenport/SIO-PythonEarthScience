# SIO Software Workshop Installation Guide

It seems like a lot, but the following tools are necessary for collaborating on open source software, working on remote servers, and developing in Python! We hope you can use this workshop as an opportunity to get your development environment working seamlessly so that you have a smooth experience going forward. We will do our live coding and examples in VSCode, you can use another code-editor if you like but you may miss out of some of the nicer VSCode features. VSCode is lightweight and widely used, so we recommend familiarizing yourself with it either way.

**If you are starting from scratch, please install in the following order:**

    1) unix-shell/bash (Only Windows users will need to install unix-shell/bash. Mac and Linux users begin with Git installation.)
    2) Git 
    3) Python/Conda 
    4) VSCode

If you already have some of the elements installed, just follow the overall order for whatever you need. 

## All users

1) A quick note about the unix shell and bash. MacOS and Linux will already have a Unix-shell (i.e. a terminal) application with bash installed. Windows does not have this and the Windows Terminal/Powershell application will _not_ work. If your chosen terminal application is not unix and does not use bash as the scripting language, then you will not be able to use the commands we teach in our lesson plan. 

2) We highly recommend that Windows users use Windows Subsystem for Linux (WSL) for unix-shell/bash unless their Windows version is too old. This will make for a smooth experience with Git, Python, and conda. In particular, OneDrive does not play well with certain software like conda and Git, so WSL will make your life much easier. It is important that you first install WSL (this is your unix shell/bash installation), and then you install the rest of the tools to the Linux subsystem.

3) [ChatGPT](https://chatgpt.com/) is very good at solving installation problems. Tip: provide some context for what it is you are trying to accomplish in addition to a screen shot or description of the error you are running into. 

If you run into issues and want to read additional/alternative instructions, they can be found [here](https://carpentries.github.io/workshop-template/install_instructions/).