def CtoFConverter():
    while True:
        try:
            cTemp = float(input("Please enter C degree: "))
            if cTemp:
                fTemp = (9*cTemp/5) + 32
                print(f"{cTemp} C is converted to {fTemp} F")
                break
        except:
            print("Wrong input or input is empty!")


def main():
    CtoFConverter()


if __name__ == "__main__":
    main()
