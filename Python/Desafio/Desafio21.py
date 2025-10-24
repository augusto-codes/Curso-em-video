'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r'C:\Users\antonio.augusto\Documents\Visual Studio 2022\Aula\Desafio\desafio21.mp3')
pygame.mixer_music.play()
pygame.event.wait()
