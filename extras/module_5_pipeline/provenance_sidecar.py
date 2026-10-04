"""Write a readable provenance record next to a frame Griptape Nodes saved (Griptape training, Module 5, Exercise 3).

    python provenance_sidecar.py path/to/BUS_010_0020_v001.png      # writes BUS_010_0020_v001.png.provenance.json

Griptape writes its record into every PNG it saves (text entries named gtn_...). This copies that record into a
JSON file a comper or a publish tool can open without Griptape: the workflow, the engine version, the node that
saved the frame and its settings. The packed graph (gtn_flow_commands) stays in the PNG; the JSON only says whether
it is there. Needs Python 3.9 or later and Pillow (the Griptape Nodes app's own Python has both). JPEG, video and audio files carry no gtn_ entries: the script says so.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError

GRAPH_KEY = "gtn_flow_commands"


def record(frame: Path) -> dict:
    try:
        with Image.open(frame) as im:
            info = {k: v for k, v in im.info.items() if isinstance(k, str) and k.startswith("gtn_")}
    except (UnidentifiedImageError, OSError):
        info = {}   # video, audio or anything Pillow cannot open carries no gtn_ entries
    if not info:
        return {"frame": frame.name, "griptape_record": None,
                "note": "No gtn_ entries: only PNGs saved by Griptape Nodes carry them."}
    params = {k.removeprefix("gtn_param_"): v for k, v in info.items() if k.startswith("gtn_param_")}
    return {
        "frame": frame.name,
        "saved_at": info.get("gtn_saved_at"),
        "workflow": info.get("gtn_workflow_name"),
        "workflow_modified": info.get("gtn_workflow_modified"),
        "engine_version": info.get("gtn_engine_version"),
        "flow": info.get("gtn_flow_name"),
        "node": info.get("gtn_node_name"),
        "parameters": params,
        "graph_in_png": GRAPH_KEY in info,
        "how_to_rebuild": "Drop the PNG on a Griptape Nodes canvas and choose Add Nodes from Workflow.",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    frame = Path(sys.argv[1])
    out = frame.with_name(frame.name + ".provenance.json")
    out.write_text(json.dumps(record(frame), indent=2, ensure_ascii=False), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
