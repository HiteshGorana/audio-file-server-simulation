# -*- coding: utf-8 -*-
# @Date    : 27-03-2021
# @Author  : Hitesh Gorana
# @Link    : None
# @Version : 0.0
import logging

from flask import Flask
from flask import request, Response, jsonify
from mongoengine.context_managers import switch_collection

from db import Podcast, Audiobook, Song

app = Flask(__name__)

status_400 = Response("The request is invalid: 400 bad request", status=400)
status_200 = Response("Action is successful: 200 OK", status=200)
status_500 = Response("Any error: 500 internal server error", status='500')


@app.route('/api/create', methods=["POST"])
def create():
    if request.method == "POST":
        metadata: dict = request.json
        _audio_file_type: str = metadata.get("audioFileType", None)
        _audio_data: dict = metadata.get("audioFileMetadata", None)
        audio_types: tuple = ('song', 'podcast', 'audiobook')
        if (not _audio_file_type) or (_audio_file_type not in audio_types) or (not _audio_data):
            return status_400 if not _audio_file_type else status_500
        elif _audio_file_type == audio_types[0]:
            # name : name of the song
            # seconds : Duration in number of seconds
            # Uploaded time: default
            _song = Song(ID=_audio_data.get('id'), name=_audio_data.get('name'),
                         seconds=_audio_data.get('duration_time'))
            crud = CRUD(data=_song, collection=Song, collection_name='song')
            response = crud.create
            return response
        elif _audio_file_type == audio_types[1]:
            # name : Name of the podcast
            # seconds : Duration in number of seconds
            # Uploaded time : default
            # host : Host
            # participants : Participants
            _participants = _audio_data.get('participants')
            cond_ = any([True if len(i) > 100 else False for i in _participants])
            if len(_participants) > 10 or cond_:
                return status_500
            else:
                _podcast = Podcast(ID=_audio_data.get('id'), name=_audio_data.get('name'),
                                   seconds=_audio_data.get('duration_time'),
                                   host=_audio_data.get('host'), participants=_participants)
                crud = CRUD(data=_podcast, collection=Podcast, collection_name='podcast')
                response = crud.create
                return response
        else:
            # name : Title of the audiobook
            # Author : Author of the title
            # Narrator : narrator
            # seconds : Duration in number of seconds
            # Uploaded time : Default
            _audiobook = Audiobook(ID=_audio_data.get('id'),
                                   name=_audio_data.get('name'),
                                   author=_audio_data.get('author'),
                                   narrator=_audio_data.get('narrator'),
                                   seconds=_audio_data.get('duration_time'))
            crud = CRUD(data=_audiobook, collection=Audiobook, collection_name='audiobook')
            response = crud.create
            return response
    return status_400


@app.route('/api/update/<audioFileType>/<audioFileID>', methods=["PUT"])
def update(audioFileType, audioFileID):
    if request.method == "PUT":
        metadata: dict = request.json
        _audio_data: dict = metadata.get("audioFileMetadata", None)
        audio_types: tuple = ('song', 'podcast', 'audiobook')
        if (not audioFileType) or (audioFileType not in audio_types) or (not _audio_data):
            return status_400 if not audioFileType else status_500
        elif audioFileType == audio_types[0]:
            # name : name of the song
            # seconds : Duration in number of seconds
            # Uploaded time: default
            _update_data = dict(ID=_audio_data.get('id'), name=_audio_data.get('name'),
                                seconds=_audio_data.get('duration_time'))
            crud = CRUD(data=_update_data, collection=Song, collection_name='song')
            response = crud.update(audioFileID)
            return response
        elif audioFileType == audio_types[1]:
            # name : Name of the podcast
            # seconds : Duration in number of seconds
            # Uploaded time : default
            # host : Host
            # participants : Participants
            _participants = _audio_data.get('participants')
            cond_ = any([True if len(i) > 100 else False for i in _participants])
            if len(_participants) > 10 or cond_:
                return status_500
            else:
                _podcast = dict(ID=_audio_data.get('id'), name=_audio_data.get('name'),
                                seconds=_audio_data.get('duration_time'),
                                host=_audio_data.get('host'), participants=_participants)
                crud = CRUD(data=_podcast, collection=Podcast, collection_name='podcast')
                response = crud.update(audioFileID)
                return response
        else:
            # name : Title of the audiobook
            # Author : Author of the title
            # Narrator : narrator
            # seconds : Duration in number of seconds
            # Uploaded time : Default
            _audiobook = dict(name=_audio_data.get('name'),
                              author=_audio_data.get('author'),
                              narrator=_audio_data.get('narrator'),
                              seconds=_audio_data.get('duration_time'))
            crud = CRUD(data=_audiobook, collection=Audiobook, collection_name='audiobook')
            response = crud.update(audioFileID)
            return response
    return status_400


