import threading
import Senal

class SignalManager():

	def __init__(self, socketAlServidor, game):
		self.socketAlServidor = socketAlServidor
		self.game = game

	def nextLine(self) -> str:
		buffer = ""
		c: str

		for i in range(1, 50):
			c = self.socketAlServidor.recv(1, 0).decode("utf8")

			buffer += c

			if c == '\n':
				return buffer
		return buffer

	def start(self):
		threading.Thread(target=self.run, args=()).start()

	def run(self):

		while True:
			try:
				resultado_str = self.nextLine()
				senal = Senal.ERROR

				senal = int(resultado_str)

				if senal == Senal.ENVIAR_NOMBRE:
					self.manejarEnviarNombre()
				elif senal == Senal.CONEXION_EXITOSA:
					self.manejarConexionExitosa()
				elif senal == Senal.ENVIAR_SELECCION:
					self.manejarEnviarSeleccion()
				elif senal == Senal.GANADOR_DE_RONDA:
					self.manejarRondaGanada()
				elif senal == Senal.PERDEDOR_DE_RONDA:
					self.manejarRondaPerdida()
				elif senal == Senal.PERDEDOR_DE_TORNEO:
					self.manejarPerderTorneo()
				elif senal == Senal.EMPATE:
					self.manejarEmpate()
				elif senal == Senal.GANADOR_DE_ENFRENTAMIENTO:
					self.manejarEnfrentamientoGanado()
				elif senal == Senal.PERDEDOR_DE_ENFRENTAMIENTO:
					self.manejarEnfrentamientoPerdido()
				elif senal == Senal.GANADOR_DE_TORNEO:
					self.manejarTorneoGanado()
				elif senal == Senal.PAQUETE_PUNTUACION:
					self.manejarObtenerPuntaje()
				elif senal == Senal.COMENZAR_PARTIDA_FINAL:
					self.manejarComenzarPartidaFinal()
				elif senal == Senal.FINAL_DE_TORNEO:
					self.manejarFinalDeTorneo()
				elif senal == Senal.NOMBRE_GANADOR_DEL_ENFRENTAMIENTO:
					self.manejarNombreGanadorEnf()
				elif senal == Senal.NOMBRE_GANADOR_DEL_TORNEO:
					self.manejarNombreGanadorTor()
				elif senal == Senal.PREGUNTA_REVANCHA:
					self.manejarPreguntaRevancha()
				elif senal == Senal.JUGADORES_EN_LOBBY:
					self.manejarJugadoresEnLobby()
				elif senal == Senal.COMENZAR_TORNEO:
					self.manejarComenzarTorneo()
				elif senal == Senal.COMENZAR_ENFRENTAMIENTO:
					self.manejarComenzarEnfrentamiento()
				elif senal == Senal.CONEXION_EXITOSA_TORNEO:
					self.manejarConexionExitosaTorneo()
				elif senal == Senal.NOMBRE_DEL_RIVAL:
					self.manejarNombreDelRival()
				elif senal == Senal.CLAVE_TORNEO:
					self.manejarClaveTorneo()
				elif senal == Senal.LISTA_TORNEOS:
					self.manejarListaTorneos()
				elif senal == Senal.NOMBRE_TORNEO:
					self.manejarNombreTorneo()
				elif senal == Senal.LOBBY_LLENO:
					self.manejarLobbyLleno()
				elif senal == Senal.ERROR:
					self.manejarError()


			except RuntimeError as e:
				print(e)
				print("Desconectado del servidor.")
				exit(-1)

	def manejarPerderTorneo(self):
		self.game.getGraphics().cambiarPantalla(self.game.getGraphics().getPantallaPerdedorTorneo())

	def manejarNombreTorneo(self):
		nombreDelTorneo = self.nextLine()
		self.game.getGraphics().setNombreTorneo(nombreDelTorneo)

	def manejarClaveTorneo(self):
		clave = self.nextLine()
		self.game.getGraphics().onClaveTorneo(clave)

	def enviarSenal(self, senal):
		self.socketAlServidor.send((str(senal) + "\n").encode('utf8'))

	def enviarPaquete(self, paquete):
		self.socketAlServidor.send((str(paquete) + "\n").encode('utf8'))

	def enviarSenalDeConexion(self):
		self.game.getGraphics().onConectando()
		self.socketAlServidor.send(Senal.CONECTARSE)

	def manejarConexionExitosa(self):
		print("Te has conectado!")
		self.game.getGraphics().onConexionExitosa()

	def manejarRondaGanada(self):
		print("¡Has ganado la ronda!")
		self.game.getGraphics().getPantallaEnfrentamiento().onRondaGanada()

	def manejarRondaPerdida(self):
		self.game.getGraphics().getPantallaEnfrentamiento().onRondaPerdida()

	def manejarEnfrentamientoGanado(self):
		self.game.getGraphics().getPantallaEnfrentamiento().onEnfrentamientoGanado()
		self.game.actualizarContinuarPartida(False)

	def manejarEnfrentamientoPerdido(self):
		self.game.getGraphics().getPantallaEnfrentamiento().onEnfrentamientoPerdido()
		self.game.actualizarContinuarPartida(False)
		self.game.actualizarContinuarTorneo(False)

	def manejarTorneoGanado(self):
		print("¡Has ganado el torneo!")
		self.game.getGraphics().cambiarPantalla(self.game.graphics.getPantallaGanadorTorneo())
		self.game.actualizarContinuarPartida(False)
		self.game.actualizarContinuarTorneo(False)

	def manejarObtenerPuntaje(self):
		# Obtener paquete puntaje

		paquete = self.nextLine()
		puntajes_str = paquete.split("\\|")
		puntajes = []

		for puntaje in puntajes_str:
			puntajes.append(int(puntaje))

		self.game.getGraphics().getPantallaEnfrentamiento().onObtenerPuntaje(puntajes)

	def manejarEnviarNombre(self):
		self.game.getGraphics().onEnviarNombre()

	def manejarFinalDeTorneo(self):
		print("Terminó el torneo señores.")
		self.game.actualizarContinuarTorneo(False)

	def manejarComenzarPartidaFinal(self):
		print("Has llegado a la final!")
		self.game.getGraphics().getPantallaEnfrentamiento().onEmpezarFinal()

	def manejarNombreGanadorEnf(self):
		ganador = self.nextLine()
		print("El ganador del enfrentamiento es: " + ganador)

	def manejarNombreGanadorTor(self):
		ganador = self.nextLine()
		print("El ganador del torneo es: " + ganador)

	# Envía paquete
	def manejarPreguntaRevancha(self):
		senal = Senal.ERROR

		while senal == Senal.ERROR:
			print("El torneo ha terminado. Deseas volver a jugar?")
			print("Selección (S/n): ")

			try:
				# str = sc.nextLine()

				if str == "S" or str == "s":
					senal = Senal.SI
				elif str == "N" or str == "n":
					senal = Senal.NO

			except Exception as e:
				print("Por favor, introduzca una opción válida.")

		self.socketAlServidor.send(senal)

	def manejarError(self):
		print("Hubo un error.")

	def manejarJugadoresEnLobby(self):
		jugadores = self.nextLine()
		self.game.getGraphics().onJugadoresEnLobby(jugadores)
		print("Jugadores en lobby: " + jugadores)

	def manejarComenzarEnfrentamiento(self):
		print("Comienza el enfrentamiento!")

	def manejarComenzarTorneo(self):
		print("Comienza el torneo!")

	# Envía paquete
	def manejarEnviarSeleccion(self):
		self.game.getGraphics().onEnviarSeleccion()

	def manejarConexionExitosaTorneo(self):
		self.game.getGraphics().onConexionExitosaTorneo()

	def manejarLobbyLleno(self):
		print("El lobby se encuentra lleno en este momento, espere unos minutos para volver a ingresar")

	def manejarNombreDelRival(self):
		nombre = self.nextLine()
		self.game.getGraphics().getPantallaEnfrentamiento().onNombreDelRival(nombre)

	def manejarListaTorneos(self):
		torneos = self.nextLine()
		print("Numero de torneos: " + torneos)

		header = ["Nombre", "Cantidad de jugadores", "Clave"]

	# modelo = Table(header, 0)

	# for (int i = 0 i < torneos i++) :
	#    String datos = self.reader.nextLine()
	#    String[] datosSplit = datos.split("\\|")
	#    modelo.addRow(datosSplit)
	#    print("Datos recibidos: " + datos)

	# JTable table = new JTable(modelo)
	# table.getColumnModel().getColumn(2).setMaxWidth(0) # Ocultar columna de clave
	# self.game.getGraphics().getPantallaUnirseTorneo().onListaTorneoRecibida(table)

	def manejarEmpate(self):
		self.game.getGraphics().getPantallaEnfrentamiento().onEmpate()




