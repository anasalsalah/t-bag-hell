from pygame import mixer
from src import printer


class Music:

    # seems there's no way to find out if music is paused or not using pygame.mixer
    # so we are creating a flag of our own
    __music_paused = False
    __song_player = None

    def __init__(self):
        mixer.init()
        self.__song_player = mixer.music
        self.__song_player.load("media/welcome-to-hell.ogg")
        self.__song_player.play()
        # TODO figure out how to get the mixer queue to keep playing songs
        # self.__song_player.queue("media/silly-pig-song.ogg")

    def toggle_music(self):
        self.__music_paused = not self.__music_paused

        if self.__music_paused:
            # TODO May decide to refactor the printing to enhance decoupling
            printer.print_music_off()
            self.__song_player.pause()
        else:
            printer.print_music_on()
            if not self.__song_player.get_busy(): # song finished and player stopped
                self.__song_player.load("media/silly-pig-song.ogg")
                self.__song_player.play()
            else:
                self.__song_player.unpause()


