# Secret Sharing
This repository fully recreates the logic and math behind Shamir's Secret Sharing algorithm.<br>
<br>
I attempted to do this as much as possible by hand instead of relying on pre-built solutions<br>
in Python packages authored by others, relying only on a few key built-in packages that come<br>
with Python 3 for unique functionalities which are hard to build myself (e.g. <code>random</code>).

### 1. The idea
The algorithm allows a secret ($S$) (e.g. a passphrase, a number) to be split into any number ($n$) <br>
of components ($S_i$), where when a threshold number of shares ($t$) are brought together the secret <br>
is revealed.<br>
<br>
It does not matter which shares are brought together to reach the threshold amount if $t < n$, and <br>
furthermore, no more information can be gained about the secret as the number of shares brought <br>
together approaches $t$ (a characteristic called *perfect secrecry*).

### 2. Mathematical principles
The algorithm exploits the fact that the equation for any polynomial can be found if 

### 3. Security

### 4. Limitations

polynomials

### Disclaimer

This algorithm should not be used for real-world security purposes.
Because


### Sources and further reading
https://en.wikipedia.org/wiki/Shamir's_secret_sharing


