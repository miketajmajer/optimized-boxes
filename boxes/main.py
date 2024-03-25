from boxes import Box

def main():
    print("Boxes main executing.")

    b = Box(10, 20, 30)

    print(b.volume)

if __name__ == '__main__':
    main()