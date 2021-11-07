https://www.cis.rit.edu/class/simg782.old/finding_connected_components.pdf

https://learnopencv.com/convex-hull-using-opencv-in-python-and-c/

### Jarvis’ march (algoritm)

*Input*: O mult ̧ime de puncte necoliniare P = {P1,P2,...,Pn} din R2 (n ≥3).

*Output*: O lista **L** care contine varfurile ce determina frontiera acoperirii convexe,
parcursa ın sens trigonometric.


1. Determinarea unui punct din P care apart ̧ine frontierei (de exemplu cel mai
mic, folosind ordinea lexicografic ̆a); acest punct este notat cu A1.
2. k ←1; L←(A1); valid ← true
3. while valid= true
4. do alege un pivot arbitrar S ∈P, diferit de Ak
5. for i ←1 to n
6. do if Pi este la dreapta muchiei orientate AkS
7. then S ←Pi
8. if S 6= A1
9. then k ←k + 1;
Ak = S
adaug ̆a Ak la L
10. else valid ← false
11. return L