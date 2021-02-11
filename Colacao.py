print("Hola, que tal? esto es un simulador de hacer colacao")

listo = input("Estás listo?: ")

if listo == "si" or listo == "sí":
    print("Perfecto, sigamos")
elif listo == "no":
    print("Bueno, no pasa nada, saliendo de la simulación...")
    exit()

print("Estás en la cocina y te diriges a ver si hay colacao")

levantarse = input("Quieres levantarte y mirar si hay colacao?: ")
if levantarse == "si" or "sí" or "vale" or "Vale" :
    print("Vas a ver si hay colacao...")
elif levantarse == "no" or "no quiero" :
        print("Vago...")
        exit()
a = input("Hay colacao?: ")
if a == "si" or "sí":
    print("Coges el colacao y lo haces")
if a == "No" or "No queda" or "no":
        print("Vas al super a comprar colacao...")
        print("...")
        print("---")
        print("...")
        print("Al salir del super, ha venido un coche y sin querer te ha dado, tienes varias opciones")
        print("Puedes hacerte el muerto o seguir andando")
b = input("Qué haces?: ")
if b == "hacerse el muerto":
    print("El conductor se pone muy nervioso y se da a la fuga,")
    print("Al haberse dado a la fuga el conductor te aplasta la pierna con las ruedas del coche")
    print("Alguien que estaba por la zona, llama a la ambulancia")
    print("Llegas al hospital y te amputan la pierna porque si no podrías morir")
    print("Te quedas pensando en la vida y piensas que podias haber seguido y que nada de esto hubiera ocurrido")
    print("Si hubieses seguido como si nada")
