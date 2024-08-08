"""
Faça um programa em Python que abra e reproduza o áudio de um MP3.
"""
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex023.mp3')
pygame.mixer.music.play()
input('Aguarde a musica inicar')
pygame.event.wait()
