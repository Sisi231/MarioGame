import pyxel
from Classes.Board import Board

board = Board()

pyxel.init(board.width, board.height)

pyxel.load("my_resource.pyxres")

pyxel.run(board.update, board.draw)
