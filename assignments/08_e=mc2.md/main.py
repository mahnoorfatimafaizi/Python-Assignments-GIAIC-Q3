def main():
    C: float = 299792458  # m/s
    
    while True:

        mass: float = float(input("Enter kilos of mass: "))
        
        energy: float = mass * C ** 2
        
        print("e = m * C^2...")
        print("m =", mass, "kg")
        print("C =", C, "m/s")
        print(energy, "joules of energy!")

if __name__ == '__main__':
    main()