import json

# Lista de preguntas y respuestas para un posible ingresante de Ingenieria en Informatica
preguntas_respuestas = {
    "preguntas_y_respuestas": [
        {
            "pregunta": "Que materias se estudian en Ingenieria en Informatica?",
            "respuesta": "En Ingenieria en Informatica se estudian materias como programacion, bases de datos, redes de computadoras, inteligencia artificial, sistemas operativos, redes neuronales y estructura de datos, entre otras."
        },
        {
            "pregunta": "Cuanto dura la carrera de Ingenieria en Informatica?",
            "respuesta": "La duracion de la carrera es de 5 anios."
        },
        {
            "pregunta": "Necesito tener conocimientos previos de programacion?",
            "respuesta": "No es necesario tener conocimientos previos, aunque puede ser util. Talque las asignaturas comienzan desde lo basico, pero es importante tener interes en aprender."
        },
        {
            "pregunta": "Cuales son las salidas laborales para un Ingeniero en Informatica?",
            "respuesta": "Los egresados pueden trabajar como desarrolladores de software, analistas de sistemas, administradores de bases de datos, ingenieros de redes, expertos en seguridad informatica, entre otros."
        },
        {
            "pregunta": "Es una carrera dificil?",
            "respuesta": "La carrera de Ingenieria en Informatica puede ser exigente, especialmente en areas como matematicas y programacion, pero con dedicacion y practica, es posible superar los desafios."
        },
        {
            "pregunta": "Que lenguajes de programacion se aprenden?",
            "respuesta": "Algunos de los lenguajes de programacion mas comunes que se aprenden en la carrera son Python, Java ,C , C++, C#, JavaScript, PHP, SQL."
        },
        {
            "pregunta": "Se requieren habilidades matematicas avanzadas?",
            "respuesta": "Si, las matematicas son una parte importante de la carrera, especialmente en areas como algoritmos, estructuras de datos y criptografia. Sin embargo, las habilidades matematicas se van desarrollando durante la carrera."
        },
        {
            "pregunta": "Que tipo de proyectos se realizan durante la carrera?",
            "respuesta": "Los proyectos varian desde la creacion de aplicaciones web y moviles, hasta el desarrollo de algoritmos avanzados, simulaciones y sistemas embebidos."
        },
        {
            "pregunta": "Cual es la diferencia entre Ingenieria en Informatica y Ciencias de la Computacion?",
            "respuesta": "Ingenieria en Informatica se enfoca mas en la aplicacion practica de la tecnologia, incluyendo hardware y software, mientras que Ciencias de la Computacion se centra mas en la teoria, los algoritmos y la investigacion cientifica en computacion."
        },
        {
            "pregunta": "Que habilidades blandas son importantes en la carrera?",
            "respuesta": "Ademas de las habilidades tecnicas, habilidades blandas como la resolucion de problemas, el trabajo en equipo, la comunicacion efectiva y la gestion del tiempo son esenciales para tener exito en Ingenieria en Informatica."
        },
        {
            "pregunta": "Que tipo de empresas contratan Ingenieros en Informatica?",
            "respuesta": "Empresas de tecnologia, bancos, aseguradoras, startups, empresas de telecomunicaciones, organismos gubernamentales y consultoras tecnicas son algunos de los lugares que contratan Ingenieros en Informatica."
        },
        {
            "pregunta": "Es posible trabajar mientras estudio la carrera?",
            "respuesta": "Si, muchos estudiantes encuentran trabajo como pasantes o en puestos de nivel inicial durante la carrera. Sin embargo, la gestion del tiempo es clave para equilibrar estudio y trabajo."
        },
        {
            "pregunta": "Hay opciones de especializacion dentro de la carrera?",
            "respuesta": "Si, puedes especializarte en areas como inteligencia artificial, ciencia de datos, ciberseguridad, desarrollo de software, redes, entre otras."
        },
        {
            "pregunta": "Cual es la diferencia entre Ingenieria en Informatica y Sistemas?",
            "respuesta": "Ingenieria en Informatica se enfoca mas en el desarrollo de software, programacion y las bases teoricas de la computacion, mientras que Ingenieria en Sistemas incluye tambien el estudio de procesos y la gestion de sistemas complejos en una organizacion, abarcando tanto tecnologia como gestion."
        },
        {
            "pregunta": "Cual es la diferencia entre Ingenieria en Informatica y Ingenieria en Inteligencia Artificial?",
            "respuesta": "Ingenieria en Informatica cubre un amplio espectro de areas de tecnologia, incluyendo el desarrollo de software y redes, mientras que Ingenieria en Inteligencia Artificial esta mas enfocada en el desarrollo de algoritmos y sistemas que permiten a las maquinas aprender y tomar decisiones de manera automatica, usando tecnicas avanzadas de aprendizaje automatico y procesamiento de datos."
        },
        {
            "pregunta": "Que diferencia hay entre desarrollo web y desarrollo de software en Ingenieria en Informatica?",
            "respuesta": "El desarrollo web se enfoca en crear aplicaciones accesibles desde navegadores web, mientras que el desarrollo de software abarca una mayor gama de aplicaciones, incluyendo software de escritorio, aplicaciones moviles y sistemas embebidos."
        },
        {
            "pregunta": "Que areas de especializacion puedo elegir en Ingenieria en Informatica?",
            "respuesta": "Dependiendo de la universidad, puedes especializarte en areas como ciencia de datos, inteligencia artificial, ciberseguridad, desarrollo de videojuegos, desarrollo de software, redes y sistemas distribuidos."
        },
        {
            "pregunta": "Cual es la importancia de las bases de datos en Ingenieria en Informatica?",
            "respuesta": "Las bases de datos son fundamentales para almacenar, organizar y gestionar grandes cantidades de informacion de manera eficiente. Los ingenieros en informatica aprenden a diseñar, implementar y optimizar bases de datos para distintas aplicaciones."
        },
        {
            "pregunta": "Que son los sistemas distribuidos en Ingenieria en Informatica?",
            "respuesta": "Los sistemas distribuidos son un area que estudia como varios equipos o servidores pueden trabajar juntos para realizar tareas compartidas, lo que es esencial para aplicaciones escalables como los servicios en la nube."
        },
        {
            "pregunta": "Que importancia tiene la ciberseguridad en Ingenieria en Informatica?",
            "respuesta": "La ciberseguridad es vital para proteger los sistemas y la informacion de posibles ataques o accesos no autorizados. Los ingenieros en informatica aprenden a implementar medidas de seguridad y criptografia para proteger datos sensibles."
        },
        {
            "pregunta": "Que rol juega la inteligencia artificial en Ingenieria en Informatica?",
            "respuesta": "La inteligencia artificial es un campo de creciente importancia en Ingenieria en Informatica, con aplicaciones en reconocimiento de voz, vision por computadora, sistemas de recomendacion, y automatizacion de tareas complejas."
        },
        {
            "pregunta": "Es posible trabajar en el extranjero como ingeniero en informatica?",
            "respuesta": "Si, la demanda de ingenieros en informatica es global, y con el conocimiento de tecnologias y lenguajes de programacion estandarizados, muchos profesionales pueden encontrar oportunidades de trabajo en el extranjero o trabajar de manera remota."
        },
        {
            "pregunta": "Como es el campo del desarrollo de videojuegos en Ingenieria en Informatica?",
            "respuesta": "El desarrollo de videojuegos es una opcion para los ingenieros en informatica, que incluye el desarrollo de motores graficos, inteligencia artificial para personajes, y optimizacion del rendimiento en diversas plataformas."
        }
    ]
}

# Guardar el diccionario en un archivo JSON
with open('preguntas_ingresante_ingenieria_informatica.json', 'w') as archivo:
    json.dump(preguntas_respuestas, archivo, indent=4)

print("Archivo JSON creado con exito.")

