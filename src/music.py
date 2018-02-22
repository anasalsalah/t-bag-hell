from pygame import mixer


class Music:

    __song_player = None
    __song_list = ["media/welcome-to-hell.ogg", "media/silly-pig-song.ogg"]
    __song_index = -1

    def __init__(self, play_now=False):
        mixer.init()
        self.__song_player = mixer.music
        if play_now:
            self.play_next()

    def play_next(self):
        # go to next song (or loop back to first song)
        self.__song_index = (self.__song_index + 1) % len(self.__song_list)
        self.__song_player.load(self.__song_list[self.__song_index])
        self.__song_player.play()

    def is_playing(self):
        return self.__song_player.get_busy()

    def toggle_music(self):
        if self.is_playing():
            self.__song_player.stop()
        else:
            self.play_next()


