import requests

class Macro_Api_Caller:
  """Methods for dealing with the api"""
  
  def serialize(name, ingredients):
    return {
      'title': name,
      'ingr' : ingredients
    }  

  def get_Data(self, name, ingr):
    to_send_data = self.serialize(name, ingr)
    api_data = requests.post("https://api.edamam.com/api/nutrition-details?app_id=0720c12f&app_key=2536f33f4e60d575d9e90d9c8012fe87", json = to_send_data)
    print(api_data.json())
    return api_data.json()

