import socket

import Senal
import graphics.Graphics

from graphics import *
from GameFunctionality import GameFunctionality
from SignalManager import SignalManager


if __name__ == "__main__":

	PUERTO = 1043
	IP_SERVER = "localhost"

	print("        APLICACIÓN CLIENTE         ")
	print("-----------------------------------")
	print("BIENVENIDO AL JUEGO PIEDRA-PAPEL-TIJERA")

	game = GameFunctionality()
	gf = graphics.Graphics.Graphics(game)
	gf.initGraphics()
	game.setGraphics(gf)

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketAlServidor:
		socketAlServidor.connect((IP_SERVER, PUERTO))

		signalManager = SignalManager(socketAlServidor, game)
		game.setSignalManager(signalManager)

		signalManager.enviarSenal(Senal.CONECTARSE)
		print("Enviada senal de conectarse")

		signalManager.start()
		"""
		} catch (UnknownHostException e) {
		System.err.println("CLIENTE: No encuentro el servidor en la dirección" + IP_SERVER)
		} catch (ConnectException e){
		System.out.println("CLIENTE: Connection timed out.")
		} catch (IOException e) {
		System.err.println("CLIENTE: Error de entrada/salida")
		} catch (Exception e) {
		System.err.println("CLIENTE: Error -> " + e)
		e.printStackTrace()
		"""


