
# =============================================================================
def uno(S):
    import re
    from collections import OrderedDict
    file_pattern = re.escape("^&'@{}[],$=!-#()%.+~_")
    file_desc_re = re.compile("[\w\d" + file_pattern + "]+\.(\w{3,4}) (\d+)b")
    music_exts = ['mp3', 'aac', 'flac']
    image_exts = ['jpg', 'bmp', 'gif']
    movie_exts = ['mp4', 'avi', 'mkv']
    stats = OrderedDict([('music', 0), ('images', 0), ('movies', 0), ('other', 0)])
    for match in file_desc_re.findall(S):
        if match[0] in music_exts:
            stats['music'] += int(match[1])
        elif match[0] in image_exts:
            stats['images'] += int(match[1])
        elif match[0] in movie_exts:
            stats['movies'] += int(match[1])
        else:
            stats['other'] += int(match[1])
    return ' '.join(['%s %ib' % (t, z) for t, z in stats.items()])
    


# =============================================================================
def dos(N):
    max_winter = N[0]
    current_max = N[0]
    partition = 0
    for i in range(len(N)):
        if N[i] <= max_winter:
            current_max = max_winter
            partition = i
        elif N[i] > current_max:
            current_max = N[i]
    return partition + 1


# =============================================================================
if __name__ == '__main__':
    # print dos([5, -2, 3, 8, 6])
    # print dos([-5, -5, 20, -42, -15, 6, 12])
    print dos([-5, -5, -42, -5, 6, 12])
    # print uno('my.song.mp3 11b greatSong.flac 1000b not3.txt 5b video.mp4 200b game.exe 100b mov!e.mkv 10000b')
