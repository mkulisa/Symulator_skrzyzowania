class SimulationError(Exception):
    """Bazowy wyjątek dla błędów w symulatorze skrzyżowania."""


class InvalidVehicleDataError(SimulationError):
    """Wyjątek rzucany przy niepoprawnych parametrach pojazdu."""


class InvalidDirectionError(SimulationError):
    """Wyjątek rzucany przy podaniu nieobsługiwanego kierunku ruchu."""