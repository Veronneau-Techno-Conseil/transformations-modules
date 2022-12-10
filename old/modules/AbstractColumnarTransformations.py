from abc import abstractmethod
from typing import Dict


class Metadata(object):
    FieldName: str
    FieldType: str
    Index: int


class AbstractColumnarTransformations(object):
    
    @abstractmethod
    def transform(df, instructions: Dict[str, object], metadata: list[Metadata]) -> any:
        pass
    
    @abstractmethod
    def configure(instructions: Dict[str, object], metadata: list[Metadata]) -> list[Metadata]:
        pass    


