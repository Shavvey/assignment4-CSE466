import error_surface as es
import util as util
import plot_points

def main():
    # es.plot_full_mse(util.DATA_FILES[1], 1000, (-5,5))
    plot_points.plot_points(util.DATA_FILES[0])
    
    
    
    
if __name__ == "__main__":
    main()
