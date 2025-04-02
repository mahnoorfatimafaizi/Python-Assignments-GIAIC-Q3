def main():

    earth_weight: float = float(input("Enter a weight on Earth: "))
    
    mars_weight: float = earth_weight * 0.378
    
    mars_weight_rounded: float = round(mars_weight, 2)
    print("The equivalent on Mars:", mars_weight_rounded)

if __name__ == "__main__":
    main()