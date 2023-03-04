from typing import Iterable
from ..rustplus_proto import AppCameraRays, AppCameraInfo, AppCameraInput, Vector2
from ...structures import Vector


class CameraManager:

    def __init__(self, rust_socket, cam_id, cam_info_message) -> None:
        self.rust_socket = rust_socket
        self._cam_id = cam_id
        self._last_packet: AppCameraRays = None
        self._cam_info_message: AppCameraInfo = cam_info_message

    def set_packet(self, packet):
        self._last_packet = packet

    def get_frame(self):
        if self._last_packet is None:
            return None

        return self._last_packet

    def can_move(self, control_type: int) -> bool:
        return self._cam_info_message.controlFlags & control_type == control_type

    async def clear_movement(self) -> None:
        await self.send_combined_movement()

    async def send_actions(self, actions: Iterable[int]) -> None:
        await self.send_combined_movement(actions)

    async def send_mouse_movement(self, mouse_delta: Vector) -> None:
        await self.send_combined_movement(joystick_vector=mouse_delta)

    async def send_combined_movement(self, movements: Iterable[int] = None, joystick_vector: Vector = None) -> None:

        if joystick_vector is None:
            joystick_vector = Vector()

        if movements is None:
            movements = []

        value = 0
        for movement in movements:
            value = value | movement

        await self.rust_socket._handle_ratelimit(0.01)
        app_request = self.rust_socket._generate_protobuf()
        cam_input = AppCameraInput()

        cam_input.buttons = value
        vector = Vector2()
        vector.x = joystick_vector.x
        vector.y = joystick_vector.y
        cam_input.mouseDelta.CopyFrom(vector)
        app_request.cameraInput.CopyFrom(cam_input)

        await self.rust_socket.remote.send_message(app_request)
        self.rust_socket.remote.ignored_responses.append(app_request.seq)
