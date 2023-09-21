def message_creator(text):
  responses = {
    'computadora': "Con mi computadora puedo programar usando Python",
    'celular': "En mi celular puedo aprender usando la app de Platzi",
    'cable': "¡Hay un cable en mi bota!"
  }
  if text.lower() in responses.keys():
    return responses[text]
  else:
    return "Artículo no encontrado"


text = "algo"
response = message_creator(text)
print(response)
