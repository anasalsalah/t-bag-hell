from pygame import mixer


class Music:

    # seems there's no way to find out if music is paused or not using pygame.mixer
    # so we are creating a flag of our own
    __music_paused = True
    __song_player = None

    def __init__(self, play_now=False):
        mixer.init()
        self.__song_player = mixer.music
        self.__song_player.load("media/welcome-to-hell.ogg")
        # TODO figure out how to get the mixer queue to keep playing songs
        # self.__song_player.queue("media/silly-pig-song.ogg")
        if play_now:
            self.start()

    def start(self):
        self.__music_paused = False
        self.__song_player.play()

    def is_paused(self):
        return self.__music_paused

    def toggle_music(self):
        self.__music_paused = not self.__music_paused

        if self.__music_paused:
            self.__song_player.pause()
        else:
            if not self.__song_player.get_busy(): # song finished and player stopped
                self.__song_player.load("media/silly-pig-song.ogg")
                self.__song_player.play()
            else:
                self.__song_player.unpause()


