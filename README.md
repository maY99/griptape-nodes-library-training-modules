# Griptape Training Modules

Ready-made Griptape Nodes workflows for the Griptape training modules, one per module, each with the results of a
full run, so every picture and video already shows when you open it.

## Install

In Griptape Nodes: **Manage**, **Library Management**, **Add Library**, paste this repository's URL, then confirm.
The library lands in your workspace's `libraries` folder; keep that folder where Griptape put it, because the
workflows find their pictures and videos there.

Or download `griptape-nodes-library-training-modules.zip` from the latest release, unzip it into your workspace's `libraries` folder (it holds one folder,
`griptape-nodes-library-training-modules`; keep that name), then add it in **Library Management**.

## Use

**File**, **Open**, the template for your module. Read the **Read Me First** note, then follow the step boxes.
**Save** makes your own copy in your workspace; the template stays as it is. When you run a step, its new results go
into your own outputs folder.

Some steps run a model on your own graphics card; the amber **GPU** note above such a node says how much video
memory it needs. Models are not in this library: they download the first time a node uses them.

`extras/` holds files a module asks you to use outside Griptape (Module 5's pipeline files); its Read Me says where.

| Module | Template |
|---|---|
| 1 | Module 1: Installation & First Workflows |
| 2 | Module 2: Models Deep Dive |
| 4 | Module 4: Customising Griptape |
| 5 | Module 5: Pipeline Integration |
| 6 | Module 6: VFX Workflows & Nuke Integration |
| 7 | Module 7: Security, Administration & Scaling |
