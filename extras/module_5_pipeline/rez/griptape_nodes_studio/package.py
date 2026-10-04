# Griptape training, Module 5, Exercise 1: a starting sketch of a studio REZ package for Griptape Nodes.
#
# Written from the Griptape Nodes 0.100.0 / engine 0.103.0 source and the REZ docs. Adapt it to your studio's REZ
# setup and log every place where it does not fit: those are your findings.
#
# Two layers, the way studios wrap other pip-installed tools:
#   1. The engine itself, from PyPI:  rez-pip -i griptape-nodes==0.100.0 --python-version 3.12
#      (griptape-nodes 0.100.0 pins griptape-nodes-engine 0.103.0; both need Python >= 3.12, < 3.14)
#   2. This wrapper package: the studio's choices about where things live.
#
# Then:  rez-env griptape_nodes_studio -- gtn doctor      (health checks)
#        rez-env griptape_nodes_studio -- gtn engine      (the engine, as a process; the editor connects to it)

name = "griptape_nodes_studio"

version = "0.1.0"

description = "Griptape Nodes engine with this studio's paths, caches and config (training sketch)"

build_command = False   # nothing to build: install with "rez-build --install" from this folder

requires = [
    "griptape_nodes-0.100.0",   # the package rez-pip makes; the name it gives may differ: check with rez-search
    "python-3.12",
]


def commands():
    # Paths below are placeholders. On Windows use a mapped drive or a UNC path (//server/...): the engine
    # ignores an XDG_CONFIG_HOME that is not absolute and silently falls back to ~/.config.
    #
    # Where the engine keeps its user config (griptape_nodes/griptape_nodes_config.json AND its .env secrets file).
    # Keep it per user: a shared folder would share everyone's secrets. FINDING TO CHECK: per user, per machine?
    env.XDG_CONFIG_HOME = "{env.HOME}/.griptape_studio"

    # Every engine setting can also be set as GTN_CONFIG_<KEY>, and environment variables win over every file.
    env.GTN_CONFIG_WORKSPACE_DIRECTORY = "/studio/griptape/workspace"  # default is <launch folder>/GriptapeNodes

    # Model downloads: the engine never sets the Hugging Face cache, so set it here or every seat downloads its own.
    env.HF_HOME = "/studio/cache/huggingface"

    # Pipeline storage for Project paths. A Project's griptape-nodes-project.yml can use it:
    #   directories:
    #     outputs:
    #       path_macro: "{SHARED_DRIVE}/griptape/outputs"
    env.SHARED_DRIVE = "/studio/projects"

    # Secrets (GT_CLOUD_API_KEY, HF_TOKEN) do NOT belong in a package. The engine reads them from the
    # environment first, then <workspace>/.env, then <XDG_CONFIG_HOME>/griptape_nodes/.env.
