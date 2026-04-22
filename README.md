# POKE

# Resolución Actividad 1: Clase Pokemon 
## Objetivos 
1. Desarrollar la clase Pokemon.
2. Definir 10 características que posee la clase Pokemon.
3. Definir 3 Acciones que puede realizar la clase Pokemon.
4. Proponer su estructura constructor.
5. Elaborar un diagrama tipo UML inicial de la clase.
6. Los atributos tengan sentido dentro del modelo.
7. Los métodos sean realistas e implementables.

> Cómo cumplimiento de los objetivos se hace entrega del presente documento, donde se trazó todo el curso y puesta en marcha del procedimiento. 
---

## Tabla de contenidos
- [POKE](#poke)
- [Resolución Actividad 1: Clase Pokemon](#resolución-actividad-1-clase-pokemon)
  - [Objetivos](#objetivos)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Contextualizacion](#contextualizacion)
  - [Diseño de clase](#diseño-de-clase)
      - [Constructor de clase pokemon](#constructor-de-clase-pokemon)
  - [Diagrama UML](#diagrama-uml)


## Contextualizacion

Para dar un buen inicio, se debe comprender el cómo se usaría la teoría de Pokémon y por qué se puede abstraer y relacionar con la Programación Orientada a Objetos.

## Diseño de clase 

A partir de lo descrito, Basándonos en la franquicia y videojuegos de pokemon, se propone cómo clase principal para nuestro diseño la entidad *POKEMON*, abstraida con atributos generales cómo: 

- ***Puntos de vida*** : Al ser una entidad viva capacitada para combatir, nos basamos en los puntos de vida cómo parametro de control, el cuál cambiara su valor constantemente durante un combate.
- ***Tipo*** : Atributo general que define los diversos caminos de cómo interactuará un pokemon en el entorno.
- ***Nombre***: Puesto que todo objeto necesita un identificador legible para el usuario y diferenciable de todo pokemon.
- ***Aspecto*** : Característica que permite visualizar con mayor detalle a cada objeto.
- ***Fuerza base***: Determina el daño que puede causar
- ***Nivel*** : Atributo pivote, capaz de moderar los atributos generales del pokemon, modificable a partir de una acción de mejora que posea el pokemon.
- ***Habilidad** especial* : Como medio de ataque el pokémon poseerá una habilidad individual que altere la fuerza y resistencia del pokemon, generando mayor diversidad y campo de juego en las relaciones.
- ***Ataques***  : Acciones consecutivas en el campo de batalla, cada una poseerá una característica especial, aumentando la variabilidad de sus estadísticas.
- ***Evolución*** : Medida importante que rastrea el desarrollo del objeto, capaz de modificar su atributo *Nivel* a partir de una acción controlada.
- ***Defensa*** : Valor numérico de resistencia inherente que actúa como reductor del impacto recibido por una Fuerza base o Habilidad especial externa

Finalmente, aunque muchas características sean bienvenidas, se consideran cómo las fundamentales y generales para la relación de un pokemon en el mundo virtual.

Por otro lado, a partir de estás características, el pokemon se comportará en un ambiente de combate con acciones que todos los objetos poseen:  
- ***Attack(target: Pokemon, attack_power: float): void***  
Acción fundamental para la interacción entre objetos. Reduce los puntos de vida del objetivo en función del poder de ataque.  
***Parametros***:  
-target (Pokemon): Pokemon que recibirá el ataque.  
-attack_power (float): Cantidad de daño que se aplicará al objetivo.  
  
- ***Defend(damage_received: float): void***  
Acción que permite al pokemon reducir el daño recibido durante un ataque, utilizando su capacidad de defensa.  
***Parámetros***:  
damage_received (float):  Cantidad de daño que el pokemon recibe antes de aplicar la defensa.  

- ***Evolve(new_level: int, new_ability: str): void***  
Acción que permite al pokemon aumentar su nivel y mejorar sus estadísticas, pudiendo también adquirir una nueva habilidad especial.  
***Parámetros***:  
-new_level (int): Nivel al que evolucionará el pokemon.  
-new_ability (str): Nueva habilidad que puede adquirir al evolucionar.  

---

#### Constructor de clase pokemon


```bash
- CONSTRUCTOR(health_points: int, base_strength: float, defense_capacity: float,
            level: int, type: str, appearance: str, special_ability: str)
```

--- 

## Diagrama UML
```mermaid
classDiagram
Trainer "1" *-- "1..6" Pokemon: posee y gestiona
Pokemon "1" *-- "1" Stats
Pokemon "1" *-- "1" Moveset
Moveset "1" o-- "4" Move: agrega
CombatEngine --> Pokemon
CombatEngine --> Move
CombatEngine --> TypeRelations

%% Esta es una clase que posee y gestiona la clase Pokemon.%%
class Trainer{
  -name: str
  -team: list[Pokemon]

  +_init_(name: str, team: list)
  +add_pokemon(pokemon: Pokemon)
  +get_active_pokemon()
  +switch_pokemon(pokemon_index: int)
}

class Pokemon{
    -name: str
    -type: str
    -stats: list
    -level: int
    -appearance: str
    -moveset: list
    -evolution_stage: int

    +_init_(name: str, type: str, stats: list, level: int, appearance: str, special_ability: str) 
    +move(target: Pokemon, move_power: float) void
    +defend(damage_received: float) void
    +evolve(new_level: int, new_ability: str): void
}

%% El constructor de la clase Pokemon deberá recibir una instancia de la clase Stats o los valores para crearla.%%
class Stats{
    -hp: int
    -attack: float
    -defense: float
    -speed: int
    -special_attack: float

    +_init_(hp: int, attack: float, defense: float, speed: int, special_attack: float)
}

%% Clase Move que mandará 4 movimientos a la clase Moveset.%%
class Move{
    -name: str
    -type: str
    -power: float
    -accuracy: float
    -pp: int

    +_init_(name: str, type: str, power: float, accuracy: float)
    +calculate_damage() float
}

%% Clase Moveset: Gestionará los cuatro movimientos (objetos Move) que enviará a la calse Pokemon.%%
class Moveset{
    -moves: list
}

%% Esta función recibirá al attacker (Pokémon), al defender (Pokémon) y al move (Movimiento).%%
class CombatEngine{
    +calculate_damage() 
    %% Dentro de calculate_damage, debe usar (llamar a) los objetos y sus métodos: %%
    %%El nivel y ataque del attacker (de pokemon.level y pokemon.stats).La defensa del defender (de pokemon.stats).%%
    %%El poder del movimiento (de move.power).%%
    %%La efectividad del tipo (llamando al get_effectiveness de la instancia de TypeRelations).%%
    +hit_accuracy() %% Está función recibirá accuracy para calcular si un movimiento acierta o falla.%%
}

%% Clase TypeRelations: Utiliza el atributo de la clase Pokemon "type: str" para gestionar en un diccionario de diccionarios que definan las interacciones entre tipos.%%
%% Una clase TypeRelations robusta, sin dependencias externas, lista para que el CombatEngine la consuma.%%
class TypeRelations{
    -fire_type: bool
    -water_type: bool
    -grass_type: bool

    +get_effectiveness(attack_type: str, defender_types: list[str]) float
}

%%Clases hijas de la clase Pokemon.%%
Pokemon <|-- FirePokemon
Pokemon <|-- WaterPokemon
Pokemon <|-- GrassPokemon

class FirePokemon{
    -type$: str = "fire_type"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}
class WaterPokemon{
    -type$: str = "water_type"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}
class GrassPokemon{
    -type$: str = "grass_type"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}

Field "1" o-- "2" Pokemon
Field --> CombatEngine

%% La clase Field gestionará los dos Pokémon activos (que ahora pueden ser FirePokemon, WaterPokemon, etc.), los turnos y las condiciones de victoria.%%
class Field{
    -active_pokemon: list[Pokemon]
    +resolve_turn()
    %%Determina qué Pokemon ataca primero basandose en la velocidad de sus stats.%%
    +execute_attack()
    %%Llamará al CombatEngine para obtener el daño y lo aplicará al HP del Pokémon defensor.%%
}
```
Se utiliza los tres metodos principales de ataque, defensa y evolucionar, con sus respectivos atributos para controlar el comportamiento del pokemon en el entorno de combate, además de los atributos generales que caracterizan a cada pokemon.

Siendo valido que se puedan usar estos metodos, aunque en el futuro se puedan agregar más, pero estos son los generales para la interacción entre pokemones.
