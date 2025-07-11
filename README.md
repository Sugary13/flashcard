# 📚 Flashy - Aplicación de Tarjetas en Francés 🇫🇷

Flashy es una aplicación de aprendizaje de vocabulario francés construida con Python, Tkinter y Pandas. Permite al usuario practicar palabras en francés y marcar las que ya ha aprendido, guardando el progreso entre sesiones.


---

## 🚀 Características

- Muestra una palabra en francés y revela su traducción en inglés después de 3 segundos.
- Guarda el progreso del usuario en `words_to_learn.csv`.
- Permite eliminar palabras conocidas para que no se repitan.
- Interfaz gráfica intuitiva construida con `tkinter`.
- Lee palabras desde un archivo CSV.

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – Interfaz gráfica
- [Pandas](https://pandas.pydata.org/) – Manejo de datos CSV
- `random` y `os` – Funcionalidad básica de Python

---

## 📂 Estructura del proyecto

flashy/
├── data/

│ ├── french_words.csv # Lista original de palabras

│ └── words_to_learn.csv # Progreso del usuario (generado automáticamente)

├── images/

│ ├── card_front.png

│ ├── card_back.png

│ ├── right.png

│ └── wrong.png

├── main.py # Código principal de la aplicación

└── README.md # Este archivo


---

## ▶️ Cómo usar

1. Asegúrate de tener Python instalado (`python --version`).
2. Instala las dependencias necesarias:

```bash
pip install pandas
```
ejecutar programa

python main.py

🔁 Reiniciar progreso
Si deseas reiniciar el progreso, simplemente elimina el archivo words_to_learn.csv. Al iniciar de nuevo, se cargará el archivo original french_words.csv.