@app.route('/api/delete/<audioFileType>/<audioFileID>', methods=["DELETE"])
def delete(audioFileType, audioFileID):
    if request.method == "DELETE":
        audio_types: tuple = ('song', 'podcast', 'audiobook')
        if (not audioFileType) or (audioFileType not in audio_types):
            return status_400 if not audioFileType else status_500
        elif audioFileType == audio_types[0]:
            # name : name of the song
            # seconds : Duration in number of seconds
            # Uploaded time: default
            crud = CRUD(data=None, collection=Song, collection_name='song')
            response = crud.delete(audioFileID)
            return response
        elif audioFileType == audio_types[1]:
            # name : Name of the podcast
            # seconds : Duration in number of seconds
            # Uploaded time : default
            # host : Host
            # participants : Participants
            crud = CRUD(data=None, collection=Podcast, collection_name='podcast')
            response = crud.delete(audioFileID)
            return response
        else:
            # name : Title of the audiobook
            # Author : Author of the title
            # Narrator : narrator
            # seconds : Duration in number of seconds
            # Uploaded time : Default
            crud = CRUD(data=None, collection=Audiobook, collection_name='audiobook')
            response = crud.delete(audioFileID)
            return response
    return status_400


@app.route('/api/get/<audioFileType>/<audioFileID>', methods=["GET"])
@app.route('/api/get/<audioFileType>', methods=["GET"])
def get(audioFileType, audioFileID=None):
    if request.method == "GET":
        if audioFileID:
            audio_types: tuple = ('song', 'podcast', 'audiobook')
            if (not audioFileType) or (audioFileType not in audio_types):
                return status_400 if not audioFileType else status_500
            elif audioFileType == audio_types[0]:
                # name : name of the song
                # seconds : Duration in number of seconds
                # Uploaded time: default
                crud = CRUD(data=None, collection=Song, collection_name='song')
                response = crud.read(audioFileID)
                return response
            elif audioFileType == audio_types[1]:
                # name : Name of the podcast
                # seconds : Duration in number of seconds
                # Uploaded time : default
                # host : Host
                # participants : Participants
                crud = CRUD(data=None, collection=Podcast, collection_name='podcast')
                response = crud.read(audioFileID)
                return response
            else:
                # name : Title of the audiobook
                # Author : Author of the title
                # Narrator : narrator
                # seconds : Duration in number of seconds
                # Uploaded time : Default
                crud = CRUD(data=None, collection=Audiobook, collection_name='audiobook')
                response = crud.read(audioFileID)
                return response
        else:
            audio_types: tuple = ('song', 'podcast', 'audiobook')
            if (not audioFileType) or (audioFileType not in audio_types):
                return status_400 if not audioFileType else status_500
            elif audioFileType == audio_types[0]:
                # name : name of the song
                # seconds : Duration in number of seconds
                # Uploaded time: default
                crud = CRUD(data=None, collection=Song, collection_name='song')
                response = crud.read(audioFileID, collection=True)
            elif audioFileType == audio_types[1]:
                # name : Name of the podcast
                # seconds : Duration in number of seconds
                # Uploaded time : default
                # host : Host
                # participants : Participants
                crud = CRUD(data=None, collection=Podcast, collection_name='podcast')
                response = crud.read(audioFileID, collection=True)
            else:
                # name : Title of the audiobook
                # Author : Author of the title
                # Narrator : narrator
                # seconds : Duration in number of seconds
                # Uploaded time : Default
                crud = CRUD(data=None, collection=Audiobook, collection_name='audiobook')
                response = crud.read(audioFileID, collection=True)
            return jsonify(response)
    return status_400


class CRUD:
    def __init__(self, data=None, collection=None, collection_name=None):
        self.data = data
        self.collection = collection
        self.collection_name = collection_name

    @property
    def create(self):
        try:
            with switch_collection(self.collection, self.collection_name) as _:
                self.data.save()
            return status_200
        except Exception as e:
            logging.exception(e)
            return status_500

    def update(self, audioFileID):
        try:
            with switch_collection(self.collection, self.collection_name) as _:
                self.collection.objects.get(ID=int(audioFileID)).update(**self.data)
            return status_200
        except Exception as e:
            logging.exception(e)
            return status_500

    def delete(self, audioFileID):
        try:
            with switch_collection(self.collection, self.collection_name) as _:
                self.collection.objects.get(ID=int(audioFileID)).delete()
            return status_200
        except Exception as e:
            logging.exception(e)
            return status_500

    def read(self, audioFileID, collection=False):
        try:
            if collection:
                response = []
                with switch_collection(self.collection, self.collection_name) as _:
                    for i in self.collection.objects.as_pymongo():
                        i.pop('_id')
                        i.pop('_cls')
                        response.append(i)
                return response
            else:
                with switch_collection(self.collection, self.collection_name) as _:
                    response = self.collection.objects(ID=audioFileID).as_pymongo()[0]
                    response.pop('_id')
                    response.pop('_cls')
                return jsonify(response)
        except Exception as e:
            logging.exception(e)
            return status_500


if __name__ == '__main__':
    app.run(debug=True)
