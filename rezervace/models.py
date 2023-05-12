from django.db import models

class Rezervace(models.Model):
    idrezervace = models.PositiveIntegerField(max_length=50, verbose_name='ID rezervace', help_text='Zadejte ID rezervace', unique=True, blank=False, null=False)
    jmenoZakaznika = models.CharField(max_length=50, verbose_name='Jméno zákazníka', help_text='Zadejte jméno zákazníka', blank=False , null=False)
    prijmeniZakaznika = models.CharField(max_length=50, verbose_name='Příjmení zákazníka',
                                      help_text='Zadejte příjmení zákazníka', blank=False, null=False)
    datumRezervace = models.DateField(verbose_name='Datum rezervace', help_text='Zadejte datum začátku rezervace', blank=False, null=False)
    class Meta:
        ordering = ['idrezervace']
        verbose_name = 'Rezervace'
        verbose_name_plural = 'Rezervace'

    def __str__(self):
        return f'{self.idrezervace}'

class Zakaznik(models.Model):
    prijmeniZakaznika = models.CharField(max_length=50, verbose_name='Příjmení zákazníka', help_text='Zadejte příjmení zákazníka', blank=False, null=False)
    email = models.CharField(max_length=150, verbose_name='Email zákazníka', help_text='Zadejte email zákazníka', blank=False, null=False)
    telefon = models.IntegerField(max_length=9, verbose_name='Telefonní číslo zákazníka', help_text='Zadejte telefonní číslo zákazníka', blank=False, null=False)

    class Meta:
        ordering = ['prijmeniZakaznika']
        verbose_name = 'Zákazník'
        verbose_name_plural = 'Zákazníci'

    def __str__(self):
        return f'{self.prijmeniZakaznika}'


class Pokoj(models.Model):
    cisloPokoje = models.CharField(max_length=50, verbose_name='Číslo pokoje', help_text='Zadejte číslo pokoje', blank=False, null=False)

    class Meta:
        ordering = ['cisloPokoje']
        verbose_name = 'Pokoj'
        verbose_name_plural = 'Pokoje'

    def __str__(self):
        return f'{self.cisloPokoje}'
