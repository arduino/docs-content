---
title: 'Usare il LED RGB integrato della MKR WiFi 1010'
difficulty: beginner
compatible-products: [mkr-wifi-1010]
description: "In questo tutorial scopriremo come controllare il LED RGB integrato della MKR WiFi 1010. Questo componente è uno strumento molto utile per qualsiasi tipo di sviluppo: possiamo usarlo per prototipare una luce intelligente, o magari come componente di feedback."
tags:
  - RGB
author: Karl Söderby
libraries:
  - name: WiFiNINA
    url:  https://www.arduino.cc/en/Reference/WiFiNINA
hardware:
  - hardware/01.mkr/01.boards/mkr-wifi-1010
software:
  - ide-v1
  - ide-v2
  - web-editor
featuredImage: 'led'
---

## Introduzione

In questo tutorial scopriremo come controllare il LED RGB integrato della MKR WiFi 1010. Questo componente è uno strumento molto utile per qualsiasi tipo di sviluppo: possiamo usarlo per prototipare una luce intelligente, o magari come componente di feedback.

## Obiettivi

Gli obiettivi di questo progetto sono:

- Imparare quali comandi possiamo usare per controllare l'RGB integrato.
- Far lampeggiare l'RGB in tre colori diversi.

## Hardware e software necessari

