from .structures import *
from .remote.rustproto import *
from .remote.rustws import RustWsClient

class BaseRustSocket:

    def __init__(self, ip : str = None, port : str = None, steamid : int = None, playertoken : int = None, ratelimit_limit : int = 25, ratelimit_refill : int = 3) -> None:
        
        if ip is None:
            raise ValueError("Ip cannot be None")
        if port is None:
            raise ValueError("Port cannot be None")
        if steamid is None:
            raise ValueError("SteamID cannot be None")
        if playertoken is None:
            raise ValueError("PlayerToken cannot be None")

        self.ip = ip
        self.port = port
        self.steamid = steamid
        self.playertoken = playertoken
        self.seq = 1

        self.ws = RustWsClient(ip=self.ip, port=self.port, protocols=['http-only', 'chat'])
        self.ws.daemon = True
        self.ws.start_ratelimiter(ratelimit_limit, ratelimit_limit, 1, ratelimit_refill)

    def _handle_ratelimit(self, amount = 1) -> None:
        """
        Handles the ratelimit for a specific request
        """
        if not self.ws.ratelimiter.can_consume():
            raise Exception()

        self.ws.ratelimiter.consume()
    
    def _generate_protobuf(self) -> AppRequest:
        """
        Generates the empty AppRequest Message
        """

        app_request = AppRequest()
        app_request.seq = self.seq
        app_request.playerId = self.steamid
        app_request.playerToken = self.playertoken

        self.seq += 1

        return app_request

    async def connect(self) -> None:
        """
        Opens the connection to the Rust Server
        """
        try:
            self.ws.connect()
        except ConnectionRefusedError:
            raise Exception()

    async def close_connection(self) -> None:
        """
        Disconnects from the Rust Server
        """
        self.ws.close()
        self.ws.responses.clear()
    
    async def get_time(self) -> RustTime:
        """
        Gets the current in-game time from the server. Returns a RustTime object
        """
        pass