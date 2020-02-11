# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Decode Base64 to data"


class Input:
    BASE64 = "base64"
    ERRORS = "errors"
    

class Output:
    DATA = "data"
    

class DecodeInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "base64": {
      "type": "string",
      "title": "Base64",
      "displayType": "bytes",
      "description": "Data to decode",
      "format": "bytes",
      "order": 1
    },
    "errors": {
      "type": "string",
      "title": "Errors",
      "description": "How errors should be handled when decoding Base64",
      "default": "nothing",
      "enum": [
        "replace",
        "ignore",
        "nothing"
      ],
      "order": 2
    }
  },
  "required": [
    "base64"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DecodeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Decoded Data",
      "description": "Decoded data result",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)