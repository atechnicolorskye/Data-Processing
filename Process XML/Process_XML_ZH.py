"""
Process_XML_ZH.py

Description
-----------
This file batch processes spaced annotated Chinese text in the .XML format by extracting the annotations
and tagging with the text StanfordPOSTagger and dumps the information into a specified file of choice.  

The annotations are extracted in the form of x,y A| where x is xth space in the sentence and yth space in the
sentence containing the annotated text and A is the annotation. Each annotation is separated by a '|' 


Usage:

BatchProcess('~/Annotated_XML/', 'Processed_Annotations.txt')
The first input is the directory containing the .XML files and the second the desired output file.

Process_ZH('~/Annotations_XML/Test.xml')
The input is the .XML file to be processed. 

Add_Divider('Processed_Annotations.txt')
The input is the processed text file for dividers to be added to between annotation segments.
"""

# import math
# -*- coding: utf-8 -*-
import os
import re
import zhon.hanzi

from nltk.tag import StanfordPOSTagger

def BatchProcess(Directory, New_File):

    #Change directory
    os.chdir(Directory)

    # Create file for text to be appended:
    with open(New_File, 'w') as NewFile:
        pass

    # Loop through files in directory
    for XML in os.listdir(os.getcwd()):
        print XML
        try:
            Process_ZH(XML)
            Add_Divider('Processed_Annotations.txt')
        except IOError:
            print XML + 'is not a readable file'

        # try:
        #     for line in Input:
        #         # Checks if identifier is in the line
        #         if 'segment' in line:
        #             #Sets counter to be on and starts count at 0
        #             Count_On = True
        #             Count = 0
        #             Right_Arrow_Count = 0
        #             Line = ''

        #             # Switch to UTF-8 to ensure accurate counting
        #             Line_UTF8_Decode = line.decode('utf-8')
        #             Line_Split_Join = ' '.join(Line_UTF8_Decode.split())
        #             print Line

        #             Annotations = ''
        #             Entities = re.findall('entity.[^\s\']*', line)
        #             for character in line.decode('utf-8'):
        #                 if '<' in character:
        #                     Count_On = False
        #                     if Right_Arrow_Count == 0:
        #                         Annotations += str(Count) + ','
        #                         Count_1 = Count
        #                 elif '>' in character:
        #                     Count_On = True
        #                     Right_Arrow_Count += 1
        #                     if Right_Arrow_Count == 2:
        #                         # print 'Test ' + Annotations
        #                         Annotations += str(Count) + ',' + str(Count_1) + ',' + str(Count) + ' ' + Entities.pop(0)[7:].upper() + ' '
        #                         Right_Arrow_Count = 0
        #                 elif ' ' in character:
        #                     Count += 1
        #                     Line += character
        #                 elif Count_On == False:
        #                     pass
        #                 else:
        #                     # Count += 1
        #                     Line += character
        #             with open('Processed_Annotations.txt', 'a') as P_A:
        #                 P_A.write(Line.encode('utf-8') + '\n')
        #                 P_A.write(Annotations + '\n' + '\n')
        # except IndexError:
        #     pass


