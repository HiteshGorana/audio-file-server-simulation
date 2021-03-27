`audio file server`

---


```text
create
API : http://127.0.0.1:5000/api/create
request type :  POST
```
`song`
```json
{
    "audioFileType": "song",
    "audioFileMetadata": {
        "id": 1,
        "duration_time": 102,
        "name": "Sia Cheap Thrills"
    }
}
```
```
Action is successful: 200 OK
```
`podcast`
```json

{
    "audioFileType": "podcast",
    "audioFileMetadata": {
        "id": 2,
        "duration_time": 102,
        "name": "The Daily",
        "host": "Michael Barbaro",
        "participants": ["A Nursing Home’s First Day Out of Lockdown", "The State of Vaccinations"]
    }
}
```
```Action is successful: 200 OK```

`audiobook`
```json

{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
        "id": 3,
        "duration_time": 102,
        "name": "Atomic Habits",
        "author":"James Clear",
        "narrator":"James Clear"
    }
}
```
```Action is successful: 200 OK```

```text
Create API
API : http://127.0.0.1:5000/api/update/<audioFileType>/<audioFileID>
audioFileType:audiobook
audioFileID:3
request type :  PUT
```
```json
{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
        "id": 3,
        "duration_time": 243,
        "name": "Atomic Habits changed",
        "author":"James Clear changed",
        "narrator":"James Clear  changed"
    }
}
```
```Action is successful: 200 OK```

```text
Delete API
API : /api/delete/<audioFileType>/<audioFileID>
audioFileType:audiobook
audioFileID:3
request type :  DELETE
```

```Action is successful: 200 OK```

```text
Get API
API-1 : /api/get/<audioFileType>/<audioFileID>
API-2 : /api/get/<audioFileType>
request type :  GET
```
API-1
```json
{
    "ID": 3,
    "author": "James Clear changed",
    "name": "Atomic Habits changed",
    "narrator": "James Clear  changed",
    "seconds": 243,
    "uploaded_time": "Sat, 27 Mar 2021 19:02:22 GMT"
}
```
API-2
```json
[
    {
        "ID": 1,
        "author": "James Clear changed",
        "name": "Atomic Habits changed",
        "narrator": "James Clear  changed",
        "seconds": 243,
        "uploaded_time": "Sat, 27 Mar 2021 19:03:31 GMT"
    },
    {
        "ID": 2,
        "author": "James Clear changed",
        "name": "Atomic Habits changed",
        "narrator": "James Clear  changed",
        "seconds": 243,
        "uploaded_time": "Sat, 27 Mar 2021 19:03:35 GMT"
    },
    {
        "ID": 3,
        "author": "James Clear changed",
        "name": "Atomic Habits changed",
        "narrator": "James Clear  changed",
        "seconds": 243,
        "uploaded_time": "Sat, 27 Mar 2021 19:03:38 GMT"
    }
]
```

```text
SOFTWARE USED :

Postman v8.0.7 : FOR testing APIs
Python : 3.8
MongoDB Compass Version 1.25.0

install python-3.8 (Anaconda)
pip install -r requirements.txt
```

