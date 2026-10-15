from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "カツカレー"
    def get_summary(self):
        return "安くて、カツが乗っていてうまい!!"
    def get_author(self):
        return "堤悠真"