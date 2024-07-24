
# Analyse de la capacité d'emprunt d'un data scientist gagnant 2700 € par mois (Crédit auto de 200 €)

## Données de base

- **Revenu mensuel net** : 2700 €
- **Taux d'endettement maximal** : 33%
- **Durée de remboursement** : 20 ans
- **Taux d'intérêt annuel** : 4%
- **Crédit auto mensuel** : 200 €

## Calcul de la mensualité maximale

### Taux d'endettement

$$
\text{Mensualité maximale} = \left(\text{Revenu mensuel net} \times \frac{33}{100}\right) - \text{Crédit auto mensuel}
$$

$$
\text{Mensualité maximale} = (2700 \times 0.33) - 200 = 891 - 200 = 691 \, \text{euros}
$$

## Calcul de la capacité d'emprunt

$$
M = \frac{C \times t \times (1 + t)^{n}}{(1 + t)^{n} - 1}
$$

### Taux mensuel et nombre de mensualités

$$
t = \frac{4\%}{12} = \frac{0,04}{12} \approx 0,003333
$$

$$
n = 20 \times 12 = 240
$$

### Résolution pour \( C \)

$$
C = \frac{691 \times \left((1 + 0,003333)^{240} - 1\right)}{0,003333 \times (1 + 0,003333)^{240}}
$$

### Résultats

En utilisant ces valeurs, nous trouvons que la capacité d'emprunt maximale est d'environ **114 040,13 euros**.

## Résumé

- **Mensualité maximale** : 691 euros
- **Capacité d'emprunt maximale** : 114 040,13 euros
