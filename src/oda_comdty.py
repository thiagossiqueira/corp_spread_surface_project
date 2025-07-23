from datetime import datetime

from constants import DI_PATH, YIELD_PATH, ODA_COMDTY_GRAPHS_PATH, AUTHOR_CALCULATION_SOURCE
from graphs.plot_audit_3d import plot_audit_3d
from graphs.plot_heatmap import plot_heatmap
from graphs.plot_historical_yield_curve import plot_historical_yield_curve
from graphs.plot_line_spread import plot_line_spread
from graphs.plot_yield_curve_surface import plot_yield_curve_surface
from calcs.calc_surface import calc_surface
from calcs.calc_interpolate import calc_interpolate
from loads.load_bonds_static import load_bonds_static
from loads.load_yield_matrix import load_yield_matrix


def main():
    ylds = load_yield_matrix(YIELD_PATH)
    bonds_static = load_bonds_static(DI_PATH)

    surface = calc_surface(ylds, bonds_static)
    yc_table = calc_interpolate(surface)
    # put columns shortest → longest for nicer surfaces
    ordered_cols = ["1-month", "3-month", "6-month",
                    "1-year", "2-year", "3-year",
                    "5-year", "10-year", "30-year"]
    df_vis = yc_table[ordered_cols]


    surface_fig   = plot_yield_curve_surface(df_vis, AUTHOR_CALCULATION_SOURCE)
    heatmap_fig   = plot_heatmap(df_vis, AUTHOR_CALCULATION_SOURCE)
    history_fig   = plot_historical_yield_curve(df_vis, AUTHOR_CALCULATION_SOURCE)
    spread_fig    = plot_line_spread(df_vis, low="2-year", high="10-year",
                                     source_text=AUTHOR_CALCULATION_SOURCE)

    #print

    # show (inline in Jupyter or pop-up in a script)
    # surface_fig.show()

    audit_fig = plot_audit_3d(surface)

    str_datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    audit_fig.write_html(ODA_COMDTY_GRAPHS_PATH / f"{str_datetime_now}-audit_fig.html")
    surface_fig.write_html(ODA_COMDTY_GRAPHS_PATH / f"{str_datetime_now}-surface_fig.html")
    heatmap_fig.write_html(ODA_COMDTY_GRAPHS_PATH / f"{str_datetime_now}-heatmap_fig.html")
    history_fig.write_html(ODA_COMDTY_GRAPHS_PATH / f"{str_datetime_now}-history_fig.html")
    spread_fig.write_html(ODA_COMDTY_GRAPHS_PATH / f"{str_datetime_now}-spread_fig.html")

    # audit_fig.show()

    # heatmap_fig.show()
    # history_fig.show()
    # spread_fig.show()

if __name__ == "__main__":
    main()
