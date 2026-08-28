---
identifier: ABX00181
title: Arduino® VENTUNO™ Q
type: maker
---

![](assets/featured.png)

# Français

# Description

L’Arduino® VENTUNO™ Q est un ordinateur IA de pointe haute performance spécialement conçu pour l’IA et la robotique de nouvelle génération. En associant de manière transparente une puissance de calcul de niveau industriel à une action en temps réel, le VENTUNO Q vous offre la puissance de traitement nécessaire pour déployer des modèles d’IA complexes et le contrôle de précision requis pour interagir avec le monde physique, le tout à partir d’un seul appareil compact en périphérie.

Au cœur de cet appareil se trouve une architecture révolutionnaire « Dual-Brain » : le microprocesseur (MPU) robuste Qualcomm Dragonwing™ IQ8 (QCS8275) (MPU) offre jusqu’à 40 TOPS denses de calcul IA pour la vision par ordinateur avancée et les modèles de langage locaux (LLM) fonctionnant sous un système d’exploitation Ubuntu Linux complet (Debian également pris en charge), tandis que le microcontrôleur (MCU) dédié STMicroelectronics STM32H5F5, exécutant Arduino Core sur le système d’exploitation Zephyr, garantit la précision à faible latence requise pour le contrôle moteur complexe et la robotique.

VENTUNO Q vous permet de rester connecté et prêt à l’emploi. Il intègre une connectivité Wi-Fi® 6 (tri-bande) et Bluetooth® 5.3, ainsi qu’une gamme complète de connecteurs intégrés, notamment USB 3.0 haut débit, HDMI, Ethernet 2,5 Gb et un connecteur M.2 pour un stockage NVMe Gen 4 extensible. La carte prend en charge nativement le vaste écosystème des shields et  carrier des Arduino UNO, ainsi que les HAT Raspberry Pi® via un connecteur à 40 broches, et les Arduino Modulino® via un connecteur Qwiic.

# Domaines d’application

IA en périphérie, LLM/VLM locaux, maison connectée, robotique, contrôle de mouvement, ville intelligente, vision industrielle, enseignement et recherche

<div style="page-break-after: always;"></div>

# SOMMAIRE

## Exemples d’application

VENTUNO Q associe un processeur Linux compatible IA à un microcontrôleur en temps réel, offrant ainsi le meilleur de la puissance de calcul de haut niveau et du contrôle déterministe. Il est spécialement conçu pour les créateurs et les développeurs qui souhaitent disposer d’une IA capable d’agir directement sur le monde physique.

- **Assistants IA et maison connectée :** Créez des assistants vocaux hors ligne, des hubs agents locaux, des bornes à interface sans contact et des traducteurs vocaux en temps réel.
- **Robotique et contrôle de mouvement :** Robots mobiles autonomes (AMR) utilisant le SLAM visuel, des manipulateurs guidés par la vision, ainsi que des robots d’accompagnement et de service.
- **Villes intelligentes et vision industrielle :** Moniteurs de trafic en périphérie, contrôle qualité automatisé sur les chaînes de montage, sécurité proactive des sites et suivi des stocks par vision.
- **Éducation et recherche :** Kits d’apprentissage avancés en IA, prototypage rapide pour la recherche, assistants de codage vocaux et plateformes de recherche en manipulation mobile.

<div style="page-break-after: always;"></div>

## Caractéristiques

### Variantes du VENTUNO Q

Le VENTUNO Q est disponible en une seule variante :

- **ABX00181** : 16 Go de mémoire vive LPDDR5, 64 Go de stockage eMMC

### Aperçu des spécifications générales

#### Processeur et mémoire

![](assets/ABX00181_ic_overview.png)

| **Sous-système**           | **Détails**                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| MPU principale             | Qualcomm Dragonwing™ IQ8 (QCS8275)                                                                       |
|                            | CPU : Arm® Cortex® octa-core                                                                             |
|                            | GPU Adreno™ 623 (graphisme 3D et OpenCL)                                                                 |
|                            | VPU Adreno™ 623 (Traitement vidéo)                                                                       |
|                            | Processeur IA Hexagon™ Tensor (NPU) : jusqu’à 40 TOPS en mode dense                                      |
|                            | Processeur d’image (ISP) Qualcomm Spectra 692                                                            |
|                            | Système d’exploitation Ubuntu Linux (Debian également pris en charge)                                    |
| Microcontrôleur temps réel | ST STM32H5F5 (microcontrôleur), Arm® Cortex®-M33 jusqu’à 250 MHz                                         |
|                            | Noyau Arduino sous le système d’exploitation Zephyr                                                      |
|                            | 4 Mo de mémoire Flash, 1,5 Mo de RAM                                                                     |
| Mémoire système            | eMMC de 64 Go pour le système d’exploitation et les données                                              |
|                            | Mémoire OSPI SAIL (MX25UW25345GXDI00-TR) pour le démarrage du microcontrôleur et les données partagées   |
|                            | Connecteur M.2 Key M 2230 pour le stockage NVMe Gen 4 (PCIe x4 directement depuis le SOM, non amorçable) |
|                            | 2 x 8 Go de RAM LPDDR5 (16 Go au total)                                                                  |

#### Connectivité et multimédia

![](assets/ABX00181_connector_overview.png)

| **Sous-système**   | **Détails**                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Réseau et sans fil | Wi-Fi® 6 2,4/5/6 GHz (tri-bande) avec 2 antennes intégrées (module NFA725B)                                          |
|                    | Bluetooth® 5.3 avec antenne intégrée                                                                                 |
|                    | 1 port Ethernet RJ45 2,5 Gbit (PHY QCA-8081)                                                                         |
| Connecteurs USB    | 1× port USB-C avec commutation des rôles hôte/périphérique, commutation du rôle d’alimentation et sortie vidéo       |
|                    | 2x USB 3.0 Type A                                                                                                    |
|                    | 2x USB 3.0 sur le connecteur JOMEGA                                                                                  |
| Vidéo              | 1x sortie HDMI via le pont DSI-vers-HDMI ADV7535 intégré. Les interfaces HDMI et MIPI DSI partagent                  |
|                    | les mêmes lignes DSI ; lorsque l'HDMI est actif, le MIPI DSI sur le connecteur JMEDIA est désactivé par multiplexage |
|                    | Sortie vidéo (mode DP Alt) via USB-C                                                                                 |
| Caméra             | 3 connecteurs MIPI CSI sur la carte (J3_1, J3_2, J3_3)                                                               |
|                    | 2 voies MIPI CSI également disponibles sur le connecteur JMEDIA (multiplexées avec les connecteurs intégrés)         |
|                    | Prise en charge des caméras USB via USB Type-A ou USB-C                                                              |
| Audio              | Codec audio : MAX98091ETM+T (Maxim)                                                                                  |
|                    | Sur JMISC : 1 sortie ligne mono, 1 sortie haut-parleur mono, 1 sortie casque stéréo, 1 entrée micro                  |
|                    | Sur JOMEGA : 1 entrée micro                                                                                          |
| Interfaces CAN     | 1 interface CAN-FD avec PHY (ATA6563-GBQW1) sur bornier à vis, pilotée par le microcontrôleur (STM32H5F5)            |
|                    | Les lignes CAN-H et CAN-L sont protégées par des diodes TVS (PJGBLC24C-AU_R1_000A1, bidirectionnelles, 24 V, 350 W)  |
|                    | Terminaison divisée intégrée sur le bus CAN à bornes à vis (2 × 60,4 Ω + 100 nF)                                     |
|                    | 3x CAN-FD (sans PHY) sur le connecteur JOMEGA, multiplexage des broches via le microcontrôleur                       |
|                    | 1x CAN-FD (sans PHY) sur les connecteurs du shield UNO (D4/D5), multiplexage des broches via le microcontrôleur      |

>📝 **Remarque :** Le bus CAN sur la borne à vis intègre une terminaison divisée intégrée (2 × 60,4 Ω + 100 nF). Si la carte ne se trouve pas à l’extrémité du bus, cette terminaison doit être prise en compte lors de la conception de la topologie du réseau.

#### Extensions et connecteurs

