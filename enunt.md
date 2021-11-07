### Detecție regiuni poligonale

--- 

Tema presupune găsirea unui algoritm/metode prin care să generăm regiuni poligonale care
să identifice cât mai simplu (rectangular, decupări în unghiuri cât mai drepte, cât mai puține
vârfuri, etc.) și pe cât posibil fără suprapuneri, pentru toate zonele de interes din cadrul unei
imagini document.

- La intrare avem pentru fiecare pixel dintr-o imagine probabilitatea ca acesta să se afle
într-o anumită clasă de elemente: text, headline, reclamă, etc.

- La ieșire ne dorim să obținem colecția de poligoane și tipul fiecărui poligon.