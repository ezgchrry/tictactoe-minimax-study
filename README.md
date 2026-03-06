### Tic-Tac-Toe Üzerinde Minimax Algoritması Gerçeklemesi

Bu çalışma, **Yapay Zeka dersinde graflar ve durum uzayı (state space)** konularını çalışırken teorik kavramların kod üzerindeki karşılığını görmek amacıyla hazırlanmıştır.

### Çalışmanın İçeriği

Ders notlarında gördüğüm **oyun ağaçları (game trees)** ve **karar mekanizmalarını** somutlaştırmak için **Tic-Tac-Toe** oyunu temel alınmıştır.  

Buradaki temel amaç, oyunun her aşamasını bir **graf düğümü (node)** olarak ele alıp bir sonraki hamleyi **matematiksel olarak hesaplayan** bir yapı kurmaktır.

### Algoritma Mantığı

Kod içerisinde yer alan **Minimax algoritması**, mevcut tahta durumundan başlayarak oyunun sonuna kadar oluşabilecek **tüm olası hamleleri** tarar.

**Mantık:**

- Algoritma, rakibin (insan oyuncu) her zaman **kendisi için en iyi hamleyi yapacağını** varsayar.  
- Buna göre bot, kendi açısından **en yüksek puanı getiren hamleyi** seçer.

### Sonuç

Tic-Tac-Toe oyununun durum uzayı küçük olduğu için bilgisayar **tüm ihtimalleri çok kısa sürede hesaplayabilir**.  

Bu nedenle Minimax algoritmasını kullanan bot **teorik olarak yenilmezdir** ve en kötü ihtimalle oyunu **berabere bitirir**.

---

### Tic-Tac-Toe Implementation with Minimax Algorithm

This implementation was prepared to observe the practical coding equivalent of theoretical concepts while studying **Graphs** and **State Space Search** in my **Artificial Intelligence course**.

### Overview

The game of **Tic-Tac-Toe** was used to concretize the **game trees** and **decision-making mechanisms** discussed in the course notes.

The main objective was to treat each stage of the game as a **graph node** and build a structure that **mathematically calculates the next move**.

### Algorithm Logic

The **Minimax algorithm** in the code scans all possible paths starting from the **current board state** until the end of the game.

**Logic:**

- The algorithm assumes that the opponent (human player) will always make the **best possible move**.
- Based on this assumption, the bot selects the path that **maximizes its own score**.

### Result

Since the **game tree of Tic-Tac-Toe is relatively small**, the computer can calculate all possible outcomes **within milliseconds**.

As a result, a bot using the **Minimax algorithm becomes theoretically unbeatable** and at worst the game ends in a **draw**.
