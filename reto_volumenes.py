import math

def volumen_cilindro(height, radio):
    volumen = (math.pi)*(radio**2)*(height)
    return volumen

def area_base(radio):
    areab = (math.pi)*(radio**2)
    return areab

def volumen_esfera(radio):
    volumenesf = (4/3)*(math.pi)*(radio**3)
    return volumenesf

def volumen_cono(radio, height):
    volumencono = (1/3)*(math.pi)*(radio**2)*(height)
    return volumencono

def run():
    print("""Let's calculate the volumen of the figure that you choose:
    1. Cylinder
    2. Sphere
    3. Cone """)
    opcion = int(input('Elige una opción:  '))
    if opcion == 1: 
        height = int(input('Insert the height of your cylinder:  '))
        radio = int(input('Insert the radio of your cylinder: '))
        vol = volumen_cilindro(height,radio)
        area = area_base(radio)
        print('Te volumen of your cylinder is:   ' + str(vol))
        print('The area of the base of your cylinder is:  ' + str(area))
    elif opcion == 2:
        radio = int(input('Insert the radio of your sphere: '))
        volesf = volumen_esfera(radio)
        print('The volume of your sphere is: ' + str(volesf))
    elif opcion == 3: 
        height = int(input('Insert the height of your cone:  '))
        radio = int(input('Insert the radio of your cone: '))
        volcono = volumen_cono(radio,height)
        print('The volumen of your cone is: ' + str(volcono))
    else:
        print('Thank you, try a different option')

if __name__ == '__main__':
    run()