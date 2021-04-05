# Livejournal-to-Drive2
Преобразование текста в формате ЖЖ в текст в формате drive2.ru

Программа делает следующие вещи.
1) Преобразование вставленных картинок из формата ЖЖ в формат drive2.ru (файлы с фотографиями лучше пронумеровать по порядку и загрузить их скопом на drive2 - тогда всё будет работать). К примеру, первая встреченная в тексте ссылка на изображение
`<img src="https://some_photo_hosting.com/some_image.jpg" alt="" width="1000" />`
преобразуется в
`<img src="1" title="">`
, а вторая встреченная в тексте ссылка на изображение
`<img src="https://some_photo_hosting.com/some_another_image.jpg" alt="" width="1000" />`
преобразуется уже в
`<img src="1" title="">`

2) Преобразование вставленных видео с YouTube из формата ЖЖ в формат drive2.ru - то есть в обычную ссылку. Например,
`<iframe src="https://www.youtube.com/embed/Kl2B_NquX6s?wmode=opaque" width="1000" height="560" frameborder="0" allowfullscreen="allowfullscreen" data-link="https://youtube.com/watch?v=Kl2B_NquX6s"></iframe>`
преобразуется в
`https://youtube.com/watch?v=Kl2B_NquX6s`

3) Преобразование обычных ссылок на профили пользователей в user name (остальные гиперссылки остаются неизменными). К примеру,
`<a href="https://www.drive2.ru/users/beacon1143/">beacon1143</a>`
преобразуется в
`<user name="beacon1143">`

4) Удаление строк lj-cut и lj-embed.
