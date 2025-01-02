import os
import pyaes

## Abrir o arquivo criptografado

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave de descriptografia

key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa o arquivo

decrypt_data = aes.descrypt(file_data)

# Remover o arquivo criptografado

os.remove(file_name)

# Criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.read(decrypt_data)
new_file.close()
