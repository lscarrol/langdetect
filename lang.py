"""
Benchmark to compare speed of different language detection models.

To add a new detector:
    1. import the required package
    2. create a detection function for detecion using that package
    3. add name to `names`
    4. add detection function to `detectors`
"""
import pandas as pd
import time
import os
import json
import tqdm

import pycld2 as cld2
import cld3
from lingua import Language, LanguageDetectorBuilder
from langdetect import detect as langdetect

SUMMARY = False # if false, benchmark headlines, otherwise summaries

# Create detectors

df = pd.read_csv('lang.csv')
df = df[df.Language != 'Malayalam']
df = df[df.Language != 'Hindi']
df = df[df.Language != 'Tamil']
df = df[df.Language != 'Kannada']
df = df[df.Language != 'Portugeese']
df = df[df.Language != 'Russian']
df = df[df.Language != 'Sweedish']
df = df[df.Language != 'Dutch']
df = df[df.Language != 'Arabic']
df = df[df.Language != 'Turkish']
df = df[df.Language != 'Danish']
df = df[df.Language != 'Greek']
df = df[df.Language != 'Italian']

encount = 0
encountdem = 0

frcount = 0
frcountdem = 0

spcount = 0
spcountdem = 0

gercount = 0
gercountdem = 0



def cld2_detect(text, langer):

    global encount
    global encountdem

    global frcount
    global frcountdem

    global spcount
    global spcountdem

    global gercount
    global gercountdem

    try:
        _, _, det = cld2.detect(text)
    except:
        return False
    lang = det[0][1]

    if langer == 'English':
        if lang == 'en':
            encount += 1
            encountdem += 1
        else:
            encountdem += 1

    if langer == 'French':
        if lang == 'fr':
            frcount += 1
            frcountdem += 1
        else:
            frcountdem += 1

    if langer == 'Spanish':
        if lang == 'es':
            spcount += 1
            spcountdem += 1
        else:
            spcountdem += 1

    if langer == 'German':
        if lang == 'de':
            gercount += 1
            gercountdem += 1
        else:
            gercountdem += 1
    return lang

def cld3_detect(text, langer):
    global encount
    global encountdem

    global frcount
    global frcountdem

    global spcount
    global spcountdem

    global gercount
    global gercountdem

    lang = cld3.get_language(text).language
    if langer == 'English':
        if lang == 'en':
            encount += 1
            encountdem += 1
        else:
            encountdem += 1

    if langer == 'French':
        if lang == 'fr':
            frcount += 1
            frcountdem += 1
        else:
            frcountdem += 1

    if langer == 'Spanish':
        if lang == 'es':
            spcount += 1
            spcountdem += 1
        else:
            spcountdem += 1

    if langer == 'German':
        if lang == 'de':
            gercount += 1
            gercountdem += 1
        else:
            gercountdem += 1
    return lang

languages = [Language.ENGLISH,
             Language.FRENCH,
             Language.GERMAN,
             Language.SPANISH,
             Language.CHINESE,
             Language.JAPANESE,
             Language.KOREAN]
lingua_detector = LanguageDetectorBuilder.from_languages(*languages).build()

def lingua_detect(text, langer):
    global encount
    global encountdem

    global frcount
    global frcountdem

    global spcount
    global spcountdem

    global gercount
    global gercountdem
    lang = lingua_detector.detect_language_of(text)
    if langer == 'English':
        if lang == Language.ENGLISH:
            encount += 1
            encountdem += 1
        else:
            encountdem += 1

    if langer == 'French':
        if lang == Language.FRENCH:
            frcount += 1
            frcountdem += 1
        else:
            frcountdem += 1

    if langer == 'Spanish':
        if lang == Language.SPANISH:
            spcount += 1
            spcountdem += 1
        else:
            spcountdem += 1

    if langer == 'German':
        if lang == Language.GERMAN:
            gercount += 1
            gercountdem += 1
        else:
            gercountdem += 1
    return lang

def langdetect_detect(text, langer):

    global encount
    global encountdem

    global frcount
    global frcountdem

    global spcount
    global spcountdem

    global gercount
    global gercountdem
    try:
        lang = langdetect(text)
    except:
        return "Null"
    if lang == None:
        return "Null"
    if langer == 'English':
        if lang == 'en':
            encount += 1
            encountdem += 1
        else:
            encountdem += 1

    if langer == 'French':
        if lang == 'fr':
            frcount += 1
            frcountdem += 1
        else:
            frcountdem += 1

    if langer == 'Spanish':
        if lang == 'es':
            spcount += 1
            spcountdem += 1
        else:
            spcountdem += 1

    if langer == 'German':
        if lang == 'de':
            gercount += 1
            gercountdem += 1
        else:
            gercountdem += 1
    return lang

