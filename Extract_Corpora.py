"""
Extract_Corpora.py

Description
-----------
This file provides methods to extract SMS text from the NUS smsCorpus and text from the ISWLT ASR development corpus.
After extraction, the extracted text is put into a new file.
"""

import re

def ExtractSMS(filename):

    with open(filename, 'r') as F:
        Input = F.readlines()

    pattern = re.compile('<text>.*<\/text>')

    with open(filename[:-4] + '.txt', 'w') as O:
        for line in Input:
            line_ = pattern.search(line)
            try:
                SMS_WithoutFrontTag = re.sub('<text>', '', line_.group())
                SMS_WithoutBackTag = re.sub('<\/text>', '', SMS_WithoutFrontTag)
                O.write(SMS_WithoutBackTag + '\n')
            except AttributeError:
                pass

def ExtractASR(filename):

    with open(filename, 'r') as F:
        Input = F.readlines()

    with open(filename[:-3] + 'Fixed.txt', 'w') as O:
        for line in Input:
            try:
                y = re.sub(r"^.*\\", '', line)
                O.write(y)
            except AttributeError:
                pass

# ExtractSMS('smsCorpus_zh_2015.03.09.xml')
ExtractASR('IWSLT09.devset.zh.20BEST.txt')
ExtractASR('IWSLT09.devset3_IWSLT05.zh.20BEST.txt')
ExtractASR('IWSLT09.devset4_IWSLT06.zh.20BEST.txt')
ExtractASR('IWSLT09.devset5_IWSLT06.zh.20BEST.txt')
ExtractASR('IWSLT09.devset7_IWSLT08.zh.20BEST.txt')
ExtractASR('IWSLT09.devset8_IWSLT08.zh.20BEST.txt')
ExtractASR('IWSLT09.devset9_IWSLT08.zh.20BEST.txt')
ExtractASR('IWSLT09.devset4_IWSLT06@spontaneous-speech.zh.20BEST.txt')
ExtractASR('IWSLT09.devset5_IWSLT06@spontaneous-speech.zh.20BEST.txt')