- Arduino IDE ([online](https://create.arduino.cc/) o [offline](https://www.arduino.cc/en/main/software)).
- Libreria [WiFiNINA](https://www.arduino.cc/en/Reference/WiFiNINA).
- Arduino MKR WiFi 1010 ([link allo store](https://store.arduino.cc/mkr-wifi-1010)).

## RGB (rosso, verde, blu)

È molto probabile che tu abbia già visto o sentito il termine **RGB**. RGB sta semplicemente per **Red** (rosso), **Green** (verde) e **Blue** (blu), i tre colori con cui si può creare praticamente qualsiasi colore. Un RGB è composto da tre piccoli LED: uno rosso, uno blu e uno verde. Guarda l'immagine qui sotto e i valori: rappresentano ciascun colore, e quando scriviamo questi valori sul componente, questo passa **magicamente** a quel colore!

![Come funzionano i LED RGB.](assets/MKR_1010_T12_IMG01.png)

Il componente RGB si usa per molti scopi diversi. È particolarmente utile per segnalare lo stato di qualcosa. Per esempio: se vogliamo segnalare che è tutto a posto, possiamo semplicemente passare al verde; se c'è un errore lieve possiamo passare al giallo, e se c'è un errore grave al rosso.

### Controllare l'RGB integrato

L'RGB integrato si trova proprio accanto al modulo Wi-Fi **NINA-W102** sulla scheda MKR 1010.

![L'RGB sulla scheda MKR WiFi 1010.](assets/MKR_1010_T12_IMG02.png)

Controllare l'RGB della MKR WiFi 1010 è un po' diverso da quanto potresti aver fatto finora con componenti simili. Prima di tutto, non possiamo accedervi direttamente: dobbiamo usare le funzionalità della libreria [WiFiNINA](https://www.arduino.cc/en/Reference/WiFiNINA). Più precisamente, per lavorarci dobbiamo accedere a un file chiamato `wifi_drv.h`. Qui sotto trovi uno snippet che mostra come includere questo file nel tuo sketch:

```arduino
#include <WiFiNINA.h>
#include <utility/wifi_drv.h>
```

Una volta incluso, il resto è piuttosto semplice. Il componente RGB usa i pin 25 (verde), 26 (rosso) e 27 (blu), quindi dobbiamo definire questi pin con i comandi seguenti:

```arduino
  WiFiDrv::pinMode(25, OUTPUT); //define GREEN LED
  WiFiDrv::pinMode(26, OUTPUT); //define RED LED
  WiFiDrv::pinMode(27, OUTPUT); //define BLUE LED
```

***Nota: in alcune versioni più vecchie i LED verde e rosso sono invertiti (pin `25` e `26`).***

Per controllarli all'interno del `loop()` usiamo semplicemente:

```arduino
  WiFiDrv::analogWrite(25, 255); //GREEN
  WiFiDrv::analogWrite(26, 0);   //RED
  WiFiDrv::analogWrite(27, 0);   //BLUE
```

Oppure, se vogliamo usare `digitalWrite()` (per accenderli semplicemente alla massima luminosità), possiamo scrivere così:

```arduino
  WiFiDrv::digitalWrite(25, HIGH); //GREEN
  WiFiDrv::digitalWrite(26, LOW);   //RED
  WiFiDrv::digitalWrite(27, LOW);   //BLUE
```

### Circuito

Questo tutorial richiede soltanto la scheda MKR WiFi 1010. Non serve nessun circuito aggiuntivo.

![La scheda MKR WiFi 1010.](assets/MKR_1010_T12_IMG03.png)


## Programmare la scheda

**1.** Per prima cosa, assicuriamoci di avere installato i driver. Se usiamo il Cloud Editor non dobbiamo installare nulla. Se usiamo un editor offline dobbiamo installarli a mano: basta andare in **Tools > Board > Board Manager...**, cercare **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** e installarlo.

**2.** Ora dobbiamo installare la libreria necessaria. Se usiamo il Cloud Editor non serve installare nulla. Se usiamo un editor offline, basta andare in **Tools > Manage libraries..**, cercare **WiFiNINA** e installarla.

**3.** Ora possiamo dare un'occhiata ad alcune delle funzioni principali di questo sketch:

- `#include <WiFiNINA.h>` - include la libreria WiFiNINA.
- `#include <utility/wifi_drv.h>` - include il file `wifi_drv.h`.
- `WiFiDrv::pinMode(pin, OUTPUT)` - imposta il pin come output.
- `WiFiDrv::analogWrite(pin, brightness)` - scrive sul pin il valore di luminosità. Per esempio, (27, 127) imposta il LED blu a metà luminosità.

Trovi lo sketch nello snippet qui sotto. Caricalo sulla scheda.

```arduino
#include <WiFiNINA.h>
#include <utility/wifi_drv.h>

void setup() {
  WiFiDrv::pinMode(25, OUTPUT); //define green pin
  WiFiDrv::pinMode(26, OUTPUT); //define red pin
  WiFiDrv::pinMode(27, OUTPUT); //define blue pin
}

void loop() {
  WiFiDrv::analogWrite(25, 255);
  WiFiDrv::analogWrite(26, 0);
  WiFiDrv::analogWrite(27, 0);

  delay(1000);

  WiFiDrv::analogWrite(25, 0);
  WiFiDrv::analogWrite(26, 255);
  WiFiDrv::analogWrite(27, 0);

  delay(1000);

  WiFiDrv::analogWrite(25, 0);
  WiFiDrv::analogWrite(26, 0);
  WiFiDrv::analogWrite(27, 255);

  delay(1000);

  WiFiDrv::analogWrite(25, 0);
  WiFiDrv::analogWrite(26, 0);
  WiFiDrv::analogWrite(27, 0);

  delay(1000);
}
```

## Proviamolo

Poco dopo aver caricato lo sketch sulla scheda, dovremmo vedere l'RGB cambiare colore. L'ordine corretto è:

- Verde.
- Rosso.
- Blu.
- Spento.

Alla fine del `loop()` abbiamo scritto il valore `0` su tutti i LED, che semplicemente li spegne. Il colore dovrebbe cambiare ogni secondo, perché tra un cambio e l'altro abbiamo usato `delay(1000)`.

![Pin e valori di luminosità.](assets/MKR_1010_T12_IMG04.png)

### Risoluzione dei problemi

Se il codice non funziona, ecco alcuni problemi comuni da verificare:

- Non abbiamo installato la libreria **WiFiNINA**.
- Non stiamo usando la scheda MKR WiFi 1010 (è l'unica scheda MKR con un RGB integrato).

## Conclusione

In questo tutorial abbiamo visto le basi per accendere e spegnere il LED RGB integrato della MKR WiFi 1010. Può essere uno strumento molto utile per segnalare lo stato di qualcosa (come la connessione o la potenza del segnale), o semplicemente per giocare con un RGB senza dover collegare nulla.
