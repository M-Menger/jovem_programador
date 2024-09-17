op = input("Escolha entre [T]riângulo, [Q]uadrado, [R]etangulo, [L]osango ou [C]írculo")

match op:
    case "T":
        print("Você escolheu Triângulo")
    case "Q":
        print("Você escolheu Quadrado")
    case "R":
        print("Você escolheu Retangulo")
    case "C":
        print("Você escolheu Círculo")
    case  "L":
        print("Você  escolheu Losango")
    case  default:
        print("opção invalida")
