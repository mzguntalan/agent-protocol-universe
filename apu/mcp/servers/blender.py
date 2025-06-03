from apu.socket.utils import check_if_connection_can_be_made_by_simple_ping


def is_running() -> bool:
    return check_if_connection_can_be_made_by_simple_ping("localhost", 9876)
