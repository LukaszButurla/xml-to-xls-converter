

class Convert_to_price_list:
    
    def __init__(self):      
        
        
        self.formStart = """<?xml version="1.0" encoding="UTF-8"?>

<ROOT xmlns="http://www.cdn.com.pl/optima/cennik">


<TOWARY>

<WERSJA>1.00</WERSJA>

<BAZA_ZRD_NAZWA>DORADCY PODATKOWI PIOTR MACIEJEWSKI , MONIKA MACIE</BAZA_ZRD_NAZWA>"""
        
        self.formEnd = """
        </TOWARY>
        </ROOT>
"""
        
        self.form = """
        <TOWAR>
<KOD>{code}</KOD>
<KOD_H>{code2}</KOD_H>
<TYP>0</TYP>
<PRODUKT>0</PRODUKT>
<NUMER_KAT/>
<SWW/>
<EAN/>
<NAZWA>{name}</NAZWA>
<GRUPA>Grupa Główna</GRUPA>
<URL/>
<NIEAKTYWNY>0</NIEAKTYWNY>
<OPIS>PRZYGOTOWANIE DOKUMENTACJI DOTYCZĄCEJ OCHRONY DANYCH OSOBOWYCH</OPIS>
<EDYCJA_NAZWY>0</EDYCJA_NAZWY>
<KOPIUJ_OPIS>0</KOPIUJ_OPIS>
<EDYCJA_OPISU>0</EDYCJA_OPISU>
<ODWROTNEOBCIAZENIE>0</ODWROTNEOBCIAZENIE>
<MPP>0</MPP>
<CENAZCZTEREMAMIEJSCAMI>0</CENAZCZTEREMAMIEJSCAMI>
<JM>{unit}</JM>
<JMZ/>
<JM_PRZELICZNIK_L>0.00</JM_PRZELICZNIK_L>
<JM_PRZELICZNIK_M/>
<JM_CALKOWITE>0</JM_CALKOWITE>
<KAUCJA>0</KAUCJA>
<WAGA_KG>0.0000</WAGA_KG>
<UDOSTEPNIAJ_W_CENNIKU>0</UDOSTEPNIAJ_W_CENNIKU>
<E_SKLEP>0</E_SKLEP>
<TYP_MINIMUM>0</TYP_MINIMUM>
<MIN_CENA_MARZA/>
<PS_FS_USLUGA_ZLOZONA>0</PS_FS_USLUGA_ZLOZONA>
<WALUTA>
<SYMBOL>PLN</SYMBOL>
<KURS_NUMER>0</KURS_NUMER>
<KURS_L>1.00</KURS_L>
<KURS_M>1</KURS_M>
</WALUTA>
<KOSZT_USLUGI>
<WALUTA>0.0000</WALUTA>
<WARTOSC>0.0000</WARTOSC>
<TYP>1</TYP>
</KOSZT_USLUGI>
<DOSTAWCA>
<KOD_U_DOSTAWCY/>
</DOSTAWCA>
<PRODUCENT>
<KOD_U_PRODUCENTA/>
</PRODUCENT>
<ILOSC_MIN>0.0000</ILOSC_MIN>
<ILOSC_MIN_JM>SZT</ILOSC_MIN_JM>
<ILOSC_MAX>0.0000</ILOSC_MAX>
<ILOSC_MAX_JM>SZT</ILOSC_MAX_JM>
<ILOSC_ZAM>0.0000</ILOSC_ZAM>
<ILOSC_ZAM_JM>SZT</ILOSC_ZAM_JM>
<STAWKA_VAT>
<STAWKA>{vat_sell}</STAWKA>
<FLAGA>2</FLAGA>
<ZRODLOWA>0.00</ZRODLOWA>
</STAWKA_VAT>
<STAWKA_VAT_ZAKUPU>
<STAWKA>{vat_buy}</STAWKA>
<FLAGA>2</FLAGA>
<ZRODLOWA>0.00</ZRODLOWA>
</STAWKA_VAT_ZAKUPU>
<NUMER_CENY>2</NUMER_CENY>
<CENA_DOMYSLNA>hurtowa 1</CENA_DOMYSLNA>
<CENY>
<CENA>
<TYP>1</TYP>
<NUMER>1</NUMER>
<NAZWA>zakupu</NAZWA>
<WARTOSC>0.0000</WARTOSC>
<SYMBOL_WALUTY>PLN</SYMBOL_WALUTY>
<ZAOKRAGLENIE>0.0000</ZAOKRAGLENIE>
<MARZA>0.00</MARZA>
<MARZAWSTU>0.00</MARZAWSTU>
<OFFSET>0.0000</OFFSET>
<AKTUALIZACJA>0</AKTUALIZACJA>
</CENA>
<CENA>
<TYP>1</TYP>
<NUMER>2</NUMER>
<NAZWA>hurtowa 1</NAZWA>
<WARTOSC>0.0000</WARTOSC>
<SYMBOL_WALUTY>PLN</SYMBOL_WALUTY>
<ZAOKRAGLENIE>0.0100</ZAOKRAGLENIE>
<MARZA>0.00</MARZA>
<MARZAWSTU>0.00</MARZAWSTU>
<OFFSET>0.0000</OFFSET>
<AKTUALIZACJA>0</AKTUALIZACJA>
</CENA>
<CENA>
<TYP>1</TYP>
<NUMER>3</NUMER>
<NAZWA>hurtowa 2</NAZWA>
<WARTOSC>0.0000</WARTOSC>
<SYMBOL_WALUTY>PLN</SYMBOL_WALUTY>
<ZAOKRAGLENIE>0.0100</ZAOKRAGLENIE>
<MARZA>0.00</MARZA>
<MARZAWSTU>0.00</MARZAWSTU>
<OFFSET>0.0000</OFFSET>
<AKTUALIZACJA>0</AKTUALIZACJA>
</CENA>
<CENA>
<TYP>1</TYP>
<NUMER>4</NUMER>
<NAZWA>hurtowa 3</NAZWA>
<WARTOSC>0.0000</WARTOSC>
<SYMBOL_WALUTY>PLN</SYMBOL_WALUTY>
<ZAOKRAGLENIE>0.0100</ZAOKRAGLENIE>
<MARZA>0.00</MARZA>
<MARZAWSTU>0.00</MARZAWSTU>
<OFFSET>0.0000</OFFSET>
<AKTUALIZACJA>0</AKTUALIZACJA>
</CENA>
<CENA>
<TYP>2</TYP>
<NUMER>5</NUMER>
<NAZWA>detaliczna</NAZWA>
<WARTOSC>{price_brutto}</WARTOSC>
<SYMBOL_WALUTY>PLN</SYMBOL_WALUTY>
<ZAOKRAGLENIE>0.0100</ZAOKRAGLENIE>
<MARZA>0.00</MARZA>
<MARZAWSTU>0.00</MARZAWSTU>
<OFFSET>0.0000</OFFSET>
<AKTUALIZACJA>0</AKTUALIZACJA>
</CENA>
</CENY>
<JEDNOSTKI_MIARY/>
<KODY_KRESKOWE/>
<ZAMIENNIKI/>
</TOWAR>"""

    
    def get_values_from_invoice(self, pathToRead, pathToSave):
        
        with open(pathToRead, "r", encoding="UTF-8") as fileRead:
            
                pathToSave = "{}/{}".format(pathToSave, "testtesddat.xml")
                
                with open(pathToSave, "w", encoding="utf-8") as fileSave:

                # fileSave = open(pathToSave, "w+", encoding="utf-8")
                
                    fileSave.write(self.formStart)

                    lines = fileRead.read()
                        
                    amountOfSubjectsStart = lines.find("<LiczbaPozycji>")
                    amountOfSubjectsEnd = lines.find("</LiczbaPozycji>")
                    amountOfSubjects = lines[amountOfSubjectsStart+15:amountOfSubjectsEnd]
                    
                        
                    try:
                        
                        for subject in range(int(amountOfSubjects)):

                        
                            subjectStart = lines.find("<Pozycja>")
                            subjectEnd = lines.find("</Pozycja>")
                            subject = lines[subjectStart:subjectEnd]
                            
                            descriptionStart = lines.find("<Opis>")
                            descriptionEnd = lines.find("</Opis>")
                            description = lines[descriptionStart+6:descriptionEnd]
                            
                            descriptionSecondStart = lines.find("<Opis1>")
                            descriptionSecondEnd = lines.find("</Opis1>")
                            descriptionSecond = lines[descriptionSecondStart+7:descriptionSecondEnd]
                            
                            fullDescription = "{} {}".format(description, descriptionSecond)
                                
                            indexStart = subject.find("<Indeks>")
                            indexEnd = subject.find("</Indeks>")
                            index = subject[indexStart+8:indexEnd]
                            
                            unitStart = lines.find("<Jednostka>")
                            unitEnd = lines.find("</Jednostka>")
                            unit = lines[unitStart+11:unitEnd]
                                                            
                            priceStart = subject.find("<Cena>")
                            priceEnd = subject.find("</Cena>")
                            price = subject[priceStart+6:priceEnd]
                            
                            vatStart = subject.find("<Procent>")
                            vatEnd = subject.find("</Procent>")
                            vat = "23"
                                
                            lines = lines[subjectEnd+10:]
                            
                            fileSave.write(self.form.format(code = index, code2 = index, name = fullDescription, unit = unit, vat_sell = vat, vat_buy = vat, price_brutto = price))
                        
                        else:
                            fileSave.write(self.formEnd)
                                
                    except Exception as e:
                        print("Error read price list", e)
            