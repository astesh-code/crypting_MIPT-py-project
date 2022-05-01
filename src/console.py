### work via console ###

from argparse import ArgumentParser
from src.Globals import Globals as gl
import src.launcher as launcher

def console():
    """read launch parameters and transfer them to module"""
    parser = ArgumentParser(description=gl.description, epilog=gl.epilog)
    parser.add_argument('-m', '--mode', dest='mode', required=True, help=gl.h_mode)
    parser.add_argument('-t', '--type', dest='scr', required=True, help=gl.h_scr)
    parser.add_argument('-i', '--input', dest='inp', required=True, help=gl.h_inp)
    parser.add_argument('-o', '--output', dest='out', required=True, help=gl.h_out)
    parser.add_argument('-k', '--key', dest='key', required=False, help=gl.h_key)

    args = parser.parse_args()
    launcher.use(args)
