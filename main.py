import error_surface_quadr as esq
import error_surface as es
import tests.plot_points as pp
import util as util


def main():
    esq.plot_fhalf_mse(util.DATA_FILES[1], 1000, (-5,5))
    esq.plot_lhalf_mse(util.DATA_FILES[1], 1000, (-5,5))


if __name__ == "__main__":
    main()
