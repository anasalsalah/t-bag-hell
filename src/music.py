from pygame import mixer, error


class MusicNotFoundError(RuntimeError):
    pass


class Music:

    __song_player = None
    __song_list = ["media/yusef-lateef-morning.ogg", "media/welcome-to-hell.ogg", "media/silly-pig-song.ogg"]
    __song_index = -1

    def __init__(self, play_now=False):
        mixer.init()
        self.__song_player = mixer.music
        if play_now:
            try:
                self.play_next(5)
            except MusicNotFoundError:
                pass # ignore error if music not found

    def play_next(self, loops=1, recursive=False):
        # go to next song (or loop back to first song)
        self.__song_index = (self.__song_index + 1) % len(self.__song_list)
        try:
            self.__song_player.load(self.__song_list[self.__song_index])
            self.__song_player.play(loops, 0.0)
        except error:
            if not recursive or (recursive and self.__song_index != 0):
                # try to play the next song
                self.play_next(loops,True)
            else: # could not load any of the songs
                raise MusicNotFoundError

    def is_playing(self):
        return self.__song_player.get_busy()

    def toggle_music(self):
        if self.is_playing():
            self.__song_player.stop()
        else:
            self.play_next()


