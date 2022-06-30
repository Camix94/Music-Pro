# MusicPro
Super admin user:
=
- Username: admin
Pass:123

URLS: 
=
- Api:'api/'
- Index:' '
- contacto:'contactanos'
- Blog:'blog'
- Productos:'productos'
- About:'sobrenuestrosproductos'

LOGINS:
=
- Cliente: Camila pass: pelicanoprueba1
- Administrador:  Admin pass: 123
- Contador: Contador pass: Pelicanoprueba1
- Bodeguero: Bodeguero pass: Pelicanoprueba1
- Vendedor: Vendedor pass: Pelicanoprueba1

POSIBLES PROBLEMAS:
=
- En caso de problemas con la base de datos ejecutar: python manage.py migrate --run-syncdb

INSTRUCCIONES PARA EL TESTING (Python):
=
- Entrar a la carpeta Test desde el CMD
- Ejecutar comando: pip install selenium
- Ejecutar comando: pip install pytest
- Tener el archivo chromedriver.exe (verifique que la versión que ya está en la carpeta es la que corresponde a su navegador. La que está es la versión Chrome 103.0.5060.66 )
- Ejecutar comando: pytest

INSTRUCCIONES PARA EL TESTING (Selenium IDE):
=
- Descargar Selenium IDE para su navegador
- Abrir Selenium IDE desde su navegador
- Abrir proyecto "Test_MusicPro" que está en la carpeta Test
- Levantar servidor desde CMD 
- Ejecutar las pruebas
