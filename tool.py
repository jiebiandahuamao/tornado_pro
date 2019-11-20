import json
from datetime import date, datetime


class ComplexEncoder(json.JSONEncoder):
  def _default(self, obj):
    if isinstance(obj, datetime):
      return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
      return obj.strftime('%Y-%m-%d')
    else:
      return json.JSONEncoder.default(self, obj)

_json = ComplexEncoder()