from django.db import models

class Rezervace(models.Model):
    idrezervace = models.PositiveIntegerField(verbose_name='ID rezervace', help_text='Zadejte ID rezervace', unique=True, blank=False, null=False)
    zakaznik = models.ForeignKey('Zakaznik', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Zákazník')
    pokoj = models.ForeignKey('Pokoj', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Pokoj')
    datumRezervace = models.DateField(verbose_name='Datum rezervace', help_text='Zadejte datum začátku rezervace', blank=False, null=False)
    class Meta:
        ordering = ['idrezervace']
        verbose_name = 'Rezervace'
        verbose_name_plural = 'Rezervace'

    def __str__(self):
        return f'{self.idrezervace}'

class Zakaznik(models.Model):
    jmenoZakaznika = models.CharField(max_length=50, verbose_name='Jméno zákazníka', help_text='Zadejte jméno zákazníka', blank=False, null=False, default='honza')
    prijmeniZakaznika = models.CharField(max_length=50, verbose_name='Příjmení zákazníka', help_text='Zadejte příjmení zákazníka', blank=False, null=False, default='honzík')
    email = models.CharField(max_length=150, verbose_name='Email zákazníka', help_text='Zadejte email zákazníka', blank=False, null=False)
    telefon = models.IntegerField(verbose_name='Telefonní číslo zákazníka', help_text='Zadejte telefonní číslo zákazníka', blank=False, null=False)
    profilovyObrazek = models.ImageField(upload_to='uploads/', default='uploads/defaultpfp.jpg')

    class Meta:
        ordering = ['prijmeniZakaznika']
        verbose_name = 'Zákazník'
        verbose_name_plural = 'Zákazníci'

    def __str__(self):
        return f'{self.prijmeniZakaznika}'


class Pokoj(models.Model):
    cisloPokoje = models.CharField(max_length=50, verbose_name='Číslo pokoje', help_text='Zadejte číslo pokoje', blank=False, null=False, unique=True)
    pocetPosteli = models.PositiveIntegerField(verbose_name='Počet postelí', help_text='Zadejte počet postelí', blank=False, null=False, default='1')

    class Meta:
        ordering = ['cisloPokoje']
        verbose_name = 'Pokoj'
        verbose_name_plural = 'Pokoje'

    def __str__(self):
        return f'{self.cisloPokoje}'
