# Coût d'un crédit immobilier à 4% par an sur 20 ans

## Données du problème
- **Capital emprunté** : 100 000 euros
- **Taux annuel** : 4%
- **Durée** : 20 ans

## Formules utilisées

### Calcul de la mensualité
La formule de calcul des mensualités pour un prêt à taux fixe est la suivante :

$$
M = \frac{C \times t \times (1 + t)^n}{(1 + t)^n - 1}
$$

où :
- \( M \) est la mensualité,
- \( C \) est le capital emprunté,
- \( t \) est le taux d'intérêt mensuel (taux annuel divisé par 12),
- \( n \) est le nombre total de mensualités (nombre d'années multiplié par 12).

### Calcul du coût total du crédit
Pour trouver le coût total du crédit, nous devons multiplier la mensualité par le nombre total de mensualités et soustraire le capital emprunté initial :

$$
\text{Coût total du crédit} = M \times n
$$

$$
\text{Intérêts totaux} = \text{Coût total du crédit} - C
$$

## Calculs

### Taux mensuel et nombre de mensualités
$$
t = \frac{4\%}{12} = \frac{0,04}{12} \approx 0,003333
$$

$$
n = 20 \times 12 = 240
$$

### Mensualité
En appliquant la formule de la mensualité :

$$
M = \frac{100000 \times 0,003333 \times (1 + 0,003333)^{240}}{(1 + 0,003333)^{240} - 1} \approx 605,98 \, \text{euros}
$$

### Coût total du crédit
$$
\text{Coût total du crédit} = 605,98 \times 240 \approx 145435,28 \, \text{euros}
$$

### Intérêts totaux
$$
\text{Intérêts totaux} = 145435,28 - 100000 \approx 45435,28 \, \text{euros}
$$

## Résultats
- **Capital emprunté** : 100 000 euros
- **Taux annuel** : 4%
- **Durée** : 20 ans
- **Mensualité** : environ 605,98 euros
- **Coût total du crédit** : environ 145 435,28 euros
- **Intérêts totaux payés** : environ 45 435,28 euros
