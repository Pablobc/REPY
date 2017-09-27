import re

##NO OLVIDAR: importa el tipo en las variables asi que tener ojo con eso.

#crea una lista con el contenido del archivo de texto
# texto = open("codigo_rust.txt")


###

#expresiones regulares

declaracion = re.compile('\s*let mut ([A-z]+_*[A-z]*) : (i16|i32|f64) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
asignacion = re.compile('\s*([A-z]+_*[A-z]*) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
operacion = re.compile('\s*((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))\s*(\+|\-)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)));?')
casteo = re.compile('\s*(\(([A-z]+_*[A-z]*) as (i16|i32|f64)\));?')
ctrl_if = re.compile('\s*if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_elseif = re.compile('\s*} else if ([A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_else = re.compile('\s*} else {')
fin = re.compile('\s*}')
ctrl_while = re.compile('\s*while ([A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
boolean = re.compile('(\s*[A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))')
printeo = re.compile('\s*println!\s*\(([A-z]+_*[A-z]*)\);') 
funcioninit = re.compile('fn ([A-z]+_*[A-z]*) \(([A-z]+_*[A-z]*):(i16|i32|f64)\) - > (i16|i32|f64) {')
ret = re.compile('\s*return\s*(([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+));')
fun_main =re.compile('fn main\(\) {')










###########################MAIN###################
texto = open("codigorust.txt", 'r')
for linea in texto:
	if re.match(declaracion,linea):
		print ("declaracion detectada")
	if re.match(asignacion,linea):
		print("asignacion detectada")
	if re.match(operacion,linea):
		print("operacion detectada")
	if re.match(casteo,linea):
		print("casteo detectado")
	if re.match(ctrl_if,linea):
		print("if detectado")
	if re.match(ctrl_elseif,linea):
		print("elseif detectado")
	if re.match(ctrl_else,linea):
		print ("else detectado")
	if re.match(ctrl_while,linea):
		print("while detectado")
	if re.match(fin,linea):
		print ("fin de control o funcion detectado")
	if re.match(boolean,linea):
		print("booleano detectado")
	if re.match(printeo,linea):
		print("print detectado")
	if re.match(funcioninit,linea):
		print("inicio de funcion detectada")
	if re.match(ret,linea):
		print("return detectado")
	if re.match(fun_main,linea):
		print("funcion main detectada")
texto.close()

    
