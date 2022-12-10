
import json
from models import Configuration, ConfigurationResult, FieldMetadata, PropertyRelationship

# configure is there for 2 things:
# 1- validate that a transformation is possible (verifying column names, data types etc)
# 2- Alter the metadata with the transformation logic to provide the final metadata representation
def configure(configuration: Configuration):
    if configuration.instructions is None:
        return configuration.field_metadata

    tgt_fm = [x.clone() for x in configuration.field_metadata]
    property_relationships: list[PropertyRelationship] = []
    
    if configuration.instructions.remove_columns is not None and len(configuration.instructions.remove_columns) > 0:
        # apply column removal logic to tgt_fm here
        print("replace this")

    # keep going with other types of transforms in instructions

    res = ConfigurationResult(field_metadata=tgt_fm, property_relationships=property_relationships)

    print(json.dumps(res.to_json(), ensure_ascii=False))
