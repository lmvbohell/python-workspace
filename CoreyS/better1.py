# Corey Shafer <<<<<<
# import time
# from datetime import datetime
# #def display_time(time=datetime.now()):  < uppdat ej tiden i displ. Exekv arg då funktionen deklareras.
# def display_time(time=None):
#     if time is None:
#         time = datetime.now()
#     print(time.strftime('%B %d, %Y %H:%M:%S'))
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time()

# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# identities = list(zip(names, heroes))   # -Skriver ut båda printarna pga list().
# print (identities)
# for identity in identities:
#     print('{} is actually {}!'.format(identity[0], identity[1]))

# #-Rename filer i en mapp (utforskaren) "Earth - Our Solar System - #4.mp4"
# import os
# os.chdir('H:/home/bohell/Python_Workspace/CoreyS/Planets')
# for f in os.listdir():
#     f_name, f_ext = (os.path.splitext(f))
#     f_title, f_course, f_num = f_name.split('-')
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num = f_num.strip()[1:].zfill(2)
# #2    print(file_name.split('-'))
# #3    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
#     new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
#     os.rename(f, new_name)  # OBS editerar i utforskaren i mappen Planets ovan. <<<<<<<<<<<<<
# #1    print(os.path.splitext(f))  #-path.splitext ger en tuple och en extention.
# #    print(f)

# #- File Objects ** READ **
# # # f = open('test.txt', 'r')    #-Man ska använda context-file för detta  'r+w' readANDwrite<<<<
# # # f.close()   #- ...då behövs ingen close
# with open('test.txt', 'r') as f:
#     size_to_read = 100
#     f_contents = f.read(size_to_read)   #Här läser vi allt i filen.
#     print(f.tell())     # Ger värde 10, då vi har läst in allt ovan.
#     f.seek(0)   # Startar från början av filen här(0).   
#    #print(f_contents, end='')
#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)   #Nytt värde på f_contents, annars loop.
# #     for line in f:
# #         print(line, end='')
# # #     f_contents = f.readline()   #f.readlines(), , end=''>ingen ny rad.
# # #     print(f_contents, end='')
# # #     f_contents = f.readline()   
# # #     print(f_contents, end='')
# # # #print(f.name, f.mode, f.closed)
# # # #print(f.read()) -Ger I/O error om filen är stängd. f.read(100) > läser 100 tkn.

#- File Objects ** WRITE **
# with open('test2.txt', 'w') as f: Skapar test2.txt och skriver.
#     f.write('Test')
with open('Wally.jpg', 'rb') as rf:   #Bilder 'jpg' använd 'rb'/'wb' binary.
    with open('Wally_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
#        for line in rf:
#            wf.write(line)