df = df.reset_index()
for col in df:
    print(df[col].unique())
print(df)
print("////////////// TESTING ON KAGGLE DATASET //////////////\n")

print("////////////// TESTING CLD2 //////////////\n")
#start = time.time()
for index, row in df.iterrows():
    #story_s = time.perf_counter_ns()
    #story_time = time.perf_counter_ns() - story_s
    lang = row['Language']
    text = row['Text']
    print("----------DATA INDEX " + str(index) + " -------------\n")
    print("EXPECTED LANGUAGE: " + lang + "\n")
    print("CLD2 CLASSIFICATION: " + cld2_detect(text, lang) + "\n")

cld2_ratio_english = encount / encountdem
cld2_ratio_french = frcount / frcountdem
cld2_ratio_spanish = spcount / spcountdem
cld2_ratio_german = gercount / gercountdem
encount = 0
encountdem = 0

frcount = 0
frcountdem = 0

spcount = 0
spcountdem = 0

gercount = 0
gercountdem = 0


print("////////////// TESTING CLD3 //////////////\n")

for index, row in df.iterrows():
    lang = row['Language']
    text = row['Text']
    print("----------DATA INDEX " + str(index) + " -------------\n")
    print("EXPECTED LANGUAGE: " + lang + "\n")
    print("CLD3 CLSSIFICATION: " + cld3_detect(text, lang) + "\n")

cld3_ratio_english = encount / encountdem
cld3_ratio_french = frcount / frcountdem
cld3_ratio_spanish = spcount / spcountdem
cld3_ratio_german = gercount / gercountdem
encount = 0
encountdem = 0

frcount = 0
frcountdem = 0

spcount = 0
spcountdem = 0

gercount = 0
gercountdem = 0


print("////////////// TESTING LINGUA //////////////\n")

for index, row in df.iterrows():
    lang = row['Language']
    text = row['Text']
    print("----------DATA INDEX " + str(index) + " -------------\n")
    print("EXPECTED LANGUAGE: " + lang + "\n")
    print("LINGUA CLASSIFICATION: " + str(lingua_detect(text, lang))  + "\n")

lingua_ratio_english = encount / encountdem
lingua_ratio_french = frcount / frcountdem
lingua_ratio_spanish = spcount / spcountdem
lingua_ratio_german = gercount / gercountdem
encount = 0
encountdem = 0

frcount = 0
frcountdem = 0

spcount = 0
spcountdem = 0

gercount = 0
gercountdem = 0


print("////////////// TESTING LANGDETECT //////////////\n")

for index, row in df.iterrows():
    lang = row['Language']
    text = row['Text']
    print("----------DATA INDEX " + str(index) + " -------------" + "\n")
    print("EXPECTED LANGUAGE: " + lang + "\n")
    print("LANGDETECT CLASSIFICATION: " + langdetect_detect(text, lang) + "\n")

langdetect_ratio_english = encount / encountdem
langdetect_ratio_french = frcount / frcountdem
langdetect_ratio_spanish = spcount / spcountdem
langdetect_ratio_german = gercount / gercountdem
encount = 0
encountdem = 0

frcount = 0
frcountdem = 0

spcount = 0
spcountdem = 0

gercount = 0
gercountdem = 0

print("CLD2 RESULTS: \n")
print("ENGLISH: " + str(cld2_ratio_english * 100) + "\n")
print("FRENCH: " + str(cld2_ratio_french * 100) + "\n")
print("GERMAN: " + str(cld2_ratio_german * 100) + "\n")
print("SPANISH: " + str(cld2_ratio_spanish * 100) + "\n")

print("\n CLD3 RESULTS: \n")
print("ENGLISH: " + str(cld3_ratio_english * 100) + "\n")
print("FRENCH: " + str(cld3_ratio_french * 100) + "\n")
print("GERMAN: " + str(cld3_ratio_german * 100) + "\n")
print("SPANISH: " + str(cld3_ratio_spanish * 100) + "\n")

print("\n LINGUA RESULTS: \n")
print("ENGLISH: " + str(lingua_ratio_english * 100) + "\n")
print("FRENCH: " + str(lingua_ratio_french * 100) + "\n")
print("GERMAN: " + str(lingua_ratio_german * 100) + "\n")
print("SPANISH: " + str(lingua_ratio_spanish * 100) + "\n")

print("\n LANGDETECT RESULTS: \n")
print("ENGLISH: " + str(langdetect_ratio_english * 100) + "\n")
print("FRENCH: " + str(langdetect_ratio_french * 100) + "\n")
print("GERMAN: " + str(langdetect_ratio_german * 100) + "\n")
print("SPANISH: " + str(langdetect_ratio_spanish * 100) + "\n")
