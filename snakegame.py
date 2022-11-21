import pygame
import random
import time

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_length = 500
dis = pygame.display.set_mode((dis_width, dis_length))
pygame.display.set_caption ("Snake Game")
clock = pygame.time.Clock()