def Process_ZH(File):
    # Read file
    with open(File, 'r') as File:
        # print 'Opened'
        Input = File.readlines()


    try:
        for line in Input:
            # Checks if identifier is in the line
            if 'segment' in line:
                #Sets counter to be on and starts count at 0
                Annotations = []
                Annotation_Next = False
                Line = []
                Word_Count = 0

                # Switch to UTF-8 to ensure accurate counting
                Line_UTF8_Decode = line.decode('utf-8')
                Line_Split = Line_UTF8_Decode.split()

                for Split in Line_Split:
                    if 'feature' in Split:
                        Annotations.append([Split[17:-1], Word_Count, 0])
                        # print Annotations

                    elif 'state=' in Split:
                        Line_Temp = re.findall('>([^>]*)</', Split)
                        # print 'State_1'
                        if Line_Temp != []:
                            # Ensures that Line_Temp is a string
                            Line_Temp = Line_Temp[0]
                            Word_Count += 1
                            # print 'State_2'

                            # To ensure nested entities are parsed correctly
                            if Annotations[-1][2] != 0:
                                Annotation_Next = True
                                Length = range(len(Annotations))
                                for x in Length[::-1]:
                                    if Annotations[x][2] == 0 and Annotation_Next == True:
                                        Annotations[x][2] = Word_Count
                                        Annotation_Next = False
                            else:
                                Annotations[-1][2] = Word_Count
                            # print Annotations
                        elif Line_Temp == [] and '<segment' in Split[15:]:
                            pass
                        else:
                            Word_Count += 1
                            Line_Temp = Split[15:]
                            # print 'State 3'
                        if Line_Temp != []:
                            Line.append(Line_Temp)

                    elif '</segment>' in Split:
                        Seg_Split = Split.split('</segment>')
                        for x in Seg_Split:
                            if x != '':
                                Word_Count += 1
                                Line.append(x)
                            elif x == '':
                                if Annotations[-1][2] != 0:
                                # print 'Seg 2'
                                    Annotation_Next = True
                                    Length = range(len(Annotations))
                                    for x in Length[::-1]:
                                    # print Annotations[x][2]
                                        if Annotations[x][2] == 0 and Annotation_Next == True:
                                        # print 'Seg 3'
                                            Annotations[x][2] = Word_Count
                                            Annotation_Next = False
                                else:
                                    Annotations[-1][2] = Word_Count
                            # print Annotations

                        # if '<' not in Split[0]:
                        #     Word_Count += 1
                        #     print Split
                        #     Line_Temp = Split[:-10]
                        #     print Line_Temp
                        #     Line.append(Line_Temp)
                        #     # print 'Seg_1'
                        #     if Annotations[-1][2] != 0:
                        #         # print 'Seg 2'
                        #         Annotation_Next = True
                        #         Length = range(len(Annotations))
                        #         for x in Length[::-1]:
                        #             # print Annotations[x][2]
                        #             if Annotations[x][2] == 0 and Annotation_Next == True:
                        #                 # print 'Seg 3'
                        #                 Annotations[x][2] = Word_Count
                        #                 Annotation_Next = False
                        #     else:
                        #         Annotations[-1][2] = Word_Count
                        #     # print Annotations

                    elif '<segment' not in Split:
                        # print Split
                        Line.append(Split)
                        # Checks if Split is a punctuation character
                        if re.findall('[%s]' % zhon.hanzi.punctuation, Split) == [] and Split != ':':
                            Word_Count += 1
                Line_Done = ' '.join(Line)

                # Tags using StanfordPOSTagger

                ST = StanfordPOSTagger('~/Annotations/models/chinese-distsim.tagger', '~/Annotations/stanford-postagger.jar', encoding='utf-8')
                Tags = ST.tag(Line)
                Tags_Done = ''
                for x in Tags:
                    # print x
                    Tags_Done += x[1][-2:] + ' '

                # print Line_Done
                # print Tags_Done

                Annotations_Done = ''
                for x in Annotations:
                    Annotations_Done += str(x[1]) + ',' + str(x[2]) + ',' + str(x[1]) + ',' + str(x[2]) + ' ' + x[0].upper() + '|'
                # print Annotations_Done

                with open('Processed_Annotations.txt', 'a') as P_A:
                        P_A.write(Line_Done.encode('utf-8') + '\n')
                        P_A.write(Tags_Done + '\n')
                        P_A.write(Annotations_Done[:-1] + '\n' + '\n')
    except IndexError:
        pass

                # Enclosed = re.findall('>([^>]*)</', Line_UTF8_Decode)
                # Entities = re.findall('entity.[^\s\']*', Line_UTF8_Decode)
    #             print Entities
    #             for character in Line_UTF8_Decode:
    #                 print character
    #                 # '''
    #                 if '<' in character:
    #                     Count_On = False
    #                     Backslash_Count += 1
    #                     Annotation_Tuple = [str(Word_Count) + ',', Word_Count]
    #                     Annotations.append(Annotation_Tuple)
    #                 elif '/' in character and Left_Arrow == True:
    #                     Annotations.pop()
    #                     Left_Arrow == False
    #                     Backslash_Count -= 1
    #                     Annotation_On = True
    #                     # Right_Arrow_Count -= 1
    #                 elif '>' in character:
    #                     Count_On = True
    #                     # Right_Arrow_Count += 1
    #                     if Backslash_Count >= 0 and Annotation_On == True:
    #                         # pass
    #                         Var = - Backslash_Count
    #                         print Var
    #                         # print Annotations[Var]
    #                         # print Annotation_Tuple
    #                         # Annotations[-1-Backslash_Count][0] += str(Word_Count) + ',' + str(Annotation_Tuple[-1]) + ',' + str(Word_Count) + ' ' + Entities.pop(Backslash_Count)[7:].upper() + ' '
    #                     #     Annotation_On = False
    #                 elif ' ' in character and Count_On == True:
    #                     # print character, True
    #                     Word_Count += 1
    #                     Line += character
    #                 elif Count_On == True:
    #                     # print character, True
    #                     Line += character
    #                 # elif Count_On == False:
    #                     # print character, False
    #                 # '''
    #             print Line
    #             print Annotations
    #             with open('Processed_Annotations.txt', 'a') as P_A:
    #                 P_A.write(Line.encode('utf-8') + '\n')
    #                 P_A.write(Annotations + '\n' + '\n')
    # except IndexError:
    #     pass


    # for line in Input:
    #     # Checks if identifier is in the line
    #     if 'segment' in line:
    #         #Sets counter to be on and starts count at 0
    #         Count_On = True
    #         Count = 0
    #         Right_Arrow_Count = 0
    #         Line = ''
    #         Annotations = ''
    #         Entities = re.findall('entity.[^\s\']*', line)
    #         for character in line.decode('utf-8'):
    #             if '<' in character:
    #                 Count_On = False
    #                 if Right_Arrow_Count == 0:
    #                     Annotations += str(Count) + ' '
    #                     Count_1 = Count
    #             elif '>' in character:
    #                 Count_On = True
    #                 Right_Arrow_Count += 1
    #                 if Right_Arrow_Count == 2:
    #                     # print 'Test ' + Annotations
    #                     Annotations += str(Count) + ' ' + str(Count_1) + ' ' + str(Count) + ' ' + Entities.pop(0)[7:] + ' '
    #                     Right_Arrow_Count = 0
    #             elif ' ' in character:
    #                 Line += ' '
    #             elif Count_On == False:
    #                 pass
    #             else:
    #                 Count += 1
    #                 Line += character
    #         with open('Processed_Annotations.txt', 'a') as P_A:
    #             P_A.write(Line.encode('utf-8') + '\n')
    #             P_A.write(Annotations + '\n' + '\n')


def Add_Divider(File):

    with open(File, 'r') as F:
        Input = F.readlines()

    with open(File[:-3] + '_P.txt', 'w') as O:
        Total = len(Input)
        Count_0 = 0
        Count_1 = 1
        Count_2 = 2
        Count_3 = 3

        try:
            while Count_3 <= Total:
                O.write(Input[Count_0])
                Count_0 += 4
                O.write(Input[Count_1])
                Count_1 += 4
                Add_Divider_1 = re.sub(' ', '|', Input[Count_2])
                Add_Divider_2 = re.sub(r'([0-9]),([A-Z])', r'\1 \2', Add_Divider_1)
                O.write(Add_Divider_2)
                Count_2 += 4
                O.write(Input[Count_3])
                Count_3 += 4
        except IndexError:
            pass

# BatchProcess('~/Annotations/recreation_an')
# BatchProcess('~/Annotations/society_an')
# BatchProcess('~/Annotations/sports_an')

# Process_ZH('~/Annotations/sports_an/0 (1)-Entity.xml')
# Process_ZH('Test.txt')

# Add_Divider('Processed_Annotations_Recreation.txt')
# Add_Divider('Processed_Annotations_Society.txt')
# Add_Divider('Processed_Annotations_Sport.txt')