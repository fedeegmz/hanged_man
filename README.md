# Hanged Man (Juego del Ahorcado)

Un juego clásico del ahorcado implementado en Python con arquitectura hexagonal.

## Descripción

Hanged Man es una implementación del clásico juego del ahorcado en la consola. El juego consiste en adivinar una palabra
elegida aleatoriamente letra por letra. El jugador tiene un número limitado de intentos para adivinar la palabra
completa, dependiendo del nivel de dificultad seleccionado.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal (versión >=3.11)
- **uv**: Herramienta para gestionar dependencias y entornos virtuales
- **Arquitectura Hexagonal**: Patrón de diseño para separar la lógica de negocio de la infraestructura

## Arquitectura Hexagonal

El proyecto sigue la arquitectura hexagonal (también conocida como "Ports and Adapters"), que divide la aplicación en
tres capas:

1. **Dominio**: Contiene las entidades y reglas de negocio centrales
    - `app/domain/`: Clases como `Word`, `Level`, y la interfaz `GameState`

2. **Aplicación**: Contiene la lógica de la aplicación
    - `app/application/`: Clase `Application` que implementa la lógica del juego

3. **Infraestructura**: Contiene adaptadores para interactuar con el mundo exterior
    - `app/infrastructure/`: Implementaciones concretas como `Console`, `Game`, `GameStateImpl`, y `WordRepository`

Esta arquitectura permite una clara separación de responsabilidades y facilita las pruebas y el mantenimiento.

## Estructura del Proyecto

```
hanged_man/
├── app/
│   ├── application/
│   │   └── application.py
│   ├── domain/
│   │   ├── game_state.py
│   │   ├── level.py
│   │   └── word.py
│   └── infrastructure/
│       ├── console.py
│       ├── game.py
│       ├── game_state_impl.py
│       └── word_repository.py
├── data/
│   └── words.txt
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Instalación

1. Asegúrate de tener Python 3.11 o superior instalado
2. Clona este repositorio:
   ```
   git clone https://github.com/fedeegmz/hanged_man.git
   cd hanged_man
   ```
3. Instala uv si aún no lo tienes:
   ```
   pip install uv
   ```
4. Crea un entorno virtual e instala las dependencias:
   ```
   uv sync
   source .venv/bin/activate
   ```

## Cómo Jugar

1. Ejecuta el juego:
   ```
   uv run main.py
   ```
2. Sigue las instrucciones en pantalla:
    - Se mostrará un mensaje de bienvenida
    - Selecciona un nivel de dificultad
    - Adivina la palabra letra por letra

## Niveles de Dificultad

El juego ofrece cuatro niveles de dificultad:

1. **Nivel 1**: La primera y última letra de la palabra se revelan automáticamente.
2. **Nivel 2**: Tienes un límite de intentos igual a 3 veces la longitud de la palabra.
3. **Nivel 3**: Tienes un límite de intentos igual a 2 veces la longitud de la palabra.
4. **Nivel DIOS**: Tienes un límite de intentos igual a la longitud de la palabra.

## Reglas del Juego

- Solo puedes ingresar letras en minúscula
- Debes adivinar la palabra completa antes de quedarte sin intentos
- El juego termina cuando:
    - Adivinas todas las letras de la palabra (¡Ganaste!)
    - Agotas todos tus intentos (¡Perdiste!)
