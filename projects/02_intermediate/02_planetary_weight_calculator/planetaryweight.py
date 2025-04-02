# Milestone #2: Adding in All Planets

def main():

    earth_weight: float = float(input("Enter a weight on Earth: "))
    
    planet: str = input("Enter a planet: ")
    
    if planet == "Mercury":
        weight_factor: float = 0.376  
    elif planet == "Venus":
        weight_factor = 0.889  
    elif planet == "Mars":
        weight_factor = 0.378  
    elif planet == "Jupiter":
        weight_factor = 2.36  
    elif planet == "Saturn":
        weight_factor = 1.081  
    elif planet == "Uranus":
        weight_factor = 0.815  
    elif planet == "Neptune":
        weight_factor = 1.14   
    
    planet_weight: float = earth_weight * weight_factor
    
    planet_weight_rounded: float = round(planet_weight, 2)
    print(f"The equivalent weight on {planet}: {planet_weight_rounded}")

if __name__ == "__main__":
    main()