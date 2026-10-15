from maps.GakushokuSample import GakushokuSample
from maps.tsudaSample import TsudaSample

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    GakushokuSample(), 
    TsudaSample(),
]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()