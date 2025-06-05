🎵 Gotanno Love - Radio App con Discord Rich Presence

Una aplicación de escritorio sencilla creada con Python que te permite escuchar la estación de radio **Gotanno Love ❤️**, controlar el volumen, iniciar/detener la reproducción y mostrar tu actividad en Discord gracias a **Rich Presence**.

🚀 Características

- ✔ Interfaz gráfica con `Tkinter`
- ✔ Reproducción de radio online con `VLC`
- ✔ Control de volumen
- ✔ Botones de reproducción y parada
- ✔ Integración con Discord Rich Presence vía `pypresence`
- ✔ Ligera, simple y funcional


📦 Requisitos

- Python 3.8 o superior
- VLC Media Player instalado en tu sistema


📚 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/diraw0/Gotanno-Radio-Player
cd gotanno-love-radio
```

2. Instala las dependencias:

```bash
pip install python-vlc pypresence
```

3. Ejecuta la app:

```bash
python Gotanno-Player-0.5.py
```

🧠 Cómo funciona

- La app usa `python-vlc` para reproducir la URL de la radio en streaming.
- La interfaz está construida con `tkinter`, por lo que no requiere librerías externas para la GUI.
- Al reproducir, la app se conecta a Discord y actualiza tu estado con un mensaje personalizado (si Discord está abierto y en segundo plano).

🛠 Personalización

- Puedes cambiar la URL de la radio en la constante `RADIO_URL`.
- Para personalizar el Discord Rich Presence, edita el bloque `self.rpc.update(...)` en `connect_discord_presence()`.

⚠️ Notas

- Asegúrate de tener **Discord abierto** antes de reproducir, de lo contrario no se podrá establecer la conexión con Discord Rich Presence.
- Para evitar problemas de compilación recomiendo desactivar windows Defender durante el proceso de compilacion.
