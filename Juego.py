import math
    def juego_angry_birds():
    print("Bienvenido al juego Angry Birds")
    print("Tu objetivo es ajustar los parámetros para que el pájaro impacte con el edificio.")
    print("\nEstas son las fórmulas usadas en el juego:")
    print("- Energía del resorte: E_s = 1/2 * k * x^2")
    print("- Velocidad inicial: v_0 = sqrt(2 * E_s / m)")
    print("- Trayectoria: x(t) = v_0 * cos(θ) * t, y(t) = v_0 * sin(θ) * t - 1/2 * g * t^2")
    print("- Conservación de la energía cinética en choques: ΔE = 1/2 * m * (v_i^2 - v_f^2)")
    
    g = 9.81  # Gravedad (m/s^2)
    k = 1000  # Constante del resorte (N/m)
    altura_edificio = 10  # Altura del edificio (m)
    distancia_edificio = 50  # Distancia al edificio (m)
    masa_edificio = 500  # Masa del edificio (kg)

    while True:
        masa_pajaro = float(input("\nIngresa la masa del pájaro (kg): "))
        angulo = float(input("Ingresa el ángulo de lanzamiento (grados): "))
        compresion_resorte = float(input("Ingresa cuanto se comprime el resorte (m): "))

        angulo_rad = math.radians(angulo)  

        energia_resorte = 0.5 * k * compresion_resorte**2  # Fórmula: E_s = 1/2 * k * x^2
        velocidad_inicial = math.sqrt(2 * energia_resorte / masa_pajaro)  # Fórmula: v_0 = sqrt(2 * E_s / m)

        print(f"\nFórmulas aplicadas:")
        print(f"1. Energía del resorte: E_s = 1/2 * k * x^2 = 1/2 * {k} * {compresion_resorte}^2")
        print(f"   Resultado: E_s = {energia_resorte:.2f} J")  # Conservación de la energía
        print(f"2. Velocidad inicial: v_0 = sqrt(2 * E_s / m) = sqrt(2 * {energia_resorte:.2f} / {masa_pajaro})")
        print(f"   Resultado: v_0 = {velocidad_inicial:.2f} m/s")  # Conservación de la energía

        t = 0
        dt = 0.01  # Incremento de tiempo en segundos 
        impacto = False
        max_x = 0

        while True:
            x = velocidad_inicial * math.cos(angulo_rad) * t  # Componente horizontal
            y = velocidad_inicial * math.sin(angulo_rad) * t - 0.5 * g * t**2  # Componente vertical

            max_x = max(max_x, x)  # Distancia máx. en el eje x 

            if distancia_edificio - 1 <= x <= distancia_edificio + 1 and 0 <= y <= altura_edificio:
                print("\n¡El pájaro impactó el edificio!")
                impacto = True
                break
            if y < 0:
                break
            t += dt 
        if impacto:
            velocidad_final = 0  
            energia_cinetica_inicial = 0.5 * masa_pajaro * velocidad_inicial**2  # Conservación de la energía cinética
            energia_cinetica_final = 0.5 * masa_edificio * velocidad_final**2  # Energía después del choque
            energia_perdida = energia_cinetica_inicial - energia_cinetica_final

            print("\nFórmula de energía cinética aplicada en el choque:")
            print(f"ΔE = 1/2 * m * (v_i^2 - v_f^2) = 1/2 * {masa_pajaro} * ({velocidad_inicial:.2f}^2 - {velocidad_final}^2)")
            print(f"Energía cinética inicial del pájaro: {energia_cinetica_inicial:.2f} J")
            print(f"Energía transferida al edificio: {energia_perdida:.2f} J")
        else:
            print("\nEl pájaro no alcanzó el edificio.")
            print(f"Distancia máxima alcanzada: {max_x:.2f} m")

        reiniciar = input("\n¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if reiniciar != "sí":
            print("¡Gracias por jugar!")
            break
juego_angry_birds()

