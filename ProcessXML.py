# import math
import os
import re

def BatchProcessXML(Directory):

    #Change directory
    os.chdir(Directory)

    # Create file for text to be appended:
    with open('Processed_Annotations.txt', 'w') as NewFile:
        pass

    # Loop through files in directory
    for XML in os.listdir(os.getcwd()):
        print XML
        try:
            with open(XML, 'r') as File:
                Input = File.readlines()
        except IOError:
            print XML + 'is not a readable file'

        try:
            for line in Input:
                # Checks if identifier is in the line
                if 'segment' in line:
                    #Sets counter to be on and starts count at 0
                    Count_On = True
                    Count = 0
                    Right_Arrow_Count = 0
                    Line = ''
                    Annotations = ''
                    Entities = re.findall('entity.[^\s\']*', line)
                    for character in line.decode('utf-8'):
                        if '<' in character:
                            Count_On = False
                            if Right_Arrow_Count == 0:
                                Annotations += str(Count) + ' '
                                Count_1 = Count
                        elif '>' in character:
                            Count_On = True
                            Right_Arrow_Count += 1
                            if Right_Arrow_Count == 2:
                                # print 'Test ' + Annotations
                                Annotations += str(Count) + ' ' + str(Count_1) + ' ' + str(Count) + ' ' + Entities.pop(0)[7:] + ' '
                                Right_Arrow_Count = 0
                        # elif ' ' in character:
                        #     Line += ' '
                        elif Count_On == False:
                            pass
                        else:
                            Count += 1
                            Line += character
                    with open('Processed_Annotations.txt', 'a') as P_A:
                        P_A.write(Line.encode('utf-8') + '\n')
                        P_A.write(Annotations + '\n' + '\n')
        except IndexError:
            pass


def ProcessXML(File):
    # Read file
    with open(File, 'r') as File:
        Input = File.readlines()

    for line in Input:
        # Checks if identifier is in the line
        if 'segment' in line:
            #Sets counter to be on and starts count at 0
            Count_On = True
            Count = 0
            Right_Arrow_Count = 0
            Line = ''
            Annotations = ''
            Entities = re.findall('entity.[^\s\']*', line)
            for character in line.decode('utf-8'):
                if '<' in character:
                    Count_On = False
                    if Right_Arrow_Count == 0:
                        Annotations += str(Count) + ' '
                        Count_1 = Count
                elif '>' in character:
                    Count_On = True
                    Right_Arrow_Count += 1
                    if Right_Arrow_Count == 2:
                        # print 'Test ' + Annotations
                        Annotations += str(Count) + ' ' + str(Count_1) + ' ' + str(Count) + ' ' + Entities.pop(0)[7:] + ' '
                        Right_Arrow_Count = 0
                elif ' ' in character:
                    Line += ' '
                elif Count_On == False:
                    pass
                else:
                    Count += 1
                    Line += character
            with open('Processed_Annotations.txt', 'a') as P_A:
                P_A.write(Line.encode('utf-8') + '\n')
                P_A.write(Annotations + '\n' + '\n')

BatchProcessXML('/Users/Sky/Desktop/Annotations/recreation_an')
# ProcessXML('0 (97)-Entity.xml')