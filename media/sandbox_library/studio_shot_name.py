"""Builds a standardized shot file name and folder path following the studio naming rule: every shot gets its own folder, and its files are named SHOW_SEQ_SHOT_task.ext, with the show in capitals, the sequence as three digits, and the shot as four digits."""

from typing import Any

from griptape_nodes.exe_types.core_types import ParameterMode
from griptape_nodes.exe_types.node_types import DataNode
from griptape_nodes.exe_types.param_types.parameter_string import ParameterString
from griptape_nodes.exe_types.param_types.parameter_int import ParameterInt


class StudioShotName(DataNode):
    def __init__(self, name: str, metadata: dict[Any, Any] | None = None) -> None:
        super().__init__(name, metadata)

        self.add_parameter(
            ParameterString(
                name="show",
                default_value="BUS",
                tooltip="Show code, e.g. BUS",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )
        self.add_parameter(
            ParameterInt(
                name="sequence",
                default_value=10,
                tooltip="Sequence number, e.g. 10",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )
        self.add_parameter(
            ParameterInt(
                name="shot",
                default_value=20,
                tooltip="Shot number, e.g. 20",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )
        self.add_parameter(
            ParameterString(
                name="task",
                default_value="comp",
                tooltip="Task name, e.g. comp",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )
        self.add_parameter(
            ParameterString(
                name="extension",
                default_value="png",
                tooltip="File extension without the dot, e.g. png",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )
        self.add_parameter(
            ParameterString(
                name="folder",
                default_value="module_4/exercise_1",
                tooltip="Base folder for the shot, e.g. module_4/exercise_1",
                allowed_modes={ParameterMode.INPUT, ParameterMode.PROPERTY},
            )
        )

        self.add_parameter(
            ParameterString(
                name="file_name",
                tooltip="Full folder/filename path following the studio naming rule.",
                allowed_modes={ParameterMode.OUTPUT},
            )
        )

    def process(self) -> None:
        show = self.get_parameter_value("show")
        sequence = self.get_parameter_value("sequence")
        shot = self.get_parameter_value("shot")
        task = self.get_parameter_value("task")
        extension = self.get_parameter_value("extension")
        folder = self.get_parameter_value("folder")

        if not show or not str(show).strip():
            msg = "StudioShotName: 'show' cannot be empty."
            raise ValueError(msg)

        show_upper = str(show).strip().upper()
        seq_str = f"{int(sequence):03d}"
        shot_str = f"{int(shot):04d}"

        shot_folder_name = f"{show_upper}_{seq_str}_{shot_str}"
        file_stem = f"{shot_folder_name}_{task}.{extension}"

        file_name = f"{folder}/{shot_folder_name}/{file_stem}"

        self.parameter_output_values["file_name"] = file_name