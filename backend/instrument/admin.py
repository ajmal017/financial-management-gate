from django.contrib import admin
from wallet.models import Wallet, Moviment
from instrument.models import Instrument, History
# Register your models here.
class AdminInstrument(admin.ModelAdmin):
    list_display = ["tckrSymb", "sgmtNm", "mktNm", "sctyCtgyNm", "isin", "cFICd", "crpnNm", "corpGovnLvlNm"] # aqui vc precisa colocar as colunas que vc quer ver
    search_fields = ["tckrSymb"]
    list_filter = ["sctyCtgyNm"]

    class Meta:
        verbose_name = "Admin Instrument"
        verbose_name_plural = "Admin Instruments"
        #ordering = ['tckrSymb']

class AdminHistory(admin.ModelAdmin):
    list_display = ["instrument", "date", "open", "high", "low", "close", "adj_close", "volume", "lastUpdate"] # aqui vc precisa colocar as colunas que vc quer ver
    search_fields = ["date","instrument__tckrSymb", "instrument__crpnNm"]
    list_filter = ["instrument"]

    class Meta:
        verbose_name = "Admin Instrument"
        verbose_name_plural = "Admin Instruments"
        ordering = ["date"]

admin.site.register(Instrument, AdminInstrument)
admin.site.register(History, AdminHistory)