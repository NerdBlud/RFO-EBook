# Nerdblud RFO E-Kitabı: Respublika Fənn Olimpiadaları Dərslik Layihəsi

Azərbaycan dilində C++20 dərsləri və informatika olimpiadaları üçün məşq materialları. On modul üzrə 51 PDF dərsi mövzuya görə axtara, brauzerdə oxuya və endirə bilərsiniz.

Veb nəşri yerli kompüterdə açmaq üçün repozitoriyanın kök qovluğunda bu əmrləri icra edin.

```sh
python site/build.py
python -m http.server 8000 --directory dist
```

Brauzerdə [dərs kataloqunu](http://localhost:8000/) açın. PDF-lərin və kod nümunələrinin təkrar istifadəsi üçün [istifadə şərtlərinə](REUSE.md) baxın.

GitHub Pages-də yayımlamaq üçün **Settings → Pages → Source** bölməsində **GitHub Actions** seçin və əsas budaqda **RFO E-Kitabı** iş axınını başladın.

## Dərslikdən necə istifadə etməli

C++ dilini yeni öyrənirsinizsə, birinci moduldan başlayın. Hər mövzuda əvvəlcə izahı oxuyun, sonra kod nümunəsini kompilyasiya edib fərqli girişlərlə yoxlayın. Modulun sonunda çalışma PDF-indən bir neçə məsələni müstəqil həll edin.

Artıq əsasları bilirsinizsə, mövzu seçmək üçün kataloqdan və tədris yol xəritəsindən istifadə edin. Məsələnin şərtini, giriş və çıxış formatını, eləcə də vaxt və yaddaş hədlərini yarış platformasında yoxlayın.

## Kurikulum

### Modul 1: C++ Giriş və Proqramın Axışı
Proqramlaşdırmanın təməli, kompilyasiya mexanizmi, sürətli IO və idarəetmə strukturları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. C++ ilə proqramlaşdırmaya giriş.pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/1.%20C%2B%2B%20il%C9%99%20proqramla%C5%9Fd%C4%B1rmaya%20giri%C5%9F.pdf) | Kompilyasiya prosesi, `main()` strukturu, `#include <iostream>`, namespace prinsipləri. |
| [`2. CP Şablonu və Sürətli IO.pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/2.%20CP%20%C5%9Eablonu%20v%C9%99%20S%C3%BCr%C9%99tli%20IO.pdf) | `ios_base::sync_with_stdio(0); cin.tie(0);`, `\n` vs `endl`, rəqabətli proqramlaşdırma şablonu. |
| [`3. Verilənlər, Tiplər və Operatorlar.pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/3.%20Veril%C9%99nl%C9%99r%2C%20Tipl%C9%99r%20v%C9%99%20Operatorlar.pdf) | Primitiv tiplər, `int`, `long long` daşmaları, `double` dəqiqliyi, bit operatorları. |
| [`4. Şərt İfadələri (If-Else, Switch).pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/4.%20%C5%9E%C9%99rt%20%C4%B0fad%C9%99l%C9%99ri%20%28If-Else%2C%20Switch%29.pdf) | Budaqlanma strukturları, məntiqi operatorlar (`&&`, `\|\|`, `!`), ternary operator. |
| [`5. Dövrlər (For, While, İç-içə).pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/5.%20D%C3%B6vrl%C9%99r%20%28For%2C%20While%2C%20%C4%B0%C3%A7-i%C3%A7%C9%99%29.pdf) | `for`, `while`, `do-while` dövrləri, `break`, `continue`, daxili dövrlər və mürəkkəblik analizi. |
| [`6. Məsələlər və Çalışmalar.pdf`](01.%20C%2B%2B%20Giri%C5%9F%20v%C9%99%20Proqram%C4%B1n%20Ax%C4%B1%C5%9F%C4%B1/6.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Giriş və riyazi operatorlar üzrə 20 seçilmiş baza məsələsi. |

---

### Modul 2: Massivlər, Sətirlər və Funksiyalar
Yaddaşın xətti modelləşdirilməsi, dinamik massivlər, simvol ardıcıllıqları və funksional bölüşdürmə.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Massivlər (Arrays) və Vector.pdf`](02.%20Massivl%C9%99r%2C%20S%C9%99tirl%C9%99r%20v%C9%99%20Funksiyalar/1.%20Massivl%C9%99r%20%28Arrays%29%20v%C9%99%20Vector.pdf) | Statik massivlər, dinamik `std::vector`, ölçü idarəetməsi, `push_back`, `resize`. |
| [`2. Sətirlər və Mətnlər (Strings).pdf`](02.%20Massivl%C9%99r%2C%20S%C9%99tirl%C9%99r%20v%C9%99%20Funksiyalar/2.%20S%C9%99tirl%C9%99r%20v%C9%99%20M%C9%99tnl%C9%99r%20%28Strings%29.pdf) | `std::string`, simvol metodları, `substr`, leksikoqrafik müqayisə, sətir funksiyaları. |
| [`3. Funksiyalar (Functions) və Rekursiya.pdf`](02.%20Massivl%C9%99r%2C%20S%C9%99tirl%C9%99r%20v%C9%99%20Funksiyalar/3.%20Funksiyalar%20%28Functions%29%20v%C9%99%20Rekursiya.pdf) | Funksiya imzası, ötürülmə qaydaları, baza halı, rekursiv çağırışlar və Call Stack. |
| [`4. İstinadlar (References) və Göstəricilər.pdf`](02.%20Massivl%C9%99r%2C%20S%C9%99tirl%C9%99r%20v%C9%99%20Funksiyalar/4.%20%C4%B0stinadlar%20%28References%29%20v%C9%99%20G%C3%B6st%C9%99ricil%C9%99r.pdf) | `&` istinadla parametr ötürmə, yaddaş ünvanları, `const` referans ilə optimallaşdırma. |
| [`5. Məsələlər və Çalışmalar.pdf`](02.%20Massivl%C9%99r%2C%20S%C9%99tirl%C9%99r%20v%C9%99%20Funksiyalar/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Massivlər, sətirlər və rekursiya üzrə 20 olimpiada məsələsi. |

---

### Modul 3: C++ STL (Standard Template Library)
Yüksək performanslı verilənlər strukturları və standart konteynerlər.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Pairs və Tuples.pdf`](03.%20C%2B%2B%20STL%20%28Standard%20Template%20Library%29/1.%20Pairs%20v%C9%99%20Tuples.pdf) | `std::pair`, `std::tuple`, `make_pair`, avtomatik leksikoqrafik sıralama mexanizmi. |
| [`2. Queue, Deque, Stack.pdf`](03.%20C%2B%2B%20STL%20%28Standard%20Template%20Library%29/2.%20Queue%2C%20Deque%2C%20Stack.pdf) | LIFO / FIFO strukturları, `std::stack`, `std::queue`, iki tərəfli `std::deque`. |
| [`3. Set, Map, Priority Queue.pdf`](03.%20C%2B%2B%20STL%20%28Standard%20Template%20Library%29/3.%20Set%2C%20Map%2C%20Priority%20Queue.pdf) | Qırmızı-Qara ağaclar: `std::set`, `std::map`, Həş cədvəli: `unordered_map`, Max/Min Heap. |
| [`4. Custom Comparators.pdf`](03.%20C%2B%2B%20STL%20%28Standard%20Template%20Library%29/4.%20Custom%20Comparators.pdf) | `std::sort` üçün xüsusi müqayisə operatorları, lambda funksiyaları və struktur çeşidlənməsi. |
| [`5. Məsələlər və Çalışmalar.pdf`](03.%20C%2B%2B%20STL%20%28Standard%20Template%20Library%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | STL strukturları üzrə 20 seçilmiş tapşırıq. |

---

### Modul 4: Riyaziyyat və Ədədlər Nəzəriyyəsi
Olimpiada riyaziyyatı, diskret strukturlar və hesablama alqoritmləri.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Sadə Ədədlər və Bölünmə.pdf`](04.%20Riyaziyyat%20v%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20N%C9%99z%C9%99riyy%C9%99si/1.%20Sad%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20v%C9%99%20B%C3%B6l%C3%BCnm%C9%99.pdf) | `O(sqrt(N))` sadəlik yoxlanması, Eratosfen Ələyi (Sieve of Eratosthenes) `O(N log log N)`. |
| [`2. ƏBOB, ƏKOB və Evklid.pdf`](04.%20Riyaziyyat%20v%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20N%C9%99z%C9%99riyy%C9%99si/2.%20%C6%8FBOB%2C%20%C6%8FKOB%20v%C9%99%20Evklid.pdf) | Evklid alqoritmi `gcd(a, b)`, `std::__gcd`, Genişləndirilmiş Evklid (Extended GCD). |
| [`3. Binar Qüvvətə Yüksəltmə.pdf`](04.%20Riyaziyyat%20v%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20N%C9%99z%C9%99riyy%C9%99si/3.%20Binar%20Q%C3%BCvv%C9%99t%C9%99%20Y%C3%BCks%C9%99ltm%C9%99.pdf) | `O(log N)` binar qüvvət, modulyar qüvvət və kombinatorik tətbiqlər. |
| [`4. Modular Arifmetika.pdf`](04.%20Riyaziyyat%20v%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20N%C9%99z%C9%99riyy%C9%99si/4.%20Modular%20Arifmetika.pdf) | Modulyar toplama/vurma, Fermat Kiçik Teoremi ilə Tərs Element (Modular Inverse). |
| [`5. Məsələlər və Çalışmalar.pdf`](04.%20Riyaziyyat%20v%C9%99%20%C6%8Fd%C9%99dl%C9%99r%20N%C9%99z%C9%99riyy%C9%99si/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Ədədlər nəzəriyyəsi üzrə 20 klassik olimpiada məsələsi. |

---

### Modul 5: Axtarış Alqoritmləri və İki Göstərici
Xətti axtarışdan `O(log N)` ikili qərarlara və effektiv aralıq emalına keçid.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Xətti və İkili Axtarış.pdf`](05.%20Axtar%C4%B1%C5%9F%20Alqoritml%C9%99ri%20v%C9%99%20%C4%B0ki%20G%C3%B6st%C9%99rici/1.%20X%C9%99tti%20v%C9%99%20%C4%B0kili%20Axtar%C4%B1%C5%9F.pdf) | `O(log N)` Binary Search, `std::lower_bound`, `std::upper_bound` mexanizmi. |
| [`2. Cavaba Görə İkili Axtarış və Üçlü Axtarış.pdf`](05.%20Axtar%C4%B1%C5%9F%20Alqoritml%C9%99ri%20v%C9%99%20%C4%B0ki%20G%C3%B6st%C9%99rici/2.%20Cavaba%20G%C3%B6r%C9%99%20%C4%B0kili%20Axtar%C4%B1%C5%9F%20v%C9%99%20%C3%9C%C3%A7l%C3%BC%20Axtar%C4%B1%C5%9F.pdf) | Monoton predikat funksiyaları, Binary Search on Answer, Ternary Search ilə ekstremum. |
| [`3. İki Göstərici Texnikası.pdf`](05.%20Axtar%C4%B1%C5%9F%20Alqoritml%C9%99ri%20v%C9%99%20%C4%B0ki%20G%C3%B6st%C9%99rici/3.%20%C4%B0ki%20G%C3%B6st%C9%99rici%20Texnikas%C4%B1.pdf) | Two Pointers invariantı, cütlərin cəmi (2-Sum), massivlərin birləşdirilməsi `O(N)`. |
| [`4. Sürüşən Pəncərə və Prefiks Cəmlər.pdf`](05.%20Axtar%C4%B1%C5%9F%20Alqoritml%C9%99ri%20v%C9%99%20%C4%B0ki%20G%C3%B6st%C9%99rici/4.%20S%C3%BCr%C3%BC%C5%9F%C9%99n%20P%C9%99nc%C9%99r%C9%99%20v%C9%99%20Prefiks%20C%C9%99ml%C9%99r.pdf) | Sliding Window invariantı, 1D/2D Prefiks cəmləri ilə `O(1)` aralıq cəmi sorğusu. |
| [`5. Məsələlər və Çalışmalar.pdf`](05.%20Axtar%C4%B1%C5%9F%20Alqoritml%C9%99ri%20v%C9%99%20%C4%B0ki%20G%C3%B6st%C9%99rici/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Axtarış və aralıq texnikaları üzrə 20 olimpiada məsələsi. |

---

### Modul 6: Qraf Nəzəriyyəsinə Giriş (DFS, BFS)
Əlaqəli şəbəkələrin təsviri və təməl qraf traversalları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Qraflara Giriş və Saxlanma Üsulları.pdf`](06.%20Qraf%20N%C9%99z%C9%99riyy%C9%99sin%C9%99%20Giri%C5%9F%20%28DFS%2C%20BFS%29/1.%20Qraflara%20Giri%C5%9F%20v%C9%99%20Saxlanma%20%C3%9Csullar%C4%B1.pdf) | Qonşuluq Matrisi (Adjacency Matrix) vs Qonşuluq Siyahısı (Adjacency List `adj[u]`). |
| [`2. Dərinliyinə Axtarış (DFS).pdf`](06.%20Qraf%20N%C9%99z%C9%99riyy%C9%99sin%C9%99%20Giri%C5%9F%20%28DFS%2C%20BFS%29/2.%20D%C9%99rinliyin%C9%99%20Axtar%C4%B1%C5%9F%20%28DFS%29.pdf) | Rekursiv DFS, əlaqəli komponentlər, rəngləmə, tsikllərin aşkarlanması `O(V + E)`. |
| [`3. Eninə Axtarış (BFS).pdf`](06.%20Qraf%20N%C9%99z%C9%99riyy%C9%99sin%C9%99%20Giri%C5%9F%20%28DFS%2C%20BFS%29/3.%20Enin%C9%99%20Axtar%C4%B1%C5%9F%20%28BFS%29.pdf) | Növbə əsaslı BFS, çəkisiz qraflarda ən qısa yol, 2D qəfəsdə BFS. |
| [`4. Ağaclar və Topoloji Sıralama.pdf`](06.%20Qraf%20N%C9%99z%C9%99riyy%C9%99sin%C9%99%20Giri%C5%9F%20%28DFS%2C%20BFS%29/4.%20A%C4%9Faclar%20v%C9%99%20Topoloji%20S%C4%B1ralama.pdf) | Ağac diametri, mərkəzi, DAG strukturları və Kahn / DFS Topoloji Sıralaması. |
| [`5. Məsələlər və Çalışmalar.pdf`](06.%20Qraf%20N%C9%99z%C9%99riyy%C9%99sin%C9%99%20Giri%C5%9F%20%28DFS%2C%20BFS%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Təməl qraf alqoritmləri üzrə 20 seçilmiş məsələ. |

---

### Modul 7: Qabaqcıl Qraflar (Dijkstra, DSU, MST, LCA)
Çəkili qraflarda optimallaşdırma və ağac üzərində iyerarxik sorğular.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Ən Qısa Yol Alqoritmləri.pdf`](07.%20Qabaqc%C4%B1l%20Qraflar%20%28Dijkstra%2C%20DSU%29/1.%20%C6%8Fn%20Q%C4%B1sa%20Yol%20Alqoritml%C9%99ri.pdf) | Dijkstra (`std::priority_queue` `O(E log V)`), Bellman-Ford, Floyd-Warshall `O(V^3)`. |
| [`2. Disjoint Set Union (DSU).pdf`](07.%20Qabaqc%C4%B1l%20Qraflar%20%28Dijkstra%2C%20DSU%29/2.%20Disjoint%20Set%20Union%20%28DSU%29.pdf) | Path Compression + Union by Size ilə amortizasiya olunmuş `O(α(N))` sabit zaman. |
| [`3. Minimum Çəkili Ağac (MST).pdf`](07.%20Qabaqc%C4%B1l%20Qraflar%20%28Dijkstra%2C%20DSU%29/3.%20Minimum%20%C3%87%C9%99kili%20A%C4%9Fac%20%28MST%29.pdf) | Kəsim Xassəsi (Cut Property), Kruskal alqoritmi, DSU ilə tsikl qarşısının alınması. |
| [`4. Ən Yaxın Ortaq Əcdad (LCA).pdf`](07.%20Qabaqc%C4%B1l%20Qraflar%20%28Dijkstra%2C%20DSU%29/4.%20%C6%8Fn%20Yax%C4%B1n%20Ortaq%20%C6%8Fcdad%20%28LCA%29.pdf) | Binar Qaldırma (Binary Lifting `up[u][i]`), `O(log N)` LCA və Ağacda Məsafə Teoremi. |
| [`5. Məsələlər və Çalışmalar.pdf`](07.%20Qabaqc%C4%B1l%20Qraflar%20%28Dijkstra%2C%20DSU%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Qabaqcıl qraflar üzrə 20 seçilmiş olimpiada məsələsi. |

---

### Modul 8: Dinamik Proqramlaşdırma (DP)
Problemlərin alt-strukturlara bölünməsi, vəziyyət fəzası və yaddaşlı hesablama.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Dinamik Proqramlaşdırmaya Giriş.pdf`](08.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rma%20%28DP%29/1.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rmaya%20Giri%C5%9F.pdf) | Optimal Substructure, Overlapping Subproblems, Pilləkən, Coin Change, Kadane. |
| [`2. Klassik DP Modelləri.pdf`](08.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rma%20%28DP%29/2.%20Klassik%20DP%20Modell%C9%99ri.pdf) | LIS `O(N log N)` sübutu (`std::lower_bound`), LCS 2D matrisi, 0/1 Knapsack geriyə dövr. |
| [`3. 2D Qəfəs və İnterval DP.pdf`](08.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rma%20%28DP%29/3.%202D%20Q%C9%99f%C9%99s%20v%C9%99%20%C4%B0nterval%20DP.pdf) | 2D Grid DP yolları, Optimal Matris Vurulması (Matrix Chain Multiplication) `O(N^3)`. |
| [`4. Bitmask və Ağac DP.pdf`](08.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rma%20%28DP%29/4.%20Bitmask%20v%C9%99%20A%C4%9Fac%20DP.pdf) | Bitmask DP (Komivoyajor - TSP `O(2^N * N^2)`), Ağacda Maksimal Müstəqil Çoxluq (MIS). |
| [`5. Məsələlər və Çalışmalar.pdf`](08.%20Dinamik%20Proqramla%C5%9Fd%C4%B1rma%20%28DP%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Dinamik proqramlaşdırma üzrə 20 standart tapşırıq. |

---

### Modul 9: Qabaqcıl Verilənlər Strukturları (Segment Tree, Fenwick)
Dinamik massivlər üzərində loqarifmik və sabit zamanlı aralıq sorğuları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Fenwick Ağacı (BIT).pdf`](09.%20Qabaqc%C4%B1l%20Veril%C9%99nl%C9%99r%20Strukturlar%C4%B1%20%28Segment%20Tree%2C%20Fenwick%29/1.%20Fenwick%20A%C4%9Fac%C4%B1%20%28BIT%29.pdf) | `lowbit = x & (-x)` riyazi sübutu, `O(log N)` prefiks cəmi və nöqtəvi yenilənmə. |
| [`2. Seqment Ağacı.pdf`](09.%20Qabaqc%C4%B1l%20Veril%C9%99nl%C9%99r%20Strukturlar%C4%B1%20%28Segment%20Tree%2C%20Fenwick%29/2.%20Seqment%20A%C4%9Fac%C4%B1.pdf) | Binar ağac strukturu, 4N yaddaş həddinin sübutu, `build`, `update`, `sum` funksiyaları. |
| [`3. Tənbəl Yayılma (Lazy Propagation).pdf`](09.%20Qabaqc%C4%B1l%20Veril%C9%99nl%C9%99r%20Strukturlar%C4%B1%20%28Segment%20Tree%2C%20Fenwick%29/3.%20T%C9%99nb%C9%99l%20Yay%C4%B1lma%20%28Lazy%20Propagation%29.pdf) | Aralıq yenilənmələri (Range Update), `push(v, tl, tr)` və `lazy[v]` bufer mexanizmi. |
| [`4. Seyrək Cədvəl və Kök N.pdf`](09.%20Qabaqc%C4%B1l%20Veril%C9%99nl%C9%99r%20Strukturlar%C4%B1%20%28Segment%20Tree%2C%20Fenwick%29/4.%20Seyr%C9%99k%20C%C9%99dv%C9%99l%20v%C9%99%20K%C3%B6k%20N.pdf) | Sparse Table ilə `O(1)` Statik RMQ (İdempotentlik), Sqrt Decomposition `O(sqrt(N))`. |
| [`5. Məsələlər və Çalışmalar.pdf`](09.%20Qabaqc%C4%B1l%20Veril%C9%99nl%C9%99r%20Strukturlar%C4%B1%20%28Segment%20Tree%2C%20Fenwick%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Aralıq sorğuları üzrə 22 seçilmiş tapşırıq. |

---

### Modul 10: Qabaqcıl Olimpiada Mövzuları (Strings, Geometry, Game Theory)
Beynəlxalq olimpiadaların ən yüksək səviyyəli kombinatorik və analitik alqoritmləri.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| [`1. Sətir Alqoritmləri (Hashing, KMP, Trie).pdf`](10.%20Qabaqc%C4%B1l%20Olimpiada%20M%C3%B6vzular%C4%B1%20%28Strings%2C%20Geometry%2C%20Game%20Theory%29/1.%20S%C9%99tir%20Alqoritml%C9%99ri%20%28Hashing%2C%20KMP%2C%20Trie%29.pdf) | Polinomial Rolling Hash, KMP Pi cədvəli və axtarış, Statik 2D massivli Maksimal XOR Trie. |
| [`2. Hesablama Həndəsəsi.pdf`](10.%20Qabaqc%C4%B1l%20Olimpiada%20M%C3%B6vzular%C4%B1%20%28Strings%2C%20Geometry%2C%20Game%20Theory%29/2.%20Hesablama%20H%C9%99nd%C9%99s%C9%99si.pdf) | Vektor Hasili (`cross`), Çoxbucaqlının Sahəsi (Shoelace), Qabarıq Örtük (Monotone Chain), Ray Casting. |
| [`3. Oyun Nəzəriyyəsi və Nim.pdf`](10.%20Qabaqc%C4%B1l%20Olimpiada%20M%C3%B6vzular%C4%B1%20%28Strings%2C%20Geometry%2C%20Game%20Theory%29/3.%20Oyun%20N%C9%99z%C9%99riyy%C9%99si%20v%C9%99%20Nim.pdf) | Impartial Games, Bouton Teoremi (Nim-Sum XOR), Sprague-Grundy Teoremi və MEX hesablanması. |
| [`4. HLD və Şəbəkə Axınları.pdf`](10.%20Qabaqc%C4%B1l%20Olimpiada%20M%C3%B6vzular%C4%B1%20%28Strings%2C%20Geometry%2C%20Game%20Theory%29/4.%20HLD%20v%C9%99%20%C5%9E%C9%99b%C9%99k%C9%99%20Ax%C4%B1nlar%C4%B1.pdf) | Heavy-Light Decomposition (`dfs_sz`, `dfs_hld`, `queryPath`), Dinic Max-Flow Alqoritmi. |
| [`5. Məsələlər və Çalışmalar.pdf`](10.%20Qabaqc%C4%B1l%20Olimpiada%20M%C3%B6vzular%C4%B1%20%28Strings%2C%20Geometry%2C%20Game%20Theory%29/5.%20M%C9%99s%C9%99l%C9%99l%C9%99r%20v%C9%99%20%C3%87al%C4%B1%C5%9Fmalar.pdf) | Qabaqcıl mövzular üzrə 20 seçilmiş olimpiada məsələsi. |

---

## 4. Tədris və Məşq Üzrə Yol Xəritəsi

Dərslik toplusu üzrə 3 pilləli tədris strategiyası tövsiyə olunur:

```
Pillə 1 (Baza Mərhələsi): 
  Modul 1 (C++ Baza) -> Modul 2 (Massivlər & Sətirlər) -> Modul 3 (STL) -> Modul 4 (Riyaziyyat)

Pillə 2 (Alqoritmik Mərhələ): 
  Modul 5 (Axtarış & İki Göstərici) -> Modul 6 (Təməl Qraflar) -> Modul 8 (Dinamik Proqramlaşdırma)

Pillə 3 (Qabaqcıl Olimpiada Mərhələsi): 
  Modul 7 (Qabaqcıl Qraflar) -> Modul 9 (Seqment & Fenwick Ağacları) -> Modul 10 (HLD, Axınlar, Həndəsə)
```

---

## 5. Müəlliflik və Təşəkkür

Bu dərslik materialları **Nerdblud Təhsil Təşəbbüsü** çərçivəsində, Azərbaycanda rəqabətli proqramlaşdırma mədəniyyətinin inkişafı və Respublika Fənn Olimpiadaları iştirakçılarının bilik səviyyəsinin beynəlxalq standartlara çatdırılması məqsədilə hazırlanmışdır.
