import pygame

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load(
        f'Tohpati - perahu kertas.mp3')
    pygame.mixer.music.play(loops=0)
    k = input("press close to exit")
