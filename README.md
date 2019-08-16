# Jobnet-automatisk-jobforeslag-tryk
Når man går på dagpenge er det et af lovkravende, at man hver 7. dag skal tykke på jobforeslag knappen på jobnet. Hvis man ikke trykker på knappen, kan man risikere at miste retten til dagpenge. Dette er et script som automatisk går ind og gør det for dig. Den kan sættes op til at køre på bestemte tidspunkter eller når computeren starter. For at sætte det til at køre automatisk tager det cirka 10 minutter.

# Installation
Hvis man har Windows skal man installere Python først. Det kan gøres her: https://www.anaconda.com/distribution/
Når Python er installeret skal man hente pakken Selenium. Dette kan gøres ved at åbne Anaconda Promt og skrive:
```
pip install selenium
```
Derefter skal man hente chromedriver fra https://chromedriver.chromium.org/downloads. Det er den der gør at vi kan interagere med Chrome. Scriptet kan også omskrives til at bruge andre browsere. For at hente den rigtige version af chromedriver kan man finde ens version af Chrome ved at trykke på de 3 prikker i højre hjørne -> Help -> About Google Chrome og så kan man se versionsnummeret. chromedriver.exe skal ligge i samme mappe som `jobnet_press_button.py`, ellers så skal stien specificeres i linjen:
```
driver = webdriver.Chrome('DIN_STI/chromedriver.exe')
```

# Set up
Du skal nu skrive dit Jobnet login ind i `jobnet_press_button.py`. Det er `your_username` og `your_password` der skal ændres. Et eksempel på hvordan det skal se ud:
```
your_username = "Karen"
your_password= "hunter2"
```
Når du kører scriptet vil den automatisk gå ind og trykke på jobforeslag knappen. Kør den for at se om det virker. Nu skal du vælge om du den skal køre på et bestemt tidspunkt eller på opstart.

# Automatisk opstart
Dette er en guide skrevet til Windows. Nu skal bat filen `Run_jobnet_button.cmd` opsættes for at kunne køre scriptet på opstart. Der er to stier der skal ændres.
```
start "" "C:\Users\USER\Anaconda3\Python.exe" "C:\Users\USER\Documents\jobnet_press_button.py"
```

Den første sti `"C:\Users\USER\Anaconda3\Python.exe"` er der hvor Python er installeret. Hvis du har kørt en standard installation så burde den være i den lokation. `USER` skal bare ændres til din brugernavn på computeren. Den anden sti `"C:\Users\USER\Documents\jobnet_press_button.py"` er lokationen hvor du har lagt `jobnet_press_button.py`, så den skal ændres til den korrekte sti. Test om den virker ved at køre `Run_jobnet_button.cmd`. Det sidste der skal gøres er, at den skal ligge i mappen hvor Windows automatisk kører programmer på computer opstart. Stien er `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`. Lig `Run_jobnet_button.cmd` der og åben Task Manager -> Start-up for at se om filen kan ses derinde. Derefter genstart computeren og se om det virker.
