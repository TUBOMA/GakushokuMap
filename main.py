from maps.GakushokuSample import GakushokuSample
from maps.tsudaSample import TsudaSample
from maps.TsuboiOsusume import TsuboiOsusume
from maps.TajiOsusume import TajiOsusume
from maps.Tsutsumi_osusume import Tsutsumi_osusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。

data = [GakushokuSample(), 
        TsuboiOsusume(), 
        TajiOsusume(),
        Tsutsumi_osusume(),
        TsudaSample(),]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()