import util as ut

def main():
    points = ut.get_points(ut.DATA_FILES[0])
    for point in points:
        print(point)

    
if __name__ == "__main__":
    main()
