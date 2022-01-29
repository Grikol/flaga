# Flaga

#### 1. Start.

Aby zacżąć włącz terminal (lub powershell) i połącz się ze swoim serwerem.

#### Dodatkowy krok tylko dla AWS Ubuntu 18/20 (Nie trzeba tego kroku robić dla VPS z Home i większość innych):
Ustawiamy uprawnienia root ("administratora").
```
sudo passwd # <----- To dla AWS tylkooo!
```
Podaj hasło i zapisz. Wpisz jeszcze poniższe i podaj hasło.
```
su -  # <----- Też tylko dla AWS!! xD
```
I jesteś na serwerze jako root. 


#### 2. Uaktualniamy paczki (packages).

```
apt update
apt upgrade
```

W trakcie instalacji gdy proces się zatrzymuje z zapytaniem "Do you want to continue? [Y/n]" na końcu, napisz "Y" aby przejść dalej.

#### 3. Git.

VPS Ubuntu 18/20 (Home i większość innych):
```
apt install git
cd /var/www
git clone https://github.com/lukasz-test/flaga.git # <--- wklej dokładnie tą linię do terminala
cd flaga
python3 xD.py
```

AWS Ubuntu 18/20 (Home i większość innych):
```
apt install git
mkdir /var/www # <---- to w AWS trzeba zrobić a nie trzeba w VPS (większości)
cd /var/www
git clone https://github.com/lukasz-test/flaga.git
cd flaga
python3 xD.py # <---- z dużej litery xD.py a nie xd.py z małej litery.
```


#### 4. Wewnątrz środowiska (env).

Wszystkie polecenia wykonywane w tym kroku są wykonywane w folderze /var/www/flaga
Napisz 
```
pwd
```
aby sprawdzić w jakim katalogu jesteś.


#### Tworzenie i aktywacja środowiska (WAŻNE!):
```
python3 -m venv flagaenv
source flagaenv/bin/activate
```

#### Tworzenie zmiennej:
```
export FLASK_APP=app.py
```

Następnie podaj swoją domenę 
```
nano settings.ini
```
wywołując nano albo jed wpisz w nowym pliku po spacji nazwę swojej domeny np (bez "www.") wg wzoru:
```
domena = nazwa_domeny.pl
```

Aby zapisać wciśnij ctrl+s
Aby zamknąć wciśnij ctrl+x


Instalacja wymaganych bibliotek.
```
pip3 install -r requirements.txt
```

Uruchom skrypt przygotowujący hosting w serwerze (1 raz).
```
python3 xd.py
```

#### 5. Restartujemy nginxa i serwisy.

```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```


#### 6. Zmiana napisu.

Będąc w folderze flaga edytujemy zawartość pliku xd.txt.
```
cd /var/www/flaga
nano xd.txt
```

I przeładowujemy stronę.
```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```

#### Jak skońćzysz
Możesz opuścić Terminal pisząć

```
exit
```

Strona nadal będzie stała.


#### Resetowanie środowiska

Zrób to w sytuacji jak coś Ci się zchrzani i będziesz chciał usunąć pliki bo:
a) Masz błąd ze ścieżką gunicorna
b) Zle podałes domenę w setting.ini

[Poprawimy to po streamie]

```
python3 oczysc.py
```

#### Flagi:
```
http://wsamselbaudat.pl/
http://przemek2940.pl/
http://rafalujma.pl/
http://laskobar.pl/
http://t-mike.pl/
http://programowanie.jgora.pl/
http://przychlast.pl/
http://saraczyz.pl/
http://konrad-wlodarczyk.pl/
http://runpython.pl/
http://kalafior.site/
http://youras.pl/
https://flag.artbit.com.pl/
https://styxu.pl/
http://adrianeight.tech/
http://webdepp.net/
http://kokopas.pl/
http://pawlowski-filip.online/
http://www.mikson.xyz/
http://portfolio-syna-kolezanki.pl/
http://grah.pl/
http://boringdev.pl/
http://etyczne-dziennikarstwo.pl/
https://free.riichi.bet/
http://aguled.pl/
http://xyder-dlgdaw.pl/
http://wulpi.pl/
http://domenafb.pl/
http://tenteteges.pl/
http://ekdevops.pl/
http://daco-python.pl/
http://pepiush.pl/
http://ebajabongo.pl/
http://mrozinscyolawa.pl/
http://www.jkubex.pl/
http://python-master.pl/
http://rafalsygut.pl/
http://zadaj.pythanie.pl/
http://optimistiksnek.pl/
http://konradptak.pl/
http://yabadabadoo.pl/
http://www.projekty-karoli.pl/
http://leniwiecc.pl/
http://cdk.wtf/
http://pawelpolaszk.pl/
http://jerryntom.pl/
http://rjgsite.pl/
http://studentmetina.pl/
http://ikosaedr.pl/
https://malinowapogoda.edu.pl/
http://tobitobisinski.pl/
http://python-programming-project.pl/
http://kung-fu-python.online/
http://alawicki.pl/
http://dbys.pl/
http://kingwaw.pl/
http://wetwater.pl/
http://mechatohiks.pl/
http://masterofdisaster.com.pl/
http://klasyd.pl/
http://www.reallynicethings.pl/
http://magnetofon.com.pl/
http://moje-programowanie.pl/
http://akarnas.pl/
http://coderiot.pl/
http://marcinxd.pl/
http://jstrozniak.pl/
http://blinkiemoon.pl/
http://dziaga.pl/
http://animuscreations.pl/
http://little-things.site/
http://ioutside.pl/
http://piotrleski.pl/
http://pythonowanie.pl/
http://kraina-zabawnego-chomika.pl/
http://www.kraina-zabawnego-chomika.pl/
http://czarny-czarlik.pl/
http://wyspany-jestem.com.pl/
http://cryptonft.com.pl/
http://mathewlg.pl/
http://www.karolinasliwa.pl/
http://paulinawierzchowskalublin.pl/
http://martyna-zalewska.pl/
http://ejdziewczyno.pl/
http://www.ejdziewczyno.pl/
http://www.stronakaroliny.pl
http://czapiewski.edu.pl/
http://kasiapolice82.pl/
http://www.moc5g.pl/
http://mexicanseafood.pl/
http://jokuna.pl/
http://mcbiru.pl/
http://danielrusak.pl/
http://xd.netadmins.pl/
http://dawidpawlas.pl/
http://marcinjanuszewski.pl/
http://arek-pe.pl
http://pythonportfolio.pl/
```

Jest jeszcze drugie tyle +


