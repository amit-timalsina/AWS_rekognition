import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)

    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
        session_token = line[4]

photo = 'founders.jpg'  # convert into base64 byte structure

client = boto3.client('rekognition',
                        aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key, aws_session_token = 'FwoGZXIvYXdzEHQaDO3LZvtBiNpX4asTnSLZAcFmsf9V7jgFCt8siES0pQa7mx7zMHRHUEIWSjkmrC4K4OABvOf8P121mGT4/9I8JNlwy5l7wINE4GCqWzIh0DdZkxLBAt6bMC4qXy858F5pGP5EEHRWDQgwTMOYeyavAIpuAorEhY6qpKC0wfzIMdrD804ZXgvzgmZUrhZX+biPADLFfKPwpcJyYU8cSGhCSLaqFQXxjcj7Etw5/dG6w2b/z4syegLEySz1Z4/HxtxceppDRf0RP5a/AlsYsylGlJ+rU/RepeoXU3yynUZn3GTmN5vq/mAyViso+Y3c+wUyLfI/J5fpc3ai3zt4eB4xSo6H28hSuJJu+1HIUSw/nb3iP8Ze+b67O/eokgLNiA==', region_name='us-east-1')


with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

# response = client.detect_labels(
#     Image = {
#         'S3Object': {
#             'Bucket': 'amitaiml',
#             'Name': 'ys logo.png'
#         }
#     },

#     MaxLabels = 2,
#     MinConfidence=50
# ) 

# response1 = client.detect_moderation_labels(
#     Image={
#         'Bytes': source_bytes
#     },
#     MinConfidence=95
# )
response2 = client.detect_faces(
    Image={
        # 'S3Object' : {
        #     'Bucket' :  'amitaiml',
        #     'Name' : '0.jpg'
        # }
        'Bytes' : source_bytes
    },
    Attributes=['ALL']
)
# print(response2)
i=0
for face in response2['FaceDetails']:
    i = i+1
    highest = str('')
    a = 50
    print('Person ' + str(i))
    print('The person in detected face is ' + str(face['Gender']['Value']) + '\n')
    print('The age of person in detected face is in between ' + str(face['AgeRange']['Low'])+ ' and ' + str(face['AgeRange']['High']) + '\n')
    for emotion in face['Emotions']:
        if(a < emotion['Confidence']):
            highest = str(emotion['Type'])
            a = emotion['Confidence'] 
    print('The person in detected face is ' + str(highest) + ' with confidence of ' + str(a) + '\n')
    Sunglass = str(face['Sunglasses']['Value'])

    if Sunglass == 'True':
        print('The detected face is wearing sunglasses\n')
    else:
        print('The detected face is wearing sunglasses\n')

    Beard = str(face['Beard']['Value'])

    if Beard == 'True':
        print('The detected face has beard\n')
    else:
        print("The detected face doesn't have beard\n\n")
































# import boto3
# import base64
# import json
# import os

# rekognition_client = boto3.client('rekognition')

# file = open('amit.jpg', 'rb').read()

# response = rekognition_client.detect_faces(
#     Image = {
#         'Bytes' : file
#     },
#     Attributes = ['ALL']
# )
# for face in response['FaceDetails']:
#     print('Here are the other attributes:')
#     print(json.dumps(face, indent=4, sort_keys=True))