import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((600, 480))
background = pg.image.load(os.path.join("Images/ChessBoard.png"))
