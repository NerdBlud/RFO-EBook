# Nerdblud RFO E-Kitabı: Respublika Fənn Olimpiadaları Dərslik Layihəsi

<div align="center">

![Language](https://img.shields.io/badge/Language-C%2B%2B20-blue.svg?style=flat-square)
![Syllabus](https://img.shields.io/badge/Syllabus-RFO%20%7C%20IOI%20%7C%20EGOI-FACC15.svg?style=flat-square)
![Scope](https://img.shields.io/badge/Scope-10%20Modules%20%7C%2051%20Textbooks-success.svg?style=flat-square)
![Format](https://img.shields.io/badge/Standard-CSES%20Handbook%20Style-purple.svg?style=flat-square)
![Target](https://img.shields.io/badge/Audience-Olympiad%20Contestants%20%26%20Students-black.svg?style=flat-square)

**İnformatika fənni üzrə Respublika Fənn Olimpiadaları (RFO) və beynəlxalq yarışlar (IOI, EGOI) üçün C++ ilə Rəqabətli Proqramlaşdırma üzrə tam akademik dərslik toplusu.**

</div>

---

## 1. Layihənin Məqsədi və Tədris Metodologiyası

**Nerdblud RFO E-Kitabı**, informatika fənni üzrə olimpiadalara hazırlaşan şagirdlər və müəllimlər üçün nəzərdə tutulmuş milli akademik dərslik layihəsidir. Dərslik toplusu C++ dilinin baza sintaksisindən başlayaraq Beynəlxalq İnformatika Olimpiadası (IOI) səviyyəsinə qədər olan bütün fundamental alqoritmik və kombinatorik mövzuları tam əhatə edir.

### Metodoloji Prinsiplər:
* **Riyazi İnvariant və Dərin Qavrayış:** Alqoritmlərin mexaniki əzbərlənməsi deyil, hər bir strukturun altındakı riyazi xassələr (məsələn: Fenwick ağacında 2-yə tamamlayıcı arxitekturası, Seqment ağacında $4N$ yaddaş həddinin həndəsi sübutu, LIS-də monotonluq invariantı) nümayiş etdirilir.
* **CSES Handbook Standartı:** Ritorik suallardan və qeyri-rəsmi ifadələrdən uzaq, beynəlxalq olimpiada ədəbiyyatına tam uyğun, dəqiq və yüksək informasiya sıxlığına malik akademik dil.
* **Şagird-Yönümlü Sadə Kod Şablonları:** Yarış gedişatında şagirdlərin ən az kod sətri ilə, sürətli və xətasız tətbiq edə biləcəyi təmiz olimpiada C++20 şablonları.
* **Hər Sətir Üzrə İzahlı Şərhlər:** Hər bir funksiya, dövr və vəziyyət keçidinin təyinatı kod daxilində Azərbaycan dilində ətraflı şəkildə qeyd edilmişdir.

---

## 2. Layihənin Keyfiyyət və Əhatə Göstəriciləri

* **51 Tammetrajlı PDF Dərsliyi:** 10 tematik modul daxilində bölünmüş, A4 çap standartlarına uyğun sənədlər.
* **Vektor Qrafikası:** Seqment Ağacları və BIT iyerarxiyaları üçün piksel itkisi olmayan xüsusi SVG vektor diaqramları.
* **200+ Seçilmiş Məsələ:** CSES, E-Olymp, Codeforces və AtCoder platformalarından mövzular üzrə təsnif edilmiş, həll ipucları və çətinlik dərəcələri (`Asan`, `Orta`, `Çətin`) qeyd olunmuş tapşırıqlar toplusu.
* **Tam Komplekt:** Heç bir əlavə xarici resursa ehtiyac duymadan sıfırdan qabaqcıl səviyyəyə qədər müstəqil öyrənmə imkanı.

---

## 3. Kurikulum və Modulların Struktur Cədvəli

### Modul 1: C++ Giriş və Proqramın Axışı
Proqramlaşdırmanın təməli, kompilyasiya mexanizmi, sürətli IO və idarəetmə strukturları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. C++ ilə proqramlaşdırmaya giriş.pdf` | Kompilyasiya prosesi, `main()` strukturu, `#include <iostream>`, namespace prinsipləri. |
| `2. CP Şablonu və Sürətli IO.pdf` | `ios_base::sync_with_stdio(0); cin.tie(0);`, `\n` vs `endl`, rəqabətli proqramlaşdırma şablonu. |
| `3. Verilənlər, Tiplər və Operatorlar.pdf` | Primitiv tiplər, `int`, `long long` daşmaları, `double` dəqiqliyi, bit operatorları. |
| `4. Şərt İfadələri (If-Else, Switch).pdf` | Budaqlanma strukturları, məntiqi operatorlar (`&&`, `\|\|`, `!`), ternary operator. |
| `5. Dövrlər (For, While, İç-içə).pdf` | `for`, `while`, `do-while` dövrləri, `break`, `continue`, daxili dövrlər və mürəkkəblik analizi. |
| `6. Məsələlər və Çalışmalar.pdf` | Giriş və riyazi operatorlar üzrə 20 seçilmiş baza məsələsi. |

---

### Modul 2: Massivlər, Sətirlər və Funksiyalar
Yaddaşın xətti modelləşdirilməsi, dinamik massivlər, simvol ardıcıllıqları və funksional bölüşdürmə.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Massivlər (Arrays) və Vector.pdf` | Statik massivlər, dinamik `std::vector`, ölçü idarəetməsi, `push_back`, `resize`. |
| `2. Sətirlər və Mətnlər (Strings).pdf` | `std::string`, simvol metodları, `substr`, leksikoqrafik müqayisə, sətir funksiyaları. |
| `3. Funksiyalar (Functions) və Rekursiya.pdf` | Funksiya imzası, ötürülmə qaydaları, baza halı, rekursiv çağırışlar və Call Stack. |
| `4. İstinadlar (References) və Göstəricilər.pdf` | `&` istinadla parametr ötürmə, yaddaş ünvanları, `const` referans ilə optimallaşdırma. |
| `5. Məsələlər və Çalışmalar.pdf` | Massivlər, sətirlər və rekursiya üzrə 20 olimpiada məsələsi. |

---

### Modul 3: C++ STL (Standard Template Library)
Yüksək performanslı verilənlər strukturları və standart konteynerlər.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Pairs və Tuples.pdf` | `std::pair`, `std::tuple`, `make_pair`, avtomatik leksikoqrafik sıralama mexanizmi. |
| `2. Queue, Deque, Stack.pdf` | LIFO / FIFO strukturları, `std::stack`, `std::queue`, iki tərəfli `std::deque`. |
| `3. Set, Map, Priority Queue.pdf` | Qırmızı-Qara ağaclar: `std::set`, `std::map`, Həş cədvəli: `unordered_map`, Max/Min Heap. |
| `4. Custom Comparators.pdf` | `std::sort` üçün xüsusi müqayisə operatorları, lambda funksiyaları və struktur çeşidlənməsi. |
| `5. Məsələlər və Çalışmalar.pdf` | STL strukturları üzrə 20 seçilmiş tapşırıq. |

---

### Modul 4: Riyaziyyat və Ədədlər Nəzəriyyəsi
Olimpiada riyaziyyatı, diskret strukturlar və hesablama alqoritmləri.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Sadə Ədədlər və Bölünmə.pdf` | `O(sqrt(N))` sadəlik yoxlanması, Eratosfen Ələyi (Sieve of Eratosthenes) `O(N log log N)`. |
| `2. ƏBOB, ƏKOB və Evklid.pdf` | Evklid alqoritmi `gcd(a, b)`, `std::__gcd`, Genişləndirilmiş Evklid (Extended GCD). |
| `3. Binar Qüvvətə Yüksəltmə.pdf` | `O(log N)` binar qüvvət, modulyar qüvvət və kombinatorik tətbiqlər. |
| `4. Modular Arifmetika.pdf` | Modulyar toplama/vurma, Fermat Kiçik Teoremi ilə Tərs Element (Modular Inverse). |
| `5. Məsələlər və Çalışmalar.pdf` | Ədədlər nəzəriyyəsi üzrə 20 klassik olimpiada məsələsi. |

---

### Modul 5: Axtarış Alqoritmləri və İki Göstərici
Xətti axtarışdan `O(log N)` ikili qərarlara və effektiv aralıq emalına keçid.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Xətti və İkili Axtarış.pdf` | `O(log N)` Binary Search, `std::lower_bound`, `std::upper_bound` mexanizmi. |
| `2. Cavaba Görə İkili Axtarış və Üçlü Axtarış.pdf` | Monoton predikat funksiyaları, Binary Search on Answer, Ternary Search ilə ekstremum. |
| `3. İki Göstərici Texnikası.pdf` | Two Pointers invariantı, cütlərin cəmi (2-Sum), massivlərin birləşdirilməsi `O(N)`. |
| `4. Sürüşən Pəncərə və Prefiks Cəmlər.pdf` | Sliding Window invariantı, 1D/2D Prefiks cəmləri ilə `O(1)` aralıq cəmi sorğusu. |
| `5. Məsələlər və Çalışmalar.pdf` | Axtarış və aralıq texnikaları üzrə 20 olimpiada məsələsi. |

---

### Modul 6: Qraf Nəzəriyyəsinə Giriş (DFS, BFS)
Əlaqəli şəbəkələrin təsviri və təməl qraf traversalları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Qraflara Giriş və Saxlanma Üsulları.pdf` | Qonşuluq Matrisi (Adjacency Matrix) vs Qonşuluq Siyahısı (Adjacency List `adj[u]`). |
| `2. Dərinliyinə Axtarış (DFS).pdf` | Rekursiv DFS, əlaqəli komponentlər, rəngləmə, tsikllərin aşkarlanması `O(V + E)`. |
| `3. Eninə Axtarış (BFS).pdf` | Növbə əsaslı BFS, çəkisiz qraflarda ən qısa yol, 2D qəfəsdə BFS. |
| `4. Ağaclar və Topoloji Sıralama.pdf` | Ağac diametri, mərkəzi, DAG strukturları və Kahn / DFS Topoloji Sıralaması. |
| `5. Məsələlər və Çalışmalar.pdf` | Təməl qraf alqoritmləri üzrə 20 seçilmiş məsələ. |

---

### Modul 7: Qabaqcıl Qraflar (Dijkstra, DSU, MST, LCA)
Çəkili qraflarda optimallaşdırma və ağac üzərində iyerarxik sorğular.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Ən Qısa Yol Alqoritmləri.pdf` | Dijkstra (`std::priority_queue` `O(E log V)`), Bellman-Ford, Floyd-Warshall `O(V^3)`. |
| `2. Disjoint Set Union (DSU).pdf` | Path Compression + Union by Size ilə amortizasiya olunmuş `O(α(N))` sabit zaman. |
| `3. Minimum Çəkili Ağac (MST).pdf` | Kəsim Xassəsi (Cut Property), Kruskal alqoritmi, DSU ilə tsikl qarşısının alınması. |
| `4. Ən Yaxın Ortaq Əcdad (LCA).pdf` | Binar Qaldırma (Binary Lifting `up[u][i]`), `O(log N)` LCA və Ağacda Məsafə Teoremi. |
| `5. Məsələlər və Çalışmalar.pdf` | Qabaqcıl qraflar üzrə 20 seçilmiş olimpiada məsələsi. |

---

### Modul 8: Dinamik Proqramlaşdırma (DP)
Problemlərin alt-strukturlara bölünməsi, vəziyyət fəzası və yaddaşlı hesablama.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Dinamik Proqramlaşdırmaya Giriş.pdf` | Optimal Substructure, Overlapping Subproblems, Pilləkən, Coin Change, Kadane. |
| `2. Klassik DP Modelləri.pdf` | LIS `O(N log N)` sübutu (`std::lower_bound`), LCS 2D matrisi, 0/1 Knapsack geriyə dövr. |
| `3. 2D Qəfəs və İnterval DP.pdf` | 2D Grid DP yolları, Optimal Matris Vurulması (Matrix Chain Multiplication) `O(N^3)`. |
| `4. Bitmask və Ağac DP.pdf` | Bitmask DP (Komivoyajor - TSP `O(2^N * N^2)`), Ağacda Maksimal Müstəqil Çoxluq (MIS). |
| `5. Məsələlər və Çalışmalar.pdf` | Dinamik proqramlaşdırma üzrə 20 standart tapşırıq. |

---

### Modul 9: Qabaqcıl Verilənlər Strukturları (Segment Tree, Fenwick)
Dinamik massivlər üzərində loqarifmik və sabit zamanlı aralıq sorğuları.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Fenwick Ağacı (BIT).pdf` | `lowbit = x & (-x)` riyazi sübutu, `O(log N)` prefiks cəmi və nöqtəvi yenilənmə. |
| `2. Seqment Ağacı.pdf` | Binar ağac strukturu, 4N yaddaş həddinin sübutu, `build`, `update`, `sum` funksiyaları. |
| `3. Tənbəl Yayılma (Lazy Propagation).pdf` | Aralıq yenilənmələri (Range Update), `push(v, tl, tr)` və `lazy[v]` bufer mexanizmi. |
| `4. Seyrək Cədvəl və Kök N.pdf` | Sparse Table ilə `O(1)` Statik RMQ (İdempotentlik), Sqrt Decomposition `O(sqrt(N))`. |
| `5. Məsələlər və Çalışmalar.pdf` | Aralıq sorğuları üzrə 22 seçilmiş tapşırıq. |

---

### Modul 10: Qabaqcıl Olimpiada Mövzuları (Strings, Geometry, Game Theory)
Beynəlxalq olimpiadaların ən yüksək səviyyəli kombinatorik və analitik alqoritmləri.

| Fayl Adı | Əsas Mövzular və Məzmun |
| :--- | :--- |
| `1. Sətir Alqoritmləri (Hashing, KMP, Trie).pdf` | Polinomial Rolling Hash, KMP Pi cədvəli və axtarış, Statik 2D massivli Maksimal XOR Trie. |
| `2. Hesablama Həndəsəsi.pdf` | Vektor Hasili (`cross`), Çoxbucaqlının Sahəsi (Shoelace), Qabarıq Örtük (Monotone Chain), Ray Casting. |
| `3. Oyun Nəzəriyyəsi və Nim.pdf` | Impartial Games, Bouton Teoremi (Nim-Sum XOR), Sprague-Grundy Teoremi və MEX hesablanması. |
| `4. HLD və Şəbəkə Axınları.pdf` | Heavy-Light Decomposition (`dfs_sz`, `dfs_hld`, `queryPath`), Dinic Max-Flow Alqoritmi. |
| `5. Məsələlər və Çalışmalar.pdf` | Qabaqcıl mövzular üzrə 20 seçilmiş olimpiada məsələsi. |

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
