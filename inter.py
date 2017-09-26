import re

##NO OLVIDAR: importa el tipo en las variables asi que tener ojo con eso.

#crea una lista con el contenido del archivo de texto
# texto = open("codigo_rust.txt")


###

#expresiones regulares

declaracion = re.compile('let mut ([A-z]+_*[A-z]*) : (i16|i32|f64) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
asignacion = re.compile('([A-z]+_*[A-z]*) = (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+));')
operacion = re.compile('((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)));?')
casteo = re.compile('(\(([A-z]+_*[A-z]*) as (i16|i32|f64)\));?')
ctrl_if = re.compile('if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_elseif = re.compile('} else if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_else = re.compile('} else {')
fin = re.compile('}')
ctrl_while = re.compile('while ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
boolean = re.compile('([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))')
printeo = re.compile('println! \(([A-z]+_*[A-z]*)\);') 
funcioninit = re.compile('fn ([A-z]+_*[A-z]*) \(([A-z]+_*[A-z]*):(i16|i32|f64)\) - > (i16|i32|f64) {')
ret = re.compile('return (([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+));')
fun_main =re.compile('fn main \(\) {')










###########################MAIN###################
def main(codigo_rust):
	mn = {}
	texto = open(codigo_rust)
	for linea in texto:
		if funcioninit.match(linea):
			linea.strip().split()
    
