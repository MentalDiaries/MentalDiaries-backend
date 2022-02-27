from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Entry, FinalRecordID
from .serializers import EntryGetSerializer
import pickle
from tqdm import tqdm
import neattext.functions as nfx
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import os

def clean_text(text):
        text_length=[]
        cleaned_text=[]
        for sent in tqdm(text):
            sent=sent.lower()
            sent=nfx.remove_special_characters(sent)
            sent=nfx.remove_stopwords(sent)
            text_length.append(len(sent.split()))
            cleaned_text.append(sent)
        return cleaned_text,text_length


class EntryView(APIView):

    permission_classes = (IsAuthenticated, )
    
    
    def get(self, request):
        user_name = request.query_params.get('username')
        user_obj = User.objects.get(username=user_name)
        entries = Entry.objects.filter(user=user_obj)
        entry_serializer = EntryGetSerializer(entries, many=True)

        return Response(entry_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        entry = request.data['entry']
        entry_title = request.data['entry_title']
        a_clean,a_length = clean_text([entry_title + "\n" + entry])
        tokenizer = Tokenizer()
        a_clean_seq=a_clean.split()
        a_clean_pad=pad_sequences(a_clean_seq,maxlen=50)
        new_model = tf.keras.models.load_model('final_model.h5')

        print(a_clean_pad)
        result = new_model.predict(a_clean_pad)
        print(result)
        user_name = request.data['username']
        user = User.objects.get(username=user_name)
        final_record_id = FinalRecordID.objects.filter(user=user)
        if final_record_id.exists():
            record = FinalRecordID.objects.get(user=user)
            entry_id = record.final_id + 1
            record.final_id = entry_id
            record.save()
        else:
            entry_id = 1
            FinalRecordID.objects.create(user=user, final_id=entry_id)
        Entry.objects.create(user=user, entry=entry, entry_id=entry_id, entry_title=entry_title)
        return Response({'Status': 'Success'}, status=status.HTTP_201_CREATED)