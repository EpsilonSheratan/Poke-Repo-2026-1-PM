class Pokemon:
    def __init__(self, tipo: str, nombre: str, vida: int = 10,
                 ataque: int = 1, defensa: float = 0.5,
                 nivel: int = 1, habilidad_especial: str = "ninguno"):

        self.tipo = tipo
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.habilidad_especial = habilidad_especial

    def attack(self, target, attack_power):
        damage = attack_power * self.ataque
        target.defender(damage)

    def defender(self, damage):
        reduced_damage = damage * (1 - self.defensa)
        self.vida -= reduced_damage

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibió {reduced_damage:.2f} de daño. Vida: {self.vida}")

    def evolucion(self, nuevo_nivel, nueva_habilidad):
        if nuevo_nivel > self.nivel:
            self.nivel = nuevo_nivel
            self.habilidad_especial = nueva_habilidad
            print(f"{self.nombre} evolucionó al nivel {self.nivel}")
        else:
            print("No puede evolucionar a un nivel menor")