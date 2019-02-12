import cognitive_face as CF
import sys
import json
from watson_developer_cloud import VisualRecognitionV3

# keys ibm e azure
ibm_key = 'u-wtKNFlyFRyCLQbTqr05wBPeZ3H7h-ZuY3hCC3a1NSc'
azure_key = '8943a700f3ca47d7bdd126b59a27f2d9'

sys.path.append('./')

# ibm: detecta idade e sexo
visual_recognition = VisualRecognitionV3(
 '2018-03-19',
 iam_apikey=ibm_key)
with open('./foto.jpg', 'rb') as images_file:
	classes = visual_recognition.detect_faces(
	images_file,
	threshold='0.6',
	classifier_ids='default').get_result()
	print('==========IBM: detecta idade e sexo ============')
	print(json.dumps(classes, indent=2))
	print('================================================\n\n')
	
	
# azure localização da face
azure_key = '8943a700f3ca47d7bdd126b59a27f2d9'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(azure_key)

BASE_URL = 'https://centralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = './foto.jpg'
faces = CF.face.detect(img_url)
print('==============Azure: localizacao da face=============')
print(faces)
print('=====================================================')
