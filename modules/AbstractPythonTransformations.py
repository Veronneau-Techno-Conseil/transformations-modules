from abc import abstractmethod
from typing import Dict
from contracts import Metadata


class AbstractColumnarTransformations(object):
    
    @abstractmethod
    def transform(json, instructions: Dict[str, object], metadata: list[Metadata]) -> any:
        pass
    
    @abstractmethod
    def configure(instructions: Dict[str, object], metadata: list[Metadata]) -> list[Metadata]:
        pass    


