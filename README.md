# 🛡️ Offensive Language Detection



Aplicación experimental de  *detección automática de lenguaje ofensivo y discurso de odio* mediante técnicas de procesamiento de lenguaje natural (NLP).



El proyecto utiliza modelos de lenguaje preentrenados para analizar textos en español e inglés y determinar si contienen contenido potencialmente ofensivo.



## 🚀 Características



*Detección automática del idioma.
* Soporte para español e inglés.
* Clasificación de contenido mediante modelos NLP preentrenados.

* Cálculo de confianza de la predicción.

* Umbral configurable de confianza.

  Interfaz web desarrollada con Streamlit.

  Procesamiento local de los textos introducidos en la aplicación.



## 🧠 Modelos utilizados



### Español



`pysentimiento/robertuito-hate-speech`



Modelo especializado en la detección de discurso de odio en español.



 ### Inglés



`cardiffnlp/twitter-roberta-base-offensive`



Modelo basado en RoBERTa orientado a la detección de lenguaje ofensivo en contenido procedente de redes sociales.



Los modelos son    *preentrenados* y no han sido entrenados desde cero como parte de este proyecto.



 ## 🏗️ Arquitectura



```text

Usuario

&#x20;  │

&#x20;  ▼

Streamlit

&#x20;  │

&#x20;  ├── Detección de idioma

&#x20;  │

&#x20;  ├── Modelo NLP español

&#x20;  │

&#x20;  └── Modelo NLP inglés

&#x20;  │

&#x20;  ▼

Clasificación

&#x20;  │

&#x20;  ▼

Resultado + confianza

```



 ## 🛠️ Tecnologías



 * Python

 * Streamlit

 * Hugging Face Transformers

 * PyTorch

 * NLP

 * Langdetect



 ## 📁 Estructura



```text

Offensive-Language-Detection/

│

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

```



 ## ⚙️ Instalación



Clonar el repositorio:



```bash

git clone https://github.com/Vicenayarza/Offensive-Language-Detection.git

cd Offensive-Language-Detection

```



Crear un entorno virtual:



```bash

python -m venv .venv

```



Activar el entorno virtual en Windows:



```powershell

.  .venv  Scripts  Activate.ps1

```



Instalar las dependencias:



```bash

pip install -r requirements.txt

```



Ejecutar la aplicación:



```bash

streamlit run app.py

```



La primera ejecución puede tardar más debido a la descarga de los modelos de NLP.



 ## 🔐 Consideraciones de seguridad



Este proyecto forma parte de un trabajo académico relacionado con  *ciberseguridad, análisis de contenido y redes sociales*.



Se han tenido en cuenta las siguientes prácticas:



 * No almacenar credenciales en el repositorio.

 * No incluir claves API.

 * No incluir información sensible en el código.

 * Uso de `.gitignore` para evitar archivos locales y entornos virtuales.

 * Uso de modelos externos mediante sus identificadores públicos.

 * Procesamiento experimental de los textos introducidos por el usuario.



 ## ⚠️ Limitaciones



Los resultados son probabilísticos y no deben considerarse una decisión definitiva sobre el contenido analizado.



El sistema puede presentar errores debido a:



 * Ironía o sarcasmo.

 * Contexto insuficiente.

 * Lenguaje coloquial.

 * Errores ortográficos.

 * Expresiones ambiguas.

 * Diferencias culturales.

 * Limitaciones propias de los modelos utilizados.



Actualmente la aplicación está preparada para español e inglés.



 ## 🎓 Contexto académico



El proyecto procede de un trabajo académico relacionado con el análisis de lenguaje ofensivo en redes sociales y técnicas de inteligencia artificial aplicadas a la ciberseguridad.



La versión publicada en este repositorio ha sido reorganizada para presentar el proyecto de forma independiente, reproducible y orientada a portfolio profesional.



 ## 👨‍💻 Autor



*Vicente Ayarza*



Ingeniero Informático · Máster en Ciberseguridad



GitHub:  [Vicenayarza](https://github.com/Vicenayarza)



