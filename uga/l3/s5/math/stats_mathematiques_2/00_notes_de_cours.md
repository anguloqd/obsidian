## 00 // notes de cours

Cours #2 :

Exemple 1.2.1

Estimons p d’une binomiale avec la fréquence relative. Soit p=0,4 mais on le sait pas. On veut n tel que :

P(f_n \in [p-0.01, p+0.01]) ≥ 0.99

Qui est le même que P(|f_n-p|\le 0.01)\ge 0.99 \iff P(|f_n-p| >0.01) \le 0.01

Appliquant B.T :

P(|f_n-p| >0.01) \le Var(f_n)/(0.01)^2=pq/n(0.01)^2

On dira que la borne de BT devra être \le 0.01. Donc : pq/n(0.01)^2 \le 0.01 \iff (0.4 \times 0.06)/(0.01)^3 \le n \iff 240000\le n

On arrive à ce qu’on veut.

Exemple 1.3.1

On pourrait applique le TCL à f_n : Soit Z_n = \frac{(f_n-p)}{\sqrt{pq/n}}. Donc Z:_n \sim \mathcal N(0,1) quand n\rightarrow\infty. On cherche un n tel que P(|Z_n| \le 0.01/\sqrt{pq/n}) \ge 0.99.

Ok, brouillon. P(|Z_n| \le B) = P(Z_n\le B) - P(Z_n\le -B) mais ces derniers sont les répartitions, donc on a \phi(b)-(1-\phi(b))= 2\phi(B)-1. On revient à ce qu’on faisait : 2\phi(0,01/\sqrt{pq/n})-1 \ge 0.99

On calcule la variance dans le dénominateur à l’intérieur de \phi. Donc \phi(0.01/\sqrt{0.24/n})\ge 0.995. On applique l’inverse de \phi : 0.01/\sqrt{0.24/n} \ge 2.57 \iff n = 6,3e5. Trop petit.

Suite de cours, intro à chapitre 2 :

On utilise une loi de Poisson pour modéliser le # d’occurrence d’un événement dans le temps ET dans le space.

Truc algébrique clever : Var(Z) = E(Z^2) - E(Z)^2 \iff E(Z^2) = Var(Z)+E(Z)^2. Utile quand on connaît ces deux derniers termes. Cas quand Z=\bar X_n.

 Premier partiel

$$V(\hat t)=Var\left(\frac{3}{2}\bar X_n \right)=\frac{9}{4}Var\left(\frac{1}{n}\sum_{i=1}^n X_i\right)
\\[10pt]
=^{\text{indep.}}\frac{9}{4n^2}\sum_{i=1}^nVar(X_i)
=^\text{ident.}\frac{9}{4n^2}\sum_{i=1}^n\frac{t^2}{18}=\frac{t^2}{8n}$$

$$V(\hat t)=(E((\hat t_n) ^2]-E(\hat t_n)^2)

\\[10pt]

\text{Terme } E( (\hat t_n)^2]: E( (\hat t_n)^2] = E\left(\frac{9}{4} (\bar X_n)^2\right)=\frac{9}{4}E[(\bar X_n)^2]=\frac{9}{4}\left(V(\bar X_n)+E[\bar X_n]^2\right)
\\
= \frac{9}{4}\left(\frac{t^2/18}{n} +  \right)$$

Let’s denote the product as ( p ), so we have:

$$[ p = \prod_{i=1}^{n} \left(0.5\right)^{x_i} \cdot \left(1.125\right)^{1-x_i} ]$$

Taking the natural logarithm of both sides, we get:

$$[ \ln(p) = \sum_{i=1}^{n} \left[ x_i \ln(0.5) + (1-x_i) \ln(1.125) \right] ]$$

Given that ( p < -\ln(3) ), we have:

$$[ \ln(p) < -\ln(3) ]$$

Substituting the expression for ( \ln(p) ) from above, we get:

$$[ \sum_{i=1}^{n} \left[ x_i \ln(0.5) + (1-x_i) \ln(1.125) \right] < -\ln(3) ]$$

Rearranging the terms, we get:

$$[ \sum_{i=1}^{n} x_i > \frac{-\ln(3) - n\ln(1.125)}{\ln(0.5) - \ln(1.125)} ]$$

So, the inequality you’re looking for is:

$$[ \sum_{i=1}^{n} x_i > \frac{-\ln(3) - n\ln(1.125)}{\ln(0.5) - \ln(1.125)} ]$$
