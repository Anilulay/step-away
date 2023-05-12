import pygame
import json
import random
import time
import os


class Window:
    def get_file_path(self, file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file)
        return file_path

    def get_random_exercise(self):
        with open(f"{self.get_file_path('exercises.json')}", "r") as f:
            exercises = json.load(f)
        random.seed(time.time())
        return random.choice(exercises)

    def get_text(self):
        duration = self.current_break_duration
        text = str(duration) if duration < 60 else str(int(duration / 60))
        text += " "
        text += "second" if duration < 60 else "minute"
        text += ": "
        text += self.get_random_exercise()
        return text

    def open(self):
        pygame.init()
        screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.get_text(), True, (255, 255, 255))
        # get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()
        # calculate the center position for the text
        x = (screen_size[0] / 2) - (text_width / 2)
        y = (screen_size[1] / 2) - (text_height / 2)
        # blit the text surface onto the center of the screen
        screen.blit(text_surface, (x, y))
        # update the display
        pygame.display.flip()

    def close(self):
        if "TRAVIS" not in os.environ:
            pygame.quit()
