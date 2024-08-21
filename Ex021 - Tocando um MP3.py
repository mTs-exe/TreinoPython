# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()
x = input('Digite algo para parar a música:')

# O comando input faz a música ser iniciada, caso queira parar é necessário digitar algo