| **Interface (connecteur)**          | **Détails**                                                                                                                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connecteurs du shield UNO           | - Compatible avec les shields Arduino UNO standard (logique 3,3 V)                                                                                                                 |
|                                     | - La plupart des broches numériques supportent une tension de 5 V. Les broches A0 et A1 du JANALOG sont des entrées ADC directes et ne supportent pas une tension de 5 V           |
| Connecteur d’extension (JOMEGA)     | - Capacités d’extension étendues, notamment USB 3.0, CAN-FD, JTAG, MIC IN, SPI du MPU                                                                                              |
| Connecteurs du carrier              | - JMEDIA : voies de caméra MIPI CSI0/CSI1 et voies d’affichage MIPI-DSI à 1,8 V                                                                                                    |
|                                     | - JMISC : terminaux audio, GPIO de l’MPU à 1,8 V et signaux du microcontrôleur à 3,3 V                                                                                             |
| Connecteur Qwiic                    | - I2C (3,3 V) connecté au microcontrôleur pour un accès « plug-and-play » instantané aux nœuds Modulino®                                                                           |
| Connecteur JHAT                     | - Connecteur à 40 broches compatible Raspberry Pi® (GPIO du processeur, avec conversion de niveau à 3,3 V pour la compatibilité HAT via les circuits TXS0108ERKSR et TXS0104ERUTR) |
| JCTL (débogage à distance de l’MPU) | - Connecteur à 10 broches (2×5) pour le débogage à distance de l’MPU, compatible avec [Arduino Bughopper](https://docs.arduino.cc/hardware/bughopper/)                             |

<div style="page-break-after: always;"></div>

## Caractéristiques techniques

### Alimentation d'entrée

| **Source**                       | **Plage de tension** | **Courant maximal** | **Connecteur**                 |
| -------------------------------- | -------------------: | ------------------: | ------------------------------ |
| USB-C PD                         |               9-20 V |         jusqu’à 3 A | Connecteur USB-C               |
| Prise cylindrique (5,5 × 2,1 mm) |               7-24 V |         jusqu’à 5 A | Prise cylindrique 5,5 × 2,1 mm |
| Borne à vis                      |               7-24 V |        jusqu’à 10 A | Borne à vis                    |

![Options d'alimentation](assets/ABX00181_power_options.png)

Les deux voies d’entrée sont protégées par des diodes TVS (SMBJ24CA, bidirectionnelles 24 V) et passent par des commutateurs de puissance indépendants (KTS1900GXAA-TA + SQS414CENW-T1_GE3) avant d’atteindre un étage de détection de courant (INA232AIDDFR). Deux convertisseurs abaisseurs multiphases (MPQ4371GVE-1001-AECC901-Z) génèrent le rail principal de 3,3 V, tandis qu’un autre convertisseur abaisseur (MPQ4371GVE-1001-AECC901-Z) génère le rail de 5 V. Le contrôleur USB-C® PD (CYPD6129-52LQXI) négocie des profils de tension allant jusqu’à 20 V à partir d’alimentations USB-C® compatibles.

> 📝 **Remarque concernant le courant d’entrée CC et le budget de puissance :** Le connecteur de type « barrel jack » est conçu pour un courant maximal de 5 A. Le budget de puissance disponible dépend de la tension d’entrée : à 7 V (5 A), la puissance maximale fournie est de 35 W ; à 12 V, elle est de 60 W ; à 24 V, elle est de 120 W. Dans le pire des cas, lorsque le MPU, le NPU et le GPU fonctionnent simultanément à pleine puissance, le SoM à lui seul peut consommer environ 23 à 25 W. L’ensemble de la carte, y compris le PHY Ethernet, le codec audio, le concentrateur USB et les autres circuits intégrés embarqués, consommera davantage, ce qui laisse une marge limitée à 7 V avant d’atteindre la limite du connecteur.
>
> Lorsque vous alimentez la carte à 7 V, veillez à tenir compte de la chute de tension dans le câble, car la carte nécessite une tension minimale de 7 V au niveau de ses connecteurs et ne s'allumera pas si la tension est inférieure à 7 V.
>
> Les deux ports USB de type A peuvent fournir chacun jusqu'à 5 V × 1,71 A = 8,55 W, soit une consommation supplémentaire maximale combinée d'environ ~17 W. Lorsque la carte fonctionne à pleine puissance et que les deux ports USB de type A sont soumis à une charge maximale, la consommation totale peut avoisiner les 42 W, dépassant ainsi la limite de 35 W de la prise CC à 7 V et risquant d’endommager les connecteurs.
>
> Le rail 3,3 V destiné aux shields UNO, aux HAT et aux modules Qwiic (`+3V3_LIMITED`) est limité à 2,8 A (environ ~9,3 W au maximum). Le rail 5 V destiné aux shields et aux HAT (`+5V_LIMITED`) est également limité à 2,8 A (environ ~14 W maximum). Veuillez noter que les rails 3,3 V et 5 V fournis aux connecteurs du support UNO et au JOMEGA ne sont **pas** limités en courant.
>
> **Il est fortement recommandé de fonctionner à 12 V ou 24 V** pour tout déploiement impliquant simultanément l’inférence IA, des périphériques USB et des shields ou HAT connectés.
>
> Pour les charges de travail importantes impliquant l’inférence IA, des périphériques USB ou des applications étendues, il est recommandé d’utiliser une alimentation d’une puissance nominale de **60 W ou plus** pour l’ensemble des sources d’alimentation afin de garantir un fonctionnement stable lors d’éventuels pics de consommation. En cas d’utilisation de la **prise cylindrique** (5,5 × 2,1 mm, 5 A max.), une alimentation de **12 V / 5 A ou 24 V / 3 A** est recommandée à titre d’exemple.

### Conditions de fonctionnement recommandées

| **Paramètre**                 | **Symbole**      | **Minimum** | **Typique** | **Maximum** | **Unité** |
| ----------------------------- | ---------------- | :---------: | :---------: | :---------: | :-------: |
| Entrée USB-C PD               | V<sub>USBC</sub> |      9      |      -      |    20,0     |     V     |
| Entrée CC (prise jack/vis)    | V<sub>IN</sub>   |     7,0     |      -      |    24,0     |     V     |
| Rail 5,0 V (sortie)           | V<sub>+5V</sub>  |    4,75     |     5,0     |    5,25     |     V     |
| Rail 3,3 V (sortie)           | V<sub>3P3</sub>  |    3,14     |     3,3     |    3,47     |     V     |
| Température de fonctionnement | T<sub>OP</sub>   |     -10     |      -      |     60      |    °C     |

>📝 **Remarque :** Le contrôleur USB-C® PD prend en charge plusieurs profils de tension (9 V, 15 V, 20 V) lorsqu’il est connecté à une alimentation compatible PD.

### Rails de tension intégrés sur la carte

| **Tension** | **Rail**              | **Origine/Régulateur**                                                                                             |
| :---------: | --------------------- | ------------------------------------------------------------------------------------------------------------------ |
|   7-24 V    | V<sub>IN</sub>        | Entrée par prise jack/bornes à vis (protégée par TVS, SMBJ24CA)                                                    |
|    5,0 V    | +5 V                  | Convertisseur abaisseur MPQ4371GVE                                                                                 |
|    3,3 V    | +3,3 V                | 2 convertisseurs abaisseurs MPQ4371GVE                                                                             |
|    1,8 V    | SOM_VREG_MDPX3_1P8    | Rail 1,8 V du domaine d'application principal du SOM (accessible à l'utilisateur via JMISC, JCTL)                  |
|    1,8 V    | SOM_VREG_S5S_SPX3_1P8 | Réservé au domaine du sous-système de sécurité du SOM (RTSS), non destiné à un usage général                       |
|    1,8 V    | +1V8                  | Convertisseur abaisseur MPQ2179GQHE (pour les circuits intégrés sur la carte QCA8081, ADV7535, MAX98091)           |
|   1,28 V    | +1,28 V               | LDO MP20312GTF (pour le codec audio MAX98091)                                                                      |
|    1,1 V    | +1,01 V               | Convertisseur abaisseur MPQ2179GQHE (pour les circuits intégrés sur cartes TUSB7340RKMR, QCA8081 et PI7C9X2G304EV) |

>📝 **Remarque :** La carte dispose de trois rails indépendants de 1,8 V. `SOM_VREG_MDPX3_1P8` est le rail du domaine d’application principal du SoM QCS8275 et constitue la référence recommandée pour toutes les interfaces 1,8 V accessibles à l’utilisateur, y compris JMISC et JCTL. `SOM_VREG_S5S_SPX3_1P8` est le rail du domaine du sous-système de sécurité (RTSS) du SoM et ne doit pas être utilisé comme alimentation ou référence à usage général. `+1V8` est le rail de 1,8 V au niveau de la carte, généré par le convertisseur abaisseur MPQ2179GQHE, qui alimente le PHY Ethernet QCA-8081, le pont d’affichage ADV7535 et le codec audio MAX98091.

>📝 **Remarque :** Indépendamment des rails ci-dessus, la broche 59 du JMISC accepte une batterie de secours RTC jusqu’à 3,3 V afin de maintenir les horloges en temps réel du SOM et du microcontrôleur lorsque la carte n’est pas alimentée par une autre source. `SOM_VCOIN` (RTC du SOM) et `VBAT` (RTC du microcontrôleur) sont deux entrées de batterie de secours pour les horloges en temps réel qui sont physiquement reliées entre elles au niveau de cette broche unique, plutôt que d’être raccordées à un rail d’alimentation commun. Chacune est connectée via sa propre résistance de 0 Ω à un nœud commun, qui est protégé par une diode TVS bidirectionnelle (Vr = 5,5 V) référencée à la masse. La consommation de courant attendue est très faible, et cette broche ne fournit pas d’alimentation pour maintenir le reste de la carte sous tension.

### Consommation électrique typique

Les mesures suivantes ont été réalisées à une température ambiante de 24,4 °C, à l’aide d’un analyseur de puissance, pour trois méthodes d’alimentation différentes : 12 V CC, 24 V CC et USB-C® PD à 20 V. Les exemples « Blink » sur le microcontrôleur, « Hello World » sur le processeur, « Edge AI Assistant » et « Detect Objects » sur l’appareil photo du smartphone sont disponibles en tant qu’exemples intégrés dans Arduino App Lab. L’exemple « Smart Mirror » s’appuie sur une note d’application dédiée.

#### Consommation électrique typique – 12 V CC

| **Scénario**                                            | **Puissance moyenne** | **Puissance minimale** | **Puissance maximale** |
| ------------------------------------------------------- | --------------------: | ---------------------: | ---------------------: |
| Démarrage                                               |                7,07 W |                      – |                 17,9 W |
| Clignotement sur le microcontrôleur                     |                7,42 W |                 5,30 W |                 12,6 W |
| « Hello World » sur le processeur                       |                7,52 W |                 5,32 W |                 13,3 W |
| Assistant IA en périphérie                              |                13,5 W |                 6,13 W |                 24,6 W |
| Exemple de « Smart Mirror »¹                            |                14,7 W |                 7,65 W |                 33,0 W |
| Détection d’objets via l’appareil photo d’un smartphone |                9,63 W |                 5,80 W |                 21,2 W |

#### Consommation électrique type - 24 V CC

| **Scénario**                                            | **Puissance moyenne** | **Puissance minimale** | **Puissance maximale** |
| ------------------------------------------------------- | --------------------: | ---------------------: | ---------------------: |
| Démarrage                                               |                9,71 W |                      – |                 23,7 W |
| Clignotement sur le microcontrôleur                     |                10,6 W |                 7,04 W |                 18,9 W |
| « Hello World » sur le processeur                       |                10,8 W |                 7,09 W |                 18,3 W |
| Assistant IA en périphérie                              |                15,5 W |                 7,44 W |                 28,8 W |
| Exemple de « Smart Mirror »¹                            |                17,3 W |                 8,47 W |                 36,6 W |
| Détection d’objets via l’appareil photo d’un smartphone |                11,5 W |                 7,88 W |                 24,7 W |

#### Consommation électrique type - USB-C® PD (20 V)

| **Scénario**                                            | **Puissance moyenne** | **Puissance minimale** | **Puissance maximale** |
| ------------------------------------------------------- | --------------------: | ---------------------: | ---------------------: |
| Démarrage                                               |                6,56 W |                      – |                 20,2 W |
| Clignotement sur le microcontrôleur                     |                7,84 W |                 6,33 W |                 16,1 W |
| « Hello World » sur le processeur                       |                9,68 W |                 6,42 W |                 16,1 W |
| Assistant IA en périphérie                              |                15,3 W |                 6,61 W |                 25,6 W |
| Exemple de « Smart Mirror »¹                            |                15,1 W |                 8,05 W |                 34,2 W |
| Détection d’objets via l’appareil photo d’un smartphone |                11,3 W |                 7,85 W |                 23,1 W |

¹ Configuration de test du « Smart Mirror » : caméra USB Logitech BRIO 4K, casque USB (microphone et haut-parleurs) et écran HDMI connectés.

>📝 **Remarque :** les mesures ont été effectuées à l’aide d’un analyseur de puissance Otii Ace Pro à titre de référence. La puissance de crête la plus élevée enregistrée sur l’ensemble des scénarios et des sources d’entrée était de 36,6 W (exemple « Smart Mirror » à 24 V CC), ce qui reste dans les limites de la recommandation d’une alimentation de 60 W ou plus mentionnée ci-dessus.

<div style="page-break-after: always;"></div>

## Présentation fonctionnelle

### Brochage

![](assets/ABX00181_pinout.png)

### Schéma fonctionnel

![Aperçu complet du schéma fonctionnel](assets/ABX00181_block_diagram.png)

![Schéma fonctionnel (Page 1/2)](assets/ABX00181_block_diagram_pg1.png)

![Schéma fonctionnel (page 2/2)](assets/ABX00181_block_diagram_pg2.png)

### Alimentation

Le VENTUNO Q prend en charge deux voies d’alimentation indépendantes : un port USB-C® avec négociation Power Delivery (PD) jusqu’à 20 V, et une entrée 7-24 V CC via la prise cylindrique de 5,5 × 2,1 mm ou la borne à vis. Ces deux voies sont protégées par des diodes TVS bidirectionnelles de 24 V et acheminées via un circuit « OR » d’alimentation composé de commutateurs de puissance indépendants, protégés contre l’inversion de polarité et les courants inverses (KTS1900 + 2x NMOS), avant d’atteindre les convertisseurs abaisseurs.

Un circuit intégré de détection de courant (INA232AIDDFR) surveille le courant d’entrée total sur le circuit actif. Deux convertisseurs abaisseurs multiphases (MPQ4371GVE-1001-AECC901-Z) génèrent le rail principal « +3,3 V », qui alimente le SOM (QCS8275) et les périphériques 3,3 V de la carte. Un troisième convertisseur abaisseur MPQ4371GVE génère le rail « +5 V ».

Un convertisseur abaisseur MPQ2179GQHE génère la tension `+1V8`, qui alimente le PHY Ethernet QCA-8081, le pont d'affichage ADV7535 et le codec audio MAX98091. Un convertisseur abaisseur MPQ2179GQHE génère la tension d’alimentation `+1V1`, alimentant le TUSB7340RKMR ainsi que le QCA-8081 et le commutateur PCIe PI7C9X2G304EV.

Le SOM fournit la tension d’alimentation du domaine d’application principal « MDPX3_1P8 » (1,8 V) via son circuit intégré de gestion de l’alimentation (PMIC) interne (« SOM_VREG_MDPX3_1P8 »), accessible à l’utilisateur via JMISC et JCTL. Le rail distinct « SOM_VREG_S5S_SPX3_1P8 » est dédié au sous-système de sécurité en temps réel (RTSS). Il ne doit pas être utilisé comme référence à usage général. Un LDO MP20312GTF génère le rail « +1,28 V » destiné au codec audio MAX98091.

Des commutateurs de charge dédiés MP5077GG-Z commandent indépendamment l’emplacement M.2 NVMe, la tension `+3V3_LIMITED` (pour les shields UNO, les HAT et les Qwiic) et la tension `+5V_LIMITED` (pour les shields et les HAT). La tension VBUS de chaque port USB de type A est activée et protégée par le TUSB7340RKMR. Tous les autres commutateurs de charge périphériques sont contrôlés par des lignes d’activation commandées par les GPIO du SOM, ce qui permet au MPU de couper l’alimentation des sous-systèmes inutilisés.

![Présentation complète de l'arborescence d'alimentation de l'Arduino VENTUNO Q](assets/ABX00181_power_tree.png)

![Arbre d'alimentation de l'Arduino VENTUNO Q (Page 1/3)](assets/ABX00181_power_tree_pg1.png)

![Arbre d'alimentation de l'Arduino VENTUNO Q (Page 2/3)](assets/ABX00181_power_tree_pg2.png)

![Arbre d'alimentation Arduino VENTUNO Q (Page 3/3)](assets/ABX00181_power_tree_pg3.png)

<div style="page-break-after: always;"></div>

## Interface utilisateur et indicateurs

| **Indicateur**     | **Type**                          | **Contrôleur**                              | **Remarques**                                                 |
| ------------------ | --------------------------------- | ------------------------------------------- | ------------------------------------------------------------- |
| Matrice LED        | 104 LED bleues (LTST-C191TBKT-5A) | Microcontrôleur via GPIO                    | Matrice d’affichage programmable                              |
| 4 LED RVB          | LTST-C28NBEGK-2A                  | Microcontrôleur via GPIO                    | Indicateurs d’état adressables par l’utilisateur              |
| LED d’alimentation | Verte (LTST-C190KGKT)             | Matériel (rail +3V3)                        | Indique que le rail +3V3 est actif                            |
| LED de défaut      | Rouge (XHY-STB0603SR)             | Contrôleur USB-C® PD (CYPD6129, GPIO9/P4.1) | Indique une condition de défaut détectée par le contrôleur PD |

- **4 LED RVB :** Quatre LED tricolores pilotées par le microcontrôleur (MCU) STM32H5F5 via 12 broches GPIO individuelles (3 par LED). Elles sont adressables par l’utilisateur et peuvent servir à indiquer l’état de l’application, l’état de la connectivité ou des événements personnalisés depuis un sketch Arduino.

| **Référence** | **LED RVB** | **Rouge** | **Vert** | **Bleu** |
| ------------- | ----------- | --------- | -------- | -------- |
| DL1_1         | LED RVB 1   | PG3       | PG6      | PK2      |
| DL1_2         | LED RVB 2   | PG4       | PD10     | PK1      |
| DL1_3         | LED RVB 3   | PD11      | PG5      | PK0      |
| DL1_4         | LED RVB 4   | PG2       | PG8      | PC6      |

![](assets/ABX00181_rgb_led.png)

>📝 Les LED RVB sont de type « actif bas » et s’allument lorsqu’elles sont mises à l’état logique « 0 ».

- **Matrice LED :** Une matrice LED monochrome bleue de 8 × 13 (104 pixels) pilotée par le microcontrôleur STM32H5F5. Elle affiche l’animation de démarrage pendant environ 20 à 30 secondes lors du démarrage de Linux. L’accès à la matrice avant la fin du démarrage peut perturber le fonctionnement du microcontrôleur.

>📝 **Remarque :** L’animation de démarrage ne s’affiche que lorsque le chargeur d’amorçage du microcontrôleur est chargé et qu’un sketch valide est en cours d’exécution. Si elle n’apparaît pas, veuillez vous reporter au [Manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) pour plus de détails.

![](assets/ABX00181_matrix.png)

- **LED d'alimentation :** Indicateur vert (LTST-C190KGKT) relié au rail `+3V3`. Il s'allume dès que la carte est sous tension.

- **LED de défaut :** voyant rouge piloté par le contrôleur USB-C® PD (CYPD6129, GPIO9/P4.1). Il signale une condition de défaut détectée par le contrôleur PD.

![](assets/ABX00181_status_led.png)

## MPU et MCU

Une MPU (unité de microprocesseur) est un processeur d’application haute performance conçu pour exécuter un système d’exploitation complet et des logiciels complexes. Une MCU (unité de microcontrôleur) est un contrôleur compact et économe en énergie, conçu pour assurer une synchronisation rapide et précise des E/S et des commandes. VENTUNO Q combine ces deux éléments afin d’associer, sur une seule carte, des capacités de calcul au niveau du système d’exploitation à un contrôle réactif et sensible au temps, et de communiquer via Bridge, une couche RPC implémentée des deux côtés.

### Processeur d’application (MPU)

Le Qualcomm® Dragonwing™ IQ8 (QCS8275) est un processeur Arm® Cortex® octa-cœur exécutant le système d’exploitation Ubuntu Linux (Debian également pris en charge). Ses E/S fonctionnent à 1,8 V et il gère les interfaces multimédias haut débit ainsi que l’inférence IA.

- Domaine de tension : 1,8 V pour les GPIO du MPU (SoC) et les interfaces haut débit.
- Pilote JMEDIA : voies de caméra MIPI CSI et voies d’affichage MIPI-DSI.
- Pilote les GPIO de la MPU à 1,8 V et les terminaux audio sur les connecteurs du carrier (JMEDIA, JMISC).
- USB-C : la commutation de rôle est gérée via le contrôleur PD CYPD6129, qui gère la négociation PD de manière indépendante (prend en charge des profils jusqu’à 20 V).
- Sortie DisplayPort via le multiplexeur USB eDP (TMUXHS4446RETT) sur le connecteur USB-C.
- Exécute le NPU Hexagon™ (jusqu’à 40 TOPS en mode dense) et le GPU Adreno™ 623 pour les charges de travail d’IA en périphérie et de graphisme.

### Microcontrôleur en temps réel (MCU)

Le STM32H5F5 de STMicroelectronics® est un processeur Arm® Cortex®-M33 exécutant Arduino Core sous le système d’exploitation Zephyr à une fréquence de 250 MHz. Il offre une synchronisation rapide et déterministe pour la robotique, le contrôle des moteurs et les E/S générales.

- Domaine de tension : 3,3 V pour les interfaces GPIO et analogiques.
- Gère l’ADC, le PWM, la matrice de LED, les LED RVB et les temporisateurs.
- Prend en charge les connecteurs 3,3 V : JDIGITAL, JANALOG et JSPI.
- Contrôle toutes les interfaces CAN-FD : PHY sur borne à vis et ports sans PHY sur les connecteurs JOMEGA et UNO Shield.

JMISC gère les deux domaines : les lignes MPU à 1,8 V coexistent avec les signaux MCU à 3,3 V (PSSI, I²C, GPIO) et l’audio analogique. Vérifiez toujours les niveaux de tension lorsque vous connectez des carriers ou des circuits logiques externes à JMISC.

>📝 **Remarque concernant VDDIO2 :** Le STM32H5F5 dispose d’un domaine d’alimentation E/S secondaire (VDDIO2) alimenté par `SOM_VREG_MDPX3_1P8` (1,8 V). Cela permet à certaines broches du microcontrôleur de communiquer directement avec le processeur à 1,8 V sans nécessiter de convertisseurs de niveau externes. Les interfaces suivantes fonctionnent dans le domaine VDDIO2 :
>
>- **MCU I2C1** est utilisé pour la communication directe entre le microcontrôleur et le processeur principal (MPU)
>- **Les broches GPIO du microcontrôleur PG9, PG10, PG11, PG12, PG13 et PG14** communiquent directement avec le processeur principal (MPU) à 1,8 V
>
> N’appliquez pas de niveau logique de 3,3 V à ces broches. Tous les autres signaux GPIO du microcontrôleur fonctionnent à 3,3 V sur le domaine VDDIO standard.

>⚠️ **Avertissement concernant le niveau de tension :** les signaux GPIO de l’MPU fonctionnent à 1,8 V, tandis que ceux du microcontrôleur fonctionnent à 3,3 V. Assurez-vous que toutes les connexions externes aux connecteurs d’extension sont compatibles avec le niveau de tension de leur domaine de processeur respectif afin d’éviter tout dommage matériel.

## Communication inter-processeurs

Le Qualcomm® Dragonwing™ IQ8 (QCS8275) (MPU) et le STM32H5F5 (MCU) communiquent via l’Arduino Bridge, une couche logicielle d’appel de procédure à distance (RPC) implémentée à la fois du côté Linux et du côté MCU. Bridge fournit une API orientée services qui permet à chacun des processeurs d’exposer des services que l’autre peut appeler, tout en prenant en charge les notifications unidirectionnelles pour les événements asynchrones. Il gère l’acheminement des messages entre les processeurs et prend en charge plusieurs protocoles de transport physiques.

Grâce à son API, Bridge permet des appels de fonction avec vérification de type, ce qui permet aux sketches de microcontrôleur d’invoquer des services Linux et de recevoir des réponses structurées ou de transmettre des données via des notifications.

La couche de transport physique entre les deux processeurs comprend les interfaces suivantes :

| **Interface** | **Direction**    | **Objectif**                                                  |
| ------------- | ---------------- | ------------------------------------------------------------- |
| USB 2.0       | SoC → MCU (hôte) | Transport de données à large bande passante                   |
| SWD           | SoC → MCU        | Interface de débogage (conversion de niveau de 1,8 V à 3,3 V) |

Si un indicateur matériel est nécessaire pour un carrier ou une logique externe, le micrologiciel peut affecter un GPIO MPU de 1,8 V sur JMISC, ou un GPIO JCTL disponible, comme sortie de signal « prêt » ou de réveil. Ce signal peut être reçu sur un GPIO du microcontrôleur via un circuit de compatibilité de niveau, tel qu’un convertisseur de niveau ou une configuration à drain ouvert avec une résistance de tirage vers le haut.

>📝 Les signaux GPIO de la MPU fonctionnent dans le domaine basse tension du processeur d’application (1,8 V). Veillez à ce que toute connexion au microcontrôleur soit compatible en niveau avec son rail de tension d’E/S (3,3 V). Utilisez par exemple un convertisseur de niveau ou une configuration à drain ouvert avec une résistance de tirage vers le haut vers le rail d’E/S du microcontrôleur.

<div style="page-break-after: always;"></div>

## Accélération matérielle

VENTUNO Q offre une accélération matérielle pour l’IA en périphérie, les graphismes 3D et l’encodage/décodage vidéo grâce au processeur d’IA Hexagon™ Tensor (NPU), au GPU Adreno™ 623 et au VPU Adreno™ 623 intégrés.

### Accélération IA (NPU)

Le processeur d’IA Hexagon™ Tensor intégré offre jusqu’à 40 TOPS (téra-opérations par seconde) de calcul de réseaux neuronaux en mode dense. Il permet à VENTUNO Q d’exécuter hors ligne des LLM (grands modèles linguistiques), des VLM (modèles linguistiques de vision) et des pipelines complexes de vision par ordinateur.

La NPU est intégrée à la pile d’IA Qualcomm et prise en charge en natif dans Arduino App Lab. Les développeurs peuvent déployer des modèles optimisés via **TensorFlow Lite, ONNX Runtime et PyTorch**. VENTUNO Q offre également une intégration directe avec **Edge Impulse Studio** pour un apprentissage et un déploiement rapides de modèles d’IA en périphérie personnalisés, sans avoir à écrire de code standard.

| **Composant**             | **Spécifications**                                                     |
| ------------------------- | ---------------------------------------------------------------------- |
| Processeur                | Processeur IA Hexagon™ Tensor                                          |
| Performances maximales    | Jusqu’à 40 TOPS en calcul dense                                        |
| Architecture              | DSP Hexagon + quadruples coprocesseurs HVX + doubles coprocesseurs HMX |
| Frameworks pris en charge | TensorFlow Lite, ONNX Runtime, PyTorch                                 |
| Intégration               | Qualcomm AI Stack, Arduino App Lab, Edge Impulse Studio                |

### Accélération graphique (GPU)

Le GPU Adreno™ 623 offre des capacités graphiques 3D accélérées par le matériel et des capacités de calcul à usage général (GPGPU) sur le SoM QCS8275. Sous Qualcomm Linux, l’accélération GPU est assurée par la pile de pilotes Adreno propriétaire de Qualcomm via le pilote noyau KGSL.

Pour consulter les spécifications matérielles complètes du GPU, veuillez vous reporter à la [fiche technique du QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html) et le [Guide graphique Qualcomm Linux](https://docs.qualcomm.com/doc/80-70018-19/topic/).

>📝 **Remarque :** Les bibliothèques du pilote Adreno et les fichiers de micrologiciel se trouvent dans le répertoire `/lib/firmware/` de l’appareil. Toutes les fonctionnalités du GPU répertoriées dans la documentation du QCS8275 ne sont pas nécessairement disponibles dans le logiciel fourni avec VENTUNO Q. Veuillez vous reporter à la [documentation VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) pour obtenir la liste actuelle des fonctionnalités prises en charge.

### Accélération vidéo (VPU)

Le VPU Adreno™ 623 assure un traitement vidéo accéléré par le matériel sur le SoM QCS8275. Les codecs et résolutions pris en charge, ainsi que les détails d’intégration, dépendent de la pile logicielle fournie avec la carte. Pour consulter les spécifications matérielles complètes, veuillez vous reporter à la [fiche technique du QCS8275 (80-73475-1)](https://docs.qualcomm.com/doc/80-73475-1/topic/device-description.html).

>📝 **Remarque :** tous les codecs ou frameworks répertoriés dans la documentation du QCS8275 ne sont pas nécessairement disponibles dans le logiciel fourni avec VENTUNO Q. Veuillez consulter la [documentation VENTUNO Q](https://docs.arduino.cc/hardware/ventuno-q/) pour obtenir la liste actuelle des fonctionnalités prises en charge.

>📝 **Remarque :** Les plugins GStreamer spécifiques à Qualcomm (`gstreamer1.0-plugins-qcom`) ne sont pas inclus par défaut dans l’image Ubuntu fournie avec VENTUNO Q. Ils peuvent être installés manuellement lorsque la capture par caméra avec accélération matérielle ou des pipelines vidéo sont nécessaires. Veuillez vous reporter au [Manuel d'utilisation de VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) pour plus de détails sur la configuration.

<div style="page-break-after: always;"></div>

## Périphériques et connecteurs

VENTUNO Q met à disposition son architecture à double cœur via un ensemble complet de connecteurs et de broches. Les connecteurs pilotés par le microcontrôleur (MCU) fonctionnent à une tension logique de **3,3 V**, tandis que ceux pilotés par le processeur (MPU) fonctionnent à **1,8 V**. Vérifiez toujours la tension de chaque connecteur avant d’y brancher des périphériques externes afin d’éviter tout dommage matériel.

### JANALOG

Le connecteur JANALOG fournit des entrées analogiques, des rails d’alimentation et des signaux de commande du microcontrôleur. Il est compatible avec la disposition standard des connecteurs analogiques de l’Arduino UNO. Les entrées analogiques se réfèrent à `VREF+` sur le rail 3,3 V et ne doivent pas dépasser `VDD + 0,3 V` (~3,6 V). **N’appliquez pas de tension de 5 V aux broches analogiques**. `IOREF` est une sortie de référence de 3,3 V ; veuillez donc ne pas y injecter de courant en retour.

| **Broche** | **Désignation** | **Réseau**            | **Domaine**           | **Broche du microcontrôleur** | **Remarques**                          |
| ---------: | --------------- | --------------------- | --------------------- | ----------------------------- | -------------------------------------- |
|          1 | NC              | JANALOG_BOOT_MCU_3V3  | 3,3 V MCU             | BOOT0                         | Circuit d'amorçage du microcontrôleur  |
|          2 | IOREF           | +3V3_LIMITED          | Alimentation          | -                             | Sortie de référence de tension E/S     |
|          3 | RESET           | JANALOG_RESET_MCU_3V3 | Microcontrôleur 3,3 V | NRST                          | Réinitialisation du microcontrôleur    |
|          4 | +3V3 OUT        | +3V3_LIMITED          | Alimentation          | -                             | Sortie d'alimentation 3,3 V            |
|          5 | +5 V USB        | +5V_LIMITED           | Alimentation          | -                             | Sortie d'alimentation 5 V (limité USB) |
|          6 | GND             | GND                   | Alimentation          | -                             | Masse                                  |
|          7 | GND             | GND                   | Alimentation          | -                             | Masse                                  |
|          8 | VIN             | 7-24 V                | Alimentation          | -                             | Entrée CC (alimentation uniquement)    |
|          9 | A0              | JANALOG_A0_MCU_3V3    | Analogique            | PA4                           | Entrée ADC, non compatible avec 5 V    |
|         10 | A1              | JANALOG_A1_MCU_3V3    | Analogique            | PA5                           | Entrée ADC, non compatible avec 5 V    |
|         11 | A2              | JANALOG_A2_MCU_3V3    | Analogique            | PE12                          | Entrée ADC / SPI4_SCK                  |
|         12 | A3              | JANALOG_A3_MCU_3V3    | Analogique            | PE13                          | Entrée ADC / SPI4_MISO                 |
|         13 | A4              | JANALOG_A4_MCU_3V3    | Analogique            | PE14                          | Entrée ADC / SPI4_MOSI                 |
|         14 | A5              | JANALOG_A5_MCU_3V3    | Analogique            | PE15                          | Entrée ADC                             |

>📝 **Remarque :** A0 et A1 sont des entrées ADC directes du microcontrôleur et ne supportent pas une tension de 5 V. La plage d’entrée valide est comprise entre 0 V et `VREF+` (~3,3 V). La broche VIN (broche 8) est une entrée réservée à l’alimentation et ne doit pas être utilisée comme GPIO. La broche VIN est protégée par un fusible PTC de 1,1 A, ce qui limite sa puissance à environ 26 W à 24 V. Il n’est pas recommandé d’alimenter la carte à partir de cette broche en pleine charge. Elle est davantage adaptée au prélèvement d’énergie pour alimenter un shield ou un périphérique plutôt qu’à servir de source d’alimentation principale pour la carte.

>📝 **Remarque :** les broches A4 (PE14) et A5 (PE15) sont exclusivement des broches analogiques compatibles SPI et ne disposent pas de périphérique I2C matériel. Les shields nécessitant une interface I2C sur les broches A4 et A5 devront utiliser une interface I2C logicielle (bit-banging). L'I2C matériel est disponible sur les broches JDIGITAL 17 (SDA, PH12) et 18 (SCL, PH11).

### JDIGITAL

Le connecteur JDIGITAL fournit des signaux d'E/S numériques, UART, SPI, I2C et PWM pilotés par le microcontrôleur à une tension logique de 3,3 V. Il est compatible avec la disposition standard du connecteur numérique de l'Arduino UNO.

| **Broche** | **Désignation** | **Net**               | **Domaine**               | **Broche du microcontrôleur** | **Remarques**                   |
| ---------: | --------------- | --------------------- | ------------------------- | ----------------------------- | ------------------------------- |
|          1 | D0 / RX         | JDIGITAL_MCU_UART_3V3 | MCU 3,3 V                 | PB11                          | UART RX                         |
|          2 | D1 / TX         | JDIGITAL_MCU_UART_3V3 | MCU 3,3 V MCU             | PB10                          | UART TX                         |
|          3 | D2              | JDIGITAL_D2_MCU_3V3   | 3,3 V MCU                 | PB0                           | GPIO                            |
|          4 | D3              | JDIGITAL_D3_MCU_3V3   | 3,3 V MCU                 | PB1                           | GPIO / PWM                      |
|          5 | D4              | JDIGITAL_D4_MCU_3V3   | Microcontrôleur 3,3 V     | PB6                           | GPIO / FDCAN2_TX                |
|          6 | D5              | JDIGITAL_D5_MCU_3V3   | Microcontrôleur 3,3 V     | PB5                           | GPIO / PWM / FDCAN2_RX          |
|          7 | D6              | JDIGITAL_D6_MCU_3V3   | Microcontrôleur 3,3 V     | PB2                           | GPIO / PWM                      |
|          8 | D7              | JDIGITAL_D7_MCU_3V3   | Microcontrôleur 3,3 V MCU | PB3                           | GPIO                            |
|          9 | D8              | JDIGITAL_D8_MCU_3V3   | 3,3 V MCU                 | PB4                           | GPIO                            |
|         10 | D9              | JDIGITAL_D9_MCU_3V3   | 3,3 V MCU                 | PB7                           | GPIO / PWM                      |
|         11 | D10 / CS        | JDIGITAL_MCU_SPI_3V3  | Microcontrôleur 3,3 V     | PB12                          | Sélection de puce SPI           |
|         12 | D11 / MOSI      | JDIGITAL_MCU_SPI_3V3  | MCU 3,3 V                 | PB15                          | SPI MOSI / PWM                  |
|         13 | D12 / MISO      | JDIGITAL_MCU_SPI_3V3  | MCU 3,3 V                 | PB14                          | SPI MISO                        |
|         14 | D13 / SCK       | JDIGITAL_MCU_SPI_3V3  | MCU 3,3 V                 | PB13                          | Horloge SPI                     |
|         15 | GND             | GND                   | Alimentation              | -                             | Masse                           |
|         16 | AREF            | JDIGITAL_AREF_MCU_3V3 | Analogique                | -                             | Référence de tension analogique |
|         17 | SDA             | JDIGITAL_MCU_I2C_3V3  | Microcontrôleur 3,3 V     | PH12                          | Données I2C (I2C4 / I3C1)       |
|         18 | SCL             | JDIGITAL_MCU_I2C_3V3  | MCU 3,3 V                 | PH11                          | Horloge I2C (I2C4 / I3C1)       |

>📝 **Remarque :** Toutes les lignes JDIGITAL sont en logique 3,3 V pour microcontrôleur. La plupart des broches tolèrent une tension de 5 V en mode numérique. AREF est une entrée de référence de tension analogique destinée au convertisseur analogique-numérique (ADC) du microcontrôleur. Elle est acheminée via un commutateur analogique intégré (U28, SGM3157YC6/TR) et n’est active que lorsque la broche PI8 du microcontrôleur est mise à l’état HAUT.

### JSPI

Le connecteur JSPI met à disposition un bus SPI dédié pour connecter des périphériques tels que des lecteurs de cartes SD, des pilotes d’affichage ou des capteurs. Il fournit également les signaux RESET et d’alimentation. Tous les signaux sont dans le domaine 3,3 V du microcontrôleur.

| **Broche** | **Désignation** | **Réseau**       | **Domaine**                           | **Broche du microcontrôleur** | **Remarques**                       |
| ---------: | --------------- | ---------------- | ------------------------------------- | ----------------------------- | ----------------------------------- |
|          1 | MISO            | JSPI_MCU_SPI_3V3 | 3,3 V du microcontrôleur              | PF14                          | SPI MISO                            |
|          2 | +5 V            | +5V_LIMITED      | Alimentation                          | -                             | Sortie d'alimentation 5 V           |
|          3 | SCK             | JSPI_MCU_SPI_3V3 | Microcontrôleur 3,3 V                 | PC10                          | Horloge SPI                         |
|          4 | MOSI            | JSPI_MCU_SPI_3V3 | Microcontrôleur 3,3 V microcontrôleur | PC12                          | MOSI SPI                            |
|          5 | RESET           | MCU_NRST         | 3,3 V microcontrôleur                 | NRST                          | Réinitialisation du microcontrôleur |
|          6 | GND             | GND              | Alimentation                          | -                             | Masse                               |

>⚠️ **Remarque concernant la protection de l’alimentation :** Les lignes d’alimentation 3,3 V et 5 V sur les connecteurs JSPI et du shield UNO sont protégées par des commutateurs de charge dédiés (MP5077GG-Z), chacun limité à **2,8 A**. Ces commutateurs empêchent les périphériques connectés de consommer un courant excessif et protègent la carte contre les retours de courant. N’essayez pas de contourner ou de désactiver ces commutateurs.

### Qwiic

Le connecteur Qwiic fournit un bus I2C de 3,3 V permettant une connexion « plug-and-play » aux nœuds Modulino® et aux capteurs tiers compatibles, sans aucune soudure requise. Le connecteur est polarisé et ne permet qu’une seule orientation pour la connexion.

| **Broche** | **Désignation** | **Réseau**   | **Domaine**  | **Broche du microcontrôleur** | **Remarques**                             |
| ---------: | --------------- | ------------ | ------------ | ----------------------------- | ----------------------------------------- |
|          1 | GND             | GND          | Alimentation | -                             | Masse                                     |
|          2 | VCC             | +3V3_LIMITED | Alimentation | -                             | Alimentation 3,3 V pour les périphériques |
|          3 | SDA             | I2C3_SDA     | MCU 3,3 V    | PC9                           | Données I2C                               |
|          4 | SCL             | I2C3_SCL     | MCU 3,3 V    | PA8                           | Horloge I2C                               |

>📝 **Remarque :** les connecteurs Qwiic sont extensibles en chaîne et plusieurs modules peuvent être connectés en série sur le même bus I2C. Le bus I2C est connecté au microcontrôleur.

### JCTL (débogage à distance du MPU)

Le connecteur JCTL est un connecteur à 10 broches (2×5) qui permet l’accès à la console UART du MPU, le contrôle de la redéfinition du démarrage et les signaux de gestion de l’alimentation. L’Arduino Bughopper est l’outil recommandé pour l’interfaçage avec ce connecteur. La plupart des broches de signal actives sont protégées contre les décharges électrostatiques (ESD) par des diodes TVS (la broche 10 ne l’est pas). Les broches de signal fonctionnent dans des domaines de tension mixtes : 1,8 V, 3,3 V et 7-24 V ; veuillez vous reporter au tableau des broches ci-dessous. La broche 9 expose directement le rail `SOM_VREG_MDPX3_1P8` ; n’appliquez aucune tension externe à cette broche.

| **Broche** | **Désignation**        | **Réseau**         | **Domaine**               | **Broche MPU** | **Remarques**                                                                                                                                                                |
| ---------: | ---------------------- | ------------------ | ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          1 | GND                    | GND                | Alimentation              | -              | Masse                                                                                                                                                                        |
|          2 | FORCED_USB_BOOT_N      | FORCE_BOOT_3V3     | 3,3 V                     | -              | Domaine 3,3 V. Commande deux transistors NMOS pilotant MD_FORCE_USB_BOOT_1V8 et RTSS_FORCE_USB_BOOT_1V8. Mettez à l'état bas pour passer en mode EDL au prochain redémarrage |
|          3 | PMIC_POWER_EN          | PMIC_POWER_EN      | MPU 1,8 V                 | -              | Activation de l’alimentation du PMIC                                                                                                                                         |
|          4 | TX                     | UART_DBG_1V8       | MPU 1,8 V                 | GPIO_43        | Émetteur UART de débogage de la MPU                                                                                                                                          |
|          5 | GPIO                   | MD_GPIO_103        | MPU 1,8 V MPU             | GPIO_103       | GPIO à usage général                                                                                                                                                         |
|          6 | RX                     | UART_DBG_1V8       | 1,8 V MPU                 | GPIO_44        | UART de débogage MPU (réception)                                                                                                                                             |
|          7 | GND                    | GND                | Alimentation              | -              | Masse                                                                                                                                                                        |
|          8 | RESIN_N                | RESIN_N            | 3,3 V                     | -              | Sortie à drain ouvert, protégée par TVS. Mettre à l’état bas pour un redémarrage à chaud (les rails d’alimentation restent sous tension)                                     |
|          9 | +1V8 OUT               | SOM_VREG_MDPX3_1P8 | Alimentation              | -              | Domaine MDPX3 1,8 V direct, ne pas appliquer de tension externe                                                                                                              |
|         10 | POWER_SWITCH_DISABLE_N | PWR_DISABLE        | 7-24 V (jusqu’à 5 V max.) | -              | Non protégé par TVS. Mettez à LOW pour un redémarrage à froid (commande l’alimentation principale)                                                                           |

> ⚠️ **À lire avant de connecter quoi que ce soit au JCTL**
>
> La broche 9 expose directement `SOM_VREG_MDPX3_1P8` (~1,8 V) ; n’appliquez aucune tension externe à cette broche. Les broches fonctionnent dans des domaines de tension mixtes : les broches 2 et 8 sont dans le domaine 3,3 V, les broches 4 et 6 (UART) sont à 1,8 V, la broche 10 est l’entrée d’activation du commutateur d’alimentation principal VIN ; un diviseur de tension interne permet une connexion directe à VIN. Ramenez la tension en dessous de 0,85 V pour désactiver l’alimentation principale, maintenez-la au-dessus de 1 V pour un fonctionnement normal et ne dépassez pas 5 V en externe. La broche 10 n’est pas protégée par un TVS. L’application de tensions incorrectes à n’importe quelle broche JCTL active peut endommager de manière irréversible le SoM QCS8275.
>
> **L’Arduino Bughopper est vivement recommandé** pour la plupart des cas d’utilisation en débogage, car il intègre des convertisseurs de niveau et des étages de sortie compatibles open-drain spécialement conçus pour une interfaçage JCTL en toute sécurité.
>
> Si vous choisissez d’utiliser un autre adaptateur USB-UART ou du matériel de débogage personnalisé, assurez-vous que toutes les lignes de signal sont alimentées à la tension correcte pour leur domaine respectif, que la broche 10 ne dépasse jamais 5 V et qu’il n’existe aucun chemin de retour de puissance vers le rail `SOM_VREG_MDPX3_1P8`.

> 📝 **Résumé des commandes de démarrage :**
>
> - **Redémarrage à chaud** (MPU uniquement, les rails de tension restent actifs) : Mettez la broche 8 (RESIN_N) à l'état BAS via un circuit à drain ouvert.
> - **Redémarrage à froid** (cycle d'alimentation complet, source d'alimentation principale coupée) : Mettez la broche 10 (POWER_SWITCH_DISABLE_N) à l'état bas via une sortie à drain ouvert.
> - **Mode EDL / Téléchargement d'urgence** : Mettez la broche 2 (FORCED_USB_BOOT_N) à l'état bas via une sortie à drain ouvert, puis déclenchez un redémarrage via la broche 8 ou la broche 10.
>
> Ce connecteur est destiné à des fins de développement et de débogage.

### JHAT

Le connecteur JHAT est un connecteur standard à 40 broches compatible Raspberry Pi®, piloté par le MPU (QCS8275) en logique **3,3 V**. Il expose les signaux I2C, SPI, UART, I2S et GPIO à usage général provenant du MPU. Les broches d’alimentation fournissent 3,3 V et 5 V aux HAT connectés.

Tous les signaux GPIO sont convertis en niveau, passant du domaine 1,8 V du MPU au domaine 3,3 V des HAT, grâce à quatre convertisseurs de niveau bidirectionnels intégrés : trois dispositifs TXS0108ERKSR à 8 canaux (U33_2, U33_3, U33_4) et un dispositif TXS0104ERUTR à 4 canaux (U21), ce qui permet une compatibilité directe avec les conceptions HAT Raspberry Pi® standard sans conversion de niveau supplémentaire.

| **Broche** | **Désignation** | **Broche MPU** | **Fonction alternative** | **Domaine**  | **Remarques**                |
| ---------: | --------------- | -------------- | ------------------------ | ------------ | ---------------------------- |
|          1 | Sortie +3,3 V   | -              | -                        | Alimentation | Sortie d'alimentation 3,3 V  |
|          2 | Sortie +5 V     | -              | -                        | Alimentation | Sortie d'alimentation 5 V    |
|          3 | GPIO 2 (SDA)    | MD_GPIO_17     | QUP0_SE0_I2C_SDA         | MPU 3,3 V    | Données I2C1                 |
|          4 | +5V OUT         | -              | -                        | Alimentation | Sortie d'alimentation 5 V    |
|          5 | GPIO 3 (SCL)    | MD_GPIO_18     | QUP0_SE0_I2C_SCL         | 3,3 V MPU    | Horloge I2C1                 |
|          6 | GND             | -              | -                        | Alimentation | Masse                        |
|          7 | GPIO 4          | MD_GPIO_83     | GPCLK0                   | 3,3 V MPU    | GPIO général                 |
|          8 | GPIO 14 (TX)    | MD_GPIO_86     | QUP1_SE2_UART_TX         | 3,3 V MPU    | UART0 TX                     |
|          9 | GND             | -              | -                        | Alimentation | Masse                        |
|         10 | GPIO 15 (RX)    | MD_GPIO_87     | QUP1_SE2_UART_RX         | 3,3 V MPU    | UART0 RX                     |
|         11 | GPIO 17         | MD_GPIO_85     | QUP1_SE2_UART_RFR        | 3,3 V MPU    | UART RFR/RTS                 |
|         12 | GPIO 18 (CLK)   | MD_GPIO_116    | LPI_I2S1_SCK             | 3,3 V MPU    | Horloge PCM                  |
|         13 | GPIO 27         | MD_GPIO_109    | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         14 | GND             | -              | -                        | Alimentation | Masse                        |
|         15 | GPIO 22         | MD_GPIO_90     | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         16 | GPIO 23         | MD_GPIO_105    | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         17 | Sortie +3V3     | -              | -                        | Alimentation | Sortie d'alimentation 3,3 V  |
|         18 | GPIO 24         | MD_GPIO_106    | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         19 | GPIO 10 (MOSI)  | MD_GPIO_26     | QUP0_SE3_SPI_MOSI        | 3,3 V MPU    | SPI0 MOSI                    |
|         20 | GND             | -              | -                        | Alimentation | Masse                        |
|         21 | GPIO 9 (MISO)   | MD_GPIO_25     | QUP0_SE3_SPI_MISO        | 3,3 V MPU    | SPI0 MISO                    |
|         22 | GPIO 25         | MD_GPIO_107    | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         23 | GPIO 11 (SCLK)  | MD_GPIO_27     | QUP0_SE3_SPI_SCK         | 3,3 V MPU    | Horloge SPI0                 |
|         24 | GPIO 8 (CE0)    | MD_GPIO_28     | QUP0_SE3_SPI_CS          | 3,3 V MPU    | CE0 SPI0                     |
|         25 | GND             | -              | -                        | Alimentation | Masse                        |
|         26 | GPIO 7 (CE1)    | MD_GPIO_88     | GPIO                     | 3,3 V MPU    | SPI0 CE1                     |
|         27 | GPIO 0 (SDA)    | MD_GPIO_19     | QUP0_SE1_I2C_SDA         | 3,3 V MPU    | I2C0 / EEPROM SDA            |
|         28 | GPIO 1 (SCL)    | MD_GPIO_20     | QUP0_SE1_I2C_SCL         | 3,3 V MPU    | I2C0 / EEPROM SCL            |
|         29 | GPIO 5          | MD_GPIO_89     | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         30 | GND             | -              | -                        | Alimentation | Masse                        |
|         31 | GPIO 6          | MD_GPIO_80     | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         32 | GPIO 12 (PWM0)  | MD_GPIO_77     | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         33 | GPIO 13 (PWM1)  | MD_GPIO_81     | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         34 | GND             | -              | -                        | Alimentation | Masse                        |
|         35 | GPIO 19 (FS)    | MD_GPIO_117    | LPI_I2S1_WS              | 3,3 V MPU    | Synchronisation de trame PCM |
|         36 | GPIO 16         | MD_GPIO_84     | QUP1_SE2_UART_CTS        | 3,3 V MPU    | CTS UART                     |
|         37 | GPIO 26         | MD_GPIO_108    | GPIO                     | 3,3 V MPU    | GPIO général                 |
|         38 | GPIO 20 (DIN)   | MD_GPIO_118    | LPI_I2S1_DATA0           | 3,3 V MPU    | Entrée de données PCM        |
|         39 | GND             | -              | -                        | Alimentation | Masse                        |
|         40 | GPIO 21 (DOUT)  | MD_GPIO_119    | LPI_I2S1_DATA1           | 3,3 V MPU    | Sortie de données PCM        |

>📝 **Remarque :** bien que les signaux GPIO du MPU soient à 1,8 V en interne, les convertisseurs de niveau TXS0108ERKSR et TXS0104ERUTR intégrés les transmettent à 3,3 V sur le connecteur JHAT, ce qui les rend directement compatibles avec les niveaux logiques standard des HAT Raspberry Pi®. N’appliquez pas de tensions supérieures à 3,3 V sur les broches de signal JHAT. Les broches d’alimentation (3,3 V et 5 V) sont des sorties de la carte ; veuillez ne pas y renvoyer de courant provenant d’un HAT connecté.

>📝 **Remarque :** les broches UART JHAT 8, 10, 11 et 36 (TX, RX, RFR et CTS) partagent le même UART QUP1_SE2 que le module Wi-Fi®/Bluetooth® LE intégré. Les broches TX, RX et RFR sont converties en niveau via U33_4 (TXS0108ERKSR), tandis que la broche CTS est convertie séparément via U21 (TXS0104ERUTR) avec les broches GPIO 26, GPIO 20 (I2S_DATA0) et GPIO 21 (I2S_DATA1) sur les broches 37, 38 et 40. Ces broches ne sont pas disponibles pour une utilisation avec des modules HAT externes lorsque le Bluetooth est actif.

### JMISC

Le connecteur JMISC est un connecteur haute densité à 60 broches qui regroupe le bus parallèle PSSI de la caméra du microcontrôleur (MCU), les broches GPIO du MCU, le bus I2C du MCU, les signaux audio (microphone, casque, sortie haut-parleur mono, sortie ligne), le bus SPI du SoC du processeur (MPU), les broches GPIO du MPU et les signaux I2S du MPU. Il s’agit d’un connecteur à tensions mixtes : **les signaux du microcontrôleur sont à 3,3 V**, **les signaux du processeur sont à 1,8 V** et les broches audio/micro sont analogiques.

| **Broche** | **Désignation**    | **Domaine**           | **Broche MCU** | **Broche MPU** | **Remarques**                                                          |
| ---------: | ------------------ | --------------------- | -------------- | -------------- | ---------------------------------------------------------------------- |
|          1 | MCU_PSSI_D0        | 3,3 V MCU             | PA9            | -              | Bit de données PSSI 0                                                  |
|          2 | MCU_TRACE_CLK      | 3,3 V MCU             | PE2            | -              | Horloge de trace du MCU                                                |
|          3 | MCU_PSSI_D1        | 3,3 V MCU             | PC7            | -              | Bit de données PSSI 1                                                  |
|          4 | MCU_TRACE_D0       | 3,3 V MCU             | PE3            | -              | Données de trace MCU 0                                                 |
|          5 | MCU_PSSI_D2        | 3,3 V MCU             | PC8            | -              | Bit de données PSSI n° 2                                               |
|          6 | MCU_TRACE_D1       | MCU 3,3 V             | PE4            | -              | Données de trace du microcontrôleur n° 1                               |
|          7 | MCU_PSSI_D3        | MCU 3,3 V             | PE1            | -              | Bit de données PSSI n° 3                                               |
|          8 | MCU_TRACE_D2       | MCU 3,3 V             | PE5            | -              | Données de trace MCU 2                                                 |
|          9 | MCU_PSSI_D4        | MCU 3,3 V             | PC11           | -              | Bit de données PSSI n° 4                                               |
|         10 | MCU_TRACE_D3       | MCU 3,3 V             | PE6            | -              | Données de trace du microcontrôleur n° 3                               |
|         11 | MCU_PSSI_D5        | MCU 3,3 V             | PD3            | -              | Bit de données PSSI n° 5                                               |
|         12 | MCU_USART2_RX      | MCU 3,3 V             | PE7            | -              | Réception USART2 du microcontrôleur                                    |
|         13 | MCU_PSSI_D6        | MCU 3,3 V             | PF4            | -              | Bit de données PSSI n° 6                                               |
|         14 | MCU_USART2_TX      | 3,3 V MCU             | PE8            | -              | Émetteur USART2 du microcontrôleur                                     |
|         15 | MCU_PSSI_D7        | 3,3 V MCU             | PI7            | -              | Bit de données PSSI n° 7                                               |
|         16 | MCU_I2C_SCL        | 3,3 V MCU             | PF1            | -              | Horloge I2C2 du microcontrôleur                                        |
|         17 | MCU_PSSI_PDCK      | 3,3 V MCU             | PA6            | -              | Horloge pixel PSSI                                                     |
|         18 | MCU_I2C_SDA        | 3,3 V MCU             | PF0            | -              | Données I2C2 du microcontrôleur                                        |
|         19 | MCU_PSSI_RDY       | 3,3 V MCU             | PI5            | -              | Prêt PSSI                                                              |
|         20 | MCU_GPIO_PA0       | 3,3 V MCU             | PA0            | -              | GPIO du microcontrôleur                                                |
|         21 | MCU_PSSI_DE        | 3,3 V MCU             | PH8            | -              | Activation des données PSSI                                            |
|         22 | MCU_GPIO_PA1       | 3,3 V MCU             | PA1            | -              | GPIO du microcontrôleur                                                |
|         23 | MCU_UART4_RX       | 3,3 V MCU             | PA11           | -              | Réception UART4 du microcontrôleur                                     |
|         24 | MCU_GPIO_PA2       | 3,3 V microcontrôleur | PA2            | -              | GPIO du microcontrôleur                                                |
|         25 | MCU_UART4_TX       | 3,3 V microcontrôleur | PA12           | -              | Sortie TX de l’UART4 du microcontrôleur                                |
|         26 | GND                | Alimentation          | -              | -              | Masse                                                                  |
|         27 | GND                | Alimentation          | -              | -              | Masse                                                                  |
|         28 | EAR_P              | Analogique            | -              | -              | Sortie haut-parleur P (mono)                                           |
|         29 | MIC_INP            | Analogique            | -              | -              | Entrée microphone+                                                     |
|         30 | EAR_M              | Analogique            | -              | -              | Sortie haut-parleur M (mono)                                           |
|         31 | MIC_INN            | Analogique            | -              | -              | Entrée microphone−                                                     |
|         32 | LINEOUT_P          | Analogique            | -              | -              | Sortie ligne P                                                         |
|         33 | MIC_BIAS           | Analogique            | -              | -              | Polarisation du microphone                                             |
|         34 | LINEOUT_M          | Analogique            | -              | -              | Sortie ligne M                                                         |
|         35 | GND                | Alimentation          | -              | -              | Masse                                                                  |
|         36 | HPH_L              | Analogique            | -              | -              | Casque gauche                                                          |
|         37 | SOC_SPI_MISO       | MPU 1,8 V             | -              | GPIO_10        | MPU SPI MISO (SE0)                                                     |
|         38 | HPH_R              | Analogique            | -              | -              | Écouteur droit                                                         |
|         39 | SOC_SPI_MOSI       | 1,8 V MPU             | -              | GPIO_11        | MPU SPI MOSI (SE0)                                                     |
|         40 | HPH_REF            | Analogique            | -              | -              | Référence casque                                                       |
|         41 | SOC_SPI_SCK        | 1,8 V MPU             | -              | GPIO_12        | Horloge SPI MPU (SE0)                                                  |
|         42 | HS_DET             | Analogique            | -              | -              | Détection du casque                                                    |
|         43 | SOC_SPI_CS0        | 1,8 V MPU             | -              | GPIO_13        | Sélection de puce SPI MPU 0 (SE0)                                      |
|         44 | GND                | Alimentation          | -              | -              | Masse                                                                  |
|         45 | SOC_SPI_CS2        | 1,8 V MPU             | -              | GPIO_15        | Sélection de puce SPI MPU 2 (SE0)                                      |
|         46 | SOC_MI2S_SCK       | 1,8 V MPU             | -              | GPIO_120       | Horloge I2S                                                            |
|         47 | SOC_SPI_CS1        | 1,8 V MPU             | -              | GPIO_14        | Sélection de puce SPI MPU 1 (SE0)                                      |
|         48 | SOC_MI2S_WS        | 1,8 V MPU             | -              | GPIO_121       | Sélection de mot I2S                                                   |
|         49 | SOC_GPIO_73        | 1,8 V MPU             | -              | GPIO_73        | GPIO SoC de la MPU                                                     |
|         50 | SOC_MI2S_DATA0     | 1,8 V MPU             | -              | GPIO_122       | Données I2S 0                                                          |
|         51 | SOC_GPIO_74        | 1,8 V MPU             | -              | GPIO_74        | GPIO du SoC MPU                                                        |
|         52 | SOC_MI2S_DATA1     | 1,8 V MPU             | -              | GPIO_123       | Données I2S 1                                                          |
|         53 | +3V3 OUT           | Alimentation          | -              | -              | Sortie d'alimentation 3,3 V                                            |
|         54 | +5V OUT            | Alimentation          | -              | -              | Sortie d'alimentation 5 V                                              |
|         55 | +3V3 OUT           | Alimentation          | -              | -              | Sortie d'alimentation 3,3 V                                            |
|         56 | +5V OUT            | Alimentation          | -              | -              | Sortie d'alimentation 5 V                                              |
|         57 | SOM_VREG_MDPX3_1P8 | Alimentation          | -              | -              | Rail SOM 1,8 V                                                         |
|         58 | GND                | Alimentation          | -              | -              | Masse                                                                  |
|         59 | SOM_VCOIN / VBAT   | Sauvegarde RTC        | -              | -              | Entrée de la batterie de secours RTC pour le SOM et le microcontrôleur |
|         60 | NON CONNECTÉ       | -                     | -              | -              | -                                                                      |

>📝 **Remarque :** les broches du MCU sont en 3,3 V, celles du SoC MPU en 1,8 V, et les broches audio/micro sont analogiques. Ne mélangez pas les domaines de tension. Les lignes GPIO du SoC sur le JMISC sont dédiées à l’interface et ne constituent pas des GPIO à usage général pour les makers.

>📝 **Remarque :** la broche 59 du JMISC accepte une batterie de secours RTC jusqu’à 3,3 V afin de maintenir les horloges en temps réel du SOM et du microcontrôleur lorsque la carte n’est pas alimentée. `SOM_VCOIN` (RTC du SOM) et `VBAT` (RTC du microcontrôleur) sont deux entrées de batterie de secours pour l’horloge en temps réel qui sont physiquement reliées entre elles au niveau de cette broche unique, plutôt que d’être raccordées à un rail d’alimentation commun. Chacune est connectée via sa propre résistance de 0 Ω à un nœud commun, qui est protégé par une diode TVS bidirectionnelle (Vr = 5,5 V) référencée à la masse. La consommation de courant attendue est très faible, et cette broche ne fournit pas d’alimentation pour maintenir le reste de la carte sous tension.

### JMEDIA

Le connecteur JMEDIA est un connecteur haute densité à 60 broches qui achemine les signaux MIPI DSI (affichage), MIPI CSI0 et CSI1, les signaux d’horloge de la caméra et les bus I2C de contrôle de la caméra. Tous les signaux sont dans le **domaine MPU à 1,8 V**. Les broches d’alimentation fournissent une tension de sortie de 3,3 V et acceptent une tension d’entrée de 7 à 24 V CC.

| **Broche** | **Désignation** | **Domaine**  | **Broche MPU** | **Remarques**                                              |
| ---------: | --------------- | ------------ | -------------- | ---------------------------------------------------------- |
|          1 | GND             | Alimentation | -              | Masse                                                      |
|          2 | GND             | Alimentation | -              | Masse                                                      |
|          3 | MIPI_DSI0_CLK_M | MIPI D-PHY   | -              | Horloge DSI −                                              |
|          4 | MIPI_DSI0_L1_P  | MIPI D-PHY   | -              | Voie DSI 1 +                                               |
|          5 | MIPI_DSI0_CLK_P | MIPI D-PHY   | -              | Horloge DSI +                                              |
|          6 | MIPI_DSI0_L1_M  | MIPI D-PHY   | -              | Voie DSI 1 −                                               |
|          7 | GND             | Alimentation | -              | Masse                                                      |
|          8 | GND             | Alimentation | -              | Masse                                                      |
|          9 | MIPI_DSI0_L2_M  | MIPI D-PHY   | -              | Voie DSI 2 −                                               |
|         10 | MIPI_DSI0_L0_P  | MIPI D-PHY   | -              | Voie DSI 0 +                                               |
|         11 | MIPI_DSI0_L2_P  | MIPI D-PHY   | -              | Voie DSI 2 +                                               |
|         12 | MIPI_DSI0_L0_M  | MIPI D-PHY   | -              | voie DSI 0 −                                               |
|         13 | GND             | Alimentation | -              | Masse                                                      |
|         14 | GND             | Alimentation | -              | Masse                                                      |
|         15 | MIPI_DSI0_L3_M  | MIPI D-PHY   | -              | Voie DSI 3 −                                               |
|         16 | SOC_CAM_MCLK0   | MPU 1,8 V    | GPIO_67        | Horloge maître de la caméra 0                              |
|         17 | MIPI_DSI0_L3_P  | MIPI D-PHY   | -              | Voie DSI 3 +                                               |
|         18 | SOC_CAM_MCLK1   | 1,8 V MPU    | GPIO_68        | Horloge maître de la caméra 1                              |
|         19 | GND             | Alimentation | -              | Masse                                                      |
|         20 | GND             | Alimentation | -              | Masse                                                      |
|         21 | CSI0_LN0_M      | MIPI D-PHY   | -              | Voie de données CSI0 0 −                                   |
|         22 | CCI_I2C2_SDA    | MPU 1,8 V    | GPIO_59        | Contrôle de la caméra I2C2 SDA                             |
|         23 | CSI0_LN0_P      | MIPI D-PHY   | -              | Voie de données CSI0 0 +                                   |
|         24 | CCI_I2C2_SCL    | 1,8 V MPU    | GPIO_60        | Contrôle de la caméra I2C2 SCL                             |
|         25 | GND             | Alimentation | -              | Masse                                                      |
|         26 | GND             | Alimentation | -              | Masse                                                      |
|         27 | CSI0_LN1_M      | MIPI D-PHY   | -              | Ligne de données CSI0 1 −                                  |
|         28 | CSI1_LN3_P      | MIPI D-PHY   | -              | Voie de données CSI1 3 +                                   |
|         29 | CSI0_LN1_P      | MIPI D-PHY   | -              | Voie de données CSI0 1 +                                   |
|         30 | CSI1_LN3_M      | MIPI D-PHY   | -              | Voie de données CSI1 n° 3 −                                |
|         31 | GND             | Alimentation | -              | Masse                                                      |
|         32 | GND             | Alimentation | -              | Masse                                                      |
|         33 | CSI0_CLK_M      | MIPI D-PHY   | -              | Horloge CSI0 −                                             |
|         34 | CSI1_LN2_P      | MIPI D-PHY   | -              | Voie de données CSI1 n° 2 +                                |
|         35 | CSI0_CLK_P      | MIPI D-PHY   | -              | Horloge CSI0 +                                             |
|         36 | CSI1_LN2_M      | MIPI D-PHY   | -              | Voie de données CSI1 n° 2 −                                |
|         37 | GND             | Alimentation | -              | Masse                                                      |
|         38 | GND             | Alimentation | -              | Masse                                                      |
|         39 | CSI0_LN2_M      | MIPI D-PHY   | -              | Voie de données CSI0 n° 2 −                                |
|         40 | CSI1_CLK_P      | MIPI D-PHY   | -              | Horloge CSI1 +                                             |
|         41 | CSI0_LN2_P      | MIPI D-PHY   | -              | Voie de données CSI0 2 +                                   |
|         42 | CSI1_CLK_M      | MIPI D-PHY   | -              | Horloge CSI1 −                                             |
|         43 | GND             | Alimentation | -              | Masse                                                      |
|         44 | GND             | Alimentation | -              | Masse                                                      |
|         45 | CSI0_LN3_M      | MIPI D-PHY   | -              | Voie de données CSI0 n° 3 −                                |
|         46 | CSI1_LN1_P      | MIPI D-PHY   | -              | Voie de données CSI1 n° 1 +                                |
|         47 | CSI0_LN3_P      | MIPI D-PHY   | -              | Voie de données CSI0 n° 3 +                                |
|         48 | CSI1_LN1_M      | MIPI D-PHY   | -              | Voie de données CSI1 n° 1 −                                |
|         49 | GND             | Alimentation | -              | Masse                                                      |
|         50 | GND             | Alimentation | -              | Masse                                                      |
|         51 | CCI_I2C0_SCL    | 1,8 V MPU    | GPIO_58        | SCL I2C0 de contrôle de la caméra                          |
|         52 | CSI1_LN0_P      | MIPI D-PHY   | -              | Voie de données CSI1 0 +                                   |
|         53 | CCI_I2C0_SDA    | 1,8 V MPU    | GPIO_57        | Contrôle de la caméra I2C0 SDA                             |
|         54 | CSI1_LN0_M      | MIPI D-PHY   | -              | Voie de données CSI1 0 −                                   |
|         55 | GND             | Alimentation | -              | Masse                                                      |
|         56 | GND             | Alimentation | -              | Masse                                                      |
|         57 | VIN IN          | Alimentation | -              | Entrée 7-24 V CC (1,5 A max., protégée par PTC)            |
|         58 | +3V3 OUT        | Alimentation | -              | Sortie d'alimentation 3,3 V                                |
|         59 | VIN IN          | Alimentation | -              | Entrée 7-24 V CC (1,5 A max., protégée par un fusible PTC) |
|         60 | Sortie +3V3     | Alimentation | -              | Sortie d'alimentation 3,3 V                                |

>📝 **Remarque :** Les broches VIN de la carte JMEDIA (broches 57 et 59) font partie du même réseau, protégé par un fusible PTC de 1,5 A (F3, MF-MSMF150/24X) et une diode TVS de 24 V. Elles peuvent alimenter un carrier, mais ne sont pas destinées à alimenter l’ensemble de la carte VENTUNO Q à partir d’une source externe.

>📝 **Remarque :** Les paires différentielles MIPI CSI/DSI sont des signaux D-PHY et ne doivent pas être utilisées comme E/S à usage général. Tous les signaux de contrôle (CCI_I2C, CAM_MCLK) relèvent du domaine MPU à 1,8 V. La tension VIN sur les broches 57 et 59 correspond uniquement à la tension d'alimentation en courant continu.

### JOMEGA

Le connecteur JOMEGA est un connecteur d’extension haute densité à 100 broches qui fournit des signaux USB 3.0, CAN-FD, JTAG, GPIO du MPU, SPI et UART, ainsi que des signaux de débogage et de gestion de l’alimentation. Les domaines de tension sont mixtes : l’USB et certains signaux de contrôle fonctionnent à 3,3 V, tandis que les signaux de débogage JTAG, SPI et UART fonctionnent à 1,8 V dans le domaine du MPU.

| **Broche** | **Désignation**           | **Domaine**              | **Broche du microcontrôleur** | **Broche du MPU** | **Remarques**                                   |
| ---------: | ------------------------- | ------------------------ | ----------------------------- | ----------------- | ----------------------------------------------- |
|          1 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|          2 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|          3 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|          4 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|          5 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|          6 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|          7 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|          8 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|          9 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|         10 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         11 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|         12 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         13 | VIN                       | Alimentation             | -                             | -                 | Entrée 7-24 V CC                                |
|         14 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         15 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         16 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         17 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         18 | USB3.0_1_SS_TX_P          | USB 3.0                  | -                             | -                 | Port USB 1 SuperSpeed TX+                       |
|         19 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         20 | USB3.0_1_SS_TX_N          | USB 3.0                  | -                             | -                 | Port USB 1 SuperSpeed TX−                       |
|         21 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         22 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         23 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         24 | USB3.0_1_HS_D_P           | USB 3.0                  | -                             | -                 | Port USB 1 HighSpeed D+                         |
|         25 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         26 | USB3.0_1_HS_D_N           | USB 3.0                  | -                             | -                 | Port USB 1 haute vitesse D−                     |
|         27 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         28 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         29 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         30 | USB3.0_1_SS_RX_P          | USB 3.0                  | -                             | -                 | Port USB 1 SuperSpeed RX+                       |
|         31 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         32 | USB3.0_1_SS_RX_N          | USB 3.0                  | -                             | -                 | Port USB 1 SuperSpeed RX−                       |
|         33 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         34 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         35 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         36 | USB3.0_2_SS_TX_P          | USB 3.0                  | -                             | -                 | Port USB 2 SuperSpeed TX+                       |
|         37 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         38 | USB3.0_2_SS_TX_N          | USB 3.0                  | -                             | -                 | Port USB 2 SuperSpeed TX−                       |
|         39 | IO0_3V3                   | 3,3 V MCU                | PC0                           | -                 | GPIO du microcontrôleur                         |
|         40 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         41 | IO1_3V3                   | 3,3 V MCU                | PC1                           | -                 | GPIO du microcontrôleur                         |
|         42 | USB3.0_2_HS_D_P           | USB 3.0                  | -                             | -                 | Port USB 2 HighSpeed D+                         |
|         43 | IO2_3V3                   | 3,3 V MCU                | PC2                           | -                 | GPIO du microcontrôleur                         |
|         44 | USB3.0_2_HS_D_N           | USB 3.0                  | -                             | -                 | Port USB 2 HighSpeed D−                         |
|         45 | IO3_3V3                   | 3,3 V MCU                | PC3                           | -                 | GPIO du microcontrôleur                         |
|         46 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         47 | IO4_3V3                   | 3,3 V MCU                | PD12                          | -                 | GPIO du microcontrôleur                         |
|         48 | USB3.0_2_SS_RX_P          | USB 3.0                  | -                             | -                 | Port USB 2 SuperSpeed RX+                       |
|         49 | IO5_3V3                   | Microcontrôleur 3,3 V    | PD13                          | -                 | GPIO du microcontrôleur                         |
|         50 | USB3.0_2_SS_RX_N          | USB 3.0                  | -                             | -                 | Port USB 2 SuperSpeed RX−                       |
|         51 | IO6_3V3                   | 3,3 V du microcontrôleur | PD14                          | -                 | GPIO du microcontrôleur                         |
|         52 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         53 | IO7_3V3                   | 3,3 V du microcontrôleur | PD15                          | -                 | GPIO du microcontrôleur                         |
|         54 | USB3.0_1_PWRON_3V3        | 3,3 V                    | -                             | -                 | Activation de l’alimentation du port USB 1      |
|         55 | IO8_3V3                   | 3,3 V MCU                | PI2                           | -                 | GPIO du microcontrôleur                         |
|         56 | USB3.0_1_OVERCUR_3V3      | 3,3 V                    | -                             | -                 | Indicateur de surintensité du port USB 1        |
|         57 | MIC_INP                   | Analogique               | -                             | -                 | Entrée microphone+                              |
|         58 | USB3.0_2_PWRON_3V3        | 3,3 V                    | -                             | -                 | Activation de l'alimentation du port USB 2      |
|         59 | MIC_INN                   | Analogique               | -                             | -                 | Entrée microphone−                              |
|         60 | USB3.0_2_OVERCUR_3V3      | 3,3 V                    | -                             | -                 | Indicateur de surintensité du port USB 2        |
|         61 | MIC_BIAS                  | Analogique               | -                             | -                 | Polarisation du microphone                      |
|         62 | SPI_ICS_MISO              | 1,8 V MPU                | -                             | GPIO_39           | MPU SPI MISO (SPI_ICS_1V8)                      |
|         63 | TMS                       | 1,8 V MPU                | -                             | -                 | JTAG TMS (JTAG_1V8)                             |
|         64 | SPI_ICS_MOSI              | 1,8 V MPU                | -                             | GPIO_40           | MPU SPI MOSI                                    |
|         65 | TDO                       | 1,8 V MPU                | -                             | -                 | JTAG TDO                                        |
|         66 | SPI_ICS_SCK               | 1,8 V MPU                | -                             | GPIO_37           | Horloge SPI MPU                                 |
|         67 | TDI                       | 1,8 V MPU                | -                             | -                 | TDI JTAG                                        |
|         68 | SPI_ICS_CS                | 1,8 V MPU                | -                             | GPIO_38           | Sélection de puce SPI du MPU                    |
|         69 | TCK                       | 1,8 V MPU                | -                             | -                 | Horloge JTAG                                    |
|         70 | PM_PS_HOLD_1V8            | 1,8 V MPU                | -                             | -                 | Maintien de l'état d'alimentation de la MPU     |
|         71 | SRST_N                    | 1,8 V MPU                | -                             | -                 | Réinitialisation du système JTAG                |
|         72 | FORCED_USB_BOOT_1V8       | 1,8 V MPU                | -                             | GPIO_52           | Forcer le mode de démarrage USB                 |
|         73 | TRST_N                    | MPU 1,8 V                | -                             | -                 | Réinitialisation JTAG TAP                       |
|         74 | PWR_EN_N                  | MPU 1,8 V                | -                             | -                 | Activation de l’alimentation (niveau bas actif) |
|         75 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         76 | USER_BUTTON               | 3,3 V                    | -                             | GPIO_79           | Entrée du bouton utilisateur                    |
|         77 | SOM_VREG_S5S_SPX3_1P8     | Alimentation             | -                             | -                 | Rail SOM RTSS 1,8 V                             |
|         78 | PM_RESIN_N_3V3            | 3,3 V                    | -                             | -                 | Entrée de réinitialisation du PMIC de l’MPU     |
|         79 | SOM_VREG_MDPX3_1P8        | Alimentation             | -                             | -                 | Rail 1,8 V du SOM                               |
|         80 | RTSS_RESIN_N_1V8          | 1,8 V MPU                | -                             | -                 | Entrée de réinitialisation RTSS                 |
|         81 | SOM_VREG_MDPX3_1P8        | Alimentation             | -                             | -                 | Rail 1,8 V du SOM                               |
|         82 | RTSS_PS_HOLD_SPX3_1P8_1V8 | MPU 1,8 V                | -                             | -                 | Maintien de l'état d'alimentation RTSS          |
|         83 | UART_DBG_TX               | 1,8 V MPU                | -                             | GPIO_71           | Émission UART de débogage MPU                   |
|         84 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         85 | UART_DBG_RX               | 1,8 V MPU                | -                             | GPIO_72           | Réception UART de débogage MPU                  |
|         86 | CAN1_TX                   | 3,3 V MCU                | PD5                           | -                 | Émission bus CAN-FD 1 (sans PHY)                |
|         87 | PWR_DISABLE_7-24V         | Système                  | -                             | -                 | Désactive le circuit d'alimentation VIN         |
|         88 | CAN1_RX                   | 3,3 V MCU                | PI9                           | -                 | Réception du bus CAN-FD 1 (sans PHY)            |
|         89 | FORCE_BOOT_3V3            | 3,3 V                    | -                             | -                 | Forçage du démarrage                            |
|         90 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         91 | +3V3 OUT                  | Alimentation             | -                             | -                 | Sortie d'alimentation 3,3 V                     |
|         92 | CAN2_TX                   | MCU 3,3 V                | PA10                          | -                 | Bus CAN-FD 2 TX (sans PHY)                      |
|         93 | +3V3 OUT                  | Alimentation             | -                             | -                 | Sortie d'alimentation 3,3 V                     |
|         94 | CAN2_RX                   | 3,3 V MCU                | PD9                           | -                 | Réception du bus CAN-FD 2 (sans PHY)            |
|         95 | +3V3 OUT                  | Alimentation             | -                             | -                 | Sortie d'alimentation 3,3 V                     |
|         96 | GND                       | Alimentation             | -                             | -                 | Masse                                           |
|         97 | +5V OUT                   | Alimentation             | -                             | -                 | Sortie d'alimentation 5 V                       |
|         98 | CAN3_TX                   | 3,3 V MCU                | PF6                           | -                 | Bus CAN-FD 3 TX (sans PHY)                      |
|         99 | +5V OUT                   | Alimentation             | -                             | -                 | Sortie d'alimentation 5 V                       |
|        100 | CAN3_RX                   | 3,3 V MCU                | PF7                           | -                 | Bus CAN-FD 3 RX (sans PHY)                      |

>📝 **Remarque :** Les signaux JTAG et SPI ICS relèvent du domaine MPU à 1,8 V. Veuillez ne pas appliquer directement une logique à 3,3 V. Les bus CAN FD sur JOMEGA ne disposent pas de couche physique PHY ; un émetteur-récepteur CAN externe est nécessaire. Les broches VIN sont réservées à l'entrée d'alimentation.

### Connecteurs de caméra MIPI CSI (J3_1, J3_2, J3_3)

Le VENTUNO Q dispose de trois connecteurs de caméra MIPI CSI indépendants (J3_1, J3_2, J3_3), chacun étant un connecteur FPC à 22 broches (TF31-22S-0.5SH, pas de 0,5 mm). Chacun prend en charge les caméras MIPI CSI-2 à 4 voies. Les signaux de commande (I2C, GPIO) fonctionnent à **3,3 V**, tant pour le GPIO d’activation sur la broche 17 que pour les bus I2C sur les broches 20 et 21. Les signaux I2C sont convertis en interne à un niveau de 1,8 V avant d’atteindre le bus `CCI_I2C` du SoM. Les paires différentielles MIPI sont de type D-PHY et ne doivent pas être utilisées comme GPIO.

#### J3_1 - Caméra 2

| **Broche** | **Désignation** | **Domaine**  | **Broche MPU** | **Remarques**                                                |
| ---------: | --------------- | ------------ | -------------- | ------------------------------------------------------------ |
|          1 | GND             | Alimentation | -              | Masse                                                        |
|          2 | LN0_M           | MIPI D-PHY   | -              | Voie de données CSI2 0 −                                     |
|          3 | LN0_P           | MIPI D-PHY   | -              | Voie de données CSI2 0 +                                     |
|          4 | GND             | Alimentation | -              | Masse                                                        |
|          5 | LN1_M           | MIPI D-PHY   | -              | Voie de données CSI2 1 −                                     |
|          6 | LN1_P           | MIPI D-PHY   | -              | Voie de données CSI2 1 +                                     |
|          7 | GND             | Alimentation | -              | Masse                                                        |
|          8 | CLK_M           | MIPI D-PHY   | -              | Voie d’horloge CSI2 −                                        |
|          9 | CLK_P           | MIPI D-PHY   | -              | Ligne d’horloge CSI2 +                                       |
|         10 | GND             | Alimentation | -              | Masse                                                        |
|         11 | LN2_M           | MIPI D-PHY   | -              | Ligne de données CSI2 2 −                                    |
|         12 | LN2_P           | MIPI D-PHY   | -              | Voie de données CSI2 n° 2 +                                  |
|         13 | GND             | Alimentation | -              | Masse                                                        |
|         14 | LN3_M           | MIPI D-PHY   | -              | Voie de données CSI2 n° 3 −                                  |
|         15 | LN3_P           | MIPI D-PHY   | -              | Voie de données CSI2 3 +                                     |
|         16 | GND             | Alimentation | -              | Masse                                                        |
|         17 | GPIO_PIN17_3V3  | 3,3 V        | GPIO_82        | GPIO de la caméra                                            |
|         18 | NON CONNECTÉ    | -            | -              | -                                                            |
|         19 | GND             | Alimentation | -              | Masse                                                        |
|         20 | SCL             | 3,3 V        | GPIO_62        | Horloge I2C de la caméra (CCI_I2C4, niveau converti à 1,8 V) |
|         21 | SDA             | 3,3 V        | GPIO_61        | Données I2C de la caméra (CCI_I2C4, niveau converti à 1,8 V) |
|         22 | +3V3            | Alimentation | -              | Alimentation 3,3 V pour le module caméra                     |

#### J3_2 - Caméra 0

| **Broche** | **Désignation** | **Domaine**  | **Broche MPU** | **Remarques**                                                |
| ---------: | --------------- | ------------ | -------------- | ------------------------------------------------------------ |
|          1 | GND             | Alimentation | -              | Masse                                                        |
|          2 | LN0_M           | MIPI D-PHY   | -              | Voie de données CSI0 0 −                                     |
|          3 | LN0_P           | MIPI D-PHY   | -              | Voie de données CSI0 0 +                                     |
|          4 | GND             | Alimentation | -              | Masse                                                        |
|          5 | LN1_M           | MIPI D-PHY   | -              | Voie de données CSI0 1 −                                     |
|          6 | LN1_P           | MIPI D-PHY   | -              | Voie de données CSI0 1 +                                     |
|          7 | GND             | Alimentation | -              | Masse                                                        |
|          8 | CLK_M           | MIPI D-PHY   | -              | Voie d'horloge CSI0 −                                        |
|          9 | CLK_P           | MIPI D-PHY   | -              | Ligne d’horloge CSI0 +                                       |
|         10 | GND             | Alimentation | -              | Masse                                                        |
|         11 | LN2_M           | MIPI D-PHY   | -              | Ligne de données CSI0 2 −                                    |
|         12 | LN2_P           | MIPI D-PHY   | -              | Voie de données CSI0 2 +                                     |
|         13 | GND             | Alimentation | -              | Masse                                                        |
|         14 | LN3_M           | MIPI D-PHY   | -              | Voie de données CSI0 3 −                                     |
|         15 | LN3_P           | MIPI D-PHY   | -              | Voie de données CSI0 3 +                                     |
|         16 | GND             | Alimentation | -              | Masse                                                        |
|         17 | GPIO_PIN17_3V3  | 3,3 V        | GPIO_64        | GPIO de la caméra                                            |
|         18 | NON CONNECTÉ    | -            | -              | -                                                            |
|         19 | GND             | Alimentation | -              | Masse                                                        |
|         20 | SCL             | 3,3 V        | GPIO_58        | Horloge I2C de la caméra (CCI_I2C0, niveau converti à 1,8 V) |
|         21 | SDA             | 3,3 V        | GPIO_57        | Données I2C de la caméra (CCI_I2C0, niveau converti à 1,8 V) |
|         22 | +3V3            | Alimentation | -              | Alimentation 3,3 V pour le module caméra                     |

#### J3_3 - Caméra 1

| **Broche** | **Désignation** | **Domaine**  | **Broche MPU** | **Remarques**                                                     |
| ---------: | --------------- | ------------ | -------------- | ----------------------------------------------------------------- |
|          1 | GND             | Alimentation | -              | Masse                                                             |
|          2 | LN0_M           | MIPI D-PHY   | -              | Voie de données CSI1 0 −                                          |
|          3 | LN0_P           | MIPI D-PHY   | -              | Voie de données CSI1 0 +                                          |
|          4 | GND             | Alimentation | -              | Masse                                                             |
|          5 | LN1_M           | MIPI D-PHY   | -              | Voie de données CSI1 1 −                                          |
|          6 | LN1_P           | MIPI D-PHY   | -              | Voie de données CSI1 1 +                                          |
|          7 | GND             | Alimentation | -              | Masse                                                             |
|          8 | CLK_M           | MIPI D-PHY   | -              | Voie d’horloge CSI1 −                                             |
|          9 | CLK_P           | MIPI D-PHY   | -              | Ligne d’horloge CSI1 +                                            |
|         10 | GND             | Alimentation | -              | Masse                                                             |
|         11 | LN2_M           | MIPI D-PHY   | -              | Ligne de données CSI1 2 −                                         |
|         12 | LN2_P           | MIPI D-PHY   | -              | Voie de données CSI1 n° 2 +                                       |
|         13 | GND             | Alimentation | -              | Masse                                                             |
|         14 | LN3_M           | MIPI D-PHY   | -              | Voie de données CSI1 n° 3 −                                       |
|         15 | LN3_P           | MIPI D-PHY   | -              | Voie de données CSI1 3 +                                          |
|         16 | GND             | Alimentation | -              | Masse                                                             |
|         17 | GPIO_PIN17_3V3  | 3,3 V        | GPIO_75        | GPIO de la caméra                                                 |
|         18 | NON CONNECTÉ    | -            | -              | -                                                                 |
|         19 | GND             | Alimentation | -              | Masse                                                             |
|         20 | SCL             | 3,3 V        | GPIO_60        | Horloge I2C de la caméra (CCI_I2C2, niveau converti à 1,8 V)      |
|         21 | SDA             | 3,3 V        | GPIO_59        | Données I2C de la caméra (CCI_I2C2, conversion de niveau à 1,8 V) |
|         22 | +3V3            | Alimentation | -              | Alimentation 3,3 V pour le module caméra                          |

>📝 **Remarque :** les voies différentielles MIPI D-PHY ne sont pas des E/S à usage général.

## Périphériques haut débit

### Réseau

Wi-Fi® 6 tri-bande (2,4/5/6 GHz) et Bluetooth® 5.3 via le module intégré NFA725B. Connectivité filaire via Ethernet RJ45 à 2,5 Gbit/s (PHY QCA-8081).

### Stockage

Stockage NVMe Gen 4 extensible via un connecteur M.2 2230 Key M (MDT580M01001), connecté directement au SOM QCS8275 via une interface PCIe Gen 4 à 4 voies. Conformément aux spécifications du QCS8275, l'emplacement M.2 n'est pas amorçable. L'alimentation de l'emplacement est activée de manière indépendante via un commutateur de charge MP5077GG-Z contrôlé par l'unité centrale (MPU).

Le commutateur de paquets PCIe Gen 2 PI7C9X2G304EV présent sur la carte est dédié au contrôleur hôte USB 3.0 xHCI (TUSB7340RKMR) et au module Wi-Fi® (NFA725B).

> 📝 **Remarque :** L’MPU gère l’alimentation de l’emplacement M.2. Si l’MPU n’a pas terminé le démarrage ou si la gestion de l’alimentation n’a pas été activée, un disque NVMe installé ne sera pas alimenté et ne sera pas détecté. Il s’agit d’un comportement normal au début du démarrage.

### USB-C

Le connecteur USB-C prend en charge la commutation des rôles hôte/périphérique, la commutation des rôles d’alimentation, la sortie DisplayPort en mode alternatif (Alt-Mode) et la négociation USB Power Delivery jusqu’à 20 V via le contrôleur PD CYPD6129-52LQXI. Les paires différentielles SuperSpeed du connecteur USB-C sont partagées entre les données USB 3.0 SuperSpeed et le mode alternatif DisplayPort via le multiplexeur USB eDP intégré (TMUXHS4446RETT).

**Lorsque le mode alternatif DisplayPort est actif**, les voies SuperSpeed sont réaffectées au DisplayPort. Les données USB sont alors limitées aux débits USB 2.0 (HighSpeed, 480 Mbps) sur la paire HS_D+/D− uniquement. Le débit USB 3.0 SuperSpeed complet n’est disponible que lorsque le mode alternatif DisplayPort n’est pas actif.

Le CYPD6129 surveille à la fois le VBUS et le VIN pour déterminer l’état d’alimentation de la carte et négocie les profils PD en conséquence. La LED de défaut (rouge, GPIO9/P4.1 sur le CYPD6129) signale les conditions de défaut. Les principaux scénarios d’alimentation sont résumés ci-dessous :

| **Scénario**                                                                         | **Résultat attendu**                                                                    |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| VIN connecté, USB non connecté                                                       | Système alimenté par VIN, contrôleur PD en mode batterie                                |
| VIN connecté, USB connecté                                                           | Système alimenté par VIN, négociation PD et rôle de données autorisés                   |
| VIN non connecté, USB-C vers USB-C                                                   | Système alimenté par VBUS, la négociation PD démarre, cible 20 V à 3 A                  |
| VIN non connecté, USB-C vers USB-A                                                   | Le PD détecte une source non-PD, le système est hors tension, la LED de défaut clignote |
| VIN non connecté, USB-C vers USB-A -> VIN connecté à la volée                        | Le PD reconnaît le VIN, débloque le VIN, maintient le VBUS bloqué                       |
| VIN non connecté, USB-C vers USB-C (alimentation négociée) → VIN connecté à la volée | Système alimenté par VBUS, VIN désactivé, la LED de défaut affiche un motif différent   |

>📝 **Remarque :** Le CYPD6129 est programmé pour exiger un profil de tension PD supérieur à 5 V avant d’activer le circuit d’alimentation principal. Une connexion via un câble USB-C vers USB-A standard, ou via un port USB-C ne fournissant que 5 V sans négociation PD, n’alimentera pas la carte et provoquera le clignotement de la LED d’erreur. Utilisez toujours une alimentation USB-C compatible PD prenant en charge 9 V, 15 V ou 20 V pour garantir un fonctionnement fiable alimenté par USB-C.
>
> Le CYPD6129 reste en permanence alimenté via un convertisseur abaisseur dédié (LMR51440SDRRR, U26) alimenté par n’importe quelle source d’alimentation connectée, ce qui lui permet de surveiller et de négocier l’alimentation de manière indépendante avant d’activer le circuit d’alimentation principal de la carte.

### USB Type-A

Les deux ports USB 3.0 de type A sont protégés indépendamment par des commutateurs de charge dédiés (MP5077GG-Z). Le courant VBUS de chaque port est limité de manière fixe à 1,71 A par le réseau de résistances ILIM. L’activation de l’alimentation de chaque port est gérée par le TUSB7340RKMR.

| **Paramètre**            | **Valeur**                         |
| ------------------------ | ---------------------------------- |
| Tension VBUS             | 5 V                                |
| Courant maximal par port | 1,71 A (défini par ILIM, par port) |
| Protection               | Commutateur de charge MP5077GG-Z   |
| Contrôle de l’activation | TUSB7340RKMR                       |

>📝 **Remarque :** La limite de courant de 1,71 A par port est définie au niveau matériel et ne peut pas être contournée par logiciel. Ne tentez pas de contourner le commutateur de charge.

### Affichage

La carte offre les sorties d'affichage suivantes :

- **HDMI** via le connecteur HDMI dédié, piloté par le pont DSI-vers-HDMI ADV7535 intégré. L’ADV7535 utilise les lignes MIPI DSI provenant du SoM. Lorsque l’HDMI est actif, les lignes MIPI-DSI du connecteur JMEDIA ne sont pas disponibles.
- **Mode alternatif DisplayPort** via le connecteur USB-C, grâce au multiplexeur USB eDP intégré (TMUXHS4446RETT).
- **MIPI DSI sur JMEDIA** disponible lorsque la sortie HDMI n’est pas active (nécessite une configuration de superposition DSI).

### Caméra

VENTUNO Q prend en charge l’entrée caméra via trois connecteurs MIPI CSI intégrés (J3_1, J3_2, J3_3) et via le connecteur JMEDIA.

**VENTUNO Q en mode autonome (par défaut) :**

Les trois connecteurs CSI intégrés (J3_1, J3_2, J3_3) sont disponibles simultanément pour l’entrée caméra. Il s’agit d’une configuration réservée à la caméra et le MIPI DSI n’est pas actif par défaut. La sortie d’affichage est disponible via le connecteur HDMI ou le mode alternatif DisplayPort sur USB-C.

>📝 **Remarque :** Le [module de caméra Arducam IMX577 Mini](https://www.arducam.com/arducam-imx577-mini-camera-module-for-qualcomm-rb3g2.html) (réf. B0488) est compatible avec le VENTUNO Q via ses connecteurs MIPI CSI intégrés. Veuillez vous reporter au [manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) pour obtenir les instructions de test et de configuration.

**VENTUNO Q avec un carrier compatible :**

Un carrier connectée à JMEDIA permet d’utiliser un écran MIPI DSI en plus des caméras intégrées. Si la superposition DSI de la carte est activée, la caméra 0 (J3_2) n’est pas disponible, car elle partage le bus CCI_I2C0 (GPIO_57/58) avec le connecteur JMEDIA. Les caméras 1 (J3_3) et 2 (J3_1) restent disponibles.

>📝 **Remarque :** la disponibilité des caméras lorsqu’une carte est connectée dépend de la configuration spécifique de cette dernière. Veuillez vous reporter à la documentation propre à la carte pour plus de détails.

<div style="page-break-after: always;"></div>

## Fonctionnement de l'appareil

### Pour commencer - Arduino App Lab

Arduino App Lab [1] est un éditeur unifié qui permet de créer et d’exécuter des projets sur les deux processeurs du VENTUNO Q. Il combine la programmation embarquée (sketch), le développement Linux et l’IA en périphérie au sein d’un environnement unique.

Un projet est une **application** pouvant inclure :

- Un programme Python® s’exécutant sur le système Linux (Qualcomm Dragonwing™ IQ8)
- Un sketch Arduino s’exécutant sur le microcontrôleur (STM32H5F5)
- Des **Bricks** facultatifs (services pré-packagés tels que des modèles d’IA, des serveurs web ou des clients API) qui sont déployés avec l’application et s’exécutent sur le système Linux.

Les applications utilisent **Bridge** pour échanger des données entre le côté Linux et le microcontrôleur.

**Trois configurations. Une seule expérience.**

![](assets/ABX00181_modes.png)

- **Mode carte :** Arduino App Lab s'exécute directement sur VENTUNO Q. Branchez un écran via HDMI (ou USB-C), un clavier et une souris pour bénéficier d'un environnement de développement tout-en-un. Aucun PC n'est nécessaire.
- **Mode hébergé sur PC :** Connectez VENTUNO Q à votre ordinateur via USB-C ou le réseau et exécutez Arduino App Lab sur votre PC.
- **Mode réseau :** VENTUNO Q fonctionne en mode « headless », sans écran, clavier ni souris. Accédez à la carte à distance via Wi-Fi® ou Ethernet.

>📝 **Remarque :** en mode **hébergé sur PC**, une connexion USB est requise pour la configuration initiale. Par la suite, vous pouvez utiliser la cible **Réseau** via le réseau local (SSH).

En mode **« Single-Board Computer »**, aucune liaison de données USB n’est nécessaire : alimentez la carte et utilisez la cible **« Réseau »** dès qu’elle se connecte à votre réseau. Les périphériques USB (clavier, souris, caméra USB, microphone) peuvent être connectés directement aux ports USB-A intégrés. Lorsque le mode alternatif DisplayPort est actif sur le port USB-C, le débit de données USB est réduit.

Pour obtenir les instructions complètes de mise en place, la configuration initiale et les conseils de première utilisation, veuillez vous reporter au [Manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Remarque :** si vous alimentez la carte via USB-C pour la première fois, la LED « Fault » peut clignoter lorsqu’elle est connectée à un ordinateur ou à un port USB-C non compatible PD. La carte nécessite une alimentation compatible PD d’au moins 9 V pour démarrer. Pour un fonctionnement à pleine performance, y compris l’inférence IA, les périphériques connectés et les HAT raccordés, une alimentation de 12 V ou plus est recommandée via USB-C PD (jusqu’à 20 V) ou via la prise cylindrique ou les bornes à vis (7-24 V). Reportez-vous à la section [Alimentation d’entrée](#alimentation-dentrée) pour connaître les limites de tension et de courant par source.

>📝 **Remarque :** le premier démarrage prend entre 20 et 30 secondes, le temps que Linux s'initialise. La matrice LED affiche une animation de démarrage lorsque le bootloader du microcontrôleur est chargé et qu'un sketch valide est en cours d'exécution. Attendez que celle-ci se termine avant d’interagir avec la carte. Si l’animation n’apparaît pas, veuillez vous reporter au [Manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/) pour plus de détails.

### Bricks

Les « Bricks » sont des modules prêts à l'emploi disponibles dans Arduino App Lab, comprenant des modèles d'IA, des services Web, des intégrations de capteurs, des bases de données et des interfaces utilisateur, qui se déploient parallèlement à votre application sur le système Linux sans que vous ayez à développer l'infrastructure sous-jacente. Pour un guide complet sur la sélection et l’utilisation des « Bricks », veuillez vous reporter au [Manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

>📝 **Remarque :** lorsqu’une application est associée et en cours d’exécution, les interfaces USB peuvent être occupées par le système. Pour utiliser des outils CLI externes via USB, arrêtez l’application ou déconnectez la carte.

### Boutons et modes de démarrage

La VENTUNO Q intègre deux boutons : un **bouton-poussoir vertical** et un **bouton utilisateur**.

![](assets/ABX00181_vertical_button.png)

### Bouton-poussoir vertical

Le bouton-poussoir vertical est connecté au GPIO PK13 du microcontrôleur. Il permet d’interagir avec la carte et de l’éteindre.

- **Appui simple (mode « Single-Board Computer ») :** affiche une boîte de dialogue d’arrêt à l’écran. L’utilisateur peut confirmer pour éteindre immédiatement la carte, ou annuler pour fermer la boîte de dialogue et poursuivre le fonctionnement normal. En l’absence de réaction, la carte s’éteint automatiquement au bout de 60 secondes.
- **Appui long (plus de 10 secondes, mode SSH / ADB) :** arrête complètement le système. La carte restera éteinte jusqu’à ce que l’alimentation soit déconnectée puis reconnectée.

>📝 **Remarque :** Un arrêt par pression longue arrête complètement l’environnement Linux et interrompt toutes les applications en cours d’exécution. Enregistrez votre travail et assurez-vous que les processus externes sont arrêtés en toute sécurité, le cas échéant. La carte démarre automatiquement dès qu’elle est alimentée ; il n’est pas nécessaire d’appuyer sur le bouton-poussoir pour un démarrage normal.

### Bouton utilisateur

![](assets/ABX00181_user_button.png)

Le bouton utilisateur est connecté à l’unité centrale (MPU) (GPIO_79) et est disponible en tant qu’entrée à usage général. Il peut être lu par des applications et des scripts Linux à l’aide d’interfaces GPIO standard. Pour des exemples d’utilisation, veuillez vous reporter au [Manuel d’utilisation du VENTUNO Q](https://docs.arduino.cc/tutorials/ventuno-q/user-manual/).

<div style="page-break-after: always;"></div>

## Informations mécaniques

La carte mesure 160 mm × 100 mm. La hauteur totale, sans le dissipateur thermique ni le ventilateur du SoM, est de 25,8 mm. Le connecteur JHAT à 40 broches est conforme aux spécifications mécaniques standard du Raspberry Pi® HAT, ce qui garantit la compatibilité physique avec les accessoires HAT compatibles.

![](assets/ABX00181_general_dimensions.svg)

Les connecteurs UNO Shield conservent l'espacement standard de l'Arduino UNO, ce qui garantit une compatibilité mécanique et électrique directe avec l'écosystème UNO Shield.

La carte comporte trois séries de trous ayant des fonctions mécaniques différentes :

- **4 entretoises M2,5** (hauteur de 5 mm, soudées à la carte) pour la fixation du dissipateur thermique, situées à 9,78 mm du bord droit et à 10,02 mm et 42,63 mm du bord supérieur.
- **4 trous de fixation d’angle de 3,2 mm** pour l’installation dans des boîtiers, sur des panneaux ou sur des cartes et accessoires personnalisés.
- **2 × 3,2 mm** trous de fixation HAT conformes à la spécification mécanique standard Raspberry Pi® HAT, compatibles avec des entretoises M3 pour la fixation d’accessoires HAT.
- **1 × entretoise M2** (hauteur de 4 mm) pour fixer une carte de stockage M.2 2230 NVMe dans l’emplacement M.2.

Le VENTUNO Q est livré avec 4 entretoises hexagonales M3 et 4 écrous M3, placés dans un sachet séparé. Dans les environnements sensibles aux décharges électrostatiques (ESD), fixez une entretoise et un écrou à chacun des quatre trous de fixation situés aux coins afin de surélever la carte par rapport à la surface de travail et d’augmenter le dégagement.

| **Article**              | **Dimensions**                                                                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| Entretoise hexagonale M3 | Longueur de la partie hexagonale : 20 mm, longueur du filetage : 6 mm, diamètre du filetage : 3 mm |
| Écrou M3                 | Hauteur : 2,4 mm, diamètre hexagonal entre les faces : 5,6 mm, diamètre intérieur : 3 mm           |

![](assets/ABX00181_esd_standoff.png)

### Dissipateur thermique et conception thermique du SoM

Le SoM Qualcomm® Dragonwing™ IQ8 (QCS8275) nécessite un refroidissement actif pour fonctionner de manière continue à pleine performance. L'empreinte du SoM sur la carte mesure **57,5 mm × 57,5 mm**, centrée à **14,26 mm** du bord gauche et à **14,73 mm** du bord inférieur, avec un décalage horizontal de **8,95 mm** et un décalage vertical de **8,55 mm** par rapport à la zone active du SoM.

![](assets/ABX00181_active_fan.png)

Les quatre entretoises M2,5 définissent le gabarit de montage de l’ensemble dissipateur thermique et ventilateur fourni, positionné symétriquement autour de l’empreinte du SoM afin d’assurer une force de serrage uniforme sur l’ensemble du couvercle du SoM.

Dans les conditions les plus défavorables, lorsque le MPU, le NPU et le GPU fonctionnent simultanément à pleine puissance, la carte peut consommer environ 25 W, voire plus. La solution de refroidissement actif fournie est optimisée pour cette charge thermique. Veillez à ce que le ventilateur reste opérationnel pendant les charges de travail soutenues à haute performance.

![](assets/ABX00181_som_heatsink.svg)

>📝 **Remarque :** L’utilisation de la carte dans le cadre de charges de travail intensives en IA ou en calcul sans refroidissement adéquat peut déclencher un ralentissement thermique du SoM QCS8275, ce qui réduit les performances. Vérifiez toujours la marge thermique disponible pour votre cas d’utilisation cible et l’environnement de votre boîtier.

<div style="page-break-after: always;"></div>

# Safety Information

Maintain a minimum separation distance of 20 cm between the device and the user during operation. The 5 GHz frequency band may be subject to operational restrictions depending on the country of use.

**Bulgarian (BG):**

Поддържайте минимално разстояние от 20 см между устройството и потребителя по време на работа.
Честотната лента 5 GHz може да бъде обект на ограничения за използване в зависимост от държавата.

**Croatian (HR):**

Održavajte minimalnu udaljenost od 20 cm između uređaja i korisnika tijekom rada.
Frekvencijski pojas od 5 GHz može podlijegati ograničenjima ovisno o zemlji uporabe.

**Czech (CS):**

Udržujte minimální vzdálenost 20 cm mezi zařízením a uživatelem během provozu.
Pásmo 5 GHz může podléhat provozním omezením v závislosti na zemi použití.

**Danish (DA):**

Oprethold en minimumsafstand på 20 cm mellem enheden og brugeren under drift.
5 GHz-båndet kan være underlagt driftsmæssige begrænsninger afhængigt af brugslandet.

**Dutch (NL):**

Houd tijdens gebruik een minimale afstand van 20 cm tussen het apparaat en de gebruiker aan.
De 5GHz-band kan onderhevig zijn aan gebruiksbeperkingen afhankelijk van het land van gebruik.

**Estonian (ET):**

Hoidke seadme ja kasutaja vahel töötamise ajal vähemalt 20 cm kaugust.
5 GHz sagedusribale võivad kehtida kasutuspiirangud sõltuvalt kasutusriigist.

**Finnish (FI):**

Pidä laitteen ja käyttäjän välillä vähintään 20 cm etäisyys käytön aikana.
5 GHz taajuuskaistaan voi kohdistua käyttörajoituksia käyttömaasta riippuen.

**French (FR):**

Maintenez une distance minimale de 20 cm entre l’appareil et l’utilisateur pendant son fonctionnement.
La bande de fréquences 5 GHz peut être soumise à des restrictions d’utilisation selon le pays.

**German (DE):**

Halten Sie während des Betriebs einen Mindestabstand von 20 cm zwischen dem Gerät und dem Benutzer ein.
Das 5‑GHz‑Frequenzband kann je nach Einsatzland Nutzungsbeschränkungen unterliegen.

**Greek (EL):**

Διατηρείτε ελάχιστη απόσταση 20 cm μεταξύ της συσκευής και του χρήστη κατά τη λειτουργία.
Η ζώνη συχνοτήτων 5 GHz ενδέχεται να υπόκειται σε περιορισμούς ανάλογα με τη χώρα χρήσης.

**Hungarian (HU):**

A működés során tartson legalább 20 cm távolságot az eszköz és a felhasználó között.
Az 5 GHz-es frekvenciasáv használata országtól függően korlátozott lehet.

**Irish (GA):**

Coinnigh ar a laghad fad 20 cm idir an gléas agus an t‑úsáideoir le linn úsáide.
D’fhéadfadh srianta oibriúcháin a bheith ar an mbanda minicíochta 5 GHz ag brath ar an tír.

**Italian (IT):**

Mantenere una distanza minima di 20 cm tra il dispositivo e l’utente durante il funzionamento.
La banda di frequenza a 5 GHz può essere soggetta a restrizioni operative a seconda del paese.

**Latvian (LV):**

Uzturiet vismaz 20 cm attālumu starp ierīci un lietotāju darbības laikā.
5 GHz frekvenču joslai var būt izmantošanas ierobežojumi atkarībā no valsts.

**Lithuanian (LT):**

Naudojimo metu laikykite bent 20 cm atstumą tarp įrenginio ir naudotojo.
5 GHz dažnių juostai gali būti taikomi naudojimo apribojimai priklausomai nuo šalies.

**Maltese (MT):**

Żomm distanza minima ta’ 20 cm bejn l-apparat u l-utent waqt l-użu.
Il-medda tal-frekwenza 5 GHz tista’ tkun soġġetta għal restrizzjonijiet skont il-pajjiż.

**Polish (PL):**

Podczas pracy zachowaj minimalną odległość 20 cm między urządzeniem a użytkownikiem.
Pasmo częstotliwości 5 GHz może podlegać ograniczeniom w zależności od kraju użytkowania.

**Portuguese (PT):**

Mantenha uma distância mínima de 20 cm entre o dispositivo e o utilizador durante o funcionamento.
A banda de frequência de 5 GHz pode estar sujeita a restrições de utilização dependendo do país.

**Romanian (RO):**

Mențineți o distanță minimă de 20 cm între dispozitiv și utilizator în timpul funcționării.
Banda de frecvență de 5 GHz poate face obiectul unor restricții în funcție de țara de utilizare.

**Slovak (SK):**

Počas prevádzky dodržiavajte minimálnu vzdialenosť 20 cm medzi zariadením a používateľom.
Pásmo 5 GHz môže podliehať prevádzkovým obmedzeniam v závislosti od krajiny použitia.

**Slovenian (SL):**

Med delovanjem ohranjajte najmanj 20 cm razdalje med napravo in uporabnikom.
Pas frekvenc 5 GHz je lahko omejen glede na državo uporabe.

**Spanish (ES):**

Mantenga una distancia mínima de 20 cm entre el dispositivo y el usuario durante su funcionamiento.
La banda de frecuencia de 5 GHz puede estar sujeta a restricciones según el país de uso.

**Swedish (SV):**

Håll ett minsta avstånd på 20 cm mellan enheten och användaren under drift.
5 GHz-bandet kan vara föremål för driftbegränsningar beroende på användningsland.

## ESD Warning

This product is a development board that contains ESD-sensitive components. Appropriate anti-static precautions should be taken when handling the device. Avoid touching exposed connectors, pins, or circuitry. Where a heatsink is installed, handle the board by the heatsink to minimise the risk of electrostatic discharge damage. Improper handling or exposure to electrostatic discharge may result in permanent damage to the product.

## Antenna Use and Compliance

- This product is approved to operate with the built-in (internal) antenna only
- The internal antenna is part of the certified module configuration and must be used for normal operation
- RF connectors may be present for development or testing purposes only
- Use of an external antenna is not part of the approved configuration
- External antenna use requires additional regulatory assessment before use

### Warning - External Antenna Use

- Connecting an external antenna may result in non-compliance with regulatory requirements
- This includes the module approval associated with FCC ID J9C-QCNFA725
- Use of an external antenna may change RF output power
- Use of an external antenna may change frequency behavior
- Use of an external antenna may change radiation characteristics
- These changes may cause the product to exceed allowed regulatory limits
- Use of an external antenna may invalidate device approval
- Use of an external antenna may void the authorization to operate the device
- Unauthorized changes, including antenna modifications, may void regulatory approvals

### Requirements for Integrators

- End products must use the internal antenna to maintain regulatory compliance
- If an external antenna is used, the integrator must perform a full regulatory assessment
- If an external antenna is used, the integrator must obtain required certifications for the final product
- Any antenna used must meet the approved gain, radiation pattern, and performance characteristics
- Approved antenna characteristics are defined in the applicable regulatory documentation, including the Qualcomm module label guide

### Operation in the 6 GHz Band

- Operation in the 6 GHz band is only permitted with the approved internal antenna configuration
- If an external antenna is used, 6 GHz operation must be disabled
- If an external antenna is used, the product must not transmit in the 6 GHz band
- Operation outside the approved configuration may violate regional regulations

### Responsibility

- The manufacturer or integrator is responsible for ensuring the final product complies with all applicable regulatory requirements
- Changes to the antenna system or RF design may require additional testing and certification

# Certifications

## RED / UK

| CE                     | Europe - EU Declaration of Conformity                                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Česky [Czech]          | Arduino S.r.l tímto prohlašuje, že tento Radiolan je ve shodě se základními požadavky a dalšími příslušnými ustanoveními směrnice 2014/53/EU.                                                    |
| Dansk [Danish]         | Undertegnede Arduino S.r.l erklærer herved, at følgende udstyr Radiolan overholder de væsentlige krav og øvrige relevante krav i direktiv 2014/53/EU.                                            |
| Deutsch [German]       | Hiermit erklärt Arduino S.r.l dass sich das Gerät Radiolan in Übereinstimmung mit den grundlegenden Anforderungen und den übrigen einschlägigen Bestimmungen der Richtlinie 2014/53/EU befindet. |
| Eesti [Estonian]       | Käesolevaga kinnitab Arduino S.r.l seadme Radiolan vastavust direktiivi 2014/53/EU põhinõuetele ja nimetatud direktiivist tulenevatele teistele asjakohastele sätetele.                          |
| English                | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of Directive 2014/53/EU.                                       |
| Español [Spanish]      | Por medio de la presente Arduino S.r.l declara que el Radiolan cumple con los requisitos esenciales y cualesquiera otras disposiciones aplicables o exigibles de la Directiva 2014/53/EU.        |
| Ελληνική [Greek]       | ΜΕ ΤΗΝ ΠΑΡΟΥΣΑ Arduino S.r.l ΔΗΛΩΝΕΙ ΟΤΙ Radiolan ΣΥΜΜΟΡΦΩΝΕΤΑΙ ΠΡΟΣ ΤΙΣ ΟΥΣΙΩΔΕΙΣ ΑΠΑΙΤΗΣΕΙΣ ΚΑΙ ΤΙΣ ΛΟΙΠΕΣ ΣΧΕΤΙΚΕΣ ΔΙΑΤΑΞΕΙΣ ΤΗΣ ΟΔΗΓΙΑΣ 2014/53/EU.                                          |
| Français [French]      | Par la présente Arduino S.r.l déclare que l'appareil Radiolan est conforme aux exigences essentielles et aux autres dispositions pertinentes de la directive 2014/53/EU.                         |
| Íslenska [Icelandic]   | Hér með lýsir Arduino S.r.l yfir því að Radiolan er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU.                                                            |
| Italiano [Italian]     | Con la presente Arduino S.r.l dichiara che questo Radiolan è conforme ai requisiti essenziali ed alle altre disposizioni pertinenti stabilite dalla direttiva 2014/53/EU.                        |
| Latviski [Latvian]     | Ar šo Arduino S.r.l deklarē, ka Radiolan atbilst Direktīvas 2014/53/EU būtiskajām prasībām un citiem ar to saistītajiem noteikumiem.                                                             |
| Lietuvių [Lithuanian]  | Šiuo Arduino S.r.l deklaruoja, kad šis Radiolan atitinka esminius reikalavimus ir kitas 2014/53/EU Direktyvos nuostatas.                                                                         |
| Malti [Maltese]        | Hawnhekk, Arduino S.r.l, jiddikjara li dan Radiolan jikkonforma mal-ħtiġijiet essenzjali u ma provvedimenti oħrajn relevanti li hemm fid-Dirrettiva 2014/53/EU.                                  |
| Magyar [Hungarian]     | Alulírott, Arduino S.r.l nyilatkozom, hogy a Radiolan megfelel a vonatkozó alapvetõ követelményeknek és az 2014/53/EU irányelv egyéb elõírásainak.                                               |
| Nederlands [Dutch]     | Hierbij verklaart Arduino S.r.l dat het toestel Radiolan in overeenstemming is met de essentiële eisen en de andere relevante bepalingen van richtlijn 2014/53/EU.                               |
| Norsk [Norwegian]      | Arduino S.r.l erklærer herved at utstyret Radiolan er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU.                                                        |
| Polski [Polish]        | Niniejszym Arduino S.r.l oświadcza, że Radiolan jest zgodny z zasadniczymi wymogami oraz pozostałymi stosownymi postanowieniami Dyrektywy 2014/53/EU.                                            |
| Português [Portuguese] | Arduino S.r.l declara que este Radiolan está conforme com os requisitos essenciais e outras disposições da Directiva 2014/53/EU.                                                                 |
| Slovensko [Slovenian]  | Arduino S.r.l izjavlja, da je ta Radiolan v skladu z bistvenimi zahtevami in ostalimi relevantnimi določili direktive 2014/53/EU.                                                                |
| Slovensky [Slovak]     | Arduino S.r.l týmto vyhlasuje, že Radiolan spĺňa základné požiadavky a všetky príslušné ustanovenia Smernice 2014/53/EU.                                                                         |
| Suomi [Finnish]        | Arduino S.r.l vakuuttaa täten että Radiolan tyyppinen laite on direktiivin 2014/53/EU oleellisten vaatimusten ja sitä koskevien direktiivin muiden ehtojen mukainen.                             |
| Svenska [Swedish]      | Härmed intygar Arduino S.r.l att denna Radiolan står I överensstämmelse med de väsentliga egenskapskrav och övriga relevanta bestämmelser som framgår av direktiv 2014/53/EU.                    |
| **UK**                 | **United Kingdom - UKCA Declaration of Conformity**                                                                                                                                              |
| United Kingdom         | Hereby, Arduino S.r.l, declares that this Radiolan is in compliance with the essential requirements and other relevant provisions of The Radio Equipment Regulations 2017.                       |

Requirements in:

Belgium (BE), Bulgaria (BG), Czech Republic (CZ), Denmark (DK), Germany (DE), Iceland (IS), Estonia (EE), Ireland (IE), Greece (EL), Spain (ES), France (FR), Croatia (HR), Italy (IT), Cyprus (CY), Latvia (LV), Liechtenstein (LI), Lithuania (LT), Luxembourg (LU), Hungary (HU), Malta (MT), Netherlands (NL), Norway (NO), Austria (AT), Poland (PL), Portugal (PT), Romania (RO), Slovenia (SI), Slovakia (SK), Turkey (TR), Finland (FI), Sweden (SE), Switzerland (CH), United Kingdom (North Irland) (UK(NI)), and United Kingdom (UK).

Operations in the 5.15-5.35GHz band are restricted to indoor usage only.

For Low power indoor (LPI use): Operations in the 5955 - 6415MHz are restricted to indoor usage only.

This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and your body.

### Radio Equipment Information (RED Compliance)

This radio equipment operates in the following frequency bands and with the maximum radio-frequency power indicated below:

| **Radio Technology**      | **Frequency Band** | **Maximum Transmit Power** |
| ------------------------- | ------------------ | -------------------------- |
| Bluetooth® EDR            | 2400 - 2483.5 MHz  | 18.31 dBm                  |
| Bluetooth® LE             | 2400 - 2483.5 MHz  | 9.97 dBm                   |
| Wi-Fi® 2.4 GHz            | 2400 - 2483.5 MHz  | 19.91 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5150 - 5350 MHz    | 22.92 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5470 - 5725 MHz    | 22.97 dBm EIRP             |
| Wi-Fi® 5 GHz              | 5725 - 5850 MHz    | 13.84 dBm EIRP             |
| Wi-Fi® 6 GHz (LPI client) | 5945 - 6425 MHz    | 22.83 dBm EIRP             |
| Wi-Fi® 6 GHz (VLP)        | 5945 - 6425 MHz    | 13.77 dBm EIRP             |

In accordance with EU regulations (RED Directive 2014/53/EU), the use of the 5 GHz band may be subject to national restrictions.

## UKCA Declaration of Conformity

Arduino S.r.l. hereby declares that this product is in compliance with the essential requirements and other relevant provisions of the applicable UK regulations. A copy of the UK Declaration of Conformity is available at: <https://docs.arduino.cc/certifications>

## FCC

Contains FCC ID: J9C-QCNFA725

**FCC Compliance Information**

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

This product does not contain any user serviceable components. Any unauthorized product changes or modifications will invalidate warranty and all applicable regulatory certifications and approvals, including authority to operate this device.

**FCC Part 15 Digital Emissions Compliance**

We Arduino S.r.l. - Via Andrea Appiani 25, 20900 Monza (Italy), declare under our sole responsibility that the product Arduino® VENTUNO Q complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

**WARNING:** This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates and radiates radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications.

However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from the one the receiver is connected to.
- Consult the dealer or an experienced radio/TV technician for help.

The user may find the following booklet prepared by the Federal Communications Commission helpful:

**The Interference Handbook**

This booklet is available from the U.S. Government Printing Office, Washington, D.C. 20402. Stock No.004-000-00345-4.

**Radiation Exposure Statement**

1. This transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.
2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

**FCC 6 GHz Statement**

a. The operation of this device is prohibited on oil platforms and aircraft, except that operation of this device in 5.925-6.425 GHz is permitted in large aircraft while flying above 10,000 feet.

b. Installation on outdoor fixed infrastructure is prohibited.

c. Controlling or communications with unmanned aircraft systems, including drones, is prohibited.

## ISED

Contains IC: 2723A-QCNFA725

*English:*

This device complies with Canadian RSS-247.
This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

*French:*

Ce dispositif est conforme à la norme CNR-247 d'Industrie Canada applicable aux appareils radio exempts de licence. Son fonctionnement est sujet aux deux conditions suivantes: (1) le dispositif ne doit pas produire de brouillage préjudiciable, et (2) ce dispositif doit accepter tout brouillage reçu, y compris un brouillage susceptible de provoquer un fonctionnement indésirable.

*English:*

Caution:

(i) the device for operation in the band 5150-5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems;

(iv) Users should also be advised that high-power radars are allocated as primary users (i.e. priority users) of the bands 5250-5350 MHz and 5650-5850 MHz and that these radars could cause interference and/or damage to LE-LAN devices.

*French:*

Avertissement :

Le guide d'utilisation des dispositifs pour réseaux locaux doit inclure des instructions précises sur les restrictions susmentionnées, notamment :

(i) les dispositifs fonctionnant dans la bande 5 150-5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux ;

(iv) Les radars à haute puissance sont désignés comme utilisateurs principaux (c'est-à-dire utilisateurs prioritaires) des bandes de fréquences 5250-5350 MHz et 5650-5850 MHz. Ces radars peuvent causer des interférences et/ou endommager les dispositifs LE-LAN.

<div style="background-color: rgba(0, 170, 228, 0.2); border-left: 6px solid rgba(0, 120, 180, 1); margin: 20px 0; padding: 15px;">
  <strong>Note:</strong> For 5GHz and/or when co-located with 5 GHz transmitters, the following statements should be provided in the user information.
</div>

**Radiation Exposure Statement**

1. To comply with the Canadian RF exposure compliance requirements, this device and its antenna must not be co-located or operating in conjunction with any other antenna or transmitter.
2. To comply with RSS 102 RF exposure compliance requirements, this equipment should be installed and operated, keeping the radiator at least 20cm or more away from the person's body.

**Déclaration d'exposition aux rayonnements**

1. Pour se conformer aux exigences de conformité RF canadienne l'exposition, cet appareil et son antenne ne doivent pas être co-localisés ou fonctionnant en conjonction avec une autre antenne ou transmetteur.
2. Pour se conformer aux exigences de conformité CNR 102 RF exposition, cet équipement doit être installé et utilisé en maintenant le radiateur à au moins 20cm ou plus du corps de la personne.

**6 GHz General statement**

*English:*

Devices shall not be used for control of or communications with unmanned aircraft systems. Devices shall not be used on oil platforms. Devices shall not be used on aircraft, except for the low-power indoor access points, indoor subordinate devices, low-power client devices, and very low-power devices operating in the 5925-6425 MHz band, that may be used on large aircraft as defined in the Canadian Aviation Regulations, while flying above 3,048 metres (10,000 feet).

*French :*

Les dispositifs ne doivent pas être utilisés pour commander des systèmes d'aéronef sans pilote ni pour communiquer avec de tels systèmes; Les dispositifs ne doivent pas être utilisés sur les plateformes de forage pétrolier; Les dispositifs ne doivent pas être utilisés dans les aéronefs, à l'exception des points d'accès intérieurs de faible puissance, des dispositifs subordonnés intérieurs, des dispositifs clients de faible puissance et des dispositifs de très faible puissance fonctionnant dans la bande de 5 925 à 6 425 MHz, qui peuvent être utilisés dans les gros aéronefs tel qu'il est défini dans le Règlement de l'aviation canadien, et ce, lorsqu'ils volent à une altitude supérieure à 3 048 mètres (10 000 pieds).

## Marques déposées

Les termes « HDMI », « HDMI High-Definition Multimedia Interface », l’habillage commercial HDMI et les logos HDMI sont des marques commerciales ou des marques déposées de HDMI Licensing Administrator, Inc.

# Informations sur la société

| Nom de la société | Arduino S.r.l.                              |
| ----------------- | ------------------------------------------- |
| Adresse           | Via Andrea Appiani 25, 20900 Monza (Italie) |

# Références de la documentation

| N°  | Référence                    | Lien                                                                                       |
| :-: | ---------------------------- | ------------------------------------------------------------------------------------------ |
|  1  | Arduino App Lab              | [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)                   |
|  2  | Documentation VENTUNO Q      | [https://docs.arduino.cc/hardware/ventuno-q/](https://docs.arduino.cc/hardware/ventuno-q/) |
|  3  | Arduino Project Hub          | [https://projecthub.arduino.cc/](https://projecthub.arduino.cc/)                           |
|  4  | Référence de la bibliothèque | [https://docs.arduino.cc/libraries/](https://docs.arduino.cc/libraries/)                   |
|  5  | Arduino Store                | [https://store.arduino.cc/](https://store.arduino.cc/)                                     |

# Historique des révisions du document

| **Date**   | **Révision** | **Modifications**    |
| :--------: | :----------: | -------------------- |
| 25/08/2026 |      1       | Première publication |
| 28/08/2026 |      2       | Updated Certifications |
