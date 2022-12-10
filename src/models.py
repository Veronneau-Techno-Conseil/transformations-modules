# example data contract
import json
from typing import Any

from helper import dict_del_or_none


class FieldMetadata(object):

    def __init__(self, field_name: str, field_type: str) -> None:
        self.field_name = field_name
        self.field_type = field_type

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return FieldMetadata(json_dct["FieldName"], json_dct["FieldType"])

    def to_json(self):
        return {
            "FieldName": self.field_name,
            "FieldType": self.field_type
        }
    
    def clone(self):
        return FieldMetadata(self.field_name, self.field_type)


class RemoveColumnCommand(object):
    def __init__(self, column_name: str):
        self.column_name = column_name

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return RemoveColumnCommand(json_dct["columnName"])

    def to_json(self):
        return {
            "columnName": self.column_name
        }


class RenameColumnCommand(object):
    def __init__(self, source_name: str, target_name: str) -> None:
        self.source_name = source_name
        self.target_name = target_name

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return RenameColumnCommand(json_dct["sourceName"], json_dct["targetName"])

    def to_json(self):
        return {
            "sourceName": self.source_name,
            "targetName": self.target_name
        }


class HashColumnCommand(object):
    def __init__(self, source_column: str, target_column: str) -> None:
        self.source_column = source_column
        self.target_column = target_column

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return HashColumnCommand(json_dct["sourceColumn"], json_dct["targetColumn"])

    def to_json(self):
        return {
            "sourceColumn": self.source_column,
            "targetColumn": self.target_column
        }


class Instructions(object):
    def __init__(self, *,
                 remove_columns: list[RemoveColumnCommand],
                 rename_columns: list[RenameColumnCommand],
                 hash_columns: list[HashColumnCommand]):
        self.remove_columns = remove_columns
        self.rename_columns = rename_columns
        self.hash_columns = hash_columns

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return Instructions(remove_columns=dict_del_or_none(json_dct, "removeColumns", lambda v: [RemoveColumnCommand.from_json(x) for x in v]),
                            rename_columns=dict_del_or_none(json_dct, "renameColumns", lambda v: [RenameColumnCommand.from_json(x) for x in v]),
                            hash_columns=dict_del_or_none(json_dct, "hashColumns", lambda v: [HashColumnCommand.from_json(x) for x in v]))

    def to_json(self):
        return {
            "removeColums": [x.to_json() for x in self.remove_columns],
            "renameColumns": [x.to_json() for x in self.rename_columns],
            "hashColumns": [x.to_json() for x in self.hash_columns]
        }


class Configuration(object):
    def __init__(self, *, field_metadata: list[FieldMetadata], instructions: Instructions) -> None:
        self.field_metadata = field_metadata
        self.instructions = instructions
    
    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return Configuration(instructions=Instructions.from_json(json_dct["instructions"]),
                             field_metadata=[FieldMetadata.from_json(x) for x in json_dct["fieldMetadata"]])

    def to_json(self):
        return {
            "instructions": self.instructions.to_json(),
            "fieldMetadata": [x.to_json() for x in self.field_metadata]
        }


class PropertyRelationship(object):
    def __init__(self, *, origin: str, target: str) -> None:
        self.origin = origin
        self.target = target

    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return PropertyRelationship(origin=json_dct["origin"],
                                    target=json_dct["target"])

    def to_json(self):
        return {
            "origin": self.origin,
            "target": self.target
        }


class ConfigurationResult(object):
    def __init__(self, *, field_metadata: list[FieldMetadata], property_relationships: list[PropertyRelationship]) -> None:
        self.field_metadata = field_metadata
        self.property_relationships = property_relationships
    
    @staticmethod
    def from_json(json_dct: dict[str, object]):
        return ConfigurationResult(field_metadata=[FieldMetadata.from_json(x) for x in json_dct["fieldMetadata"]],
                                   property_relationships=[PropertyRelationship.from_json(x) for x in json_dct["propertyRelationships"]])

    def to_json(self):
        return {
            "fieldMetadata": [x.to_json() for x in self.field_metadata],
            "propertyRelationships": [x.to_json() for x in self.property_relationships]
        }