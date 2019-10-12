import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from cartopy.io.img_tiles import Stamen


def main():
    tiler = Stamen('terrain-background')
    #tiler = Stamen('toner')
    mercator = tiler.crs

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1, projection=mercator)
    ax.set_extent([-111.9, -108.2, 34.4, 36.9], crs=ccrs.PlateCarree())

    ax.add_image(tiler, 8)
    
    ax.plot(-109.221, 36.3061, 'bo', markersize=10, 
            transform=ccrs.Geodetic())
    ax.text(-109.221, 36.35, 'Tsaile', 
            transform=ccrs.Geodetic(), fontsize=16)

    plt.show()


if __name__ == '__main__':
    main()