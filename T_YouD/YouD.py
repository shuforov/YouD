import pafy

url = pafy.new(raw_input('Type your url video ->'))
print '------------------'
print 'Title:', url.title
print 'Thumb:', url.thumb
print 'Duration:', url.duration
print '------------------'
z = {1: 'audiostreams', 2: 'streams', 3: 'allstreams'}
print 'Chose the list of available formats and enter the number:'
temp_list = ['audio streams','streams','all streams']
counter_for_inf = 1
for x in temp_list:
    print counter_for_inf, x
    counter_for_inf += 1
number = int(raw_input('->'))
list_of_formats = []
counter = 0
if number == 1:
    list_of_formats = url.audiostreams
    for x in url.audiostreams:
        print counter, x
        counter += 1
elif number == 2:
    list_of_formats = url.streams
    for x in url.streams:
        print counter, x
        counter += 1
elif number == 3:
    list_of_formats = url.allstreams
    for x in url.allstreams:
        print counter, x
        counter += 1

format_url = int(raw_input('Chose format to download ->'))
print 'Type the path where will be downloaded file'
print 'Example for windows "D:/" or "D:/downloads"'
print 'Example for linux "/home/<user_name>"'
print 'leave empty to download in app director'
path_file = raw_input('->')
list_of_formats[format_url].download(filepath=path_file)


#https://www.youtube.com/watch?v=WEvby-c1WnI
