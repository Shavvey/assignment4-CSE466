import error_surface_quadr as esq
import error_surface as es
import util as util


def main():
    esq.plot_full_mse(util.DATA_FILES[0], 1000, (-5, 5))


if __name__ == "__main__":
    main()
