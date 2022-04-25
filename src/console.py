### работа через консоль ###

from argparse import ArgumentParser
from src.Globals import Globals as gl
import src.launcher as launcher

### считывает параметры запуска и передает модулю
def console():
    parser = ArgumentParser(description=gl.DESCRIPTION, epilog=gl.EPILOG)
    parser.add_argument('-m', '--mode', dest='mode', required=True, help=gl.H_MODE)
    parser.add_argument('-t', '--type', dest='scr', required=True, help=gl.H_SCR)
    parser.add_argument('-i', '--input', dest='inp', required=True, help=gl.H_INP)
    parser.add_argument('-o', '--output', dest='out', required=True, help=gl.H_OUT)
    parser.add_argument('-k', '--key', dest='key', required=False, help=gl.H_KEY)

    args = parser.parse_args()
    launcher.use(args)
