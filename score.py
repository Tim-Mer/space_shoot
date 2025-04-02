import pygame
from constants import *


class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.time = 0.0
        
    def add_score(self, value):
        self.score += value
    
        
    def display(self):
        print(f"Your score was {self.score}")
        print(f"You lived for {self.time:.2f} seconds")