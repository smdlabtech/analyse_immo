
# Analyse de la capacité d'emprunt d'un data scientist gagnant 2700 € par mois (Taux d'intérêt de 6%)

## Données de base

- **Revenu mensuel net** : 2700 €
- **Taux d'endettement maximal** : 33% (généralement accepté par les banques)
- **Durée de remboursement** : 20 ans
- **Taux d'intérêt annuel** : 6%

## Calcul de la mensualité maximale

### Taux d'endettement

$$
\text{Mensualité maximale} = \text{Revenu mensuel net} \times \frac{33}{100}
$$

$$
\text{Mensualité maximale} = 2700 \times 0.33 = 891 \, \text{euros}
$$

## Calcul de la capacité d'emprunt

$$
M = \frac{C \times t \times (1 + t)^{n}}{(1 + t)^{n} - 1}
$$

### Taux mensuel et nombre de mensualités

$$
t = \frac{6\%}{12} = \frac{0,06}{12} \approx 0,005
$$

$$
n = 20 \times 12 = 240
$$

### Résolution pour \( C \)

$$
C = \frac{891 \times \left((1 + 0,005)^{240} - 1\right)}{0,005 \times (1 + 0,005)^{240}}
$$

### Résultats

En utilisant ces valeurs, nous trouvons que la capacité d'emprunt maximale est d'environ **121 657,05 euros**.

## Résumé

- **Mensualité maximale** : 891 euros
- **Capacité d'emprunt maximale** : 121 657,05 euros
