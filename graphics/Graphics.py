import GameFunctionality

class Graphics:

	def plantilla(self):
		print("hola")

	pantallaGanadorTorneo : PantallaGanadorTorneo

	pantallaInicial : PantallaInicial

	pantallaConexion : PantallaConexion

	pantallaEnfrentamiento: PantallaEnfrentamiento

	pantallaLobby: PantallaLobby

	pantallaCreacionTorneo: PantallaCreacionTorneo

	pantallaUnirseTorneo: PantallaUnirseTorneo

	functionality : GameFunctionality
	pantallaPerdedorTorneo: PantallaPerdedorTorneo


	def __init__(self, functionality: GameFunctionality.GameFunctionality):
		self.functionality = functionality
		self.pantallaPerdedorTorneo = PantallaPerdedorTorneo(self)
		self.pantallaGanadorTorneo = PantallaGanador(self)
		self.pantallaEnfrentamiento = PantallaEnfrentamiento(self)
		self.pantallaInicial = PantallaInicial(self)
		self.pantallaConexion = PantallaConexion(self)
		self.pantallaLobby = PantallaLobby(self)
		self.pantallaCreacionTorneo = PantallaCreacionTorneo(self)
		self.pantallaUnirseTorneo = PantallaUnirseTorneo(self)

		"""
		self.setContentPane(pantallaInicial)
		self.setSize(pantallaInicial.getSize())
		self.setLocationRelativeTo(null)
		self.setDefaultCloseOperation(EXIT_ON_CLOSE)
		self.setVisible(true)
		"""

	def onConectando(self) :
		self.cambiarPantalla(self.pantallaConexion)

	def onConexionExitosa(self):
		print("GRAPHICS dice: Conectado!")
		self.pantallaConexion.onConexionExitosa()

	def getFunctionality(self):
		return self.functionality

	def onEnviarSeleccion(self) :
		self.cambiarPantalla(self.pantallaEnfrentamiento)

	def onEnviarNombre(self) :
		System.out.println("GRAPHICS dice: Esperando a que el usuario escriba su nombre.")
		self.cambiarPantalla(self.pantallaConexion)

	def onConexionExitosaTorneo(self) :
		self.cambiarPantalla(self.pantallaLobby)

	def onJugadoresEnLobby(jugadores: str):
		pantallaLobby.onJugadoresEnLobby(jugadores)

	def getPantallaInicial(self):
		return self.pantallaInicial

	def setPantallaInicial(self, pantallaInicial: PantallaInicial) :
		self.pantallaInicial = pantallaInicial

	def getPantallaConexion(self):
		return self.pantallaConexion

	def setPantallaConexion(self, pantallaConexion: PantallaConexion) :
		self.pantallaConexion = pantallaConexion


	def getPantallaEnfrentamiento(self):
		return self.pantallaEnfrentamiento

	def setPantallaEnfrentamiento(self, pantallaEnfrentamiento: PantallaEnfrentamiento):
		self.pantallaEnfrentamiento = pantallaEnfrentamiento

	def getPantallaLobby(self):
		return self.pantallaLobby

	def setPantallaLobby(self, pantallaLobby: PantallaLobby):
		self.pantallaLobby = pantallaLobby

	def getPantallaCreacionTorneo(self) :
		return self.pantallaCreacionTorneo

	def getPantallaUnirseTorneo(self) :
		return self.pantallaUnirseTorneo

	def onClaveTorneo(self, clave : str):
		self.functionality.setClaveTorneo(clave)
		self.pantallaLobby.onClaveTorneo(clave)

	def setNombreTorneo(self, nombreTorneo: str) :
		self.pantallaLobby.setNombreTorneo(nombreTorneo)

	def cambiarPantalla(self, pantallaSiguiente: PantallaBase):
		"""

		#pantallaActual = (PantallaBase) self.getContentPane()
		if(pantallaActual instanceof PantallaCreacionTorneo):
			self.pantallaCreacionTorneo = PantallaCreacionTorneo(self)
		elif (pantallaActual instanceof PantallaLobby) :
			pantallaLobby = PantallaLobby(self)
		elif (pantallaActual instanceof PantallaUnirseTorneo) :
			pantallaUnirseTorneo = PantallaUnirseTorneo(self)
		elif (pantallaActual instanceof PantallaEnfrentamiento) :
			pantallaEnfrentamiento = PantallaEnfrentamiento(self)


		self.setContentPane(pantallaSiguiente)
		"""

	def getPantallaGanadorTorneo(self):
		return self.pantallaGanadorTorneo

	def setPantallaGanadorTorneo(self, pantallaGanadorTorneo: PantallaGanador) :
		self.pantallaGanadorTorneo = pantallaGanadorTorneo

	def volver(self) :
		# self.setContentPane(pantallaInicial)
		print("placeholder")

	def getPantallaPerdedorTorneo(self):
		return self.pantallaPerdedorTorneo
