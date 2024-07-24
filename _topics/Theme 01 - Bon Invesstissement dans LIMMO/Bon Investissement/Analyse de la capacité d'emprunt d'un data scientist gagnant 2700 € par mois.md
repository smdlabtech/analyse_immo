# Analyse de la capacité d'emprunt d'un data scientist gagnant 2700 € par mois

## Données de base

- **Revenu mensuel net** : 2700 €
- **Taux d'endettement maximal** : 33% (généralement accepté par les banques)
- **Durée de remboursement** : 20 ans (standard pour un prêt immobilier)
- **Taux d'intérêt annuel** : 4% (hypothèse de base)

## Calcul de la mensualité maximale

### Taux d'endettement

Les banques considèrent généralement qu'un emprunteur ne doit pas consacrer plus de 33% de ses revenus mensuels nets au remboursement de ses dettes.

$$
\text{Mensualité maximale} = \text{Revenu mensuel net} \times \frac{33}{100}
$$

$$
\text{Mensualité maximale} = 2700 \times 0.33 = 891 \, \text{euros}
$$

## Calcul de la capacité d'emprunt

Pour calculer la capacité d'emprunt, nous utilisons la formule de calcul des mensualités pour un prêt à taux fixe :

$$
M = \frac{C \times t \times (1 + t)^n}{(1 + t)^n - 1}
$$

où :
- \( M \) est la mensualité maximale (891 €),
- \( C \) est le capital emprunté (ce que nous voulons trouver),
- \( t \) est le taux d'intérêt mensuel (taux annuel divisé par 12),
- \( n \) est le nombre total de mensualités (nombre d'années multiplié par 12).

### Taux mensuel et nombre de mensualités

$$
t = \frac{4\%}{12} = \frac{0,04}{12} \approx 0,003333
$$

$$
n = 20 \times 12 = 240
$$

### Résolution pour \( C \)

Nous devons réarranger la formule pour isoler \( C \) :

$$
C = \frac{M \times \left((1 + t)^n - 1\right)}{t \times (1 + t)^n}
$$

En substituant les valeurs, nous obtenons :

$$
C = \frac{891 \times \left((1 + 0,003333)^{240} - 1\right)}{0,003333 \times (1 + 0,003333)^{240}}
$$

### Résultats

En utilisant ces valeurs, nous trouvons que la capacité d'emprunt maximale est d'environ **147 034,48 euros**.

## Résumé

- **Mensualité maximale** : 891 euros
- **Capacité d'emprunt maximale** : 147 034,48 euros

Ce montant correspond au capital maximum qu'un data scientist gagnant 2700 € par mois peut emprunter, en supposant qu'il consacre 33% de ses revenus au remboursement de son prêt sur une durée de 20 ans avec un taux d'intérêt de 4% par an.
