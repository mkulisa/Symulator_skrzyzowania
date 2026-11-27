from abc import ABC, abstractmethod

from src.exceptions import InvalidVehicleDataError,InvalidDirectionError
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, direction: str)-> None:
        if not vehicle_id or not vehicle_id.strip():
            raise InvalidVehicleDataError("Vehicle ID nie może być pusty.")
        if not direction or not direction.strip():
            raise InvalidDirectionError("Kierunek ruchu nie może być pusty.")
        
        self.vehicle_id = vehicle_id
        self.direction = direction.upper()
        self.waiting_time = 0  # Czas oczekiwania pojazdu w sekundach
        @property
        def waiting_time(self) -> int:
            return self._waiting_time
        def tick(self) -> None:
            """Zwiększa czas oczekiwania pojazdu o 1 sekundę."""
            self._waiting_time += 1
        @property
        @abstractmethod
        def priority(self) -> int:
            """Zwraca priorytet pojazdu. Wyższa wartość oznacza wyższy priorytet."""
        @property
        @abstractmethod
        def symbol(self) -> str:
            """Zwraca symbol reprezentujący pojazd na skrzyżowaniu."""
        def __str__(self) -> str:
            return F"[{self.symbol}:{self._vehicle_id} | czekanie: {self._wait_time}s]"
        

    def __repr__(self) -> str:
        return (
            F"{self.__class__.__name__}("
            F"vehicle_id={self.vehicle_id!r}, direction={self.direction!r})"
        )
