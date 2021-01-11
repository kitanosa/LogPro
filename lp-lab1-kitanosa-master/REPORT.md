# Отчет по лабораторной работе №1
## Работа со списками и реляционным представлением данных
## по курсу "Логическое программирование"

### студент: Гордовой Денис Сергеевич

## Результат проверки

| Преподаватель     | Дата         |  Оценка       |
|-------------------|--------------|---------------|
| Сошников Д.В. |              |               |
| Левинская М.А.|              |     З         |

> *Комментарии проверяющих (обратите внимание, что более подробные комментарии возможны непосредственно в репозитории по тексту программы)*


## Введение
Список в прологе похож на связный список в обычных императивных языках программирования. Интересным его отличием является то, что в прологе мы выделяем в списке хвост и голову. И также в отличии от тех же C/C++ или Java в списках пролога могут хранится элементы любых типов, что дает дополнительные приятные возможности. Все операции над списками производятся рекурсивно.

## Задание 1.1: Предикат обработки списка

`deleteN(List,N)` - удаление N последних эементов

Примеры использования:
```prolog
?- deleteN([1,2,3,4,5,6],2).
[1, 2, 3, 4]
true

Реализация:
```prolog
deleteN(List,N):-
    reverse(List,RevList),
    deleteFirstN(RevList,Y,N),
    reverse(Y,Res),
    write(Res),!.

reverse(List, ReverseList):-
   reverse(List, [], ReverseList). 

reverse([], Buffer, Buffer):-!.
reverse([Head|Tail], Buffer, ReverseList):-
   reverse(Tail, [Head|Buffer], ReverseList).

deleteFirstN(List,List,0):-!. % число N = 0 , то мы уже удалили первые символы , поэтому полчаем ответ 
deleteFirstN([_|List],Res,N):-
	N1 is N - 1,
	deleteFirstN(List,Res,N1).
...
```

Переворачиваем список. Удаляем N первых ементов. Переворачиваем обратно
## Задание 1.2: Предикат обработки числового списка

Вычисление позиции максимального элемента в списке
Реализация:
```prolog
result([H|T]):- find_max([H|T], R), find_pos([H|T], R, 1).

find_max([X],X).
find_max([X,Y|T],Max):-X=<Y,find_max([Y|T],Max).
find_max([X,Y|T],Max):-X>=Y,find_max([X|T],Max).

find_pos([],_,1):-!.
find_pos([X|_],X,K):-write(K),!.
find_pos([_|T],X,K):- K1 is K+1,find_pos(T,X,K1).
```prolog

result([H|T]):- find_max([H|T], R), find_pos([H|T], R, 1).

find_max([A], A).
find_max([A, B|C], R) :- A < B, find_max([B|C], R), !.
find_max([A, _|B], R) :- find_max([A|B], R).

find_pos([],_,1):-!.
find_pos([X|_],X,K):-write(K),!.
find_pos([_|T],X,K):- K1 is K+1,find_pos(T,X,K1).
...
```
рекурсивный вызов функции с сравнением


## Задание 2: Реляционное представление данных
Реляционное представление показывает отношения между объектами, а задачей программиста является анализ этих отношений. Результат запроса к таким данным -- это множество ответов, удовлетворяющих внутренней структуре программы. Вся задача сводится к реализации такой структуры, которая обеспечит выдачу ответов. Это вынуждает постоянно проверять выходные данные на правильность и полноту. В ходе отладки своей программы я сталкивалась с ситуацией, когда ответ охватывал не все необходимые объекты. К преимуществам можно отнести относительную простоту разработки: программа разбивается на отдельные компоненты, которые реализуются независимо друг от друга. То есть в ходе написания программы ее можно сразу тестировать, заменяя еще ненаписанные компоненты множеством фактов.

averege_mark(Subject, Mark) считает средний балл для каждого предмета
```prolog
s_grade([], 0).
s_grade([H|T], N) :- s_grade(T, M), N is H + M.

averege_mark(Subject, Mark) :-
  findall(Grade, grade(_,_,Subject,Grade), Grades),
  s_grade(Grades, M),
  length(Grades, C),
  Mark is M/C.
```
averege_mark('Психология', X) 
X = 3.9285714285714284

person_from_group(Group, Number) считает количество несдавших студентов в группе
```prolog
person_from_group(Group, Number) :-
  setof(Surname, Subject^grade(Group,Surname,Subject,2), List),
  length(List, Number).
```
person_from_group(102, Number)
Number = 5

person_fall_sub(Subject, Number) считает количество несдавших из каждого из предметов
```prolog
person_fall_sub(Subject, Number) :-
  findall(1, grade(_,_,Subject,2), List),
  length(List, Number).
```
person_fall_sub('Психология', Number) 
Number = 1

## Выводы

В императивных языках мы указываем как что-либо сделать, в Прологе -- что необходимо сделать. Мы сообщаем системе, что нам известно и задаем вопросы.



