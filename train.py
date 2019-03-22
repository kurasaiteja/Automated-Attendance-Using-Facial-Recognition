import cognitive_face as CF
from global_variables import personGroupId

BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
Key = '3450ac16772e40428ba787c62dd3eda4'
CF.Key.set(Key)

res = CF.person_group.train(personGroupId)
print res
