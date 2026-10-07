# Griptape Training Modules

Ready-made Griptape Nodes workflows for the Griptape training modules, one per module, each with the results of a
full run, so every picture and video already shows when you open it.

## Install

In Griptape Nodes: **Manage**, **Library Management**, **Add Library**, paste this repository's URL, then confirm.
The library lands in your workspace's `libraries` folder; keep that folder where Griptape put it, because the
workflows find their pictures and videos there. Then restart Griptape Nodes once: a newly added library's templates
show only after a restart.

Or download `griptape-nodes-library-training-modules.zip` from the latest release, unzip it into your workspace's `libraries` folder (it holds one folder,
`griptape-nodes-library-training-modules`; keep that name), then add it in **Library Management**.

## Use

**File**, **Open**, the template for your module. Every template comes with the results of a full run: each picture
and video shows as soon as it opens, with nothing to run. Read the **Read Me First** note, then follow the step boxes.
Your changes go into your own copy in your workspace; the template itself stays as it is. Running nodes yourself uses credits, and
their new results go into your own outputs folder.

Some steps run a model on your own graphics card; the amber **GPU** note above such a node says how much video
memory it needs. Models are not in this library: they download the first time a node uses them.

`extras/` holds files a module asks you to use outside Griptape (Module 5's pipeline files); Module 5's **Read Me
First** note says what to do with them.

| Module | Template |
|---|---|
| 1 | Module 1, 1 Sources |
| 1 | Module 1, 2 Exercise 1: Install and launch Griptape Nodes |
| 1 | Module 1, 3 Exercise 2: API vs local model |
| 1 | Module 1, 4 Exercise 3: Project basics |
| 2 | Module 2, 1 Sources |
| 2 | Module 2, 2 Exercise 1: Proxy vs local, same task |
| 2 | Module 2, 3 Exercise 2: Under the hood with Diffusers |
| 2 | Module 2, 4 Exercise 3: Chain generation and cleanup |
| 3 | Module 3, 1 Sources |
| 3 | Module 3, 2 Exercise 1: Iterative prompt refinement, by hand |
| 3 | Module 3, 3 Exercise 2: The agent picks the tool and the model |
| 4 | Module 4, 1 Sources |
| 4 | Module 4, 2 Exercise 1: One custom node or widget |
| 4 | Module 4, 3 Exercise 2: Package it into a library |
| 4 | Module 4, 4 Exercise 3: Make your Module 2 workflow reusable |
| 5 | Module 5, 1 Sources |
| 5 | Module 5, 2 Exercise 1: REZ configuration |
| 5 | Module 5, 3 Exercise 2: Headless execution |
| 5 | Module 5, 4 Exercise 3: Publish with provenance |
| 6 | Module 6, 1 Sources |
| 6 | Module 6, 2 Exercise 1: Make a shot that was never filmed |
| 6 | Module 6, 3 Exercise 2: Swap the car on a still |
| 6 | Module 6, 4 Exercise 3: Swap the car on video |
| 6 | Module 6, 5 Exercise 4: Swap a face on video |
| 6 | Module 6, 6 Exercise 5: Clean up a shot on video |
| 6 | Module 6, 7 Exercise 6: Extend the set on video |
| 6 | Module 6, 8 Exercise 7: Make a 3D model of the new car |
| 6 | Module 6, 9 Exercise 8: Turn the clean plate into a 360 panorama and a splat |
| 6 | Module 6, 10 Exercise 9: Finish the shot in Nuke |
| 6 | Module 6, 11 Exercise 10: Publish a workflow as a Nuke gizmo |
| 7 | Module 7, 1 Sources |
| 7 | Module 7, 2 Exercise 1: Read the topology |
| 7 | Module 7, 3 Exercise 2: Issue a seat |
| 7 | Module 7, 4 Exercise 3: Trace provenance |
